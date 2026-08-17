# Design Audit Manifest Schema

The audit CLI accepts a JSON object. Unknown evidence remains false, empty, or explicitly unresolved; never fill fields by inference.

## Top-level shape

```json
{
  "surface": {"mode": "read", "scope": "page", "platform": "web"},
  "claims": [],
  "content_changes": [],
  "perceptual_layers": [],
  "components": [],
  "responsive": {},
  "accessibility": {},
  "deviations": [],
  "performance": {},
  "consistency": {},
  "verification": {}
}
```

## Claims

Each claim records `kind`, `text`, `verified`, `provided_by_user`, and ideally `source`. A claim fails as `truth.unverified-claim` unless it is supplied by the user or independently verified.

## Content changes

Each change records `path`, `before`, `after`, `classification`, and `authorized`. Unauthorized substantive changes fail as `content.unauthorized-change`.

## Perceptual layers

Provide L0 through L4 with status `pass`, `fail`, or `review` and observable evidence. Missing layers produce `perception.missing-layer`; unresolved layers produce `perception.layer-unresolved`; downstream passes after an unresolved lower layer produce `perception.blocked-downstream`.

## Components

Record `name`, `interactive`, `fine_pointer`, `asynchronous`, `reports_outcome`, and `implemented_states`. Requirements are derived semantically. Missing applicable states produce `state.missing`.

## Responsive evidence

For web work, record `required_widths`, `checked_widths`, `zoom_percent`, and `text_scaling_checked`. The default required widths are 320, 375, 414, 768, 1024, and 1440 CSS pixels. Native surfaces record shipped device classes through project-specific evidence rather than pretending these widths apply.

## Accessibility

Boolean evidence keys: `semantics`, `labels`, `focus_order`, `visible_focus`, `contrast`, `keyboard`, `reduced_motion`, and `non_color_state`. Missing evidence produces `accessibility.missing`.

## Deviations

Record `pattern`, `intentional`, `rationale`, and `verification`. An intentional deviation without both rationale and verification produces `deviation.no-rationale`.

## Performance and consistency

Performance checks: `blocking_assets_checked`, `layout_shift_checked`, and `interaction_latency_checked`.

Consistency checks: `tokens`, `typography`, `spacing`, `icon_voice`, and `component_behavior`.

## Verification

Record `inspection_passes`. More than two produces `verification.pass-budget`. The count covers the initial batched inspection and optional confirmation pass collectively.
