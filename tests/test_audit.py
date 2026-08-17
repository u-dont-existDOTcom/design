from __future__ import annotations

import copy
import unittest

from design_os.audit import audit_manifest


def valid_manifest() -> dict:
    return {
        "surface": {"mode": "read", "scope": "page", "platform": "web"},
        "claims": [],
        "content_changes": [],
        "perceptual_layers": [
            {"layer": layer, "status": "pass", "evidence": f"{layer} evidence"}
            for layer in ("L0", "L1", "L2", "L3", "L4")
        ],
        "components": [
            {
                "name": "subscribe",
                "interactive": True,
                "fine_pointer": True,
                "asynchronous": True,
                "reports_outcome": True,
                "implemented_states": [
                    "default", "hover", "focus-visible", "active", "disabled",
                    "loading", "error", "success",
                ],
            }
        ],
        "responsive": {
            "checked_widths": [320, 375, 414, 768, 1024, 1440],
            "zoom_percent": 200,
            "text_scaling_checked": True,
        },
        "accessibility": {
            "semantics": True,
            "labels": True,
            "focus_order": True,
            "visible_focus": True,
            "contrast": True,
            "keyboard": True,
            "reduced_motion": True,
            "non_color_state": True,
        },
        "deviations": [],
        "performance": {
            "blocking_assets_checked": True,
            "layout_shift_checked": True,
            "interaction_latency_checked": True,
        },
        "consistency": {
            "tokens": True,
            "typography": True,
            "spacing": True,
            "icon_voice": True,
            "component_behavior": True,
        },
        "verification": {"inspection_passes": 2},
    }


class AuditTests(unittest.TestCase):
    def finding_codes(self, manifest: dict) -> set[str]:
        return {finding.code for finding in audit_manifest(manifest).findings}

    def test_valid_manifest_passes(self) -> None:
        report = audit_manifest(valid_manifest())
        self.assertTrue(report.passed)
        self.assertEqual((), report.findings)

    def test_unverified_metric_fails_truth_gate(self) -> None:
        manifest = valid_manifest()
        manifest["claims"] = [{
            "kind": "metric",
            "text": "Trusted by 50,000 people",
            "verified": False,
            "provided_by_user": False,
        }]
        self.assertIn("truth.unverified-claim", self.finding_codes(manifest))

    def test_unauthorized_substantive_change_is_blocked(self) -> None:
        manifest = valid_manifest()
        manifest["content_changes"] = [{
            "path": "hero",
            "before": "The original argument",
            "after": "A gentler summary",
            "classification": "substantive",
            "authorized": False,
        }]
        self.assertIn("content.unauthorized-change", self.finding_codes(manifest))

    def test_missing_layer_is_reported(self) -> None:
        manifest = valid_manifest()
        manifest["perceptual_layers"] = manifest["perceptual_layers"][:-1]
        self.assertIn("perception.missing-layer", self.finding_codes(manifest))

    def test_failed_lower_layer_blocks_downstream_passes(self) -> None:
        manifest = valid_manifest()
        manifest["perceptual_layers"][0]["status"] = "fail"
        self.assertIn("perception.blocked-downstream", self.finding_codes(manifest))

    def test_accessibility_omission_is_reported(self) -> None:
        manifest = valid_manifest()
        manifest["accessibility"]["keyboard"] = False
        self.assertIn("accessibility.missing", self.finding_codes(manifest))

    def test_missing_responsive_width_is_reported(self) -> None:
        manifest = valid_manifest()
        manifest["responsive"]["checked_widths"].remove(320)
        self.assertIn("responsive.width-missing", self.finding_codes(manifest))

    def test_missing_semantic_component_state_is_reported(self) -> None:
        manifest = valid_manifest()
        manifest["components"][0]["implemented_states"].remove("loading")
        self.assertIn("state.missing", self.finding_codes(manifest))

    def test_intentional_deviation_needs_rationale_and_verification(self) -> None:
        manifest = valid_manifest()
        manifest["deviations"] = [{
            "pattern": "centered hero",
            "intentional": True,
            "rationale": "",
            "verification": "",
        }]
        self.assertIn("deviation.no-rationale", self.finding_codes(manifest))

    def test_excess_visual_verification_passes_are_reported(self) -> None:
        manifest = valid_manifest()
        manifest["verification"]["inspection_passes"] = 3
        self.assertIn("verification.pass-budget", self.finding_codes(manifest))

    def test_input_manifest_is_not_mutated(self) -> None:
        manifest = valid_manifest()
        original = copy.deepcopy(manifest)
        audit_manifest(manifest)
        self.assertEqual(original, manifest)


if __name__ == "__main__":
    unittest.main()
