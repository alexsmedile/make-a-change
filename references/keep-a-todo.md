# Keep a Todo Specification (v1.0.0)

A predictable, human-first, soft-markdown standard for project task lists (`TODO.md`).

---

## 1. Principles

1. **Dual-Audience Contract**: YAML frontmatter (`schema: make-a-change/todo/v1`) for agents/tools + readable GFM markdown for humans.
2. **Flexible Heading Clustering (No Enforced Taxonomy)**:
   - Headings like `## Now` / `## Next` / `## Later` are common illustrative examples (like "Bob and Alice" in cryptography).
   - Projects are free to use any clustering:
     - *Horizon*: `## Now`, `## Next`, `## Later`
     - *Kanban*: `## Todo`, `## Doing`, `## Done`
     - *Agile*: `## Backlog`, `## In Progress`, `## Done`
     - *Domain Packages*: `## Auth`, `## CLI`, `## Frontend`, `## Docs`
     - *Flat / Chronological*: Pure recency order with zero section headings
     - *Omission*: Omitting completed / `Done` sections entirely
   - The standard and linters never enforce rigid heading names—they only validate syntax, unclosed blocks, and frontmatter correctness.
3. **Nested Subtasks Supported**: Indented checkboxes (`  - [ ] child task`) are natively supported and parsed as parent-child task hierarchies.
4. **Primary Topic vs Multi-Tags**:
   - `[topic]`: Architectural domain / package (`[auth]`, `[cli]`, `[billing]`, `[ui]`).
   - `#tags`: Cross-cutting labels (`#bug`, `#security`, `#dx`, `#perf`).
5. **Surgical In-Place Edits**: Tools parse and update sections without wiping uncommitted notes or comments.
6. **Case-Insensitive Integrity**: The file is canonically `TODO.md`. Never create `todo.md` concurrently.

---

## 2. Frontmatter Declaration

```yaml
---
schema: make-a-change/todo/v1
extensions:
  - octopus:all # Options: octopus:all | octopus:sigils | octopus:topics | octopus:yaml
---
```

### Supported Extensions

| Extension | Unlocked Capability |
|:---|:---|
| *(None / Base)* | Standard GFM task lists `- [ ] [topic] Task description` with any heading layout or nested subtasks. |
| `octopus:sigils` | Compact inline sigils: `~bucket`, `!priority`, `due:`, `#tags`. |
| `octopus:topics` | Strict primary domain classification: `[topic]` vs multi-tag `#tag1 #tag2`. |
| `octopus:yaml` | Indented body blocks (`> ...`) and rich YAML blocks (blockers, actor, energy, stage). |
| `octopus:all` | Full superpower bundle (Sigils + Topics + YAML Blocks + Subtasks). |

---

## 3. Syntax Grammar

### A. Buckets (`~`)
- `~o` or `~!` : **Open / Now** (Active in current cycle)
- `~n` : **Next** (Prioritized queue)
- `~b` : **Backlog / Later** (Ideas, icebox)
- `~d` : **Done** (Completed, ready for changelog)

### B. Priority (`!`)
- `!P1` / `!!` : **P1 - Critical / Urgent** (Blocker, top priority)
- `!P2` / `!h` : **P2 - Normal / High** (Current sprint focus)
- `!P3` / `!l` : **P3 - Low / Nice-to-have** (Polish, non-blocking)

### C. Due & Dates
- `due:YYYY-MM-DD` or `date:YYYY-MM-DD`
- `📅 YYYY-MM-DD` / `🗓️ YYYY-MM-DD` / `📆 YYYY-MM-DD`

---

## 4. Standard Structure Examples

### Example 1: Horizon Clustering (`Now` / `Next` / `Later`)

```markdown
---
schema: make-a-change/todo/v1
---

# Todo

Project roadmap and task ledger.

## Now

- [ ] [setup] Configure test environment and linter
  - [ ] Add pre-commit hook installer
  - [ ] Add GitHub Actions CI workflow
- [ ] [api] Implement health check endpoint

## Next

- [ ] [auth] User login and registration flow

## Later

- [ ] [infra] Staging deployment setup
```

---

### Example 2: Kanban Clustering (`Todo` / `Doing` / `Done`)

```markdown
---
schema: make-a-change/todo/v1
---

# Todo

## Doing

- [ ] [auth] Fix token refresh race condition

## Todo

- [ ] [billing] Integrate Stripe webhook verification
- [ ] [docs] Write API documentation

## Done

- [x] [setup] Initialize repository structure
```

---

### Example 3: Flat Recency List (Zero Headings)

```markdown
---
schema: make-a-change/todo/v1
---

# Todo

- [ ] [cli] Add --json output flag to audit script
- [ ] [auth] Fix session cookie expiration
- [ ] [docs] Add architecture diagram to README
```
