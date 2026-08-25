# Privacy, Secret Scrubbing & IP Sanitizer Guide

Before writing or updating items in `TODO.md` or `FEEDBACK.md` (especially in public or shared repositories), apply these sanitization rules.

---

## 1. Threat Models & What to Filter

### A. Hard Secrets & Credentials (Zero Tolerance)
- API Keys (`sk-`, `ghp_`, `AKIA...`, `Bearer ...`)
- Database connection strings (`postgres://user:pass@host:port/db`)
- Private IP addresses, internal domain hostnames (`*.corp.internal`)
- Authorization headers or session cookies

### B. Confidential Business Secrets & Roadmap IP
- Unannounced confidential product features or proprietary algorithm names
- Commercial deal values, enterprise customer names (`Acme Corp $100k POC`)
- Proprietary partnership negotiations or legal strategies
- Internal pricing formulas

### C. Personal Identifiable Information (PII)
- Customer personal emails, phone numbers, addresses, user IDs in raw logs

---

## 2. Sanitization & Abstraction Patterns

| Raw Context / Request | ❌ Unsafe Public Todo | ✅ Sanitized Public Todo |
|:---|:---|:---|
| "Need to hook up Stripe live key sk_live_abc123 to charge BigClient Inc for their custom plan" | `- [ ] Setup Stripe live key sk_live_abc123 for BigClient` | `- [ ] [billing] Integrate automated enterprise invoice generation` |
| "Customer user@acme.com reported database timeout on postgres://admin:pass@prod-db:5432" | `- [ ] Fix DB timeout for user@acme.com on prod-db` | `- [ ] [perf] Optimize connection pool under concurrent read queries` |
| "Start work on Project StealthX quantum compiler feature for Q4 launch" | `- [ ] Implement StealthX quantum engine for Q4 launch` | `- [ ] [engine] Refactor AST parser pipeline for multi-pass optimization` |

---

## 3. The 3-Tier Resolution Strategy

1. **Tier 1: Generalize & Abstract (Recommended for public repos)**
   - Express the engineering goal cleanly without exposing commercial names, keys, or internal secrets.
2. **Tier 2: Divert to Private Local Companion (`TODO.local.md`)**
   - Public `TODO.md` keeps the clean, sanitized entry.
   - Private details, customer notes, or live credentials live in gitignored `TODO.local.md` (default root location) or `_local/TODO.local.md` / `.local/TODO.local.md`.
3. **Tier 3: Git Clean-Filter Redaction**
   - In repos using git clean filters (like `dotagents`), use `<prefix>REDACTED` tags so working tree keeps local data while commits are masked.
