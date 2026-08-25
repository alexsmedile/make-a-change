# Keep a Decision Specification (v1.0.0)

A lightweight, soft-markdown Architecture Decision Record (ADR) convention for `DECISIONS.md` (or `ADR.md`).

---

## 1. Principles

1. **Dual-Audience Contract**: YAML frontmatter (`schema: make-a-change/decisions/v1`) + human-scannable markdown.
2. **Context, Choice, & Consequences**: Every decision captures why it was made, alternatives considered, and what downstream work it spawns.
3. **Status Horizons**: Grouped by status: `## Accepted`, `## Proposed`, `## Superseded`, `## Deprecated`.
4. **Actionable Spawns**: Decisions link directly to tasks spawned in `TODO.md` via `<!-- spawns: todo-xxx -->`.

---

## 2. Frontmatter Declaration

```yaml
---
schema: make-a-change/decisions/v1
---
```

---

## 3. Standard Structure

```markdown
---
schema: make-a-change/decisions/v1
---

# Decisions

Architectural decision log and design choices for this repository.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## Accepted

### 2026-08-25: Dual-Audience YAML Frontmatter for Work Items <!-- ref: adr-001 -->
- **Context**: Need standard schema declaration that agents can parse deterministically while keeping files clean on GitHub.
- **Decision**: Adopt YAML frontmatter (`schema: make-a-change/todo/v1`) with hierarchical slash notation.
- **Consequences**: Standardized cross-tool parsing, zero parser collisions on unquoted strings, native metadata cards on GitHub.
- **Spawns**: [TODO] Update templates and linter script <!-- ref: todo-004 -->

## Proposed

### 2026-09-01: SQLite vs JSON for Session Memory Caching <!-- ref: adr-002 -->
- **Context**: High concurrency during multi-agent sessions causes write contention on flat JSON files.
- **Proposed**: Migrate memory persistence layer to SQLite WAL mode.
- **Status**: Under review / benchmarking.

## Superseded

### 2026-05-10: Monolithic Shell Scripts <!-- ref: adr-000, superseded-by: adr-001 -->
- Superseded by modular Python CLI tools.
```
