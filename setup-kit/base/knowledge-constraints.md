# Constraints — What Any Proposal Must Respect

**Owner:** Head of Product · **Last verified:** 2026-08-08

The `product-improvement-loop` reads this file. Any proposal that violates a hard
constraint should be killed at the gate rather than reframed.

## Hard constraints

| Constraint | Implication for proposals |
|---|---|
| **Team of 2–10** | Anything beyond 1–2 weeks for a single engineer must be reframed smaller or killed. No proposal may assume a dedicated team. |
| **Invite-only, demo-gated** | Proposals assuming self-serve signup, public trials, or PLG loops are out of scope until access changes. |
| **A VM per instance** | Per-tenant cost scales with tenants, not usage. Proposals that multiply instances — free tiers, per-team sandboxes, ephemeral demo environments — carry a cost the proposal must acknowledge. |
| **A free credible OSS baseline exists** | Any proposal whose value a competent engineer could self-host in a weekend needs an explicit "why pay" answer inside the proposal. |
| **Governance is the wedge** | Anything that weakens ownership, lineage, versioning, or auditability costs us disproportionately. Convenience features that bypass review are net negative. |

## Surface area already committed

Studio, Control Plane, iOS app, VS Code / Cursor extension, `nut` CLI, REST API, MCP
server, A2A endpoint, connectors for ten-plus systems, agent runtime, skills marketplace,
mail system, image/audio/video generation, interactive terminal, full git operations
including worktrees.

Every one of these needs maintenance, security review, and documentation. **A proposal that
adds a new surface must argue why it beats deepening an existing one.** Breadth is the
expensive way to lose a category race.

## Where we are structurally weak

- **Retrieval is undocumented.** We say knowledge is "indexed and available for retrieval"
  and stop there. At least one direct competitor publishes query expansion, reciprocal rank
  fusion over embeddings and full-text search, and a named reranker. Technical evaluators
  notice which vendor shows its work.
- **No SOC 2 claim.** Mechanical blocker in enterprise security review.
- **Review workflow unshipped.** The load-bearing beam of the governance pitch.
- **Vocabulary inconsistency on our own site.** Layer 02 is "Domain" on the platform page
  and "Product" in the FAQ.
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
