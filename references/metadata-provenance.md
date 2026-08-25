# Metadata, Provenance, & Private Companions Guide (v1.0.0)

How to link work items across the lifecycle and safely isolate sensitive data.

---

## 1. Lightweight HTML Comment Tags

Use single-line HTML comments to embed machine-readable metadata that remains invisible in rendered markdown:

| Tag | Purpose | Where to Use | Example |
|:---|:---|:---|:---|
| `<!-- ref: <id> -->` | Unique item identifier | All files | `<!-- ref: todo-045 -->` or `<!-- ref: fb-012 -->` |
| `<!-- from: <id> -->` | Source provenance link | `TODO.md` | `<!-- from: fb-012 -->` (spawned from feedback) |
| `<!-- blocked-by: <id> -->` | Dependency link | `TODO.md` | `<!-- blocked-by: todo-040 -->` |
| `<!-- spawns: <id> -->` | Triggered task link | `DECISIONS.md` | `<!-- spawns: todo-050 -->` |
| `<!-- promoted: <target> -->`| Status progression | `FEEDBACK.md` | `<!-- promoted: TODO.md#now -->` |
| `<!-- graduated: <version> -->`| Release graduation | `TODO.md` | `<!-- graduated: v1.2.0 -->` |
| `<!-- superseded-by: <id> -->`| Decision replacement | `DECISIONS.md` | `<!-- superseded-by: adr-005 -->` |

---

## 2. Multi-Property YAML Codeblocks

When a work item requires rich, multi-property attributes (blockers, assigned agent, energy, stage), use indented markdown YAML blocks:

```markdown
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
```

---

## 3. The `_local/` & `*.local.md` Private Companions Convention

For repos where public task tracking is committed to git, but certain notes, API keys, or confidential customer details must remain local:

### Rules
1. **Public File (`TODO.md`)**: Committed to git. Uses sanitized, high-level task descriptions.
2. **Private Companion (`_local/TODO.local.md` or `TODO.local.md`)**: Always gitignored. Contains credentials, customer names, private draft links, and internal context.
3. **Linkage**: Both files share the same `<!-- ref: id -->` identifiers so tools can correlate them locally.

```text
my-project/
├── .gitignore             # Includes: _local/ and *.local.md
├── TODO.md                # Public sanitized tasks (schema: make-a-change/todo/v1)
└── _local/
    └── TODO.local.md      # Private companion notes & internal keys
```
