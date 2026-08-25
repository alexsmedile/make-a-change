<div align="center">

# make-a-change

**The Dual-Audience Work-Item & Repository Governance Standard**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Schema](https://img.shields.io/badge/schema-make--a--change%2Fv1-blueviolet.svg)](#the-document-suite)
[![Platform](https://img.shields.io/badge/platform-Claude%20%7C%20Codex%20%7C%20Antigravity%20%7C%20Hermes%20%7C%20Cursor-black.svg)](#multi-harness-installation)
[![Octopus Compatible](https://img.shields.io/badge/Octopus-compatible-orange.svg)](#octopus-superpowers)

<p align="center">
  <b>Observation</b> (<code>FEEDBACK.md</code>) &nbsp;→&nbsp; 
  <b>Decisions</b> (<code>DECISIONS.md</code>) &nbsp;→&nbsp; 
  <b>Planning</b> (<code>TODO.md</code>) &nbsp;→&nbsp; 
  <b>Release</b> (<code>CHANGELOG.md</code>)
</p>

</div>

---

> **Plain claim**: A zero-dependency, human-first Markdown standard that gives AI coding assistants deterministic schema safety, protects gitignored files from silent OS case-collisions, and guarantees sensitive business secrets never leak into public task lists.

---

## ⚡ The Contrast: Why `make-a-change`?

| Without `make-a-change` | With `make-a-change` |
|:---|:---|
| **Silent Data Loss**: An agent told `todo.md` silently clobbers `TODO.md` on case-insensitive macOS (APFS) / Windows (NTFS). | **Inode & Case Safety**: Pre-flight collision checks and strict non-destructive update invariants. |
| **Accidental Secret Leaks**: Raw API keys, internal endpoints, or confidential deal sizes committed to public `TODO.md`. | **Privacy Sanitizer & `_local/`**: Automated abstraction for public git + gitignored `_local/TODO.local.md` companions. |
| **Parsing Guesswork**: Agents struggle to parse ad-hoc task lists, mixing completed items with active bugs. | **Dual-Audience Contract**: Clean YAML frontmatter (`schema: make-a-change/todo/v1`) for agents + scannable GFM for humans. |
| **Broken Traceability**: Feedback gets lost in chat logs; shipped features miss changelog entries. | **End-to-End Provenance**: Unbroken trace: `FEEDBACK.md` → `DECISIONS.md` → `TODO.md` → `CHANGELOG.md`. |

---

## 🚀 Quick Start (Under 60 Seconds)

### 1. Give it to your AI Assistant
Paste this prompt into **Claude Code**, **Codex**, **Antigravity**, or **Cursor**:
> Scaffold standard `make-a-change` work-item tracking (`TODO.md`, `FEEDBACK.md`, `CHANGELOG.md`) in this repository.

### 2. Prefer the CLI Linter?
Audit your repository's task files, case collisions, and secret patterns:
```bash
python3 scripts/audit-work-items.py .
```

---

## 📄 The Document Suite

Every document follows the **Dual-Audience pattern**: structured YAML frontmatter at the top for deterministic agent and script parsing, followed by standard human-first Markdown:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        make-a-change Ecosystem                         │
├────────────────────────────────────────────────────────────────────────┤
│  Strategic:      ROADMAP.md         (schema: make-a-change/roadmap/v1) │
│  Intake:         FEEDBACK.md        (schema: make-a-change/feedback/v1)│
│  Decisions:      DECISIONS.md       (schema: make-a-change/decisions/v1│
│  Execution:      TODO.md            (schema: make-a-change/todo/v1)    │
│  Investigation:  EXPERIMENTS.md     (schema: make-a-change/experiments/│
│  Learning:       INCIDENTS.md       (schema: make-a-change/incidents/v1│
│  Historical:     CHANGELOG.md       (schema: make-a-change/changelog/v1│
│  Private:        _local/*.local.md  (Local confidential companions)    │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 📝 Syntax & Standard Anatomy

### `TODO.md` (`schema: make-a-change/todo/v1`)

```markdown
---
schema: make-a-change/todo/v1
extensions:
  - octopus:all
---

# Todo

Project roadmap and actionable task list.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## Now

- [ ] [auth] Fix token refresh race condition ~o !P1 due:2026-08-30 #security
- [ ] [cli] Add `--json` streaming format ~o !P2 #dx

## Next

- [ ] [billing] Integrate Stripe webhook verification ~n !P2 📅 2026-09-15 #billing

## Later

- [ ] [plugin] Native VS Code extension bridge ~b !P3 #idea

## Done (Unreleased)

- [x] [core] Prevent file overwrites on case-insensitive filesystems
```

---

## 🐙 Octopus Superpowers

When `extensions: [octopus:all]` or `[octopus:sigils]` is declared, your `TODO.md` unlocks full compatibility with the **Octopus** task engine:

| Grammar | Purpose | Meaning |
|:---|:---|:---|
| `[topic]` | Primary Domain | Single architectural package (e.g. `[auth]`, `[cli]`, `[billing]`). |
| `#tags` | Cross-Cutting Labels | Multi-label descriptors (e.g. `#bug`, `#security`, `#dx`). |
| `~o` / `~n` / `~b` / `~d` | Execution Bucket | `~o` (Open/Now), `~n` (Next), `~b` (Backlog), `~d` (Done). |
| `!P1` / `!P2` / `!P3` | Priority Horizon | `!P1` (Critical), `!P2` (Normal/High), `!P3` (Low). |
| `due:YYYY-MM-DD` | Due Date | Explicit deadline timestamp or calendar emoji (`📅`). |
| ````yaml ... ```` | Rich Block | Indented YAML block for blockers, assigned actor, energy, and stage. |

---

## 💬 Simulated Execution Transcript

Here is how an autonomous agent uses `make-a-change` during a real engineering session:

```text
User: "The search bar crashes when searching special characters, let's fix it and make sure we log everything."

Agent: 1. Logging intake into FEEDBACK.md:
          - [ ] **[Bug]** Search query crashes on unescaped regex characters <!-- ref: fb-019 -->
       2. Triaging to TODO.md under ## Now:
          - [ ] [search] Escape regex query delimiters in search parser ~o !P1 <!-- from: fb-019 -->
       3. Implementing fix in src/search/parser.ts...
       4. Running test suite... 12/12 passing ✓
       5. Marking TODO.md as completed:
          - [x] [search] Escape regex query delimiters in search parser
       6. Staging release note in CHANGELOG.md [Unreleased]:
          ### Fixed
          - Fixed application crash caused by unescaped regex special characters in search input.

System: Verified 0 case collisions, 0 leaked credentials. Ready to ship!
```

---

## 🛡️ Privacy Sanitizer & Private Companions (`TODO.local.md`)

Before committing tasks to public repositories, `make-a-change` enforces strict secret scrubbing:

1. **Public File (`TODO.md`)**: Committed to Git with abstracted, public-safe descriptions.
2. **Private Companion (`TODO.local.md`)**: Root-level gitignored companion holding raw credentials, customer names, or private deal terms. (Subfolders `_local/TODO.local.md` and `.local/TODO.local.md` are also supported).
3. **Trace Linkage**: Both files share the same `<!-- ref: ... -->` comment IDs for local tool correlation.

```text
my-repo/
├── .gitignore             # Includes: *.local.md, _local/, .local/
├── TODO.md                # Public sanitized tasks (schema: make-a-change/todo/v1)
└── TODO.local.md          # Default private companion (root, gitignored)
```

---

## 📦 Multi-Harness Installation

`make-a-change` is natively packaged as a cross-platform skill.

### Method 1: Instant Symlink Bridge (Claude, Codex, Antigravity, Hermes, Grok, OpenClaw, Cursor)
```bash
# Clone to your local skills library
git clone https://github.com/alexsmedile/make-a-change.git ~/vault/data/skills_db/make-a-change

# Link into your preferred harness
ln -sfn ~/vault/data/skills_db/make-a-change ~/.claude/skills/make-a-change
ln -sfn ~/vault/data/skills_db/make-a-change ~/.agents/skills/make-a-change
ln -sfn ~/vault/data/skills_db/make-a-change ~/.gemini/config/skills/make-a-change
ln -sfn ~/vault/data/skills_db/make-a-change ~/.hermes/skills/make-a-change
ln -sfn ~/vault/data/skills_db/make-a-change ~/.grok/skills/make-a-change
ln -sfn ~/vault/data/skills_db/make-a-change ~/.openclaw/skills/make-a-change
ln -sfn ~/vault/data/skills_db/make-a-change ~/.cursor/skills/make-a-change
```

---

## 🎯 Who This Is For / Not For

### Right for you if:
- You work with AI coding agents (Claude Code, Codex, Antigravity, Cursor, OpenCode) and want **zero accidental file clobbers**.
- You want clean, scannable, human-readable repository governance without heavyweight database tooling.
- You maintain open-source or commercial repositories and need strict privacy guardrails for roadmap and task notes.

### Not for you if:
- You require a heavy, database-backed enterprise issue tracker (e.g. Jira, Linear) for multi-thousand-person task assignments.
- You prefer binary/proprietary task formats over plain text Markdown.

---

## 📜 License

MIT © 2026 [Alex Smedile](https://github.com/alexsmedile).
