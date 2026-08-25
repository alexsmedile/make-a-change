---
name: make-a-change
description: |
  Standardized work-item management for repositories following soft markdown standards:
  FEEDBACK.md (Keep a Feedback) → TODO.md (Keep a Todo) → CHANGELOG.md (Keep a Changelog).
  Enforces case-collision protection, safe in-place updates, secret scrubbing, and
  business IP sanitization before writing tasks or feedback.
version: 1.0.0
category: workflow
status: current
tags: [todo, feedback, changelog, work-items, privacy, sanitization]
---

# make-a-change

Unified work-item lifecycle manager and soft-markdown guardian for **`FEEDBACK.md`**, **`TODO.md`**, and **`CHANGELOG.md`**.

```text
  Observation / Intake          Prioritized Planning               Shipped Release
┌──────────────────────┐      ┌──────────────────────┐      ┌─────────────────────────┐
│     FEEDBACK.md      │ ───► │       TODO.md        │ ───► │      CHANGELOG.md       │
│  (Keep a Feedback)   │      │    (Keep a Todo)     │      │   (Keep a Changelog)    │
└──────────────────────┘      └──────────────────────┘      └─────────────────────────┘
           │                             │
           └──────────────┬──────────────┘
                          ▼
             🛡️ PRIVACY & IP SANITIZER
             - Zero API keys / credentials
             - De-identify private business IP
             - Route secrets to _local/
```

---

## 1. Trigger Matrix

Activate this skill when:
- User asks to add, update, organize, prioritize, or check items in `TODO.md` or `todo.md`.
- User provides feedback, bug observations, UX friction, or feature requests to log in `FEEDBACK.md`.
- Tasks are completed and ready to be graduated into `CHANGELOG.md` (`[Unreleased]`).
- User asks to initialize standard task/feedback tracking in a repository.
- Auditing repository work items for sensitive credentials or private business secrets.

---

## 2. Invariant Guardrails & Safe File Operations

1. **Case-Insensitive APFS / NTFS Hazard**:
   - Never create a parallel lowercase `todo.md` if `TODO.md` exists (or vice versa).
   - Before creating any work-item file, check existing casing in the repo root and preserve canonical convention.
2. **Never Blind-Overwrite / Truncate**:
   - NEVER overwrite, clobber, or write whole-file templates over non-empty existing files.
   - Always read and parse existing sections (`## Now`, `## Next`, `## Open`, etc.), then perform surgical insertions or status toggles (`- [ ]` -> `- [x]`).
3. **Zero Secrets & IP Sanitization**:
   - Audit every incoming item against the **Privacy Sanitizer**:
     - No API keys, passwords, bearer tokens, or internal credentials.
     - In public repos, sanitize/generalize unannounced proprietary roadmap items, commercial deal details, and customer PII.
     - Divert sensitive execution notes to `_local/TODO.local.md` (gitignored).

---

## 3. Standard Soft Markdown Specifications

### A. `TODO.md` (Keep a Todo)
Groups tasks by planning horizon:
- **`# Todo`**: Header with brief description.
- **`## Now`**: Actively in-progress or top-priority items for the current cycle.
- **`## Next`**: Prioritized queue for upcoming iterations.
- **`## Later`**: Backlog, exploration ideas, or icebox.
- **`## Done (Unreleased)`**: Recently finished items ready to graduate into `CHANGELOG.md`.

*Item Format*: `- [ ] [category] Clear task description <!-- ref: optional-id -->`

### B. `FEEDBACK.md` (Keep a Feedback)
Captures raw observations and user feedback:
- **`# Feedback`**: Header.
- **`## Open`**: New observations awaiting triage.
- **`## Under Review`**: Feedback being evaluated or designed.
- **`## Addressed`**: Feedback promoted to `TODO.md` or already resolved.

*Item Format*: `- [ ] **[Bug|UX|Perf|Feature]** Title: Detail description <!-- ref: fb-id -->`

### C. `CHANGELOG.md` (Keep a Changelog)
Follows [Keep a Changelog](https://keepachangelog.com/en/2.0.0/) standard:
- **`## [Unreleased]`**: Staging ground for changes waiting for next version tag.
- Subheaders: `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`.

---

## 4. Operational Workflows

### Flow 1: Adding a Todo Item (`TODO.md`)
1. **Pre-Flight**: Check root for `TODO.md` (or `todo.md`). Read full contents.
2. **Sanitize**: Check input for keys, URLs with tokens, private customer names, or sensitive business IP.
   - If sensitive: generalize for public `TODO.md` and log specifics in `_local/TODO.local.md`.
3. **Categorize & Insert**: Place in appropriate section (`## Now`, `## Next`, `## Later`) maintaining alphabetical or priority order.
4. **Verify**: Ensure no duplicate entries and file structure remains valid markdown.

### Flow 2: Recording Feedback (`FEEDBACK.md`)
1. **Pre-Flight**: Check root for `FEEDBACK.md`. Create from template if missing.
2. **Sanitize & Tag**: Classify type (`[Bug]`, `[UX]`, `[Perf]`, `[Feature]`).
3. **Append**: Add to `## Open` section with actionable summary.

### Flow 3: Promoting Feedback to Todo
1. Move/tag item in `FEEDBACK.md` under `## Addressed` with reference pointer: `(Promoted to TODO.md: [category] ...)`.
2. Insert actionable task into `TODO.md` under `## Next` or `## Now`.

### Flow 4: Graduating Done Todos to Changelog
1. Identify `- [x]` items under `TODO.md` `## Now` or `## Done (Unreleased)`.
2. Format entries under appropriate `CHANGELOG.md` `## [Unreleased]` subcategory (`Added`, `Fixed`, etc.).
3. Clear graduated items from `TODO.md` (or archive to `_archive/` if large).

---

## 5. References & Helpers

- Detailed Specs: See [`references/keep-a-todo.md`](references/keep-a-todo.md) and [`references/keep-a-feedback.md`](references/keep-a-feedback.md).
- Privacy & Redaction Guide: See [`references/privacy-sanitizer.md`](references/privacy-sanitizer.md).
- Templates: See [`templates/`](templates/).
- CLI Linter: `python3 scripts/audit-work-items.py <repo-path>`
