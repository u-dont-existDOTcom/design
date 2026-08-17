# Perceptual Diagnosis

The five layers form a dependency stack. Diagnose and derive requirements bottom-up.

## L0 — Cognitive load

Can a first-time user perceive the next meaningful action without carrying unnecessary information in working memory? Inspect competing focal points, hidden state, unexplained terminology, decision count, navigation burden, and missing external memory.

## L1 — First impression

Does the first meaningful view communicate purpose, audience, emotional register, and basic trust quickly enough to earn attention? Inspect coherence, dominant signal, genre fit, quality-to-stakes fit, and immediate purpose.

## L2 — Processing fluency

Is the experience legible, consistent, predictable, and easy to parse without flattening meaningful complexity? Inspect typography, measure, spacing rhythm, tokens, grouping, interaction behavior, and language clarity.

## L3 — Perception bias

Does the surface address what users actually respond to while separating behavior evidence, reported preference, and designer speculation? Inspect genuine outcomes, trust signals, survey/analytics gaps, and stakeholder bias.

## L4 — Decision architecture

Does the structure create an honest, intelligible trail to the user's goal at the right commitment distance? Inspect navigation language, defaults, CTA placement, evidence, reversibility, and expert-control preservation.

## Requirement record

```text
Layer:
Constraint:
Observed evidence:
Violation or risk:
Requirement R#:
Verification method:
Confidence and evidence type:
```

## Dependency handling

A failed lower layer caps downstream confidence. A Critical lower-layer failure blocks shipping. Upper layers do not compensate. Satisfy the lower requirement first.

## Ethical boundary

- Alignment: user and project goals must not conflict through manipulation.
- Sincerity: presentation must match delivery.
- Golden Rule: the designer should accept the same treatment as a user.

High fluency applied to unsupported claims is a danger signal, not success.
