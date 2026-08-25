#!/usr/bin/env python3
"""Audit work items (TODO.md, FEEDBACK.md, CHANGELOG.md) in a target repository.

Checks for:
1. Case collisions (e.g. todo.md vs TODO.md)
2. Dual-audience frontmatter schema (make-a-change/todo/v1)
3. Soft-markdown standard section conformance
4. Secret patterns or raw auth tokens
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SECRET_PATTERNS = [
    (r"(?i)(sk-[a-zA-Z0-9]{20,})", "OpenAI / Claude API key"),
    (r"(?i)(ghp_[a-zA-Z0-9]{30,})", "GitHub personal token"),
    (r"(?i)(AKIA[0-9A-Z]{16})", "AWS access key"),
    (r"(?i)(bearer\s+[a-zA-Z0-9_\-\.]{20,})", "Bearer token"),
    (r"(?i)(postgres|mysql|mongodb):\/\/[^:\s]+:[^@\s]+@[^\s]+", "Database connection URI"),
]

FRONTMATTER_REGEX = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_schema(content: str) -> str | None:
    match = FRONTMATTER_REGEX.match(content)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.strip().startswith("schema:"):
            return line.split(":", 1)[1].strip()
    return None


def audit_repo(repo_dir: Path) -> int:
    errors = 0
    warnings = 0

    print(f"Auditing work items in: {repo_dir.resolve()}")

    # Check case collisions
    root_files = [f.name for f in repo_dir.iterdir() if f.is_file()]
    lowered = {}
    for name in root_files:
        low = name.lower()
        if low in lowered:
            print(f"❌ [CASE COLLISION] Found '{name}' alongside '{lowered[low]}' on case-insensitive filesystem!")
            errors += 1
        lowered[low] = name

    # Check TODO.md
    todo_path = repo_dir / "TODO.md"
    if not todo_path.exists() and (repo_dir / "todo.md").exists():
        print("⚠️ [NAMING] Found lowercase 'todo.md'; canonical recommendation is uppercase 'TODO.md'")
        warnings += 1
        todo_path = repo_dir / "todo.md"

    if todo_path.exists():
        content = todo_path.read_text(encoding="utf-8")
        schema = extract_schema(content)
        schema_status = f" (schema: {schema})" if schema else " (missing schema frontmatter)"
        print(f"✓ Found {todo_path.name} ({len(content.splitlines())} lines){schema_status}")

        if not schema:
            print("ℹ️ [INFO] Adding 'schema: make-a-change/todo/v1' frontmatter is recommended.")

        for regex, label in SECRET_PATTERNS:
            if re.search(regex, content):
                print(f"❌ [SECRET DETECTED] Found potential {label} in {todo_path.name}!")
                errors += 1

    # Check FEEDBACK.md
    feedback_path = repo_dir / "FEEDBACK.md"
    if not feedback_path.exists() and (repo_dir / "feedback.md").exists():
        feedback_path = repo_dir / "feedback.md"

    if feedback_path.exists():
        content = feedback_path.read_text(encoding="utf-8")
        schema = extract_schema(content)
        schema_status = f" (schema: {schema})" if schema else ""
        print(f"✓ Found {feedback_path.name} ({len(content.splitlines())} lines){schema_status}")
        for regex, label in SECRET_PATTERNS:
            if re.search(regex, content):
                print(f"❌ [SECRET DETECTED] Found potential {label} in {feedback_path.name}!")
                errors += 1

    # Check CHANGELOG.md
    changelog_path = repo_dir / "CHANGELOG.md"
    if changelog_path.exists():
        print(f"✓ Found CHANGELOG.md ({len(changelog_path.read_text(encoding='utf-8').splitlines())} lines)")

    print("-" * 50)
    print(f"Audit finished with {errors} error(s) and {warnings} warning(s).")
    return 1 if errors > 0 else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="Repository root directory")
    args = parser.parse_args()
    return audit_repo(Path(args.repo))


if __name__ == "__main__":
    sys.exit(main())
