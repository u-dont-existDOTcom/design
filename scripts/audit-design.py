#!/usr/bin/env python3
"""Audit a design evidence manifest against the canonical production gates."""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from design_os.audit import audit_manifest


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("manifest", type=pathlib.Path)
    result.add_argument("--format", choices=("json", "markdown"), default="markdown")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"audit error: {exc}", file=sys.stderr)
        return 2
    if not isinstance(payload, dict):
        print("audit error: manifest must be a JSON object", file=sys.stderr)
        return 2

    report = audit_manifest(payload)
    if args.format == "json":
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print(f"# Design audit: {'PASS' if report.passed else 'FAIL'}")
        if not report.findings:
            print("\nNo findings.")
        for finding in report.findings:
            print(f"\n- **{finding.severity.upper()} · `{finding.code}`** — {finding.message} (`{finding.path}`)")
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
