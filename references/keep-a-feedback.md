# Keep a Feedback Specification (v1.0.0)

A soft-markdown convention for capturing qualitative user feedback, bug reports, and UX friction in `FEEDBACK.md` (or `FEEDBACKS.md`).

---

## 1. Principles

1. **Dual-Audience Contract**: YAML frontmatter (`schema: make-a-change/feedback/v1`) for agents + GFM task lists for humans.
2. **Intake Before Planning**: Feedback captures raw observations and user friction before engineering triage turns them into `TODO.md` tasks.
3. **Traceable Lifecycle**: Seamlessly promotes from `FEEDBACK.md` → `TODO.md` → `CHANGELOG.md`.

---

## 2. Frontmatter Declaration

```yaml
---
schema: make-a-change/feedback/v1
---
```

---

## 3. Standard Structure

```markdown
---
schema: make-a-change/feedback/v1
---

# Feedback

All notable user feedback, bug reports, and UX observations.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## Open

- [ ] **[UX]** Search filter reset on second tag selection. <!-- ref: fb-001 -->
- [ ] **[Bug]** CLI crashes when config file is empty. <!-- ref: fb-002 -->

## Under Review

- [ ] **[Feature]** Add multi-tenant organization support. <!-- ref: fb-003 -->

## Addressed

- [x] **[Bug]** Fix crash on empty config. (Promoted to TODO: [cli] Fix config parser → Released in v1.1.0)
```

---

## 4. Item Classification

| Tag | Category | Example |
|:---|:---|:---|
| **`[Bug]`** | Functional failure or error | `**[Bug]** Non-zero exit code missing on failed build` |
| **`[UX]`** | Visual quirk, confusion, friction | `**[UX]** Delete button has no confirmation prompt` |
| **`[Perf]`** | Latency, memory pressure, CPU spike | `**[Perf]** High memory during 50+ file diffs` |
| **`[Feature]`** | New capability request | `**[Feature]** Add --json output flag to status verb` |
| **`[Doc]`** | Confusing or missing docs | `**[Doc]** Missing environment variables list in README` |
