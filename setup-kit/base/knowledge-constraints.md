# Constraints — What Any Proposal Must Respect

**Owner:** Head of Product · **Last verified:** 2026-08-18

The `product-improvement-loop` reads this file. Any proposal that violates a hard
constraint should be killed at the gate rather than reframed.

## Hard constraints

| Constraint | Implication for proposals |
|---|---|
| **Team of 2–10** | Anything beyond 1–2 weeks for a single engineer must be reframed smaller or killed. No proposal may assume a dedicated team. |
| **Invite-only, demo-gated** | Sales is gated. The *product* now documents two self-serve paths — the space-template gallery and a local Compose stack — so a proposal may build on those, but may not assume a public signup funnel marketing has not announced. |
| **Two documented products** | We publish two doc sites describing incompatible object models and link the marketing nav to the older one. Any proposal touching documentation, onboarding, or developer surface must say which product it is for. |
| **One agent per space** | Automation is scoped to the space. A proposal needing two differently-scoped automations over the same pages must either split the space or explain why the ACL cost is acceptable. |
| **A free credible OSS baseline exists** | Any proposal whose value a competent engineer could self-host in a weekend needs an explicit "why pay" answer inside the proposal. |
| **Governance is the wedge** | Anything that weakens ownership, lineage, versioning, or auditability costs us disproportionately. Convenience features that bypass review are net negative. |

## Surface area already committed

Browser app, HTTP API, MCP server, connectors for ten-plus systems, space agents with
schedules and run records, webhooks, page and space templates plus the gallery, export/import,
views, full-text search, the link graph, SCIM, and three deployment paths (Compose, Helm,
Terraform).

The newer documentation **removed** a great deal — CLI, terminals, git operations, code
sessions, media generation, the skills marketplace. That was the right call and it must not be
quietly undone. **A proposal that adds a new surface must argue why it beats deepening an
existing one**, and a proposal that revives a removed surface must say so explicitly.

## Where we are structurally weak

- **Retrieval is Postgres full-text search, and the reason is unpublished.** No embeddings,
  no reranker, no vector store. A direct competitor publishes query expansion, reciprocal rank
  fusion over embeddings and full-text, and a named reranker. Our position — that state
  questions belong to the metadata engine, not to retrieval — is defensible and nowhere argued,
  so evaluators score it as a missing feature.
- **SOC 2 is an engagement letter, not a report.** Still a mechanical blocker in enterprise
  security review, even with ~57 monitored controls published.
- **Review workflow unshipped.** The load-bearing beam of the governance pitch, absent from a
  freshly written 27-page object model that found room for webhooks, templates and SCIM.
- **We publish two contradictory documentation sites** and the marketing nav points at the
  stale one. This is our own thesis failing in public.
- **Vocabulary inconsistency on our own site.** Layer 02 is "Domain" on the platform page and
  "Product" in the FAQ — and the taxonomy appears nowhere in the shipped model.
- **Name collision.** Procurement teams and journalists researching "Coconut" find four
  other companies first.
- **One public customer reference.** No case studies, no scale metrics.

## Deliberately out of scope

- Becoming a destination app. We are the layer underneath, not another place to work.
- Competing on connector count with Glean. We lose that race on headcount alone.
- Building our own model or inference stack.
- Vertical-specific data models (CAD, BOM, firmware). That is a different company, and
  someone is already building it.

## What "good" looks like for a proposal here

It names a real user at a real moment of friction, grounds itself in a signal from this
knowledge base, names two existing alternatives and what each gets wrong, scopes to 1–2
weeks for one engineer, states a user-behaviour leading indicator, and includes a harsh
three-point pre-mortem. Anything less does not clear the bar.
