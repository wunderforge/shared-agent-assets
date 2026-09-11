#!/usr/bin/env python3
"""Dependency-free structural and safety checks for shared agent assets."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MAX_FILE_BYTES = 1_000_000
FORBIDDEN_SUFFIXES = {
    ".7z", ".class", ".dll", ".dylib", ".exe", ".gz", ".jar", ".o",
    ".key", ".pem", ".pyc", ".so", ".tar", ".wasm", ".zip",
}
FORBIDDEN_NAMES = {".env", "id_rsa", "id_ed25519"}
IGNORED_DIRS = {".git", ".venv", "__pycache__", "artifacts"}
FRONTMATTER_RE = re.compile(r"\A---\s*\n(?P<body>.*?)\n---\s*\n", re.DOTALL)
FIELD_RE = re.compile(r"^(?P<key>[a-zA-Z][a-zA-Z0-9_-]*):\s*(?P<value>.+?)\s*$")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\((?P<target>[^)]+)\)")


def iter_repository_files(root: Path = ROOT):
    for path in root.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file() or path.is_symlink():
            yield path


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")
    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        field = FIELD_RE.match(line)
        if field:
            fields[field.group("key")] = field.group("value").strip("\"'")
    return fields


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]
    try:
        fields = parse_frontmatter(skill_file)
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"{skill_file}: {exc}"]
    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != skill_dir.name:
        errors.append(f"{skill_file}: name must match folder '{skill_dir.name}'")
    if not KEBAB_RE.fullmatch(name):
        errors.append(f"{skill_file}: name must be lowercase kebab-case")
    if not description or len(description) < 20:
        errors.append(f"{skill_file}: description is missing or too vague")
    return errors


def validate_links(path: Path) -> list[str]:
    if path.suffix.lower() != ".md":
        return []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeError:
        return [f"{path.relative_to(ROOT)}: Markdown must be UTF-8"]
    errors: list[str] = []
    for match in LINK_RE.finditer(text):
        raw_target = match.group("target").strip().split()[0].strip("<>")
        if not raw_target or raw_target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = raw_target.split("#", 1)[0]
        if target and not (path.parent / target).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link '{raw_target}'")
    return errors


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    required = ["README.md", "AGENTS.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE"]
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in iter_repository_files(root):
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"{relative}: symbolic links are not allowed")
            continue
        if path.stat().st_size > MAX_FILE_BYTES:
            errors.append(f"{relative}: file exceeds {MAX_FILE_BYTES} bytes")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES or path.name.lower() in FORBIDDEN_NAMES:
            errors.append(f"{relative}: forbidden secret-bearing or binary file type")
        if path.name.lower().startswith(".env.") or "secrets" in {
            part.lower() for part in relative.parts
        }:
            errors.append(f"{relative}: forbidden secret-bearing path")
        errors.extend(validate_links(path))

    skills = root / "skills"
    if not skills.is_dir():
        errors.append("missing skills directory")
    else:
        skill_dirs = sorted(
            path for path in skills.iterdir()
            if path.is_dir() and not path.name.startswith((".", "_"))
        )
        for skill_dir in skill_dirs:
            errors.extend(validate_skill(skill_dir))
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository structure and deterministic safety checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
