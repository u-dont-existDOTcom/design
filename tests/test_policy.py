from __future__ import annotations

import unittest

from design_os.policy import (
    AUTHORITY_ORDER,
    PERCEPTUAL_LAYERS,
    SURFACE_MODES,
    Candidate,
    applicable_states,
    choose_direction,
)


class PolicyTests(unittest.TestCase):
    def test_clear_winner_continues_without_human_gate(self) -> None:
        result = choose_direction(
            [
                Candidate("evidence-first", 0.91),
                Candidate("generic-wellness", 0.67),
            ]
        )
        self.assertEqual("select", result.action)
        self.assertEqual("evidence-first", result.selected)
        self.assertIn("clearly dominates", result.reason)

    def test_close_survivors_require_human_choice(self) -> None:
        result = choose_direction(
            [Candidate("editorial", 0.82), Candidate("quiet-technical", 0.78)]
        )
        self.assertEqual("ask", result.action)
        self.assertIsNone(result.selected)

    def test_candidate_with_unmet_requirements_cannot_win(self) -> None:
        result = choose_direction(
            [
                Candidate("beautiful-but-inaccessible", 0.99, ("keyboard access",)),
                Candidate("accessible", 0.74),
            ]
        )
        self.assertEqual("select", result.action)
        self.assertEqual("accessible", result.selected)

    def test_no_survivor_requires_human_intervention(self) -> None:
        result = choose_direction(
            [
                Candidate("one", 0.9, ("L0",)),
                Candidate("two", 0.8, ("truth",)),
            ]
        )
        self.assertEqual("ask", result.action)
        self.assertIsNone(result.selected)
        self.assertIn("No candidate", result.reason)

    def test_inert_component_only_requires_default_state(self) -> None:
        self.assertEqual(
            ("default",),
            applicable_states(
                interactive=False,
                fine_pointer=False,
                asynchronous=False,
                reports_outcome=False,
            ),
        )

    def test_pointer_interaction_requires_hover_but_touch_does_not(self) -> None:
        pointer_states = applicable_states(
            interactive=True,
            fine_pointer=True,
            asynchronous=False,
            reports_outcome=False,
        )
        touch_states = applicable_states(
            interactive=True,
            fine_pointer=False,
            asynchronous=False,
            reports_outcome=False,
        )
        self.assertIn("hover", pointer_states)
        self.assertNotIn("hover", touch_states)

    def test_async_action_requires_outcome_states(self) -> None:
        self.assertEqual(
            (
                "default",
                "hover",
                "focus-visible",
                "active",
                "disabled",
                "loading",
                "error",
                "success",
            ),
            applicable_states(
                interactive=True,
                fine_pointer=True,
                asynchronous=True,
                reports_outcome=True,
            ),
        )

    def test_policy_constants_preserve_required_order(self) -> None:
        self.assertEqual(("L0", "L1", "L2", "L3", "L4"), PERCEPTUAL_LAYERS)
        self.assertEqual(
            ("persuade", "operate", "read", "experience"), SURFACE_MODES
        )
        self.assertEqual("explicit-user-truth", AUTHORITY_ORDER[0])
        self.assertEqual("agent-taste", AUTHORITY_ORDER[-1])


if __name__ == "__main__":
    unittest.main()
