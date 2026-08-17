# Integrated Design OS

A canonical, repository-native design methodology for agentic UI and UX work.

This repository synthesizes the strongest compatible parts of four upstream systems without turning them into an undifferentiated bundle:

- **Impeccable** contributes durable product/design context, surface modes, operation routing, and bounded craft verification.
- **Perception-First Design** contributes bottom-up diagnosis, dependency ordering, and an ethical boundary between clarifying real value and manufacturing false value.
- **UI UX Pro Max** contributes searchable pattern, typography, color, UX, motion, and implementation-stack intelligence.
- **Hallmark** contributes structural anti-slop review, factual-copy protection, token discipline, and responsive/state completeness.

The synthesis is original. Upstream projects remain separately licensed and pinned in [`UPSTREAMS.lock.json`](UPSTREAMS.lock.json).

## Mandatory activation

For any task involving UI, UX, frontend visual implementation, website or application redesign, long-form reading experience, visual hierarchy, typography, color, layout, motion, interaction design, component design, design-system work, or visual production audit:

1. recover the current head of this repository;
2. read [`skills/design/SKILL.md`](skills/design/SKILL.md);
3. load the consuming project's `PRODUCT.md`, `DESIGN.md`, and relevant `surfaces/*.md` file;
4. inspect the target implementation before proposing changes.

A remembered copy is not authoritative when the live repository is available.

## Canonical workflow

```text
recover current state
  → classify scope and surface mode
  → establish product and content truth
  → diagnose L0 through L4
  → derive non-negotiable requirements
  → generate materially different candidates
  → select a clear winner or expose a real trade-off
  → implement inside explicit boundaries
  → run truth, accessibility, responsive, state, anti-slop,
    performance, and consistency gates
  → inspect once, correct once, confirm at most once
  → persist decisions and reusable lessons
```

The complete workflow is in [`core/DESIGN-OPERATING-SYSTEM.md`](core/DESIGN-OPERATING-SYSTEM.md).

## Surface modes

- **Persuade:** the visitor decides and acts.
- **Operate:** the user completes a task.
- **Read:** the reader understands sustained material.
- **Experience:** the work itself dominates the interface.

Mode belongs to the surface, not the organization. A software product's article is still Read; a publisher's subscription page may be Persuade.

## Commands

The conceptual command surface is implemented by the canonical skill and the Python CLI:

```bash
python -m design_os init ./project --name "Project Name" --slug project-name
python -m design_os query "long form article" --domain pattern --mode read
python -m design_os audit ./DESIGN-AUDIT.json --format markdown
python -m design_os adapters --check
python -m design_os install --platform codex --target ./project
python -m design_os upstreams --offline
python -m design_os verify
```

Thin script entry points under `scripts/` provide the same functions.

## Project context

A consuming project should contain:

```text
PRODUCT.md
DESIGN.md
surfaces/
  README.md
  <surface>.md
DECISION-LOG.md
```

These files preserve decisions that must survive across agents and sessions. They never authorize invention: unknown project facts remain explicitly unknown.

## First consumer

[`projects/innerself-love/`](projects/innerself-love/) contains the initial profile for `innerself.love`. It treats the site primarily as a long-form Read environment with a Read + Persuade homepage, and explicitly rejects generic wellness styling as a substitute for trust, clarity, source visibility, and argument preservation.

## Installation

Generate adapters from the canonical skill:

```bash
python scripts/generate-adapters.py --write
python scripts/generate-adapters.py --check
```

Install into a project without overwriting local files:

```bash
python scripts/install.py --platform codex --target /path/to/project
```

Supported platform destinations:

| Platform | Destination inside project |
|---|---|
| Codex | `.codex/skills/design/` |
| Claude Code | `.claude/skills/design/` |
| OpenCode | `.opencode/skills/design/` |
| Generic agent | `.agents/skills/design/` |

Pass `--force` only after reviewing the local files that will be replaced.

## Verification

The repository uses Python's standard library only.

```bash
python scripts/verify.py
```

Verification covers unit and smoke tests, generated-adapter drift, upstream lock validity, template contracts, and the prohibition on committed font binaries.

## Upstream drift

```bash
python scripts/check-upstream-drift.py
```

This reports newer upstream heads. It never changes pins or canonical behavior. Integration changes require an explicit source-evaluation note and reviewed commit.

## Licensing

No repository-wide license has been declared for the original synthesis. Upstream material retains its own license. See [`ATTRIBUTIONS.md`](ATTRIBUTIONS.md) for exact relationships and boundaries.
