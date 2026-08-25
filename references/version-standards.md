# Versioning & Release Standard (v1.0.0)

How to manage semantic releases, changelog graduations, and schema invariance across `make-a-change` repositories.

---

## 1. The Release Graduation Ritual

When cutting a release (e.g. `v1.2.0`):

1. **Promote `[Unreleased]`**:
   In `CHANGELOG.md`, rename `## [Unreleased]` to the new version header:
   ```markdown
   ## [1.2.0] - 2026-08-25
   ```
   Add a fresh empty `## [Unreleased]` section at the top.

2. **Archive Completed Tasks**:
   Save a milestone snapshot of the finished cycle (e.g. `_archive/TODO@v1.2.0.md` or `snapshots/TODO@v1.2.0.md`).

3. **Clear Completed Tasks in `TODO.md`**:
   Remove `- [x]` items that have graduated to the changelog, leaving the active backlog clean for the next cycle.

4. **Tag Git Commit**:
   ```bash
   git commit -am "chore(release): cut v1.2.0"
   git tag -a v1.2.0 -m "Release v1.2.0"
   ```

---

## 2. Semantic Versioning Rules (SemVer 2.0.0)

| Version Component | When to Bump | Example |
|:---|:---|:---|
| **`MAJOR` (X.0.0)** | Breaking API or contract changes that require user migration. | Removing a CLI flag, breaking schema changes. |
| **`MINOR` (1.X.0)** | Backwards-compatible new features or new document types. | Adding `ROADMAP.md` support or `--json` CLI flag. |
| **`PATCH` (1.0.X)** | Backwards-compatible bug fixes and security patches. | Fixing a regex in linter, correcting a doc typo. |

---

## 3. The Rule of Schema Invariance

> **Application releases bump SemVer; schema frontmatter reflects the grammar contract.**

- A repository operating at release `v2.4.0` continues to declare `schema: make-a-change/todo/v1`.
- The `/v1` suffix indicates the **parsing grammar version**, which only bumps if the core AST or frontmatter structure fundamentally breaks.
- Additive fields (`extensions: [...]`, new HTML comment tags, custom headings) do **NOT** bump the schema version.
