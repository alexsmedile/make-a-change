# The 7 Tenets of make-a-change (The Manifesto)

A declaration of repository governance, machine-agent collaboration, and human-first markdown standards.

---

### 1. Dual-Audience Contract
Every repository document starts with structured YAML frontmatter (`schema: make-a-change/<type>/v1`) for deterministic parsing by AI coding assistants and CLI scripts, followed by standard GitHub Flavored Markdown for human readers.

### 2. Inode & Case Safety
Filesystems on macOS (APFS/HFS+) and Windows (NTFS) are case-insensitive. Writing to `todo.md` when `TODO.md` exists causes silent, unrecoverable data loss. Tools and agents must perform pre-flight case checks and non-destructive in-place edits.

### 3. Zero Secrets in Public Git
Sensitive credentials, private API tokens, customer names, and confidential commercial roadmap items must never enter public Git history. Public files stay clean, while live private details live in gitignored `TODO.local.md` companions.

### 4. Flexible Topology
We enforce syntax, bracket integrity, and block closure—never rigid heading names. Whether a project clusters by Horizons (`## Now`/`## Next`), Kanban (`## Todo`/`## Doing`/`## Done`), Sprints, Domain Packages, or uses a flat recency list with zero headings, all topologies are first-class citizens.

### 5. End-to-End Lineage
Work flows seamlessly through an auditable lifecycle:
`FEEDBACK.md` (Intake) → `DECISIONS.md` (Architecture) → `TODO.md` (Execution) → `CHANGELOG.md` (Release).

### 6. Progressive Extensions
The core standard is minimal and unencumbered. Specialized tool capabilities—such as inline sigils (`~o`, `!P1`, `due:`) or rich YAML execution blocks—are opt-in extensions (`extensions: [octopus:*]`) disclosed on demand.

### 7. Deterministic Verification
Governance must be verifiable without human ceremony. Deterministic CLI linters and drift checks run silently in local pre-commit hooks and automated CI pipelines to catch defects before code is merged.
