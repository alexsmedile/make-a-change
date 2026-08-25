#!/usr/bin/env python3
"""audit-work-items.py — Universal Linter & Auto-Fixer for make-a-change standard.

Checks for:
1. Case collisions (e.g. todo.md vs TODO.md on APFS/NTFS)
2. Dual-audience frontmatter schema (make-a-change/*/v1)
3. Checkbox syntax errors (e.g. '- []', '-[ ]', '* []') while supporting nested subtasks
4. Unclosed codeblocks (e.g. unclosed ```yaml or ```)
5. Leaked secrets & raw auth tokens
6. Flexible headings (no rigid names enforced; clusters/categories/recency are all valid)

Usage:
  python3 scripts/audit-work-items.py [options] [path]

Options:
  --fix       Auto-inject missing schema frontmatter safely
  --json      Output results in machine-readable JSON
  --strict    Exit code 1 on warnings as well as errors
"""
from __future__ import annotations

import argparse
import json
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

# Malformed checkbox patterns
MALFORMED_CHECKBOXES = [
    (r"^\s*-\s*\[\s{2,}\]", "Checkbox with multiple spaces inside bracket: '- [  ]'"),
    (r"^\s*-\s*\[\]", "Checkbox missing space inside bracket: '- []'"),
    (r"^\s*-\[\s*[ xX]?\s*\]", "Missing space between dash and bracket: '-[ ]'"),
    (r"^\s*\*\s*\[[ xX]\]", "Asterisk checkbox (recommend dash '- [ ]'): '* [ ]'"),
]

DOC_TYPES = [
    ("TODO.md", ["todo.md"], "make-a-change/todo/v1"),
    ("FEEDBACK.md", ["feedback.md", "feedbacks.md", "FEEDBACKS.md"], "make-a-change/feedback/v1"),
    ("CHANGELOG.md", ["changelog.md"], "make-a-change/changelog/v1"),
    ("DECISIONS.md", ["decisions.md", "ADR.md", "adr.md"], "make-a-change/decisions/v1"),
    ("ROADMAP.md", ["roadmap.md"], "make-a-change/roadmap/v1"),
    ("INCIDENTS.md", ["incidents.md"], "make-a-change/incidents/v1"),
    ("EXPERIMENTS.md", ["experiments.md"], "make-a-change/experiments/v1"),
]


def extract_schema(content: str) -> str | None:
    match = FRONTMATTER_REGEX.match(content)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.strip().startswith("schema:"):
            return line.split(":", 1)[1].strip()
    return None


def check_unclosed_blocks(content: str) -> list[int]:
    """Returns line numbers of unclosed code blocks."""
    lines = content.splitlines()
    in_block = False
    block_start = 0
    for idx, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            if not in_block:
                in_block = True
                block_start = idx
            else:
                in_block = False
    return [block_start] if in_block else []


def check_checkboxes(content: str) -> list[tuple[int, str]]:
    """Validates checkbox lines, supporting nested items."""
    findings = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        for pattern, msg in MALFORMED_CHECKBOXES:
            if re.search(pattern, line):
                findings.append((idx, msg))
    return findings


def audit_document(file_path: Path, expected_schema: str, fix: bool = False) -> tuple[list[str], list[str], bool]:
    errors: list[str] = []
    warnings: list[str] = []
    modified = False

    content = file_path.read_text(encoding="utf-8")
    schema = extract_schema(content)

    if not schema:
        if fix:
            header = f"---\nschema: {expected_schema}\n---\n\n"
            file_path.write_text(header + content, encoding="utf-8")
            warnings.append(f"Auto-injected 'schema: {expected_schema}' frontmatter")
            modified = True
        else:
            warnings.append(f"Missing schema frontmatter (expected: 'schema: {expected_schema}')")

    # Check unclosed codeblocks
    unclosed = check_unclosed_blocks(content)
    for line_no in unclosed:
        errors.append(f"L{line_no}: Unclosed code block (```)")

    # Check checkbox formatting (supports nested checkboxes)
    cb_errors = check_checkboxes(content)
    for line_no, msg in cb_errors:
        warnings.append(f"L{line_no}: Malformed checkbox: {msg}")

    # Check secrets
    for regex, label in SECRET_PATTERNS:
        matches = re.finditer(regex, content)
        for m in matches:
            line_no = content[:m.start()].count("\n") + 1
            errors.append(f"L{line_no}: [SECRET] Potential {label} detected in public file")

    return errors, warnings, modified


def audit_repo(repo_dir: Path, fix: bool = False, as_json: bool = False, strict: bool = False) -> int:
    results: dict = {
        "repo": str(repo_dir.resolve()),
        "case_collisions": [],
        "documents": {},
        "errors_count": 0,
        "warnings_count": 0,
    }

    # 1. Check Case Collisions
    root_files = [f.name for f in repo_dir.iterdir() if f.is_file()]
    lowered = {}
    for name in root_files:
        low = name.lower()
        if low in lowered:
            msg = f"Found '{name}' alongside '{lowered[low]}' on case-insensitive filesystem"
            results["case_collisions"].append(msg)
            results["errors_count"] += 1
        lowered[low] = name

    # 2. Check Each Registered Document Type
    for canonical_name, aliases, expected_schema in DOC_TYPES:
        target_path = repo_dir / canonical_name
        is_alias = False
        if not target_path.exists():
            for alias in aliases:
                alt = repo_dir / alias
                if alt.exists():
                    target_path = alt
                    is_alias = True
                    break

        if target_path.exists():
            doc_errs, doc_warns, modified = audit_document(target_path, expected_schema, fix=fix)
            if is_alias:
                doc_warns.append(f"Named '{target_path.name}'; canonical uppercase recommendation is '{canonical_name}'")

            results["documents"][target_path.name] = {
                "path": str(target_path),
                "lines": len(target_path.read_text(encoding="utf-8").splitlines()),
                "errors": doc_errs,
                "warnings": doc_warns,
                "auto_fixed": modified,
            }
            results["errors_count"] += len(doc_errs)
            results["warnings_count"] += len(doc_warns)

    if as_json:
        print(json.dumps(results, indent=2))
        return 1 if results["errors_count"] > 0 or (strict and results["warnings_count"] > 0) else 0

    # Human-readable output
    print(f"Auditing make-a-change ecosystem in: {repo_dir.resolve()}")
    print("-" * 60)

    for coll in results["case_collisions"]:
        print(f"❌ [CASE COLLISION] {coll}")

    for doc_name, data in results["documents"].items():
        err_count = len(data["errors"])
        warn_count = len(data["warnings"])
        icon = "❌" if err_count > 0 else "⚠️" if warn_count > 0 else "✓"
        status_msg = f"{data['lines']} lines"
        if data["auto_fixed"]:
            status_msg += " (auto-fixed)"
        print(f"{icon} {doc_name:18} ({status_msg})")

        for err in data["errors"]:
            print(f"    ❌ {err}")
        for warn in data["warnings"]:
            print(f"    ⚠️ {warn}")

    print("-" * 60)
    print(f"Audit finished: {results['errors_count']} error(s), {results['warnings_count']} warning(s).")

    if strict and results["warnings_count"] > 0:
        return 1
    return 1 if results["errors_count"] > 0 else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("repo", nargs="?", default=".", help="Repository root directory (default: .)")
    parser.add_argument("--fix", action="store_true", help="Auto-inject missing frontmatter safely")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    parser.add_argument("--strict", action="store_true", help="Exit code 1 on warnings as well as errors")
    args = parser.parse_args()

    return audit_repo(Path(args.repo), fix=args.fix, as_json=args.json, strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
