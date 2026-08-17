# Optional Vercel Preview-Review Integration

**Status:** Approved by continuation instruction  
**Date:** 2026-08-17  
**Relationship:** Optional operational adapter to the Integrated Design OS

## 1. Purpose

Add a hosting-neutral Vercel integration module that helps consuming web projects turn branch and pull-request deployments into structured design-review evidence.

Vercel is not a design authority. It supplies execution, collaboration, performance, and browser-observation infrastructure. Every observation remains subordinate to user truth, project context, accessibility, and the canonical L0–L4 workflow.

## 2. Goals

The module must:

1. document when Vercel preview review is useful and when it is unnecessary;
2. distinguish Vercel deployment, Vercel Plugin, and Vercel MCP;
3. require protection review before sharing sensitive previews;
4. normalize Toolbar evidence into a compact JSON manifest;
5. map Vercel observations into the canonical design audit without treating them as complete proof;
6. preserve a manual-review requirement for content integrity, screen readers, keyboard workflows, responsive coverage, and project truth;
7. keep Web Analytics and Speed Insights optional;
8. prohibit sensitive user-entered content from preview fixtures, comments, analytics, and custom events;
9. work without Vercel credentials or network access;
10. pin the optional Vercel Plugin separately from the four design-methodology upstreams.

## 3. Non-goals

The module will not:

- make Vercel the required host;
- deploy or migrate `innerself.love` automatically;
- create or store Vercel tokens;
- install the Vercel Plugin or MCP silently;
- treat automated accessibility checks as complete accessibility verification;
- enable analytics by default;
- add session replay;
- require Next.js or React;
- let Vercel-specific implementation advice override the real project stack.

## 4. Architecture

```text
skills/design/references/vercel-preview-review.md
  ↓
templates/VERCEL-REVIEW.json
  ↓
design_os/vercel.py
  ↓
canonical design audit preview_evidence section
```

Optional companion metadata lives in `INTEGRATIONS.lock.json`, separate from `UPSTREAMS.lock.json`.

## 5. Evidence model

A review record contains:

- project and commit identity;
- preview URL and deployment kind;
- whether protection was checked and enabled where required;
- whether Toolbar review occurred;
- accessibility issue counts by impact and whether interactive-state recording ran;
- layout-shift observations;
- slow-interaction observations and worst measured interaction;
- unresolved and resolved comment counts;
- widths, zoom, text scaling, keyboard, and screen-reader checks performed outside or alongside Toolbar;
- optional Speed Insights environment and collection status;
- optional Web Analytics status and privacy decision;
- reviewer, timestamp, and evidence limitations.

The schema uses explicit unknowns. Missing evidence cannot be converted into a pass.

## 6. Security policy

A preview is classified as `public-safe`, `sensitive`, or `unknown`.

- `public-safe`: no secrets, personal data, unreleased sensitive content, or privileged behavior.
- `sensitive`: contains owner-only work, privileged behavior, protected content, non-public copy, or sensitive fixtures.
- `unknown`: classification has not been completed.

Sensitive and unknown previews fail the protection gate unless protection is verified. Public-safe previews may be unprotected only when the project explicitly accepts public discoverability.

Never place real therapy/hypnosis transcripts, personal mental-health content, medical information, crisis content, credentials, or production user data in preview fixtures or comments.

## 7. Analytics policy

Web Analytics and Speed Insights are optional evidence sources.

Enabling Web Analytics requires a recorded privacy decision. Custom events use an allowlist and cannot include free text, prompts, article selections that reveal sensitive intent, session content, diagnoses, or personal identifiers.

Speed Insights may inform the performance gate but does not replace route-specific profiling or interaction testing.

## 8. Agent integration

The Vercel Plugin may be installed explicitly for Vercel-specific coding guidance. Its default telemetry state must be disclosed, and privacy-sensitive environments should document whether `VERCEL_PLUGIN_TELEMETRY=off` is used.

Vercel MCP may be connected explicitly for authenticated project actions. It remains outside the repository's deterministic core and must never be required for tests.

## 9. `innerself.love` adoption boundary

The design profile should recommend protected preview review for homepage, article, FAQ, method, safety, and trainer-preview surfaces once the actual public-site source repository is identified.

No production migration occurs until the current source, stack, build, host, domain configuration, and rollback path are known. The local `innerSignalGraph/apps/web` interface must not be mistaken for the public site.

## 10. Acceptance criteria

The integration is complete when:

1. the optional integration pin is recorded separately;
2. the canonical skill links to the preview-review reference without making it mandatory;
3. a JSON review template exists and validates deterministically;
4. protection failures are detected for sensitive or unknown previews;
5. automated Toolbar evidence is marked insufficient for manual accessibility and truth gates;
6. analytics defaults to disabled or undecided;
7. `innerself.love` project context names protected preview review as a future adoption step without claiming production is hosted on Vercel;
8. tests pass without network or Vercel credentials.
