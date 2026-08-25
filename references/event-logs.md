# Event-Based Logs Specification (v1.0.0)

A universal, repeatable soft-markdown convention for all event-based records: **`INCIDENTS.md`**, **`EXPERIMENTS.md`**, **`BENCHMARKS.md`**, **`RETROSPECTIVES.md`**, etc.

---

## 1. The Core Pattern

Every event log follows the same elegant, flexible structure:
1. **Dual-Audience Frontmatter**: `schema: make-a-change/<type>/v1`
2. **Human Title & Subtitle**: Format disclaimer.
3. **Event Headings**: Identifiers formatted as `### <DATE>: <TITLE>` or `### <CODE>: <TITLE>`.
4. **Structured Bullets**: Key metadata and observations.

---

## 2. Example A: `INCIDENTS.md` (Postmortems & Failures)

```markdown
---
schema: make-a-change/incidents/v1
---

# Incidents

Blameless incident log and postmortem records.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## 2026-08-25: APFS Case-Insensitive Silent File Truncation <!-- ref: inc-001 -->
- **Severity**: High (Data Loss)
- **Impact**: `TODO.md` content overwritten during `todo.md` write due to APFS inode collision.
- **Root Cause**: APFS case-insensitivity + agent blind truncation without pre-read check.
- **Remediation**:
  - [x] Added non-negotiable workspace safety invariants to `shared/l1/00-invariants.md`.
  - [x] Added case-collision detection to `scripts/audit-work-items.py`.
```

---

## 3. Example B: `EXPERIMENTS.md` (Research, Spikes, & Benchmarks)

```markdown
---
schema: make-a-change/experiments/v1
---

# Experiments

Hypothesis testing, benchmark logs, and technical spikes.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## EXP-004: Token Densification via Squirrel Micro-Kernel <!-- ref: exp-004 -->
- **Date**: 2026-08-25
- **Hypothesis**: Replacing conversational prompt prose with decision matrices reduces always-loaded token overhead by >60% without losing routing accuracy.
- **Method**: Rewrote base prompt modules and benchmarked on 50 multi-turn test scenarios.
- **Result**: Slashed prompt size by 73% (100% test pass rate).
- **Outcome**: **ADOPTED** <!-- graduated: v2.0.0 -->
```
