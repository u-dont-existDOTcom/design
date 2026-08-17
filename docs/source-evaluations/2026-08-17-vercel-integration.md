# Vercel Integration Evaluation — 2026-08-17

## Decision

Integrate Vercel as an **optional deployment and design-verification adapter**, not as a fifth canonical design authority and not as a mandatory hosting platform.

The design OS remains framework-neutral and functional without Vercel. Consuming web projects may opt into Vercel when preview deployments and in-browser review materially improve the work.

## Why it is useful

Vercel's Git integration can create a live preview for branch pushes and pull requests. The preview can carry the Vercel Toolbar, which provides:

- comments attached to visible page locations;
- Git-provider feedback links and unresolved-comment status;
- accessibility checks based on axe rules for WCAG 2.0 A and AA;
- layout-shift detection and replay;
- interaction-timing inspection, including warnings for interactions above 200 ms;
- branch, commit, deployment, Open Graph, and sharing context.

This directly strengthens the design OS's bounded visual-verification stage. It converts subjective review into a durable preview artifact and collects some evidence that otherwise requires separate tools.

## What it does not replace

Vercel Toolbar evidence does not prove:

- screen-reader usability;
- correct keyboard workflow across all states;
- content or argument preservation;
- absence of fabricated claims;
- correct product truth;
- responsive behavior across every required viewport;
- production performance across real traffic;
- a complete security or privacy review.

The canonical truth, perception, accessibility, responsive, state, performance, and consistency gates still run.

## Plugin, MCP, and hosting are separate choices

### Vercel Plugin

The official `vercel/vercel-plugin` supplies agent knowledge, skills, deployment guidance, React/Next.js rules, and specialized Vercel workflows. It shapes how a coding agent reasons about Vercel. It does not authenticate the agent to the user's Vercel account.

Reviewed source:

- repository: `https://github.com/vercel/vercel-plugin`
- version: `0.48.0`
- commit: `11c32588786a9d49791372657433b88d49561874`
- license: Apache-2.0

The plugin's telemetry is enabled by default. It can be disabled with `VERCEL_PLUGIN_TELEMETRY=off`. The design OS must not install the plugin silently.

### Vercel MCP

Vercel MCP provides authenticated account actions such as listing projects, inspecting deployments and logs, and managing project context. It may be used alongside the plugin. The design OS must not require it and must never store Vercel credentials in repository files.

### Vercel deployment

A project may deploy on Vercel without installing the plugin or MCP. Conversely, an agent may use the plugin for Vercel-specific guidance without moving production hosting.

## Security and privacy constraints

Generated deployment URLs may be publicly accessible unless Deployment Protection is configured. Sensitive, unreleased, or owner-only previews must use Vercel Authentication or another reviewed protection method before a preview URL is shared.

For privacy-sensitive products:

- preview fixtures must not contain real user sessions, therapy/hypnosis transcripts, secrets, personal identifiers, or production data;
- comments must not include secrets or private case material;
- Web Analytics and custom events remain opt-in;
- custom events must never contain user-entered mental-health, therapy, hypnosis, medical, crisis, or memory content;
- session replay is not introduced by this integration;
- Speed Insights and Web Analytics evidence is advisory and must be described accurately in the privacy policy when enabled.

Vercel Web Analytics is described by Vercel as anonymized and cookie-free. That improves its privacy posture but does not make analytics mandatory or eliminate the need for an explicit project decision.

## Recommended workflow

```text
feature branch or pull request
  → Vercel Preview Deployment
  → confirm Deployment Protection
  → activate Toolbar
  → inspect target widths and states
  → record accessibility, layout-shift, and interaction-timing evidence
  → leave and resolve page comments
  → export a compact VERCEL-REVIEW.json record
  → run canonical design audit
  → merge only when required gates pass
```

## `innerself.love`

The public site is a strong candidate for Vercel preview review because it contains long-form reading surfaces, navigation, tables, citations, safety copy, and multiple audience paths that benefit from live mobile inspection.

The connected GitHub repositories do not currently expose a clearly identifiable source repository for the public `innerself.love` marketing and article site. `u-dont-existDOTcom/innerSignalGraph/apps/web` is the local runtime interface, not the public multi-page site. Therefore:

- do not migrate production hosting as part of the design-repository build;
- first identify the actual public-site source and build command;
- connect that project to Vercel only after preserving its current deployment and rollback path;
- use protected preview deployments before considering any production-domain change.

## Official references

- `https://vercel.com/docs/git/vercel-for-github`
- `https://vercel.com/docs/vercel-toolbar`
- `https://vercel.com/docs/vercel-toolbar/accessibility-audit-tool`
- `https://vercel.com/docs/vercel-toolbar/interaction-timing-tool`
- `https://vercel.com/docs/deployment-protection`
- `https://vercel.com/docs/deployments/generated-urls`
- `https://vercel.com/docs/analytics`
- `https://vercel.com/docs/speed-insights`
- `https://vercel.com/docs/agent-resources/vercel-mcp`
- `https://github.com/vercel/vercel-plugin`
