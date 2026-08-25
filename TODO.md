---
schema: make-a-change/todo/v1
extensions:
  - octopus:all
---

# Todo

Project roadmap and actionable task list for `make-a-change`.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## Now

- [ ] [adr] Check Spectacular ADR / Decision system and decide whether to conform / harmonize ~o !P1 <!-- ref: mac-002 -->
- [ ] [cli] Add GitHub Actions workflow for automated work-item validation in CI ~o !P1 <!-- ref: mac-001 -->
- [ ] [docs] Add visual badges and markdown cheatsheet to README ~o !P2

## Next

- [ ] [integration] Add pre-commit hook installer script `scripts/install-hooks.sh` ~n !P2
- [ ] [templates] Support custom template variables via optional `.make-a-change.toml` ~n !P3

## Later

- [ ] [export] Optional JSON/YAML export adapter for external issue sync (Taskwarrior / Linear / GitHub Issues) ~b !P3

## Done (Unreleased)

- [x] [core] Initial specification for Keep a Todo and Keep a Feedback
- [x] [security] Built-in privacy sanitizer and case-collision protections
- [x] [cli] Deterministic work-item auditor script `audit-work-items.py`
- [x] [schema] Dual-audience YAML frontmatter schema declaration standard (`make-a-change/todo/v1`)
- [x] [suite] Full ecosystem suite: DECISIONS.md, ROADMAP.md, INCIDENTS.md, EXPERIMENTS.md, and `_local/` private companions
