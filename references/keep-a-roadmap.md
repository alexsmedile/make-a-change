# Keep a Roadmap Specification (v1.0.0)

A soft-markdown convention for strategic vision, milestones, and release targets in `ROADMAP.md`.

---

## 1. Principles

1. **Dual-Audience Contract**: YAML frontmatter (`schema: make-a-change/roadmap/v1`) + milestone checklist.
2. **Strategic Horizons**: Organizes high-level objectives into versions, quarters, or strategic phases.
3. **Public-Safe Abstraction**: Defines user-facing capabilities without leaking internal secret implementations or private deal specifics.
4. **Traceability**: Roadmap goals link downward to actionable tasks in `TODO.md`.

---

## 2. Frontmatter Declaration

```yaml
---
schema: make-a-change/roadmap/v1
---
```

---

## 3. Standard Structure

```markdown
---
schema: make-a-change/roadmap/v1
---

# Roadmap

Strategic direction, version milestones, and long-term targets.
Format adheres to [make-a-change](https://github.com/alexsmedile/make-a-change).

## 🎯 v2.0: Core Engine & Multi-Agent Mesh (Q3 2026) <!-- ref: road-v2 -->
- [ ] Universal skill synchronization across 7 agent harnesses.
- [ ] Invariant file safety against silent APFS overwrites.
- [ ] Deterministic CLI linting in automated CI.

## 🚀 v3.0: Cloud Collaboration & Autonomous Fleet (Q4 2026) <!-- ref: road-v3 -->
- [ ] Real-time session streaming and peer agent coordination.
- [ ] Native IDE sidecar extension.

## 🔭 Future Horizons (Icebox / Exploration)
- [ ] Universal bi-directional sync adapter (Linear / GitHub Issues / Taskwarrior).
```
