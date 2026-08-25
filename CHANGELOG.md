---
schema: make-a-change/changelog/v1
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of `make-a-change` skill and tool suite.
- Soft-markdown specifications for `FEEDBACK.md` (Keep a Feedback) and `TODO.md` (Keep a Todo).
- Dual-Audience YAML frontmatter schema declaration standard (`make-a-change/todo/v1`).
- Expanded ecosystem suite: `DECISIONS.md`, `ROADMAP.md`, `INCIDENTS.md`, `EXPERIMENTS.md`.
- Provenance tag standards (`ref:`, `from:`, `blocked-by:`, `spawns:`, `graduated:`) and `_local/` private companions.
- Integrated Privacy & IP Sanitizer for stripping secrets, credentials, and confidential roadmap IP.
- Deterministic CLI auditor `scripts/audit-work-items.py` with case-collision and secret detection.
- Starter templates for all 7 document types.
- Multi-harness deployment symlinks for Claude, Codex, Gemini/Antigravity, Grok, Hermes, OpenClaw, and Cursor.
