from __future__ import annotations

import json
import pathlib
import tempfile
import unittest

from design_os.query import QueryError, load_catalogs, search_catalog, validate_query

ROOT = pathlib.Path(__file__).resolve().parents[1]


class QueryTests(unittest.TestCase):
    def test_read_query_prefers_long_form_pattern(self) -> None:
        results = search_catalog(
            "long form article",
            domain="pattern",
            mode="read",
            root=ROOT / "knowledge",
        )
        self.assertEqual("read-long-form", results[0].entry_id)

    def test_stack_filter_prefers_matching_stack(self) -> None:
        results = search_catalog(
            "render performance",
            domain="stack",
            stack="nextjs",
            root=ROOT / "knowledge",
        )
        self.assertEqual("stack-react-next-boundaries", results[0].entry_id)

    def test_ties_have_stable_id_order(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = pathlib.Path(temp_dir)
            group = root / "patterns"
            group.mkdir()
            entries = [
                {
                    "id": "z-last",
                    "domain": "pattern",
                    "title": "Alpha beta",
                    "keywords": ["alpha", "beta"],
                    "modes": [],
                    "stacks": [],
                    "guidance": ["One"],
                    "avoid": [],
                },
                {
                    "id": "a-first",
                    "domain": "pattern",
                    "title": "Alpha beta",
                    "keywords": ["alpha", "beta"],
                    "modes": [],
                    "stacks": [],
                    "guidance": ["Two"],
                    "avoid": [],
                },
            ]
            (group / "catalog.json").write_text(json.dumps(entries), encoding="utf-8")
            results = search_catalog("alpha beta", root=root)
            self.assertEqual(["a-first", "z-last"], [item.entry_id for item in results])

    def test_zero_score_entries_are_not_returned(self) -> None:
        results = search_catalog(
            "quantum pottery",
            root=ROOT / "knowledge",
        )
        self.assertEqual([], results)

    def test_broad_multi_problem_query_is_rejected(self) -> None:
        with self.assertRaises(QueryError):
            validate_query(
                "typography, checkout, animation, charts, icons, mobile, pricing, forms"
            )

    def test_one_term_query_is_rejected(self) -> None:
        with self.assertRaises(QueryError):
            validate_query("typography")

    def test_catalog_schema_is_validated(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = pathlib.Path(temp_dir)
            group = root / "broken"
            group.mkdir()
            (group / "catalog.json").write_text('[{"id":"broken"}]', encoding="utf-8")
            with self.assertRaises(QueryError):
                load_catalogs(root)


if __name__ == "__main__":
    unittest.main()
