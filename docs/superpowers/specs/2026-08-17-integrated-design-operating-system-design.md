# Integrated Design Operating System

**Status:** Approved architecture  
**Date:** 2026-08-17  
**Repository:** `u-dont-existDOTcom/design`  
**Decision:** Original synthesis with pinned upstream adapters

## 1. Purpose

This repository will be the canonical design methodology and reusable agent skill for Joel's projects. It will synthesize the strongest compatible parts of four upstream systems:

- Impeccable
- Perception-First Design
- UI UX Pro Max
- Hallmark

The repository will not merely collect those projects. It will resolve their overlaps and conflicts into one coherent operating system for websites, application interfaces, components, design systems, brand surfaces, reading experiences, audits, redesigns, and production verification.

The first named consumer is `innerself.love`, but the architecture must remain project-neutral and reusable across future work.

Interactive web and application design are the first implementation priority. Non-interactive visual artifacts such as presentations, reports, diagrams, and social graphics may reuse the system's product-truth, hierarchy, perception, anti-slop, token, and verification modules. Their medium-specific production rules remain delegated to the relevant artifact skill rather than being duplicated here.

## 2. Activation rule

For future work, agents must load the live `skills/design/SKILL.md` from this repository before acting whenever the task concerns or would materially benefit from:

- UI or UX design;
- frontend visual implementation;
- website or application redesign;
- long-form reading experience;
- visual hierarchy, typography, color, layout, motion, or interaction design;
- component design or component-state review;
- design-system creation or extraction;
- accessibility, responsiveness, or visual production audits;
- brand-surface or visual-artifact decisions covered by the reusable modules.

The live repository is authoritative over remembered copies. The agent must recover the current repository head rather than assuming a previous conversation contains the latest rules.

## 3. Goals

The system must:

1. Preserve product truth, supplied copy, factual claims, routes, behavior, and established identity unless the user explicitly authorizes changes.
2. Diagnose perceptual and usability failures before selecting visual treatments.
3. Produce designs with a clear point of view rather than generic AI styling.
4. Use searchable design intelligence without allowing a catalog to dictate the design.
5. Detect structural and visual AI clichés before shipping.
6. Enforce accessibility, responsive behavior, applicable interaction states, performance, and factual integrity as production requirements.
7. Persist project-specific product and design decisions so later agents do not rediscover them.
8. Provide one canonical skill source with generated or installed adapters for Codex, Claude Code, OpenCode, Cursor-compatible agents, and generic agent runtimes.
9. Pin upstream versions and make upstream drift visible without silently changing canonical behavior.
10. Remain useful when optional upstream tooling is inaccessible.
11. Continue automatically through routine design decisions; request human intervention only when materially competing directions remain, product truth is unavailable, or destructive changes require authorization.

## 4. Non-goals

The repository will not:

- merge the four upstream repositories wholesale;
- treat any upstream aesthetic preference as universally correct;
- replace a project's established visual identity merely because a catalog recommends another style;
- silently rewrite user-supplied arguments, copy, claims, testimonials, or metrics;
- invent proof, testimonials, customer logos, statistics, or capabilities to complete a layout;
- vendor font binaries;
- require a particular frontend framework;
- use unlimited self-critique or polishing loops;
- delete or replace production structures without explicit authorization;
- force a user-approval pause when one direction is clearly superior and no destructive or factual uncertainty remains.

## 5. Upstream roles

### 5.1 Impeccable: workflow and craft architecture

Impeccable contributes:

- durable project context through product, design, and surface briefs;
- separation of surface purposes into **Persuade**, **Operate**, **Read**, and **Experience**;
- explicit operations such as shape, critique, audit, polish, harden, adapt, typeset, layout, and optimize;
- the distinction between refinement, which preserves an incumbent world, and redesign, which intentionally replaces it;
- bounded visual verification rather than open-ended polishing;
- the principle that a clear brief overrides generic taste.

Its exact runtime, command implementation, and complete reference corpus will not become the canonical architecture.

### 5.2 Perception-First Design: ordered diagnosis and ethical constraints

Perception-First Design contributes an ordered dependency stack:

1. **L0 — Cognitive load:** Can the user perceive and act without unnecessary working-memory burden?
2. **L1 — First impression:** Does the surface immediately communicate the right purpose, emotional register, and trust signal?
3. **L2 — Processing fluency:** Is the experience legible, coherent, predictable, and internally consistent?
4. **L3 — Perception bias:** Does the design address what users actually respond to rather than relying only on what they report?
5. **L4 — Decision architecture:** Does the interface create an honest, intelligible path to the user's goal?

Lower-layer failures take precedence over upper-layer optimization. The system must derive requirements at every layer before proposing a solution.

The synthesis also adopts three ethical tests:

- **Alignment:** user and project goals must not be placed in conflict through manipulation;
- **Sincerity:** presentation must match what the user will actually receive;
- **Golden Rule:** the design should remain acceptable when experienced from the user's position.

The repository will use an original summary and operational interpretation rather than copying the upstream framework prose. Attribution and the upstream CC BY-SA 4.0 terms must remain explicit. The Perception-First Design name and trademark must not be presented as the name of this repository's original system.

### 5.3 UI UX Pro Max: searchable design intelligence

UI UX Pro Max contributes:

- searchable product, style, color, typography, landing-page, chart, icon, motion, UX, performance, and implementation-stack knowledge;
- one-dominant-intent queries instead of broad, noisy searches;
- stack-specific implementation guidance;
- a persistent master design system with page- or surface-specific overrides;
- design dials for variance, motion, and density;
- explicit validation of responsive text behavior and compact UI.

Its search results are evidence and options. They cannot override project truth, perceptual requirements, established brand constraints, accessibility, or the user brief.

### 5.4 Hallmark: anti-slop and structural-diversity gates

Hallmark contributes:

- anti-slop review of generic AI visual and structural defaults;
- structural variety, not merely palette variation;
- factual-copy protection and prohibition of fabricated proof;
- token discipline;
- complete applicable interaction-state coverage;
- responsive verification at narrow and intermediate widths;
- preservation of routes, component ownership, information architecture, and implementation boundaries during refinement;
- a pre-delivery self-critique that triggers at most one bounded revision pass.

Its aesthetic prohibitions are heuristics, not constitutional law. Deliberate, coherent, brief-supported deviations are permitted and must be documented. Within one product, consistency is more important than forcing every surface to look unrelated; structural diversification applies primarily across unrelated projects and when an existing project has fallen into a repeated generic pattern.

## 6. Integration modes

Each upstream relationship must be classified in `UPSTREAMS.lock.json`:

| Source | Canonical relationship |
|---|---|
| Impeccable | Conceptual synthesis; optional adapter only where a narrowly useful command can be invoked without importing its entire runtime. |
| Perception-First Design | Conceptual diagnostic and ethical layer with attribution; no copied canonical framework prose. |
| UI UX Pro Max | Conceptual synthesis plus optional executable search adapter against a pinned source revision or CLI release. |
| Hallmark | Conceptual anti-slop and structural-review layer; optional adapter only where results can be normalized through this repository's authority rules. |

Optional executable adapters may enrich a result, but no upstream runtime is required for the canonical workflow to function.

## 7. Authority and conflict resolution

When instructions conflict, use this precedence order:

1. Explicit user instruction and supplied factual or content truth.
2. The project's durable `PRODUCT.md`, `DESIGN.md`, and surface brief.
3. Functional correctness, accessibility, safety, ethics, and legal constraints.
4. Lower-layer perceptual requirements before higher-layer requirements.
5. Existing framework, route, component, and deployment constraints.
6. Deliberate project identity and cross-surface consistency.
7. Searchable pattern and implementation guidance.
8. Anti-pattern heuristics and aesthetic preferences.
9. Agent taste.

### Required conflict behavior

- **Brief versus anti-pattern:** preserve a deliberate brief. Record why the deviation is intentional.
- **Brand versus catalog result:** brand wins. Use the catalog to refine execution, not replace identity.
- **Perceptual clarity versus novelty:** clarity wins at the failing lower layer. Novelty may be reintroduced after the lower layer passes.
- **Cross-project variety versus within-project consistency:** vary across unrelated projects; preserve a coherent family within one product.
- **User copy versus layout convenience:** copy wins. Change the layout rather than silently shortening, sanitizing, or replacing the argument.
- **Aesthetic polish versus factual integrity:** factual integrity wins absolutely.
- **Clearly superior direction versus approval ritual:** choose the superior direction and continue. Ask only when trade-offs are genuinely close or require a human preference.

## 8. Canonical workflow

### Stage 0 — Recover current state

Before design work:

- read repository instructions and the live project head;
- inspect product, design, and surface context;
- inspect representative incumbent tokens, styles, components, assets, and routes;
- determine whether the task is greenfield, refinement, redesign, audit, or a component-level change;
- identify whether production deletion or replacement is implicated.

No destructive assumption is permitted from a missing `DESIGN.md` alone.

### Stage 1 — Classify the surface

Classify both scope and mode.

**Scope:**

- product or brand system;
- multi-surface application;
- page or route;
- section;
- component;
- audit or study;
- non-interactive visual artifact using the reusable modules.

**Mode:**

- **Persuade:** help the visitor decide and act;
- **Operate:** help the user complete a task;
- **Read:** help the reader understand sustained content;
- **Experience:** let the work itself dominate the interface.

The mode belongs to the surface, not the company category.

### Stage 2 — Establish truth and success criteria

Load or create durable project context:

- `PRODUCT.md` — audience, jobs, product truth, claims, constraints, risks, and success criteria;
- `DESIGN.md` — visual principles, tokens, typography, color, imagery, motion, component voice, and intentional deviations;
- one file under `surfaces/` — mode, task, primary user path, content hierarchy, page-specific constraints, and deviations from `DESIGN.md`.

A narrow refinement may proceed from incumbent implementation evidence. The absence of durable context should be reported and repaired as part of project hardening rather than filled with invented product facts.

### Stage 3 — Perceptual diagnosis before solutions

For L0 through L4, record:

- the constraint;
- current evidence;
- the violation or risk;
- a non-negotiable requirement.

Do not select a visual solution until the accumulated requirement set is complete. When requirements conflict, the lower layer wins.

### Stage 4 — Generate and compare candidate directions

Use project evidence and optional searchable design intelligence to form two or three materially different directions when the visual world is not already fixed.

Candidates must differ in structure or experience, not merely color. Each candidate must be tested against:

- all perceptual requirements;
- surface mode;
- project identity;
- implementation constraints;
- content truth;
- accessibility and performance risk;
- generic-AI-pattern risk.

When one candidate clearly dominates, select it and continue. Present a human choice only when materially competing candidates survive. Persist the chosen direction in `DESIGN.md` or the relevant surface override.

### Stage 5 — Implement within explicit boundaries

Implementation rules:

- use the project's real stack and conventions;
- use semantic or project tokens rather than uncontrolled one-off values;
- preserve supplied content and claims unless edits are explicitly authorized;
- preserve routes and component ownership during refinement;
- avoid deleting production files without explicit authorization;
- provide all interaction states applicable to the component's semantics;
- use one coherent icon voice per product;
- use real assets or clearly marked placeholders rather than fabricated proof;
- support reduced motion and keyboard operation;
- treat long text, localization, zoom, and narrow viewports as normal conditions.

### Stage 6 — Production gates

Run the following gates in order:

1. **Truth gate:** no invented metrics, testimonials, logos, citations, capabilities, or outcomes.
2. **Argument-preservation gate:** no silent weakening, sanitizing, or substitution of user-supplied claims.
3. **Perceptual gate:** L0 through L4 requirements pass, with lower-layer failures blocking downstream approval.
4. **Accessibility gate:** semantics, labels, focus order, visible focus, contrast, keyboard use, reduced motion, and non-color state communication.
5. **Responsive gate:** verify at 320, 375, 414, 768, 1024, and 1440 CSS pixels where applicable; ensure zoom and text scaling do not clip essential content.
6. **State gate:** every interactive component documents and implements applicable states. Default, focus-visible, active, and disabled are normally required. Hover applies where a fine pointer exists. Loading, error, and success are required for asynchronous or stateful actions and may be marked not applicable for purely navigational or inert controls.
7. **Anti-slop gate:** check both structural and visual generic-AI signatures while respecting documented intentional deviations.
8. **Performance gate:** avoid unnecessary blocking assets, layout instability, oversized media, and interaction jank.
9. **Consistency gate:** confirm tokens, typography, spacing, imagery, and component behavior remain coherent with the product system.

### Stage 7 — Bounded visual verification

For executable UI work:

- build the complete scoped change;
- inspect desktop and mobile together in one batched pass;
- fix the observed defect set in one batch;
- perform at most one confirmation pass;
- stop unless a named acceptance criterion still fails.

This limit applies to screenshots, micro-edits, rebuilds, and aesthetic self-critique collectively.

### Stage 8 — Persist decisions and learnings

After completion:

- update project design truth only when the implementation intentionally changes it;
- append significant decisions to `DECISION-LOG.md`;
- record reusable lessons in this repository rather than leaving them in conversation state;
- update pinned upstream metadata only through the explicit synchronization workflow;
- keep project-specific lessons separate from universal rules until they survive reuse.

## 9. Repository architecture

```text
design/
├── README.md
├── AGENTS.md
├── ATTRIBUTIONS.md
├── UPSTREAMS.lock.json
├── core/
│   ├── DESIGN-OPERATING-SYSTEM.md
│   ├── AUTHORITY-AND-CONFLICTS.md
│   ├── PERCEPTUAL-DIAGNOSIS.md
│   ├── PATTERN-SELECTION.md
│   ├── ANTI-SLOP-GATE.md
│   └── PRODUCTION-VERIFICATION.md
├── templates/
│   ├── PRODUCT.md
│   ├── DESIGN.md
│   ├── SURFACE.md
│   ├── DESIGN-AUDIT.md
│   └── DECISION-LOG.md
├── skills/
│   └── design/
│       ├── SKILL.md
│       └── references/
├── knowledge/
│   ├── anti-patterns/
│   ├── patterns/
│   └── stack-rules/
├── adapters/
│   ├── codex/
│   ├── claude/
│   ├── opencode/
│   └── generic-agent/
├── scripts/
│   ├── install.sh
│   ├── design-query.py
│   ├── audit-design.py
│   ├── check-upstream-drift.py
│   └── generate-adapters.py
├── projects/
│   └── innerself-love/
│       ├── PRODUCT.md
│       ├── DESIGN.md
│       ├── surfaces/
│       │   ├── README.md
│       │   ├── homepage.md
│       │   └── article.md
│       └── DECISION-LOG.md
├── tests/
│   ├── policy/
│   ├── fixtures/
│   └── smoke/
└── docs/
    ├── source-evaluations/
    └── superpowers/specs/
```

### Single-source rule

`skills/design/SKILL.md` and the files under `core/` are canonical. Platform adapters must be generated or installed from those sources. Generated copies must not be edited manually. CI must detect adapter drift.

## 10. Command surface

The canonical skill will support these conceptual operations:

| Operation | Purpose |
|---|---|
| `init` | Capture durable product and design context. |
| `shape` | Diagnose and specify a design problem before implementation. |
| `build` | Create a new surface after requirements and direction are resolved. |
| `refine` | Improve the incumbent design while preserving identity and behavior. |
| `redesign` | Replace the visual world while preserving product truth and required behavior. |
| `study` | Extract transferable design DNA from a reference without cloning it. |
| `critique` | Evaluate experience, hierarchy, content flow, and perceptual performance. |
| `audit` | Evaluate accessibility, responsiveness, states, implementation quality, and performance. |
| `polish` | Perform the bounded final craft pass. |
| `harden` | Address edge cases, errors, localization, long content, and failure states. |
| `query` | Search optional upstream design intelligence for one dominant concern. |
| `doctor` | Report drift in project context, adapters, source pins, and generated artifacts. |
| `sync-upstreams` | Inspect newer upstream revisions and prepare an explicit review; never silently alter canonical behavior. |

The implementation may expose platform-specific command syntax, but behavior and precedence remain canonical here.

## 11. Upstream pinning and updates

`UPSTREAMS.lock.json` will record, for every source:

- repository URL;
- pinned commit SHA;
- observed release or version when available;
- license;
- selected concepts, files, or optional adapters;
- last review date;
- whether the relationship is conceptual, executable, or both.

`check-upstream-drift.py` will report newer upstream heads. It must not update pins or canonical rules automatically.

An upstream update follows this sequence:

1. fetch metadata for the pinned and current upstream revisions;
2. identify changed source areas relevant to the integration;
3. produce a source-evaluation note;
4. classify changes as compatible, conflicting, redundant, or irrelevant;
5. update canonical behavior only through a reviewed commit;
6. update attribution and lock metadata together;
7. run policy and smoke tests.

## 12. Licensing and attribution

- Impeccable is Apache-2.0.
- UI UX Pro Max is MIT.
- Hallmark is MIT.
- Perception-First Design's canonical framework is CC BY-SA 4.0 and its name is trademarked.

The repository will prefer original synthesis and links over copying substantial upstream prose. Any copied or adapted source must retain the required notices and be isolated clearly enough to preserve its license.

Applying Perception-First Design's methodology is described upstream as exempt from creating a share-alike derivative; this repository will nevertheless attribute the framework and avoid presenting the upstream trademark as the name of this original system.

No repository-wide open-source license is currently declared. Until the owner deliberately adds one, original synthesis files remain under default copyright, while third-party material retains its own license.

Font binaries will not be copied from upstream repositories. Font recommendations may reference licensed public fonts, and each consuming project remains responsible for its own font loading and license compliance.

## 13. Error and degraded-mode behavior

### Missing project context

Infer from the incumbent implementation when possible. Create or propose durable context files without inventing product facts. Mark unknown facts explicitly.

### Conflicting source guidance

Apply the authority order in Section 7 and record the decision when it materially affects the design system.

### Optional upstream tool unavailable

Continue using the canonical workflow and checked-in original knowledge. Report that catalog search or stack-specific enrichment was unavailable; do not pretend it ran.

### Upstream drift

Report drift without silently updating behavior.

### Insufficient evidence for a claim

Label the recommendation as a heuristic or practitioner judgment. Do not fabricate research, metrics, or authority.

### Ambiguous destructive scope

Preserve existing production files and choose an additive or in-place implementation. Deletions require explicit authorization.

### Design system and implementation disagree

Treat the implementation as evidence, not automatic authority. Classify the discrepancy as stale documentation, accidental drift, or intentional evolution before changing either side.

### Medium-specific artifact rule unavailable

Apply the reusable design modules, then defer production details to the relevant artifact-specific skill. Do not improvise a replacement export or rendering workflow inside this repository.

## 14. Testing strategy

### Policy tests

Tests must verify that the skill:

- never invents metrics, testimonials, logos, citations, or capabilities;
- never silently rewrites user-supplied arguments;
- applies lower-layer perceptual requirements before downstream styling;
- preserves incumbent identity during refinement;
- distinguishes refinement from redesign;
- respects intentional deviations from anti-pattern guidance;
- requires explicit authorization for destructive file changes;
- limits visual QA to the bounded pass budget;
- persists project truth separately from universal guidance;
- continues automatically when one direction clearly dominates;
- loads the live canonical skill for relevant future design work.

### Fixture scenarios

At minimum:

1. a long-form reading site such as `innerself.love`;
2. a persuasive landing page;
3. an expert dashboard where option density is legitimate;
4. a single interactive component with semantically applicable states;
5. an established branded project requesting refinement;
6. an explicit redesign request;
7. a deliberately brutalist or maximalist brief that should not be normalized;
8. a project containing unsupported metrics that the system must not repeat as fact;
9. an inaccessible upstream catalog requiring degraded mode;
10. two unrelated projects that should not receive the same generic macrostructure;
11. a non-interactive visual artifact that reuses the canonical modules but delegates medium-specific production.

### Structural tests

- adapter generation is deterministic;
- generated adapters match the canonical skill;
- lock-file schema is valid;
- all attributed sources have licenses recorded;
- internal markdown links resolve;
- no font binaries are committed;
- templates contain no unresolved placeholders outside explicitly marked user-input fields.

### Smoke tests

A temporary fixture project will run:

1. initialization;
2. surface classification;
3. perceptual diagnosis;
4. candidate-direction comparison;
5. production-gate audit;
6. decision persistence;
7. adapter installation in an isolated destination.

## 15. `innerself.love` adoption

The repository will include a project profile for `innerself.love` after the core architecture exists.

The profile must treat it primarily as a **Read** surface, with possible **Persuade** behavior only where a page has a genuine subscription, navigation, or project-introduction objective. It must prioritize:

- sustained reading comfort;
- clear hierarchy for unusually long and conceptually dense material;
- trustworthy presentation without generic wellness styling;
- preservation of Joel's arguments and idiolect;
- citation and footnote legibility;
- mobile reading and navigation;
- article-to-article orientation;
- restrained motion;
- explicit differentiation between editorial content, tools, and calls to action.

The profile will be based on evidence from the live site and its source repository. It will not assume that a generic meditation, therapy, or wellness palette is appropriate.

## 16. Acceptance criteria

The architecture is implemented when:

1. the repository contains the canonical core documents and skill;
2. all four upstream sources are attributed and pinned;
3. a deterministic installer produces usable adapters without manual editing;
4. policy tests cover precedence, truth, argument preservation, perceptual ordering, anti-slop exceptions, automatic continuation, and destructive-change safety;
5. smoke tests pass in an isolated fixture;
6. the `innerself.love` project profile exists and points future work to the canonical workflow;
7. README and agent instructions direct all relevant design work through this repository;
8. upstream drift can be reported without silently changing behavior;
9. no font binaries or unattributed copied framework prose are committed;
10. future design work can recover its architecture from the repository without relying on conversation memory.