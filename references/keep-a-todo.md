# Keep a Todo Specification (v1.0.0)

A predictable, human-first, soft-markdown standard for project task lists (`TODO.md`).

---

## 1. Principles

1. **Dual-Audience Contract**: YAML frontmatter (`schema: make-a-change/todo/v1`) for agents/tools + readable GFM markdown for humans.
2. **Horizon-Based Grouping**: Tasks are prioritized by execution timing (`Now`, `Next`, `Later`, `Done (Unreleased)`), avoiding brittle numeric ranking.
3. **Primary Topic vs Multi-Tags**:
   - `[topic]`: Architectural domain / package (`[auth]`, `[cli]`, `[billing]`, `[ui]`). Exactly one primary topic per task.
   - `#tags`: Cross-cutting labels (`#bug`, `#security`, `#dx`, `#perf`).
4. **Surgical In-Place Edits**: Tools parse and update sections without wiping uncommitted notes or comments.
5. **Case-Insensitive Integrity**: The file is canonically `TODO.md`. Never create `todo.md` concurrently.

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
| *(None / Base)* | Standard GFM task lists `- [ ] [topic] Task description` organized in `## Now`, `## Next`, `## Later`. |
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

### Minimal Baseline (Empty Canvas)

```markdown
---
schema: make-a-change/todo/v1
---

# Todo

Project roadmap and task ledger.

## Now

- [ ] [setup] Configure test environment and linter
- [ ] [api] Implement health check endpoint

## Next

- [ ] [auth] User login and registration flow

## Later

- [ ] [infra] Staging deployment setup

## Done (Unreleased)

- [x] [repo] Initialize repository structure
```

---

### Extended with Octopus Superpowers (`extensions: [octopus:all]`)

```markdown
---
schema: make-a-change/todo/v1
extensions:
  - octopus:all
---

# Todo

Project roadmap and task ledger.

## Now

- [ ] [auth] Enterprise SSO with Multi-Tenant SAML/OIDC ~o !P1 due:2026-09-01 #auth #enterprise
  > Complete SAML 2.0 and OIDC authorization code grant flow with PKCE.
  ```yaml
  kind: feat
  actor: ai
  stage: spec
  energy: high
  blocked_by: database-tenant-isolation
  pinned: true
  ```
  - [ ] Implement SAML metadata parser
  - [ ] Add ACS callback endpoint and session cookie issuer

- [ ] [perf] Memory pressure fix during large diff rendering ~o !P1 #perf

## Next

- [ ] [cli] Add interactive task triage mode ~n !P2 #dx

## Later

- [ ] [export] Taskwarrior and Linear bi-directional sync ~b !P3 #idea

## Done (Unreleased)

- [x] [security] Invariant rules for zero file overwrites <!-- ref: todo-001 -->
```
