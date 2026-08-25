# Keep a Feedback Specification (v1.0.0)

A soft-markdown convention for capturing qualitative user feedback, bug reports, and UX friction in `FEEDBACK.md` (or `FEEDBACKS.md`).

## 1. Principles

1. **Intake Before Planning**: Feedback captures what users observed, struggled with, or requested before triage turns it into engineering tasks.
2. **Clear Triage States**: Feedback lives in `Open` (raw), `Under Review` (evaluating), or `Addressed` (promoted to `TODO.md` or completed).
3. **Traceability**: An item can graduate cleanly: `Feedback → Todo → Changelog`.

---

## 2. Standard Structure

```markdown
# Feedback

All notable user feedback, bug reports, and UX observations.

## Open

- [ ] **[UX]** Search filters clear on second tag selection. <!-- ref: fb-001 -->
- [ ] **[Bug]** CLI crashes when config file is empty. <!-- ref: fb-002 -->

## Under Review

- [ ] **[Feature]** Add multi-tenant organization support. <!-- ref: fb-003 -->

## Addressed

- [x] **[Bug]** Fix crash on empty config. (Promoted to TODO `[cli] Fix config parse` → Released in v1.1.0)
```

---

## 3. Feedback Item Classification

| Tag | Purpose | Example |
|:---|:---|:---|
| **`[Bug]`** | Functional failure or crash | `**[Bug]** Exit code 0 returned on syntax error` |
| **`[UX]`** | Confusion, visual quirk, friction | `**[UX]** Delete button has no confirmation modal` |
| **`[Perf]`** | Slowness, latency, high memory | `**[Perf]** High CPU on large markdown rendering` |
| **`[Feature]`** | New capability request | `**[Feature]** Support export to CSV` |
| **`[Doc]`** | Missing or confusing documentation | `**[Doc]** Missing environment variables list in README` |
