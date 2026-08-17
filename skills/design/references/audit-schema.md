# Design Audit Manifest Schema

The audit CLI accepts a JSON object. Unknown evidence must remain false, empty, or explicitly marked incomplete; do not fill fields by inference.

## Top-level fields

```json
{
  "surface": {"mode": "read", "scope": "page"},
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

Each claim records kind, text, verified, provided_by_user, and source. Proof-shaped claims must be user-supplied or independently verified.

## Content changes

Each change records path, before, after, classification, and authorized. Unauthorized substantive changes fail.

## Perceptual layers

Provide exactly L0 through L4 in order, with status `pass`, `fail`, or `review`, plus observable evidence. A lower-layer failure blocks downstream approval.

## Components

Record name, interactive, fine_pointer, asynchronous, reports_outcome, and implemented states.

## Responsive

For web work record checked widths, zoom percentage, and text-scaling evidence. For native surfaces record shipped device classes.

## Accessibility

Boolean evidence keys: semantics, labels, focus_order, visible_focus, contrast, keyboard, reduced_motion, and non_color_state.

## Deviations

Record pattern, intentional, rationale, and verification.

## Verification

Record inspection passes. More than two fails unless a named acceptance criterion remained false.
