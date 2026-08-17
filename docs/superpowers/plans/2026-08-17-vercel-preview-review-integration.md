# Vercel Preview-Review Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an optional, deterministic Vercel preview-review module that converts protected deployment observations into bounded design-audit evidence without making Vercel a design authority or required host.

**Architecture:** A focused reference and JSON template define the review protocol. A standard-library Python validator enforces preview classification, protection, evidence limitations, and analytics privacy. The existing audit engine consumes normalized preview evidence, while optional Vercel Plugin and MCP metadata remain separate from canonical design upstreams.

**Tech Stack:** Markdown, JSON, Python 3.11 standard library, `unittest`.

## Global Constraints

- Vercel is an optional operational adapter, never a canonical design authority.
- Do not migrate or deploy `innerself.love` automatically.
- Sensitive and unknown previews require verified protection.
- Automated accessibility evidence never replaces keyboard, screen-reader, content-integrity, or truth checks.
- Web Analytics and Speed Insights remain optional.
- Never place real therapy, hypnosis, mental-health, medical, crisis, memory, credential, or production-user data in fixtures, comments, analytics, or custom events.
- No Vercel credentials or tokens may be stored in repository files.
- Tests must pass offline.

---

### Task V1: Integration Metadata and Canonical Reference

**Files:**
- Create: `INTEGRATIONS.lock.json`
- Create: `integrations/vercel/README.md`
- Create: `skills/design/references/vercel-preview-review.md`
- Create: `templates/VERCEL-REVIEW.json`
- Modify: `skills/design/SKILL.md`
- Modify: `README.md`
- Test: `tests/test_vercel_contract.py`

**Interfaces:**
- `INTEGRATIONS.lock.json` records optional integration IDs, pins, licenses, and activation conditions.
- The review template is the public manifest contract consumed by Task V2.

- [ ] Write failing contract tests for the separate Vercel pin, optional-language requirement, plugin/MCP distinction, protected-preview rule, explicit accessibility limitations, analytics opt-in, sensitive-data prohibition, and valid JSON template.
- [ ] Run `python -m unittest tests.test_vercel_contract -v`; confirm missing-file failures.
- [ ] Pin `vercel/vercel-plugin` version `0.48.0`, commit `11c32588786a9d49791372657433b88d49561874`, license `Apache-2.0`, reviewed `2026-08-17`.
- [ ] Write the integration guide with separate deployment, Plugin, and MCP sections and explicit telemetry disclosure.
- [ ] Add a small optional Vercel entry to the canonical skill and README; do not add it to the authority order.
- [ ] Run the contract tests and commit `docs: add optional Vercel preview review contract`.

---

### Task V2: Offline Review Validator

**Files:**
- Create: `design_os/vercel.py`
- Create: `scripts/validate-vercel-review.py`
- Test: `tests/test_vercel.py`

**Interfaces:**
- Produces: `VercelReview`, `VercelFinding`, `validate_review(payload)`, and `load_review(path)`.
- Stable finding codes: `vercel.preview-unclassified`, `vercel.preview-unprotected`, `vercel.toolbar-missing`, `vercel.accessibility-manual-missing`, `vercel.analytics-no-decision`, `vercel.analytics-sensitive-event`, `vercel.sensitive-fixture`, and `vercel.evidence-incomplete`.

- [ ] Write failing tests for sensitive/unprotected preview, unknown classification, protected preview, public-safe accepted risk, missing manual keyboard/screen-reader checks, analytics default undecided, prohibited custom-event fields, and sensitive fixture notes.
- [ ] Run `python -m unittest tests.test_vercel -v`; confirm missing-module failure.
- [ ] Implement pure validation with no network calls. Unknown or absent evidence remains a finding.
- [ ] Implement CLI output as JSON or Markdown with non-zero exit for blocking findings.
- [ ] Run focused tests and validate `templates/VERCEL-REVIEW.json`.
- [ ] Commit `feat: validate Vercel preview review evidence`.

---

### Task V3: Canonical Audit Integration

**Files:**
- Modify: `design_os/audit.py`
- Modify: `templates/DESIGN-AUDIT.json`
- Modify: `skills/design/references/audit-schema.md`
- Modify: `tests/test_audit.py`
- Test: `tests/test_vercel_audit_integration.py`

**Interfaces:**
- `audit_manifest()` accepts optional `preview_evidence` containing a normalized Vercel review.
- Vercel findings are namespaced and cannot convert absent manual evidence into a pass.

- [ ] Write failing tests proving a protected, clean Toolbar run can add evidence but cannot satisfy screen-reader or content-integrity gates; an unprotected sensitive preview blocks delivery; and absence of Vercel evidence is neutral for projects not using Vercel.
- [ ] Run the focused tests and confirm expected failure.
- [ ] Integrate `validate_review()` as an optional evidence provider.
- [ ] Update schema and starter manifest without making `preview_evidence` required.
- [ ] Run all audit and Vercel tests.
- [ ] Commit `feat: integrate Vercel evidence into design audit`.

---

### Task V4: Inner Self Adoption Note and Verification

**Files:**
- Modify: `projects/innerself-love/DESIGN.md`
- Modify: `projects/innerself-love/DECISION-LOG.md`
- Create: `projects/innerself-love/surfaces/vercel-preview-review.md`
- Modify: `tests/test_project.py`
- Modify: `tests/test_smoke.py`
- Modify: `scripts/verify.py`

**Interfaces:**
- The profile names Vercel preview review as a future optional surface after source-repository identification.
- It explicitly states that production hosting is unknown and unchanged.

- [ ] Add failing tests for the hosting-unknown statement, no-migration boundary, protected-preview requirement, and privacy-sensitive event prohibition.
- [ ] Run focused tests and confirm failure.
- [ ] Add the profile surface and decision record.
- [ ] Add Vercel contract and validator checks to the repository verifier.
- [ ] Run `python scripts/verify.py` and confirm all core and integration tests pass.
- [ ] Commit `feat: adopt protected Vercel review for Inner Self design work`.
