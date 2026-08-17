"""Ordered, deterministic design-production audit gates."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping

from .policy import PERCEPTUAL_LAYERS, applicable_states

WEB_WIDTHS = (320, 375, 414, 768, 1024, 1440)
ACCESSIBILITY_CHECKS = (
    "semantics",
    "labels",
    "focus_order",
    "visible_focus",
    "contrast",
    "keyboard",
    "reduced_motion",
    "non_color_state",
)
PERFORMANCE_CHECKS = (
    "blocking_assets_checked",
    "layout_shift_checked",
    "interaction_latency_checked",
)
CONSISTENCY_CHECKS = (
    "tokens",
    "typography",
    "spacing",
    "icon_voice",
    "component_behavior",
)


@dataclass(frozen=True, slots=True)
class Finding:
    code: str
    severity: str
    message: str
    path: str
    blocking: bool = True


@dataclass(frozen=True, slots=True)
class AuditReport:
    findings: tuple[Finding, ...]

    @property
    def passed(self) -> bool:
        return not any(finding.blocking for finding in self.findings)

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "findings": [asdict(finding) for finding in self.findings],
        }


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _sequence(value: object) -> list[Any]:
    return list(value) if isinstance(value, (list, tuple)) else []


def audit_manifest(manifest: Mapping[str, Any]) -> AuditReport:
    """Run canonical gates without mutating the supplied manifest."""

    findings: list[Finding] = []

    # 1. Truth gate.
    for index, raw_claim in enumerate(_sequence(manifest.get("claims"))):
        claim = _mapping(raw_claim)
        if not bool(claim.get("verified")) and not bool(claim.get("provided_by_user")):
            findings.append(
                Finding(
                    code="truth.unverified-claim",
                    severity="critical",
                    message="Proof-shaped content must be user-supplied or independently verified.",
                    path=f"claims[{index}]",
                )
            )

    # 2. Argument-preservation gate.
    for index, raw_change in enumerate(_sequence(manifest.get("content_changes"))):
        change = _mapping(raw_change)
        if (
            str(change.get("classification", "")).casefold() == "substantive"
            and not bool(change.get("authorized"))
        ):
            findings.append(
                Finding(
                    code="content.unauthorized-change",
                    severity="critical",
                    message="A substantive content change lacks owner authorization.",
                    path=f"content_changes[{index}]",
                )
            )

    # 3. Perceptual dependency stack.
    raw_layers = _sequence(manifest.get("perceptual_layers"))
    indexed_layers: dict[str, Mapping[str, Any]] = {}
    for raw_layer in raw_layers:
        layer = _mapping(raw_layer)
        name = str(layer.get("layer", ""))
        if name and name not in indexed_layers:
            indexed_layers[name] = layer

    missing_layers = [name for name in PERCEPTUAL_LAYERS if name not in indexed_layers]
    if missing_layers:
        findings.append(
            Finding(
                code="perception.missing-layer",
                severity="critical",
                message=f"Missing perceptual layers: {', '.join(missing_layers)}.",
                path="perceptual_layers",
            )
        )

    blocker: str | None = None
    for name in PERCEPTUAL_LAYERS:
        layer = indexed_layers.get(name)
        if layer is None:
            if blocker is None:
                blocker = name
            continue
        status = str(layer.get("status", "review")).casefold()
        evidence = str(layer.get("evidence", "")).strip()
        if status not in {"pass", "fail", "review"}:
            status = "review"
        if status == "pass" and not evidence:
            findings.append(
                Finding(
                    code="perception.missing-evidence",
                    severity="major",
                    message=f"{name} is marked pass without observable evidence.",
                    path=f"perceptual_layers.{name}",
                )
            )
        if blocker is not None and status == "pass":
            findings.append(
                Finding(
                    code="perception.blocked-downstream",
                    severity="critical",
                    message=f"{name} cannot pass while lower layer {blocker} is unresolved.",
                    path=f"perceptual_layers.{name}",
                )
            )
        if status in {"fail", "review"}:
            findings.append(
                Finding(
                    code="perception.layer-unresolved",
                    severity="critical" if status == "fail" else "major",
                    message=f"{name} remains {status}.",
                    path=f"perceptual_layers.{name}",
                )
            )
            if blocker is None:
                blocker = name

    # 4. Accessibility gate.
    accessibility = _mapping(manifest.get("accessibility"))
    for check in ACCESSIBILITY_CHECKS:
        if not bool(accessibility.get(check)):
            findings.append(
                Finding(
                    code="accessibility.missing",
                    severity="critical",
                    message=f"Required accessibility evidence is missing: {check}.",
                    path=f"accessibility.{check}",
                )
            )

    # 5. Responsive and text-resilience gate.
    surface = _mapping(manifest.get("surface"))
    responsive = _mapping(manifest.get("responsive"))
    if str(surface.get("platform", "web")).casefold() == "web":
        required_widths = tuple(
            int(width)
            for width in _sequence(responsive.get("required_widths", WEB_WIDTHS))
            if isinstance(width, (int, float))
        )
        checked_widths = {
            int(width)
            for width in _sequence(responsive.get("checked_widths"))
            if isinstance(width, (int, float))
        }
        for width in required_widths:
            if width not in checked_widths:
                findings.append(
                    Finding(
                        code="responsive.width-missing",
                        severity="major",
                        message=f"Required viewport width was not checked: {width}px.",
                        path="responsive.checked_widths",
                    )
                )
        if int(responsive.get("zoom_percent", 0) or 0) < 200:
            findings.append(
                Finding(
                    code="responsive.zoom-missing",
                    severity="major",
                    message="Web review must include 200% zoom.",
                    path="responsive.zoom_percent",
                )
            )
        if not bool(responsive.get("text_scaling_checked")):
            findings.append(
                Finding(
                    code="responsive.text-scaling-missing",
                    severity="major",
                    message="User text scaling or expanded-text behavior was not checked.",
                    path="responsive.text_scaling_checked",
                )
            )

    # 6. Semantic state gate.
    for index, raw_component in enumerate(_sequence(manifest.get("components"))):
        component = _mapping(raw_component)
        required_states = set(
            applicable_states(
                interactive=bool(component.get("interactive")),
                fine_pointer=bool(component.get("fine_pointer")),
                asynchronous=bool(component.get("asynchronous")),
                reports_outcome=bool(component.get("reports_outcome")),
            )
        )
        implemented = {
            str(state) for state in _sequence(component.get("implemented_states"))
        }
        missing = sorted(required_states - implemented)
        if missing:
            findings.append(
                Finding(
                    code="state.missing",
                    severity="critical",
                    message=f"Component is missing applicable states: {', '.join(missing)}.",
                    path=f"components[{index}].implemented_states",
                )
            )

    # 7. Intentional-deviation gate.
    for index, raw_deviation in enumerate(_sequence(manifest.get("deviations"))):
        deviation = _mapping(raw_deviation)
        if bool(deviation.get("intentional")) and (
            not str(deviation.get("rationale", "")).strip()
            or not str(deviation.get("verification", "")).strip()
        ):
            findings.append(
                Finding(
                    code="deviation.no-rationale",
                    severity="major",
                    message="Intentional anti-pattern deviation needs rationale and verification.",
                    path=f"deviations[{index}]",
                )
            )

    # 8. Performance gate.
    performance = _mapping(manifest.get("performance"))
    for check in PERFORMANCE_CHECKS:
        if not bool(performance.get(check)):
            findings.append(
                Finding(
                    code="performance.missing",
                    severity="major",
                    message=f"Required performance evidence is missing: {check}.",
                    path=f"performance.{check}",
                )
            )

    # 9. Consistency gate.
    consistency = _mapping(manifest.get("consistency"))
    for check in CONSISTENCY_CHECKS:
        if not bool(consistency.get(check)):
            findings.append(
                Finding(
                    code="consistency.missing",
                    severity="major",
                    message=f"Required consistency evidence is missing: {check}.",
                    path=f"consistency.{check}",
                )
            )

    # 10. Bounded visual-verification gate.
    verification = _mapping(manifest.get("verification"))
    passes = verification.get("inspection_passes", 0)
    if not isinstance(passes, int) or passes < 0:
        findings.append(
            Finding(
                code="verification.invalid-pass-count",
                severity="major",
                message="Inspection pass count must be a non-negative integer.",
                path="verification.inspection_passes",
            )
        )
    elif passes > 2:
        findings.append(
            Finding(
                code="verification.pass-budget",
                severity="major",
                message="Visual verification exceeded one inspection and one confirmation pass.",
                path="verification.inspection_passes",
            )
        )

    return AuditReport(tuple(findings))
