# Positioning — What We Claim and What Survives a Follow-Up

**Owner:** Head of Product · **Last verified:** 2026-08-08

Every claim below is paired with the follow-up question a sharp buyer asks next. A claim
without a surviving answer is not positioning, it is a slogan.

## Claim 1 — Model-agnostic and portable

*"The same context serves Claude, ChatGPT, Copilot, Gemini, and whatever you adopt next.
Your context travels with you."*

**Follow-up:** "Do you run on Claude yourselves?"
**Honest answer:** Yes. Our agent loop is Claude Code and the AI chat endpoint defaults to
Claude Sonnet 4.5. We are agnostic about which tool *consumes* context, not about what
*runs* our own agent. Say this plainly. Getting caught conflating the two costs more than
the admission does.

## Claim 2 — Governance-first

*"Owners, versions, lineage, tiered review, decay signals. Every answer traceable, every
change accountable."*

**Follow-up:** "Show me the review workflow."
**Honest answer:** Versioning, lineage, rollback, ownership, and RBAC are shipped.
Propose-then-publish review is marked coming soon. Until it ships this claim is partly a
roadmap. Do not demo it as present tense.

## Claim 3 — A context layer, not enterprise search

*"Search helps people find information. A context layer gives AI the knowledge to act on it."*

**Follow-up:** "Glean has agents now. What is the difference?"
**Honest answer:** This is the sharpest line we have and it is under pressure. Glean Agents
is closing the distance, and Glean has the connector library, ACL enforcement, and
procurement relationships. Our differentiation has to be the governance surface and the fact
that we are not a destination app — not the search-versus-act framing alone.

## Claim 4 — Days to value, not quarters

*"No blank screen. Bootstrap from templates and materials you already have."*

**Follow-up:** "How long until my team sees something useful?"
**Honest answer:** This is our strongest claim against Palantir-style ontology projects and
against self-hosting. It has to hold up in a pilot, measured. If a pilot takes six weeks to
first value, this claim is doing damage rather than work.

## Claim 5 — Enterprise-ready

*"AWS, AES-256, TLS 1.2+, RBAC, MFA, audit logging, penetration testing, self-hosted option."*

**Follow-up:** "Do you have SOC 2?"
**Honest answer:** An audit is under way and visible — `trust.coconut.dev` publishes ~57
continuously monitored controls, all passing — but the only downloadable artifact is an
engagement letter, not a report. Competitors with narrower scope advertise completed Type II.
Say the true thing: in flight, instrumented, not yet certified. It is a far better answer than
silence and still the most mechanical gap in the enterprise motion.

**Second follow-up:** "How does retrieval rank?"
**Honest answer:** Postgres full-text search, ACL-filtered, with no embeddings or reranker —
because ranking prose is not where we compete. State questions go to the metadata engine and
are answered exactly. Say that plainly rather than letting the evaluator discover it.

## The one-liner against each threat

| Threat | Our answer | Strength |
|---|---|---|
| ChatGPT / Claude memory | Platform memory is locked to one tool; a context layer is an asset you own | Holds only while buyers run multiple AI vendors |
| Microsoft Copilot | Not locked to the Microsoft estate | Weak against a CIO already paying for E5 |
| GBrain (free) | Managed connectors, permission enforcement, deployment options, someone to call | Real, but prices us against engineering cost, not context value |
| Glean | We give agents knowledge to act on; they help people find things | Under pressure from Glean Agents |
| Hyper and the YC cohort | Shipped 1.0, full API, deployment models, an enterprise reference | A lead measured in months, not a moat |

## Segments, in order of fit

1. **Investors (VC/PE)** — the sharpest fit. One page per target, body is the living memo,
   metadata carries stage, conviction, sources, review dates. The Monday partner list becomes
   a query. This is the segment where our metadata design is obviously better than a wiki.
2. **Leadership** — board prep, synthesis, in-the-moment questions.
3. **Operating functions** — marketing, sales, CS, product, ops, people.
4. **Compliance-shaped work** — legal, supplier audit, SRE runbooks. New, and structurally
   the best fit after investors: every one is a date field, a score, and a sweep for what has
   gone stale, which is exactly what metadata queries answer and retrieval never could.
5. **Developers** — no longer a segment. The CLI, IDE extension and git surface are gone from
   the shipped product; what remains is an HTTP API for systems, not a developer product.
