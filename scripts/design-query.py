#!/usr/bin/env python3
"""Search the offline Integrated Design OS knowledge catalogs."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from design_os.query import QueryError, search_catalog


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("query")
    result.add_argument("--domain")
    result.add_argument("--mode")
    result.add_argument("--stack")
    result.add_argument("--limit", type=int, default=10)
    result.add_argument("--format", choices=("json", "markdown"), default="markdown")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        results = search_catalog(
            args.query,
            domain=args.domain,
            mode=args.mode,
            stack=args.stack,
            limit=args.limit,
            root=ROOT / "knowledge",
        )
    except QueryError as exc:
        print(f"query error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(
            json.dumps(
                [
                    {
                        "id": item.entry_id,
                        "title": item.title,
                        "domain": item.domain,
                        "score": item.score,
                        "matched_terms": item.matched_terms,
                        "guidance": item.guidance,
                        "avoid": item.avoid,
                    }
                    for item in results
                ],
                indent=2,
            )
        )
    else:
        if not results:
            print("No verified catalog match found.")
        for index, item in enumerate(results, start=1):
            print(f"## {index}. {item.title} (`{item.entry_id}`)")
            print(f"\nScore: {item.score} · Domain: `{item.domain}`")
            print(f"\nMatched: {', '.join(item.matched_terms)}")
            print("\nGuidance:")
            for line in item.guidance:
                print(f"- {line}")
            if item.avoid:
                print("\nAvoid:")
                for line in item.avoid:
                    print(f"- {line}")
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
