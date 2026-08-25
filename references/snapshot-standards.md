# Snapshot & State Preservation Standard (v1.0.0)

Conventions for immutable point-in-time file snapshots, milestone freezing, and pre-migration recovery.

---

## 1. Snapshot Naming Conventions

`make-a-change` standardizes **file naming formats** for immutable snapshots. Projects choose their preferred storage location (`_archive/`, `snapshots/`, `_backups/`, `backups/`, etc.):

| Pattern | Format | Primary Use Case | Example |
|:---|:---|:---|:---|
| **Content-Hash** | `<file>@<short-hash>.<ext>` | Deduplicated configuration & prompt snapshots (8-char SHA-256). | `CLAUDE@5ec4b283.md`<br>`settings@33cd0ed5.json` |
| **Milestone Release** | `<file>@<version>.<ext>` | Frozen tasklist snapshots at release graduation. | `TODO@v1.2.0.md`<br>`TODO@2026.08.md` |
| **Timestamped Backup** | `YYYY-MM-DD_<name>.bak`<br>`YYYY-MM-DD_<name>.zip` | Point-in-time recovery before batch refactors or agent migrations. | `2026-08-25_TODO.bak`<br>`2026-08-25_backup.zip` |

---

## 2. When to Snapshot

1. **At Version Release**: Freeze completed tasks to `<file>@<version>.<ext>` when graduating items into `CHANGELOG.md`.
2. **Before Destructive Migrations**: Save `YYYY-MM-DD_<name>.bak` before running automated bulk refactors or mass regex rewrites.
3. **Continuous Config Backups**: Use `<file>@<short-hash>.<ext>` when tracking external tool configs into a central repository.

---

## 3. Guiding Invariant: Non-Prescriptive Storage

> The standard defines **how to name snapshots**, not where to store them.

- Storing snapshots in `_archive/`, `snapshots/`, `_backups/`, or directly alongside files is project discretion.
- Any directory holding raw local snapshots that should not be tracked in Git should be declared in `.gitignore` (e.g. `_backups/`, `*.bak`).
