---
name: make-a-change
description: |
  Standardized work-item management for repositories following soft markdown standards:
  FEEDBACK.md (Keep a Feedback) → TODO.md (Keep a Todo) → CHANGELOG.md (Keep a Changelog).
  Uses Dual-Audience YAML frontmatter (schema: make-a-change/todo/v1) and extension flags (octopus:all).
  Enforces case-collision protection, safe in-place updates, secret scrubbing, and
  business IP sanitization before writing tasks or feedback.
version: 1.1.0
category: workflow
status: current
tags: [todo, feedback, changelog, work-items, privacy, sanitization, octopus]
---

# make-a-change

Unified work-item lifecycle manager and soft-markdown guardian for **`FEEDBACK.md`**, **`TODO.md`**, and **`CHANGELOG.md`**.

```text
  Observation / Intake          Prioritized Planning               Shipped Release
┌──────────────────────┐      ┌──────────────────────┐      ┌─────────────────────────┐
│     FEEDBACK.md      │ ───► │       TODO.md        │ ───► │      CHANGELOG.md       │
│ (make-a-change/      │      │ (make-a-change/      │      │ (make-a-change/         │
│  feedback/v1)        │      │  todo/v1)            │      │  changelog/v1)          │
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

## 3. Standard Dual-Audience Specifications

### A. `TODO.md` (`schema: make-a-change/todo/v1`)
Dual-audience frontmatter declaring schema and extensions:
- **`schema: make-a-change/todo/v1`**
- **`extensions: [octopus:all | octopus:sigils]`** (optional)
- **`[topic]` vs `#tags`**: Primary architectural domain `[auth]` vs cross-cutting `#bug #security`.
- **Buckets**: `~o` (open/now), `~n` (next), `~b` (backlog), `~d` (done).
- **Priorities**: `!P1` (critical), `!P2` (normal/high), `!P3` (low).
- **Sections**: `## Now`, `## Next`, `## Later`, `## Done (Unreleased)`.

### B. `FEEDBACK.md` (`schema: make-a-change/feedback/v1`)
Captures raw observations and user feedback:
- **`schema: make-a-change/feedback/v1`**
- **Sections**: `## Open`, `## Under Review`, `## Addressed`.
- **Item Format**: `- [ ] **[Bug|UX|Perf|Feature|Doc]** Title: Detail description <!-- ref: fb-id -->`

### C. `CHANGELOG.md` (`schema: make-a-change/changelog/v1`)
Follows [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/) standard:
- **`## [Unreleased]`**: Staging ground for changes waiting for next version tag.
- Subheaders: `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`.

---

## 4. Operational Workflows

### Flow 1: Adding a Todo Item (`TODO.md`)
1. **Pre-Flight**: Check root for `TODO.md` (or `todo.md`). Read full contents.
2. **Detect Schema**: Verify frontmatter `schema: make-a-change/todo/v1`. If missing, add frontmatter safely preserving all existing content.
3. **Sanitize**: Check input for keys, URLs with tokens, private customer names, or sensitive business IP.
   - If sensitive: generalize for public `TODO.md` and log specifics in `_local/TODO.local.md`.
4. **Categorize & Insert**: Place in appropriate section (`## Now`, `## Next`, `## Later`) maintaining alphabetical or priority order.
5. **Verify**: Ensure no duplicate entries and file structure remains valid markdown.

### Flow 2: Recording Feedback (`FEEDBACK.md`)
1. **Pre-Flight**: Check root for `FEEDBACK.md`. Create from template if missing.
2. **Sanitize & Tag**: Classify type (`[Bug]`, `[UX]`, `[Perf]`, `[Feature]`).
3. **Append**: Add to `## Open` section with actionable summary.

### Flow 3: Promoting Feedback to Todo
1. Move/tag item in `FEEDBACK.md` under `## Addressed` with reference pointer: `(Promoted to TODO: [category] ...)`.
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
