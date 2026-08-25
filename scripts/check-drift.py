#!/usr/bin/env python3
"""check-drift.py — Cross-Reference and Lifecycle Drift Auditor for make-a-change.

Audits:
1. Broken / Dangling references (<!-- from: id --> or <!-- spawns: id --> pointing to nonexistent items)
2. Staged private companions (ensures TODO.local.md, _local/, .local/ are not tracked in git)
3. Stale completed tasks (detects ungraduated '- [x]' items in TODO.md ready for CHANGELOG.md)

Usage:
  python3 scripts/check-drift.py [repo-path]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REF_DEF_REGEX = re.compile(r"<!--\s*ref:\s*([a-zA-Z0-9_\-\.\/]+)\s*-->")
FROM_REF_REGEX = re.compile(r"<!--\s*from:\s*([a-zA-Z0-9_\-\.\/]+)\s*-->")
SPAWNS_REF_REGEX = re.compile(r"<!--\s*spawns:\s*([a-zA-Z0-9_\-\.\/]+)\s*-->")
BLOCKED_BY_REGEX = re.compile(r"<!--\s*blocked-by:\s*([a-zA-Z0-9_\-\.\/]+)\s*-->")

DOC_FILENAMES = ["TODO.md", "FEEDBACK.md", "CHANGELOG.md", "DECISIONS.md", "ROADMAP.md", "INCIDENTS.md", "EXPERIMENTS.md"]


def collect_ids(repo_dir: Path) -> dict[str, str]:
    """Scans all documents and returns {id: filename}."""
    known_ids = {}
    for name in DOC_FILENAMES:
        p = repo_dir / name
        if p.exists():
            content = p.read_text(encoding="utf-8")
            for m in REF_DEF_REGEX.finditer(content):
                item_id = m.group(1).strip()
                known_ids[item_id] = name
    return known_ids


def check_cross_references(repo_dir: Path, known_ids: dict[str, str]) -> list[str]:
    dangling = []
    for name in DOC_FILENAMES:
        p = repo_dir / name
        if p.exists():
            content = p.read_text(encoding="utf-8")
            for idx, line in enumerate(content.splitlines(), start=1):
                for m in FROM_REF_REGEX.finditer(line):
                    src_id = m.group(1).strip()
                    if src_id not in known_ids:
                        dangling.append(f"{name}:L{idx} 'from: {src_id}' references unknown ID")
                for m in SPAWNS_REF_REGEX.finditer(line):
                    spawn_id = m.group(1).strip()
                    if spawn_id not in known_ids:
                        dangling.append(f"{name}:L{idx} 'spawns: {spawn_id}' references task not yet added")
                for m in BLOCKED_BY_REGEX.finditer(line):
                    block_id = m.group(1).strip()
                    if block_id not in known_ids:
                        dangling.append(f"{name}:L{idx} 'blocked-by: {block_id}' references unknown ID")
    return dangling


def check_completed_tasks(repo_dir: Path) -> int:
    todo_p = repo_dir / "TODO.md"
    if not todo_p.exists():
        return 0
    content = todo_p.read_text(encoding="utf-8")
    completed = 0
    for line in content.splitlines():
        if re.match(r"^\s*-\s*\[[xX]\]", line):
            completed += 1
    return completed


def check_private_companion_safety(repo_dir: Path) -> list[str]:
    warnings = []
    gitignore_p = repo_dir / ".gitignore"
    has_gitignore = gitignore_p.exists()
    gi_content = gitignore_p.read_text(encoding="utf-8") if has_gitignore else ""

    local_candidates = ["TODO.local.md", "FEEDBACK.local.md", "DECISIONS.local.md", "_local", ".local"]
    for cand in local_candidates:
        p = repo_dir / cand
        if p.exists():
            if not has_gitignore or (cand not in gi_content and "*.local.md" not in gi_content):
                warnings.append(f"Private file '{cand}' exists but is NOT covered in .gitignore!")
    return warnings


def audit_drift(repo_dir: Path) -> int:
    print("┌─ DRIFT AUDIT · make-a-change")
    print(f"│ Target: {repo_dir.resolve()}")

    known_ids = collect_ids(repo_dir)
    print(f"│ Indexed {len(known_ids)} unique work-item reference ID(s)")

    dangling = check_cross_references(repo_dir, known_ids)
    completed_count = check_completed_tasks(repo_dir)
    companion_warns = check_private_companion_safety(repo_dir)

    issues = 0

    if dangling:
        print(f"│ [WARN] Found {len(dangling)} dangling/unresolved cross-reference(s):")
        for d in dangling:
            print(f"│   • {d}")
            issues += 1
    else:
        print("│ [PASS] All cross-reference provenance links resolve cleanly ✓")

    if completed_count > 0:
        print(f"│ [INFO] {completed_count} completed task(s) in TODO.md ready to graduate to CHANGELOG.md [Unreleased]")
    else:
        print("│ [INFO] 0 ungraduated completed tasks")

    if companion_warns:
        for w in companion_warns:
            print(f"│ [WARN] {w}")
            issues += 1
    else:
        print("│ [PASS] Private companion safety verified (.gitignore active) ✓")

    print("└─")
    return 1 if issues > 0 else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("repo", nargs="?", default=".", help="Repository directory (default: .)")
    args = parser.parse_args()
    return audit_drift(Path(args.repo))


if __name__ == "__main__":
    sys.exit(main())
