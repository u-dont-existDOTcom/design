# Design Operating System

This is the canonical staged workflow. It applies to new surfaces, refinements, redesigns, components, audits, and reusable visual modules.

## Stage 0 — Recover current state

Before design work:

- resolve the live repository and target-project heads;
- read repository instructions and durable project context;
- inspect representative tokens, styles, components, routes, assets, and content;
- identify whether the request is greenfield, refinement, redesign, study, critique, audit, or component scope;
- identify any proposed deletion or replacement.

A missing design document is evidence of missing documentation, not proof that an incumbent identity does not exist.

## Stage 1 — Classify scope and mode

### Scope

- product or brand system;
- multi-surface application;
- page or route;
- section;
- component;
- audit or study;
- non-interactive artifact using reusable modules.

### Mode

- **Persuade:** earn a decision and an honest action.
- **Operate:** support efficient task completion.
- **Read:** support comprehension and sustained attention.
- **Experience:** let the artifact or work dominate.

The mode controls hierarchy, density, motion, proof, and interaction expectations.

## Stage 2 — Establish truth

Load or create:

- `PRODUCT.md`: audience, jobs, facts, claims, boundaries, constraints, success;
- `DESIGN.md`: identity, tokens, typography, color, imagery, motion, component voice, deviations;
- `surfaces/<name>.md`: mode, primary task, content hierarchy, path, and local overrides.

Unknown facts remain explicit. Do not transform an unknown into plausible marketing copy.

## Stage 3 — Diagnose L0 through L4

For each layer record:

1. constraint;
2. observed evidence;
3. violation or risk;
4. non-negotiable requirement;
5. verification method.

Do not select a visual answer before all five requirements exist. When they conflict, the lower layer wins.

## Stage 4 — Generate candidates

When direction is not fixed, generate two or three candidates that differ in structure, hierarchy, or interaction—not merely palette.

Test each against product truth, L0–L4, mode, identity, accessibility, performance, implementation risk, and generic-pattern risk. Reject unmet requirements. Continue automatically when one survivor clearly dominates.

## Stage 5 — Implement inside boundaries

Follow the actual stack, use project tokens, preserve supplied content, preserve routes during refinement, avoid unauthorized deletion, implement applicable states, support keyboard and reduced motion, and treat long text, localization, zoom, and narrow screens as normal.

## Stage 6 — Production gates

Run truth, argument preservation, L0–L4, accessibility, responsive behavior, semantic states, anti-slop, performance, and consistency in order. A lower failure blocks downstream approval.

## Stage 7 — Bounded visual verification

Complete the scope, inspect device classes together, correct the whole defect set in one batch, run at most one confirmation pass, and stop unless a named acceptance criterion remains false.

## Stage 8 — Persist decisions

Update project truth only for intentional changes, record significant choices, keep surface exceptions local, promote lessons only after reuse, and update upstream pins only through reviewed synchronization.

## Degraded mode

The workflow remains functional when optional upstream tools or visual automation are unavailable. Use checked-in guidance, label missing evidence, and never claim an unavailable check passed.
