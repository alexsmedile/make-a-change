# make-a-change

Unified work-item lifecycle manager, architectural decision logger, and soft-markdown guardian for developer workspaces.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        make-a-change Ecosystem                         │
├────────────────────────────────────────────────────────────────────────┤
│  Strategic:      ROADMAP.md         (Where we are going)               │
│  Intake:         FEEDBACK.md        (What users/observers notice)      │
│  Decisions:      DECISIONS.md       (Why we chose this architecture)   │
│  Execution:      TODO.md            (What we are building now/next)    │
│  Investigation:  EXPERIMENTS.md     (What we tested & benchmarked)     │
│  Learning:       INCIDENTS.md       (What failed & how we remediated)  │
│  Historical:     CHANGELOG.md       (What we actually shipped)         │
│  Private:        _local/*.local.md  (Local confidential companion)     │
└────────────────────────────────────────────────────────────────────────┘
```

## Why `make-a-change`?

1. **Dual-Audience Contract**: Every document starts with structured YAML frontmatter (`schema: make-a-change/<type>/v1`) for AI agents and CLI tools, followed by standard GFM markdown for human readability.
2. **The Work-Item Lifecycle**: Seamlessly connects raw user feedback → architectural decisions → prioritized tasks → shipped release notes.
3. **Case-Collision & Inode Safety**: Prevents silent data loss caused by case-insensitive filesystems (macOS APFS / Windows NTFS) where `todo.md` clobbers `TODO.md`.
4. **Built-in Privacy & IP Sanitizer**: Prevents accidental leakage of API keys, confidential business roadmaps, customer PII, or internal credentials into public repository task lists.
5. **Private Companions (`_local/`)**: Native support for gitignored `_local/TODO.local.md` companions to store sensitive credentials and internal notes safely.

---

## The Document Suite

| Document | Schema | Purpose | Key Sections |
|:---|:---|:---|:---|
| **`TODO.md`** | `make-a-change/todo/v1` | Execution roadmap & active tasks | `## Now`, `## Next`, `## Later`, `## Done (Unreleased)` |
| **`FEEDBACK.md`** | `make-a-change/feedback/v1` | Raw user observations & bug intake | `## Open`, `## Under Review`, `## Addressed` |
| **`CHANGELOG.md`** | `make-a-change/changelog/v1` | Shipped release notes (Keep a Changelog) | `## [Unreleased]`, `### Added`, `### Fixed`, etc. |
| **`DECISIONS.md`** | `make-a-change/decisions/v1` | Architecture decision records (ADR) | `## Accepted`, `## Proposed`, `## Superseded` |
| **`ROADMAP.md`** | `make-a-change/roadmap/v1` | Strategic milestones & target releases | `## 🎯 v1.0`, `## 🚀 v2.0`, `## 🔭 Future` |
| **`INCIDENTS.md`** | `make-a-change/incidents/v1` | Blameless incident postmortems | Event headings (`### YYYY-MM-DD: Title`) + Bullets |
| **`EXPERIMENTS.md`**| `make-a-change/experiments/v1` | Hypothesis testing & benchmark logs | Event headings (`### EXP-001: Title`) + Bullets |

---

## Provenance & Metadata Tags

Link work items across files with lightweight HTML comments:

```markdown
<!-- ref: todo-045 -->               <!-- Unique ID -->
<!-- from: fb-012 -->                <!-- Spawned from feedback -->
<!-- blocked-by: todo-040 -->        <!-- Dependency link -->
<!-- spawns: todo-050 -->            <!-- Triggered from decision -->
<!-- graduated: v1.2.0 -->           <!-- Shipped release tag -->
```

---

## Directory Structure

```text
make-a-change/
├── SKILL.md                          # Primary agent skill definition
├── README.md                         # Project documentation
├── TODO.md                           # Repository task list
├── FEEDBACK.md                       # Feedback ledger
├── CHANGELOG.md                      # Changelog
├── references/
│   ├── keep-a-todo.md                # Soft-markdown spec for TODO.md
│   ├── keep-a-feedback.md            # Soft-markdown spec for FEEDBACK.md
│   ├── keep-a-decision.md            # Soft-markdown spec for DECISIONS.md (ADR)
│   ├── keep-a-roadmap.md             # Soft-markdown spec for ROADMAP.md
│   ├── event-logs.md                 # Event-based spec (INCIDENTS.md, EXPERIMENTS.md)
│   ├── metadata-provenance.md        # Provenance tags & _local/ private companions
│   └── privacy-sanitizer.md          # IP sanitization & secret filtering guide
├── templates/
│   ├── TODO.md.template              # Canonical starter template
│   ├── FEEDBACK.md.template          # Canonical feedback starter
│   ├── CHANGELOG.md.template         # Keep a Changelog standard starter
│   ├── DECISIONS.md.template         # Architecture decision starter
│   ├── ROADMAP.md.template           # Roadmap starter
│   ├── INCIDENTS.md.template         # Incident postmortem starter
│   └── EXPERIMENTS.md.template       # Experiment spike starter
└── scripts/
    └── audit-work-items.py           # CLI validation & secret scanner script
```

## CLI Linter

Run the built-in validator against any repository:

```bash
python3 scripts/audit-work-items.py /path/to/repo
```

## License

MIT © 2026 Alex Smedile
