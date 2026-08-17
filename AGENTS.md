# Agent Instructions

## Repository purpose

This repository is the canonical design methodology for Joel's projects. Do not rebuild its architecture from memory or substitute an upstream skill without first reading the current canonical files.

## Required read order

For repository maintenance:

1. `README.md`
2. `skills/design/SKILL.md`
3. the relevant document under `core/`
4. `UPSTREAMS.lock.json` and `ATTRIBUTIONS.md` when upstream material is involved
5. the applicable implementation plan under `docs/superpowers/plans/`

For design work in a consuming project:

1. that project's repository instructions;
2. its `PRODUCT.md`;
3. its `DESIGN.md`;
4. the relevant file under `surfaces/`;
5. `core/AUTHORITY-AND-CONFLICTS.md`;
6. `core/PERCEPTUAL-DIAGNOSIS.md`;
7. one operation reference from `skills/design/references/operations.md`;
8. representative target code, tokens, assets, routes, and content.

## Authority order

1. Explicit user instruction and supplied factual or content truth.
2. Durable project context.
3. Correctness, accessibility, safety, ethics, and law.
4. Lower perceptual-layer requirements.
5. Existing implementation boundaries.
6. Deliberate project identity and within-product consistency.
7. Verified searched guidance.
8. Anti-pattern heuristics.
9. Agent taste.

Do not use a catalog recommendation, aesthetic rule, or convenient layout to override a higher authority.

## Content integrity

- Never invent metrics, testimonials, logos, citations, capabilities, outcomes, or proof.
- Never silently weaken, sanitize, summarize away, or replace an owner's argument.
- When supplied copy does not fit, change the layout.
- Treat vivid, fluent presentation of unsupported claims as a more serious failure than visibly unfinished presentation.

## Scope safety

- Refinement preserves identity, routes, behavior, content intent, and component ownership.
- Redesign may replace the visual world only when explicitly requested.
- Missing `DESIGN.md` does not prove a project is greenfield.
- Production deletions require explicit authorization.
- Inspect all target conflicts before writing generated or installed files.

## Design process

- Diagnose L0 through L4 before selecting a solution.
- Generate structurally different candidates only when the visual direction is not already fixed.
- Continue automatically when one valid candidate clearly dominates.
- Ask for a human choice only when material trade-offs survive or product truth is missing.
- Document intentional deviations from anti-slop heuristics.
- Verify web work at the applicable widths: 320, 375, 414, 768, 1024, and 1440 CSS pixels.
- Use one inspection pass, one batched correction, and at most one confirmation pass.

## Development rules

- Use Python 3.11+ standard library only.
- Write a failing test before production code.
- Run focused tests after each change and `python scripts/verify.py` before completion.
- Generated adapters must be produced by `scripts/generate-adapters.py`; do not edit them manually.
- Upstream checks may report drift but must not mutate `UPSTREAMS.lock.json`.
- Do not commit `.ttf`, `.otf`, `.woff`, or `.woff2` files.
- Keep original synthesis separate from copied third-party text. Retain required notices for any adapted source.

## Durable learning

Record reusable design lessons in this repository. Keep project-specific findings in that project's profile or decision log until the lesson survives reuse elsewhere.
