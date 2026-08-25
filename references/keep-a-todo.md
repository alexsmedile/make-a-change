# Keep a Todo Specification (v1.0.0)

A predictable, human-first, soft-markdown standard for project task lists (`TODO.md`).

## 1. Principles

1. **Human & Agent Readable**: Standard GitHub Flavored Markdown (GFM) task lists (`- [ ]`, `- [x]`).
2. **Horizon-Based Grouping**: Tasks are prioritized by execution timing (`Now`, `Next`, `Later`), not rigid numerical scores that rot quickly.
3. **Surgical In-Place Edits**: Tools must parse and update sections without wiping uncommitted notes or comments.
4. **Case-Insensitive Integrity**: The file is canonically `TODO.md`. Never create `todo.md` concurrently.

---

## 2. Standard Structure

```markdown
# Todo

Brief one-line statement of project focus or current cycle goal.

## Now

- [ ] [scope] Active or immediate priority item <!-- ref: optional-id -->
- [ ] [scope] Another active task

## Next

- [ ] [scope] Upcoming prioritized feature or refactor
- [ ] [scope] Secondary improvement

## Later

- [ ] [scope] Long-term exploration, ideas, or icebox items

## Done (Unreleased)

- [x] [scope] Finished task ready for next changelog release <!-- graduated-to: CHANGELOG.md -->
```

---

## 3. Item Syntax

```markdown
- [ ] [tag] Imperative action statement <!-- ref: id, from: fb-id -->
```

- **Status Box**: `- [ ]` (pending) or `- [x]` (completed).
- **Category Tag**: `[area]` or `[package]`, e.g., `[auth]`, `[cli]`, `[docs]`, `[ui]`, `[perf]`.
- **Imperative Verb**: Start with action verb (e.g. `Add`, `Fix`, `Refactor`, `Benchmark`, `Document`).
- **Optional Metadata**: HTML comment `<!-- ref: ... -->` for provenance and non-distracting cross-links.
