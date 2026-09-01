---
name: make-a-change
description: |
  Dual-Audience work-item lifecycle standard for managing repo markdown artifacts
  (FEEDBACK.md, DECISIONS.md, TODO.md, CHANGELOG.md, ROADMAP.md, INCIDENTS.md, EXPERIMENTS.md).
  Guarantees APFS case safety, zero blind overwrites, secret scrubbing, and private companion routing (TODO.local.md).

  Triggers on: "update TODO", "log to FEEDBACK.md", "record decision in DECISIONS.md", "cut changelog",
  "work-item intake", "bump changelog", "make a change", or authoring repo-level task/decision markdown files.

  Do NOT invoke for: Casual chat feedback review, conversational brainstorming, clarifying user notes,
  user commentary, feature critiques, or conversational "#feedback" tags on skills/tools/code where no
  repository work-item markdown files (FEEDBACK.md, TODO.md, etc.) are explicitly requested to be created or modified.
version: 0.2.2
category: workflow
status: current
tags: [work-items, todo-md, feedback-md, changelog-md, decisions, roadmap, privacy, release, snapshot]
---

# make-a-change

Dual-Audience work-item lifecycle and soft-markdown governance standard.

## 1. Non-Negotiable Invariants

- **Scope Boundary**: Governs repository markdown files only. DO NOT activate for conversational chat triage, prompt brainstorming, general Q&A, or informal "#feedback" commentary on features/skills unless explicitly instructed to write/append to a repository work-item file (`FEEDBACK.md`, `TODO.md`, `DECISIONS.md`).
- **Case-Insensitive APFS/NTFS Safety**: Check root casing before writing. Never create parallel lowercase `todo.md` when `TODO.md` exists.
- **No Blind Overwrites**: Inspect target content before editing. Perform in-place section updates; never truncate non-empty files.
- **Zero Secrets in Public Git**: Sanitize credentials/private IP. Divert internal notes to `TODO.local.md` (root default, gitignored) or `_local/`.
- **Dual-Audience Contract**: Preserve `schema: make-a-change/<type>/v1` frontmatter on all managed documents.

## 2. Operation Matrix

| Op | Trigger / Intent | Action & Target File | Progressive Disclosure |
|---|---|---|---|
| `intake` | Explicitly log item to `FEEDBACK.md` | Append to `FEEDBACK.md` (`## Open`) with `[Bug\|UX\|Perf\|Feature]` | [keep-a-feedback.md](references/keep-a-feedback.md) |
| `decide` | Architecture / design choice | Record in `DECISIONS.md` (`## Accepted` / `## Proposed`) | [keep-a-decision.md](references/keep-a-decision.md) |
| `plan` | Add / prioritize task | Insert into `TODO.md` (`## Now` / `## Next` / `## Later`) with `[topic]` | [keep-a-todo.md](references/keep-a-todo.md) |
| `roadmap` | Strategic vision / horizon | Update `ROADMAP.md` (`## 🎯 vX.X` / `## 🚀 vY.Y`) | [keep-a-roadmap.md](references/keep-a-roadmap.md) |
| `event` | Incident / experiment spike | Log to `INCIDENTS.md` or `EXPERIMENTS.md` (`### DATE: Title` + bullets) | [event-logs.md](references/event-logs.md) |
| `release` | Cut release / ship version | Graduate `[Unreleased]` → `[vX.Y.Z]`, snapshot cycle, clear `- [x]` | [version-standards.md](references/version-standards.md) |
| `snapshot` | Backup state before refactor | Save point-in-time state (`<file>@<hash>`, `<file>@<ver>`, `.bak`) | [snapshot-standards.md](references/snapshot-standards.md) |
| `audit` | Lint / check leaks / case | Run `python3 scripts/audit-work-items.py <repo>` | [privacy-sanitizer.md](references/privacy-sanitizer.md) |

## 3. Work-Item Lifecycle Pipeline

```text
FEEDBACK.md (Open) ──► DECISIONS.md (Accepted) ──► TODO.md (Now/Next) ──► CHANGELOG.md (Unreleased)
     │                                                    │
     └───────────────► 🛡️ PRIVACY SANITIZER ──────────────┘
                       (Strip secrets ──► TODO.local.md)
```

## 4. Base Standard & Extensions

- **Base Item (Clean GFM)**: `- [ ] [topic] Imperative action statement <!-- ref: id, from: id -->`
  - *Sections*: `## Now` (current focus) · `## Next` (upcoming) · `## Later` (backlog) · `## Done (Unreleased)`
  - *Domain*: `[topic]` = single primary architectural package (`[auth]`, `[cli]`, `[ui]`)
- **Optional Extensions (`extensions: [octopus:*]`)**: Rich sigils (`~bucket`, `!priority`, `due:`, `#tags`) and YAML blocks are opt-in for tool integrations. See [keep-a-todo.md](references/keep-a-todo.md).
