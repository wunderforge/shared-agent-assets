#!/usr/bin/env python3
"""Run SkillSpector against every published skill and accept only SAFE."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REPORTS = ROOT / "artifacts" / "skillspector"


def main() -> int:
    scanner = shutil.which("skillspector")
    if scanner is None:
        print("skillspector is not installed", file=sys.stderr)
        return 2

    skill_dirs = sorted(
        path for path in SKILLS.iterdir()
        if path.is_dir() and not path.name.startswith((".", "_"))
    )
    if not skill_dirs:
        print("No skills found; refusing to publish an empty catalog.", file=sys.stderr)
        return 1

    REPORTS.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    for skill_dir in skill_dirs:
        report = REPORTS / f"{skill_dir.name}.json"
        completed = subprocess.run(
            [scanner, "scan", str(skill_dir), "--no-llm", "--format", "json", "--output", str(report)],
            cwd=ROOT,
            check=False,
        )
        if completed.returncode not in (0, 1):
            failures.append(f"{skill_dir.name}: scanner error {completed.returncode}")
            continue
        if not report.is_file():
            failures.append(f"{skill_dir.name}: scanner did not produce a report")
            continue
        try:
            payload = json.loads(report.read_text(encoding="utf-8"))
            recommendation = payload["risk_assessment"]["recommendation"]
            execution_successful = payload["execution_successful"]
            analysis_complete = payload["analysis_completeness"]["is_complete"]
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            failures.append(f"{skill_dir.name}: invalid scanner report ({exc})")
            continue
        print(
            f"{skill_dir.name}: {recommendation}; "
            f"execution_successful={execution_successful}; complete={analysis_complete}"
        )
        if recommendation != "SAFE":
            failures.append(f"{skill_dir.name}: recommendation is {recommendation}")
        if not execution_successful or not analysis_complete:
            failures.append(f"{skill_dir.name}: scan did not complete successfully")

    if failures:
        print("Skill security gate failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("All skills passed the SAFE-only SkillSpector gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
