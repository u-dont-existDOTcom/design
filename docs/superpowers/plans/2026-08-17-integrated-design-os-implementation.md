# Integrated Design OS Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a repository-native, framework-neutral design operating system that synthesizes Impeccable, Perception-First Design, UI UX Pro Max, and Hallmark; persists project design truth; generates agent adapters; audits design decisions; and provides an evidence-based `innerself.love` profile.

**Architecture:** Canonical behavior lives in `skills/design/SKILL.md` and focused documents under `core/`. A Python 3.11 standard-library package supplies deterministic policy, audit, query, project-initialization, adapter-generation, installation, and upstream-drift commands. Original JSON knowledge catalogs provide an offline floor; optional upstream adapters may enrich results but never override canonical authority rules.

**Tech Stack:** Markdown, JSON, Python 3.11 standard library, `unittest`, GitHub Actions.

## Global Constraints

- Explicit user instructions and supplied factual or content truth outrank all framework guidance.
- Never silently weaken, sanitize, shorten, or replace user-supplied arguments to make a layout easier.
- Never invent metrics, testimonials, logos, citations, capabilities, outcomes, or proof.
- Lower perceptual layers L0 through L4 outrank higher-layer optimization.
- Refinement preserves incumbent identity, behavior, routes, and component ownership; redesign replaces the visual world only when explicitly authorized.
- Anti-slop rules are heuristics. A coherent, brief-supported intentional deviation is permitted and documented.
- Future relevant design work must recover the current repository head and load `skills/design/SKILL.md` before acting.
- The canonical workflow must work without any optional upstream runtime.
- Upstream pins may be checked for drift but must never update silently.
- No font binaries may be committed.
- Python implementation must use the standard library only.
- Visual verification is bounded to one inspection pass, one batched correction, and at most one confirmation pass.
- Continue automatically when one candidate clearly dominates; ask only when material trade-offs remain, product truth is unavailable, or destructive changes require authorization.

---

## Task 1: Policy Kernel

**Files:**
- Create: `pyproject.toml`
- Create: `design_os/__init__.py`
- Create: `design_os/policy.py`
- Test: `tests/test_policy.py`

**Interfaces:**
- Produces: `Candidate`, `DirectionDecision`, `choose_direction()`, `applicable_states()`, `AUTHORITY_ORDER`, `SURFACE_MODES`, and `PERCEPTUAL_LAYERS`.
- Consumed by: audit engine, skill contract tests, project initialization, and CLI.

- [ ] Write tests first for a clearly dominant candidate, materially close candidates, candidates with unmet requirements, inert component states, fine-pointer hover, and asynchronous outcome states.

```python
from design_os.policy import Candidate, applicable_states, choose_direction


def test_clear_winner_continues_without_human_gate():
    result = choose_direction([
        Candidate("evidence-first", 0.91),
        Candidate("generic-wellness", 0.67),
    ])
    assert result.action == "select"
    assert result.selected == "evidence-first"


def test_async_action_requires_outcome_states():
    assert applicable_states(
        interactive=True,
        fine_pointer=True,
        asynchronous=True,
        reports_outcome=True,
    ) == (
        "default", "hover", "focus-visible", "active", "disabled",
        "loading", "error", "success",
    )
```

- [ ] Run `python -m unittest tests.test_policy -v`; confirm failure because `design_os.policy` is absent.
- [ ] Implement immutable dataclasses and pure functions. `choose_direction()` filters candidates with unmet requirements, sorts survivors by score, auto-selects a sole survivor or a lead of at least `0.12`, and otherwise returns `action="ask"`.
- [ ] Run `python -m unittest tests.test_policy -v`; confirm all tests pass.
- [ ] Commit with `feat: add canonical design policy kernel`.

---

## Task 2: Canonical Guidance, Templates, and Repository Contract

**Files:**
- Create: `README.md`, `AGENTS.md`, `ATTRIBUTIONS.md`, `UPSTREAMS.lock.json`
- Create: all six `core/*.md` canonical documents
- Create: `skills/design/SKILL.md`
- Create: `skills/design/references/operations.md`
- Create: `skills/design/references/audit-schema.md`
- Create: `skills/design/references/project-context.md`
- Create: all five `templates/*` files
- Create: three `knowledge/*/catalog.json` files
- Create: `docs/source-evaluations/2026-08-17-upstream-synthesis.md`
- Test: `tests/test_repository_contract.py`

**Interfaces:**
- Canonical read order: repository instructions; project `PRODUCT.md`; project `DESIGN.md`; relevant `surfaces/*.md`; authority rules; perceptual diagnosis; one operation reference; target implementation evidence.
- The skill routes `init`, `shape`, `build`, `refine`, `redesign`, `study`, `critique`, `audit`, `polish`, `harden`, `query`, `doctor`, and `sync-upstreams`.

- [ ] Write repository-contract tests first.

```python
ROOT = pathlib.Path(__file__).resolve().parents[1]


def test_required_canonical_files_exist():
    required = [
        "README.md", "AGENTS.md", "ATTRIBUTIONS.md", "UPSTREAMS.lock.json",
        "core/DESIGN-OPERATING-SYSTEM.md",
        "core/AUTHORITY-AND-CONFLICTS.md",
        "core/PERCEPTUAL-DIAGNOSIS.md",
        "core/PATTERN-SELECTION.md",
        "core/ANTI-SLOP-GATE.md",
        "core/PRODUCTION-VERIFICATION.md",
        "skills/design/SKILL.md",
    ]
    assert not [path for path in required if not (ROOT / path).is_file()]
```

- [ ] Add tests that the skill contains the truth, argument-preservation, lower-layer, live-head, auto-continuation, and bounded-QA rules; JSON catalogs parse; templates contain no ambiguous incomplete markers; no `.ttf`, `.otf`, `.woff`, or `.woff2` files exist.
- [ ] Run `python -m unittest tests.test_repository_contract -v`; verify missing-file failures.
- [ ] Write original synthesis documents rather than copying upstream prose. Keep Perception-First Design attribution and trademark boundaries explicit.
- [ ] Create original catalog entries using the stable keys `id`, `domain`, `title`, `keywords`, `modes`, `stacks`, `guidance`, and `avoid`. Cover Read, Persuade, Operate, Experience, Ghost, generic web, React/Next.js, accessibility, responsive text, factual integrity, and anti-slop concerns.
- [ ] Run the repository-contract tests; confirm all pass.
- [ ] Commit with `feat: establish canonical design operating system`.

---

## Task 3: Offline Design-Intelligence Query Engine

**Files:**
- Create: `design_os/query.py`
- Create: `scripts/design-query.py`
- Test: `tests/test_query.py`

**Interfaces:**
- Produces: `CatalogEntry`, `QueryResult`, `QueryError`, `load_catalogs()`, `validate_query()`, and `search_catalog()`.
- CLI supports `--domain`, `--mode`, `--stack`, `--limit`, and `--format`.

- [ ] Write tests first for long-form Read matching, stack matching, stable tie ordering, zero-score rejection, and broad multi-problem query rejection.

```python
def test_read_query_prefers_long_form_pattern():
    results = search_catalog(
        "long form article", domain="pattern", mode="read", root="knowledge"
    )
    assert results[0].entry_id == "read-long-form"


def test_broad_multi_problem_query_is_rejected():
    with pytest_raises(QueryError):
        validate_query("typography, checkout, animation, charts, icons, mobile, pricing, forms")
```

Use `unittest` helpers in the actual test file; the pseudo-helper above only names the expected exception.

- [ ] Run `python -m unittest tests.test_query -v`; verify missing-module failure.
- [ ] Implement deterministic token overlap scoring, with boosts for exact domain, surface mode, and stack. Require at least two meaningful terms. Reject more than ten terms, more than two commas, or more than one semicolon as lacking one dominant concern.
- [ ] Run tests and `python scripts/design-query.py "long form article" --domain pattern --mode read --format markdown`; confirm `read-long-form` ranks first.
- [ ] Commit with `feat: add offline design intelligence search`.

---

## Task 4: Structured Design Audit Engine

**Files:**
- Create: `design_os/audit.py`
- Create: `scripts/audit-design.py`
- Test: `tests/test_audit.py`
- Finalize: `skills/design/references/audit-schema.md`
- Finalize: `templates/DESIGN-AUDIT.json`

**Interfaces:**
- Produces: `Finding`, `AuditReport`, and `audit_manifest(manifest)`.
- Consumes: `applicable_states()` and `PERCEPTUAL_LAYERS`.

- [ ] Write tests first for unverified metrics, unauthorized argument changes, missing L0–L4 layers, downstream passes blocked by lower-layer failure, accessibility omissions, missing responsive widths, missing component states, undocumented intentional deviations, and excess verification passes.

```python
def test_unverified_metric_fails_truth_gate():
    manifest = valid_manifest()
    manifest["claims"] = [{
        "kind": "metric",
        "text": "Trusted by 50,000 people",
        "verified": False,
        "provided_by_user": False,
    }]
    report = audit_manifest(manifest)
    assert "truth.unverified-claim" in {finding.code for finding in report.findings}
```

- [ ] Run `python -m unittest tests.test_audit -v`; verify missing-module failure.
- [ ] Implement gates in this order: truth; unauthorized content change; perceptual dependency stack; accessibility; responsive widths and scaling; applicable states; anti-slop deviations; performance; consistency; two-pass visual-verification budget.
- [ ] Use stable codes including `truth.unverified-claim`, `content.unauthorized-change`, `perception.missing-layer`, `perception.blocked-downstream`, `accessibility.missing`, `responsive.width-missing`, `state.missing`, `deviation.no-rationale`, and `verification.pass-budget`.
- [ ] Run tests and a CLI audit of the starter manifest.
- [ ] Commit with `feat: add ordered production gate audit`.

---

## Task 5: Deterministic Agent Adapters and Installer

**Files:**
- Create: `design_os/adapters.py`
- Create: `scripts/generate-adapters.py`
- Create: `scripts/install.py`
- Generate: `adapters/codex/SKILL.md`, `adapters/claude/SKILL.md`, `adapters/opencode/SKILL.md`, `adapters/generic-agent/SKILL.md`
- Test: `tests/test_adapters.py`

**Interfaces:**
- Produces: `canonical_digest()`, `render_adapter()`, `generate_adapters()`, and `install_adapter()`.
- Destinations: `.codex/skills/design`, `.claude/skills/design`, `.opencode/skills/design`, `.agents/skills/design`.

- [ ] Write tests first for deterministic generation, a canonical SHA-256 marker, generated-file drift detection, copying references, and refusal to overwrite local customizations without `force=True`.
- [ ] Run `python -m unittest tests.test_adapters -v`; verify missing-module failure.
- [ ] Generate each adapter with a `DO NOT EDIT` header naming `skills/design/SKILL.md`, a 64-character lowercase SHA-256 digest, and the platform. Append canonical skill content unchanged.
- [ ] Implement installation of the adapter, canonical references, and `.design-os-source.json`. Scan all target conflicts before writing anything.
- [ ] Run `python scripts/generate-adapters.py --write`, `python scripts/generate-adapters.py --check`, and the adapter tests.
- [ ] Commit with `feat: generate and install deterministic design adapters`.

---

## Task 6: Upstream Lock Validation and Drift Reporting

**Files:**
- Create: `design_os/upstreams.py`
- Create: `scripts/check-upstream-drift.py`
- Finalize: `UPSTREAMS.lock.json`
- Finalize: `ATTRIBUTIONS.md`
- Test: `tests/test_upstreams.py`

**Interfaces:**
- Produces: `Upstream`, `DriftResult`, `load_lock()`, `validate_lock()`, and `check_drift()`.
- Live network fetch is injectable for tests and only reports; it never writes pins.

- [ ] Write tests first for all four source IDs, required fields, 40-character lowercase commit validation, license presence, injected drift, no mutation, and offline reporting.
- [ ] Run `python -m unittest tests.test_upstreams -v`; verify missing-module failure.
- [ ] Implement lock validation and GitHub public-ref lookup using `urllib.request` with a finite timeout and a descriptive User-Agent.
- [ ] Pin these reviewed heads:

```text
Impeccable:              5c5553b1d7f9e89bb833f9179cea681742a17720
Perception-First Design: 1704ff61c18872a66d969e860c9b6e45a8f50f16
UI UX Pro Max:           a38d04c3d5c298c851dbe5e6ee1965ee3de42cb5
Hallmark:                13ac0ec7e148655948100b6396439e481361d690
```

- [ ] Record observed versions `4.1.1`, `3.6`, `2.0`, and `1.1.0` and reviewed date `2026-08-17`.
- [ ] Run tests and `python scripts/check-upstream-drift.py --offline`.
- [ ] Commit with `feat: pin and audit upstream design sources`.

---

## Task 7: Safe Project Initialization and `innerself.love` Profile

**Files:**
- Create: `design_os/project.py`
- Create: `scripts/init-project.py`
- Create: `projects/innerself-love/PRODUCT.md`
- Create: `projects/innerself-love/DESIGN.md`
- Create: `projects/innerself-love/surfaces/README.md`
- Create: `projects/innerself-love/surfaces/homepage.md`
- Create: `projects/innerself-love/surfaces/article.md`
- Create: `projects/innerself-love/DECISION-LOG.md`
- Test: `tests/test_project.py`

**Interfaces:**
- Produces: `initialize_project(destination, project_name, project_slug, force=False)`.
- Writes `PRODUCT.md`, `DESIGN.md`, `surfaces/README.md`, `DECISION-LOG.md`, and `.design-os.json` only after a complete conflict scan.

- [ ] Write tests first for materialization, replacement of `{{PROJECT_NAME}}` and `{{PROJECT_SLUG}}`, preservation of explicit `[REQUIRED: owner-supplied fact]` markers, no partial writes, and no overwrite without force.
- [ ] Run `python -m unittest tests.test_project -v`; verify missing-module failure.
- [ ] Implement staging-directory materialization and atomic moves. Substitute only the two named project tokens; never infer factual claims from a project name or category.
- [ ] Build the evidence-based Inner Self profile from public pages reviewed on `2026-08-17` and owner-supplied context. Record unknown analytics, conversion data, and Ghost theme implementation explicitly.
- [ ] Encode primary mode `Read`; homepage hybrid `Read + Persuade`; audience paths for preview, method, and safety; source-visible/protector-first/no-trance/memory-humility truth; hard non-therapy and non-crisis boundaries; long-form reading, table, citation, mobile-navigation, and idiolect-preservation requirements; and a prohibition on defaulting to generic pastel wellness styling.
- [ ] Run tests and a temporary initialization smoke command.
- [ ] Commit with `feat: add safe project initialization and Inner Self profile`.

---

## Task 8: Unified CLI, Smoke Tests, and CI Verification

**Files:**
- Create: `design_os/cli.py`
- Create: `design_os/__main__.py`
- Create: `scripts/verify.py`
- Create: `tests/test_smoke.py`
- Create: `.github/workflows/verify.yml`
- Modify: `README.md`
- Modify: `AGENTS.md`

**Interfaces:**
- `python -m design_os query ...`
- `python -m design_os audit ...`
- `python -m design_os adapters --check|--write`
- `python -m design_os install --platform ... --target ...`
- `python -m design_os upstreams --offline`
- `python -m design_os init <destination> --name ... --slug ...`
- `python -m design_os verify`

- [ ] Write an end-to-end smoke test first that initializes a temporary project, executes a Read-mode query, checks generated adapters, validates the upstream lock offline, and runs an audit manifest.
- [ ] Run `python -m unittest tests.test_smoke -v`; verify failure because `design_os.__main__` is absent.
- [ ] Implement argparse dispatch without third-party dependencies.
- [ ] Implement `scripts/verify.py` to print and run, in order: `python -m unittest discover -s tests -v`; adapter `--check`; upstream `--offline` validation. Return the first non-zero exit status.
- [ ] Add a GitHub Actions workflow using `actions/checkout@v4`, `actions/setup-python@v5` with Python `3.11`, and `python scripts/verify.py`; do not add a dependency-install step.
- [ ] Run `python scripts/verify.py`; confirm all tests, adapter drift, upstream schema, no-font, and smoke checks pass with clean output.
- [ ] Commit with `feat: complete integrated design OS workflow`.

---

## Self-Review

The tasks cover the canonical workflow, durable context, perceptual ordering, searchable intelligence, anti-slop and production gates, deterministic adapters, source pinning and drift, the first consumer profile, degraded mode, tests, and CI. The interfaces retain consistent names across tasks. No incomplete implementation instruction remains; project templates use the explicit marker `[REQUIRED: owner-supplied fact]` rather than invented content.