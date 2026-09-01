---
schema: make-a-change/changelog/v1
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.2] - 2026-09-01

### Fixed
- **Anti-Overtrigger Guard for Chat Hashtags & Critique**: Hardened `SKILL.md` frontmatter, invariants, and `intake` operation against conversational `#feedback` hashtags, user commentary, and feature critiques aimed at skills or tools.
- **Specific Tag Namespaces**: Replaced broad tags (`todo`, `feedback`) with precise document tags (`todo-md`, `feedback-md`, `work-items`) to prevent generic semantic token matching across platforms.

## [0.2.1] - 2026-09-01

### Fixed
- **Skill Routing Boundaries**: Added explicit positive trigger matching and direct negative constraints (`Do NOT invoke for: Casual chat feedback review...`) in `SKILL.md` frontmatter and invariants to prevent over-triggering during conversational chat triage.


### Added
- **Expanded Document Suite**: Full support and templates for `DECISIONS.md` (ADR), `ROADMAP.md` (Milestones), `INCIDENTS.md`, and `EXPERIMENTS.md`.
- **Developer Tooling Suite**:
  - `scripts/audit-work-items.py`: Universal linter with `--fix`, `--json`, and `--strict` flags, flexible heading support, unclosed codeblock detection, and nested checkbox validation.
  - `scripts/check-drift.py`: Cross-reference provenance auditor and private companion safety checker.
  - `scripts/install-hooks.sh`: 1-command Git pre-commit guard installer.
  - `.github/workflows/make-a-change-audit.yml`: Turnkey GitHub Actions CI workflow for pull requests and pushes.
- **The Manifesto & Governance Standards**:
  - `docs/manifesto.md`: The 7 Tenets of `make-a-change`.
  - `references/version-standards.md`: Release graduation ritual, SemVer guidance, and Schema Invariance rules.
  - `references/snapshot-standards.md`: State preservation naming conventions (`@hash`, `@version`, `.bak`).
- **Private Companions Convention**: Root-level `TODO.local.md` as default private companion, with `_local/` and `.local/` supported.
- **5-Layer Micro-Kernel**: Densified `SKILL.md` to 51 lines with operational matrix (`op: release`, `op: snapshot`).

## [0.1.0] - 2026-08-25

### Added
- Initial core release of `make-a-change`.
- Soft-markdown specifications for `FEEDBACK.md` (Keep a Feedback), `TODO.md` (Keep a Todo), and `CHANGELOG.md` (Keep a Changelog).
- Dual-Audience YAML frontmatter schema declaration standard (`schema: make-a-change/<type>/v1`).
- APFS and NTFS case-collision and blind overwrite prevention invariants.
- Integrated Privacy & IP Sanitizer for stripping secrets and credentials.
- Starter templates for `TODO.md`, `FEEDBACK.md`, and `CHANGELOG.md`.
- Multi-harness deployment symlinks for Claude Code, Codex, Antigravity/Gemini, Grok, Hermes, OpenClaw, and Cursor.
