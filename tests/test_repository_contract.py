from __future__ import annotations

import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_required_canonical_files_exist(self) -> None:
        required = [
            "README.md",
            "AGENTS.md",
            "ATTRIBUTIONS.md",
            "UPSTREAMS.lock.json",
            "core/DESIGN-OPERATING-SYSTEM.md",
            "core/AUTHORITY-AND-CONFLICTS.md",
            "core/PERCEPTUAL-DIAGNOSIS.md",
            "core/PATTERN-SELECTION.md",
            "core/ANTI-SLOP-GATE.md",
            "core/PRODUCTION-VERIFICATION.md",
            "skills/design/SKILL.md",
            "skills/design/references/operations.md",
            "skills/design/references/audit-schema.md",
            "skills/design/references/project-context.md",
            "templates/PRODUCT.md",
            "templates/DESIGN.md",
            "templates/SURFACE.md",
            "templates/DESIGN-AUDIT.json",
            "templates/DECISION-LOG.md",
            "docs/source-evaluations/2026-08-17-upstream-synthesis.md",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_skill_contains_non_negotiable_rules(self) -> None:
        text = (ROOT / "skills/design/SKILL.md").read_text(encoding="utf-8")
        for phrase in [
            "Never invent proof",
            "lower perceptual layer wins",
            "preserve the user's argument",
            "one confirmation pass",
            "load the live canonical skill",
            "Continue automatically",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_skill_carries_claim_integrity_checks(self) -> None:
        text = " ".join(
            (ROOT / "skills/design/SKILL.md").read_text(encoding="utf-8").split()
        )
        # Claim-integrity check IDs, each with phrases that must stay in the skill.
        anchors = (
            ("CI-01", "Every sentence about what a brief, the owner, a design, its content, or user research says, shows, or does must rest on a passage or element you can point to."),
            ("CI-02", "Put only a source's exact words inside quotation marks, both in your reports and in the design itself"),
            ("CI-03", "search all of it for counterexamples. The claim covers only what you searched; when that was less than all of it"),
            ("CI-04", "Check them against a source, or say they come from memory. For a standard, name the version and the criterion or section you checked"),
            ("CI-05", "open the primary source behind it, not only a page that repeats it"),
            ("CI-05", "When a figure the owner supplied does not match the source it cites, point it out instead of changing the copy."),
            ("CI-06", "must name what you compared against which source or version: for example, which foreground and background pairs you measured and how"),
            ("CI-07", "When the owner disputes a finding or claim, recheck it before agreeing, as you would before defending it. Agreement is not verification."),
            ("CI-08", "When you add or rewrite a factual claim, figure, quotation, or attribution in copy the owner will publish"),
            ("CI-08", "check it against its source at that moment, even if you checked it earlier"),
            ("CI-09", "state the strongest reading under which it is not a problem, such as a deliberate choice the brief supports, and drop the flag if that reading is plausible"),
            ("CI-09", "When a flag depends on what the owner meant and the project context does not say, raise it as a question instead of asserting it."),
            ("CI-09", "Once the owner rejects a flag, drop it; do not bring it back as a warning about how users might react unless new evidence appears."),
            ("CI-09", "Neither a plausible reading nor the owner's rejection changes a measured result"),
            ("CI-09", "There is no minimum number of findings."),
            ("CI-10", "Before sending, compare what you are about to say with what you already said on the same topic."),
        )
        for check_id, anchor in anchors:
            with self.subTest(check=check_id, anchor=anchor):
                self.assertIn(anchor, text)

    def test_skill_claim_integrity_text_is_self_contained(self) -> None:
        text = (ROOT / "skills/design/SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("universal-dev-architecture", text.casefold())
        self.assertIsNone(re.search(r"\bUDA\b", text))

    def test_skill_declares_all_surface_modes_and_operations(self) -> None:
        text = (ROOT / "skills/design/SKILL.md").read_text(encoding="utf-8")
        for mode in ("Persuade", "Operate", "Read", "Experience"):
            self.assertIn(mode, text)
        for operation in (
            "init",
            "shape",
            "build",
            "refine",
            "redesign",
            "study",
            "critique",
            "audit",
            "polish",
            "harden",
            "query",
            "doctor",
            "sync-upstreams",
        ):
            self.assertRegex(text, rf"`{re.escape(operation)}`")

    def test_catalogs_follow_stable_schema(self) -> None:
        required_keys = {
            "id",
            "domain",
            "title",
            "keywords",
            "modes",
            "stacks",
            "guidance",
            "avoid",
        }
        catalogs = list((ROOT / "knowledge").glob("*/catalog.json"))
        self.assertEqual(3, len(catalogs))
        for path in catalogs:
            entries = json.loads(path.read_text(encoding="utf-8"))
            self.assertIsInstance(entries, list)
            self.assertGreaterEqual(len(entries), 4)
            for entry in entries:
                self.assertEqual(required_keys, set(entry))
                self.assertTrue(entry["id"])
                self.assertIsInstance(entry["keywords"], list)
                self.assertIsInstance(entry["guidance"], list)

    def test_templates_use_explicit_unknown_markers_not_ambiguous_placeholders(self) -> None:
        banned = re.compile(r"\b(?:TBD|TODO|FIXME|fill in later)\b", re.IGNORECASE)
        for path in (ROOT / "templates").glob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                self.assertIsNone(banned.search(text), str(path))
        product = (ROOT / "templates/PRODUCT.md").read_text(encoding="utf-8")
        self.assertIn("[REQUIRED: owner-supplied fact]", product)

    def test_no_font_binaries_are_committed(self) -> None:
        forbidden = {".ttf", ".otf", ".woff", ".woff2"}
        found = [
            str(path.relative_to(ROOT))
            for path in ROOT.rglob("*")
            if path.is_file() and path.suffix.lower() in forbidden
        ]
        self.assertEqual([], found)

    def test_upstream_lock_is_json_object(self) -> None:
        payload = json.loads((ROOT / "UPSTREAMS.lock.json").read_text(encoding="utf-8"))
        self.assertEqual(1, payload["schema_version"])
        self.assertEqual(4, len(payload["upstreams"]))


if __name__ == "__main__":
    unittest.main()
