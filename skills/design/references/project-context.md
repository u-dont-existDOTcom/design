# Durable Project Context

## `PRODUCT.md`

Owns audience, jobs, product truth, claims, boundaries, constraints, risks, success criteria, and unknowns. It must not contain inferred claims presented as facts.

## `DESIGN.md`

Owns design principles, modes, tokens, type roles, color roles, imagery, motion, component voice, density, accessibility posture, and documented deviations.

## `surfaces/*.md`

Owns one surface's mode, primary task, entry conditions, content hierarchy, user path, local overrides, acceptance criteria, and unresolved evidence.

## `DECISION-LOG.md`

Records decisions future agents would otherwise rediscover. It is not a changelog of every CSS edit.

## Precedence

Surface overrides may specialize `DESIGN.md` but cannot contradict `PRODUCT.md`, truth, accessibility, or explicit user instruction. `DESIGN.md` cannot override product facts.

## Unknowns

Use `[REQUIRED: owner-supplied fact]` for facts that must come from the owner. Use `[UNKNOWN: evidence not available]` for evidence that may remain unknown. Do not turn either marker into plausible copy.
