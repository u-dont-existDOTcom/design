"""Deterministic offline search over the checked-in design knowledge catalogs."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

REQUIRED_KEYS = {
    "id",
    "domain",
    "title",
    "keywords",
    "modes",
    "stacks",
    "guidance",
    "avoid",
}
TERM_RE = re.compile(r"[a-z0-9][a-z0-9+.-]*", re.IGNORECASE)
STOP_WORDS = {
    "a",
    "an",
    "and",
    "for",
    "in",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}


class QueryError(ValueError):
    """Raised when a query or catalog cannot be used safely."""


@dataclass(frozen=True, slots=True)
class CatalogEntry:
    id: str
    domain: str
    title: str
    keywords: tuple[str, ...]
    modes: tuple[str, ...]
    stacks: tuple[str, ...]
    guidance: tuple[str, ...]
    avoid: tuple[str, ...]

    @classmethod
    def from_mapping(cls, payload: object, *, source: Path) -> "CatalogEntry":
        if not isinstance(payload, dict):
            raise QueryError(f"Catalog entry in {source} must be an object.")
        if set(payload) != REQUIRED_KEYS:
            missing = sorted(REQUIRED_KEYS - set(payload))
            extra = sorted(set(payload) - REQUIRED_KEYS)
            raise QueryError(
                f"Catalog entry in {source} has invalid keys; missing={missing}, extra={extra}."
            )

        def text(value: object, field: str) -> str:
            if not isinstance(value, str) or not value.strip():
                raise QueryError(f"{source}: {field} must be non-empty text.")
            return value.strip()

        def texts(value: object, field: str) -> tuple[str, ...]:
            if not isinstance(value, list) or any(
                not isinstance(item, str) or not item.strip() for item in value
            ):
                raise QueryError(f"{source}: {field} must be a list of non-empty strings.")
            return tuple(item.strip() for item in value)

        return cls(
            id=text(payload["id"], "id"),
            domain=text(payload["domain"], "domain").casefold(),
            title=text(payload["title"], "title"),
            keywords=tuple(item.casefold() for item in texts(payload["keywords"], "keywords")),
            modes=tuple(item.casefold() for item in texts(payload["modes"], "modes")),
            stacks=tuple(item.casefold() for item in texts(payload["stacks"], "stacks")),
            guidance=texts(payload["guidance"], "guidance"),
            avoid=texts(payload["avoid"], "avoid"),
        )


@dataclass(frozen=True, slots=True)
class QueryResult:
    entry_id: str
    title: str
    domain: str
    score: int
    matched_terms: tuple[str, ...]
    guidance: tuple[str, ...]
    avoid: tuple[str, ...]


def _terms(text: str) -> tuple[str, ...]:
    return tuple(
        term.casefold()
        for term in TERM_RE.findall(text)
        if term.casefold() not in STOP_WORDS
    )


def validate_query(query: str) -> tuple[str, ...]:
    """Enforce one dominant, meaningful concern before search."""

    if not isinstance(query, str) or not query.strip():
        raise QueryError("Query must be non-empty text.")
    if query.count(",") > 2 or query.count(";") > 1:
        raise QueryError("Query contains too many separate concerns.")
    terms = _terms(query)
    unique = tuple(dict.fromkeys(terms))
    if len(unique) < 2:
        raise QueryError("Query must contain at least two meaningful terms.")
    if len(unique) > 10:
        raise QueryError("Query must contain no more than ten meaningful terms.")
    return unique


def load_catalogs(root: str | Path) -> tuple[CatalogEntry, ...]:
    """Load and validate all `*/catalog.json` files below root."""

    root_path = Path(root)
    paths = sorted(root_path.glob("*/catalog.json"))
    if not paths:
        raise QueryError(f"No catalogs found below {root_path}.")

    entries: list[CatalogEntry] = []
    seen_ids: set[str] = set()
    for path in paths:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise QueryError(f"Could not load {path}: {exc}") from exc
        if not isinstance(payload, list):
            raise QueryError(f"Catalog {path} must contain a JSON list.")
        for raw_entry in payload:
            entry = CatalogEntry.from_mapping(raw_entry, source=path)
            if entry.id in seen_ids:
                raise QueryError(f"Duplicate catalog id: {entry.id}")
            seen_ids.add(entry.id)
            entries.append(entry)
    return tuple(entries)


def _entry_terms(entry: CatalogEntry) -> set[str]:
    joined = " ".join((entry.title, *entry.keywords, *entry.guidance, *entry.avoid))
    return set(_terms(joined))


def _score(
    entry: CatalogEntry,
    query_terms: Sequence[str],
    *,
    domain: str | None,
    mode: str | None,
    stack: str | None,
) -> tuple[int, tuple[str, ...]]:
    haystack = _entry_terms(entry)
    matched = tuple(term for term in query_terms if term in haystack)
    if not matched:
        return 0, ()

    score = len(matched) * 10
    title_terms = set(_terms(entry.title))
    score += sum(4 for term in matched if term in title_terms)
    score += sum(2 for term in matched if term in entry.keywords)

    if domain and entry.domain == domain:
        score += 8
    if mode and mode in entry.modes:
        score += 6
    if stack and stack in entry.stacks:
        score += 6
    return score, matched


def search_catalog(
    query: str,
    *,
    domain: str | None = None,
    mode: str | None = None,
    stack: str | None = None,
    limit: int = 10,
    root: str | Path | None = None,
    entries: Iterable[CatalogEntry] | None = None,
) -> list[QueryResult]:
    """Return stable, verified matches for one design concern."""

    query_terms = validate_query(query)
    if limit < 1:
        raise QueryError("limit must be at least 1.")
    normalized_domain = domain.casefold() if domain else None
    normalized_mode = mode.casefold() if mode else None
    normalized_stack = stack.casefold() if stack else None

    if entries is None:
        catalog_root = (
            Path(root)
            if root is not None
            else Path(__file__).resolve().parents[1] / "knowledge"
        )
        entries = load_catalogs(catalog_root)

    results: list[QueryResult] = []
    for entry in entries:
        if normalized_domain and entry.domain != normalized_domain:
            continue
        score, matched = _score(
            entry,
            query_terms,
            domain=normalized_domain,
            mode=normalized_mode,
            stack=normalized_stack,
        )
        if score <= 0:
            continue
        results.append(
            QueryResult(
                entry_id=entry.id,
                title=entry.title,
                domain=entry.domain,
                score=score,
                matched_terms=matched,
                guidance=entry.guidance,
                avoid=entry.avoid,
            )
        )

    results.sort(key=lambda result: (-result.score, result.entry_id))
    return results[:limit]
