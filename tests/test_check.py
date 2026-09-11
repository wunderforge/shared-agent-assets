from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check.py"
SPEC = importlib.util.spec_from_file_location("repository_check", MODULE_PATH)
assert SPEC and SPEC.loader
repository_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repository_check)


class SkillValidationTests(unittest.TestCase):
    def test_valid_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            skill_dir = Path(temporary) / "useful-skill"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text(
                "---\nname: useful-skill\n"
                "description: A sufficiently precise description for a useful skill.\n"
                "---\n\n# Useful skill\n",
                encoding="utf-8",
            )
            self.assertEqual(repository_check.validate_skill(skill_dir), [])

    def test_folder_and_name_must_match(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            skill_dir = Path(temporary) / "expected-name"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text(
                "---\nname: different-name\n"
                "description: A sufficiently precise description for a useful skill.\n"
                "---\n\n# Useful skill\n",
                encoding="utf-8",
            )
            errors = repository_check.validate_skill(skill_dir)
            self.assertTrue(any("must match folder" in error for error in errors))

    def test_missing_frontmatter_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            skill_dir = Path(temporary) / "broken-skill"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text("# No frontmatter\n", encoding="utf-8")
            errors = repository_check.validate_skill(skill_dir)
            self.assertTrue(any("missing YAML frontmatter" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

