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

## Why `make-a-change`?

1. **The Work-Item Lifecycle**: Seamlessly connects raw user feedback → prioritized tasks → shipped release notes without heavy, fragile JSON machinery.
2. **Case-Collision & Overwrite Protection**: Prevents silent data loss caused by case-insensitive filesystems (macOS APFS / Windows NTFS) where `todo.md` clobbers `TODO.md`.
3. **Built-in Privacy & IP Sanitizer**: Prevents accidental leakage of API keys, confidential business roadmaps, customer PII, or internal credentials into public repository task lists.
4. **Soft-Markdown Standards**: Follows human-scannable GFM task lists and predictable heading hierarchies.

---

## The Trinity Specifications

### 1. `FEEDBACK.md` (Keep a Feedback)
Captures raw observations, bug reports, UX friction, and user input:
- `## Open`: New triage items.
- `## Under Review`: Items being evaluated.
- `## Addressed`: Feedback promoted to `TODO.md` or resolved.

### 2. `TODO.md` (Keep a Todo)
Prioritizes execution across execution horizons:
- `## Now`: In-progress / immediate sprint items.
- `## Next`: Prioritized upcoming backlog.
- `## Later`: Long-term exploration & icebox.
- `## Done (Unreleased)`: Completed tasks ready to graduate into `CHANGELOG.md`.

### 3. `CHANGELOG.md` (Keep a Changelog)
Standard release ledger conforming to [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/) and Semantic Versioning.

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
│   └── privacy-sanitizer.md          # IP sanitization & secret filtering guide
├── templates/
│   ├── TODO.md.template              # Canonical starter template
│   ├── FEEDBACK.md.template          # Canonical feedback starter
│   └── CHANGELOG.md.template         # Keep a Changelog standard starter
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
