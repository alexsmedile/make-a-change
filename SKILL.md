---
name: make-a-change
description: |
  Dual-Audience work-item lifecycle standard (FEEDBACK → DECISIONS → TODO → CHANGELOG).
  Guarantees APFS case-collision safety, zero blind overwrites, secret scrubbing, and
  private companion routing (TODO.local.md).
version: 1.2.0
category: workflow
status: current
tags: [todo, feedback, changelog, decisions, roadmap, privacy, octopus]
---

# make-a-change

Dual-Audience work-item lifecycle and soft-markdown governance standard.

## 1. Non-Negotiable Invariants

- **Case-Insensitive APFS/NTFS Safety**: Check root casing before writing. Never create parallel lowercase `todo.md` when `TODO.md` exists.
- **No Blind Overwrites**: Inspect target content before editing. Perform in-place section updates; never truncate non-empty files.
- **Zero Secrets in Public Git**: Sanitize credentials/private IP. Divert internal notes to `TODO.local.md` (root default, gitignored) or `_local/`.
- **Dual-Audience Contract**: Preserve `schema: make-a-change/<type>/v1` frontmatter on all managed documents.

## 2. Operation Matrix

| Op | Trigger / Intent | Action & Target File | Progressive Disclosure |
|---|---|---|---|
| `intake` | Log bug, friction, feedback | Append to `FEEDBACK.md` (`## Open`) with `[Bug\|UX\|Perf\|Feature]` | [keep-a-feedback.md](references/keep-a-feedback.md) |
| `decide` | Architecture / design choice | Record in `DECISIONS.md` (`## Accepted` / `## Proposed`) | [keep-a-decision.md](references/keep-a-decision.md) |
| `plan` | Add / prioritize task | Insert into `TODO.md` (`## Now` / `## Next` / `## Later`) with `[topic]` | [keep-a-todo.md](references/keep-a-todo.md) |
| `roadmap` | Strategic vision / horizon | Update `ROADMAP.md` (`## 🎯 vX.X` / `## 🚀 vY.Y`) | [keep-a-roadmap.md](references/keep-a-roadmap.md) |
| `event` | Incident / experiment spike | Log to `INCIDENTS.md` or `EXPERIMENTS.md` (`### DATE: Title` + bullets) | [event-logs.md](references/event-logs.md) |
| `graduate` | Task done (`- [x]`) | Move from `TODO.md` → stage in `CHANGELOG.md` (`## [Unreleased]`) | [metadata-provenance.md](references/metadata-provenance.md) |
| `audit` | Lint / check leaks / case | Run `python3 scripts/audit-work-items.py <repo>` | [privacy-sanitizer.md](references/privacy-sanitizer.md) |

## 3. Work-Item Lifecycle Pipeline

```text
FEEDBACK.md (Open) ──► DECISIONS.md (Accepted) ──► TODO.md (Now/Next) ──► CHANGELOG.md (Unreleased)
     │                                                    │
     └───────────────► 🛡️ PRIVACY SANITIZER ──────────────┘
                       (Strip secrets ──► TODO.local.md)
```

## 4. Syntax Quick-Cheatsheet

- **TODO Item**: `- [ ] [topic] Imperative action ~bucket !priority due:YYYY-MM-DD #tags <!-- ref: id, from: id -->`
  - *Buckets (`~`)*: `~o` (open/now) · `~n` (next) · `~b` (backlog) · `~d` (done)
  - *Priorities (`!`)*: `!P1` (critical) · `!P2` (high/normal) · `!P3` (low)
  - *Scope vs Tag*: `[topic]` = single primary architectural domain · `#tags` = multi cross-cutting labels
- **Rich Context Block**: Use indented blockquote `  > desc` and `  ```yaml` block (`kind:`, `actor:`, `blocked_by:`, `energy:`).
