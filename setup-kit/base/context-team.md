# Team

Roles rather than names. Coconut AI Inc. does not publicly name its leadership, so this
document describes the seats that own work in this instance, not real individuals. Replace
with real names and handles when you run this for a real org.

## Seats

| Seat | Owns | Consulted on |
|---|---|---|
| Head of Product | Roadmap, positioning, this instance's Domain and State layers | Everything |
| Founding Engineer — Platform | Postgres schema and migrations, revisions, the metadata query engine, deployment paths (Compose/Helm/Terraform) | Scope estimates, unit economics |
| Founding Engineer — Integrations | Connectors, MCP server, OAuth scopes, webhooks, SCIM | Anything touching a source system |
| Design | App, views, templates gallery, onboarding | Time-to-first-value proposals |
| GTM / Founder-led sales | Demos, pilots, pricing conversations | Buyer objections, procurement blockers |

## Ownership convention

Every page in this instance has exactly one owning seat. A page with no owner is treated as
decayed regardless of how recently it was edited — unowned context is how a context layer
rots, and we should feel that pain ourselves before customers do.

## Escalation

- **Routine update** — the owning seat publishes directly.
- **High-impact change** (pricing, positioning, security posture, anything customer-facing)
  — do not edit the page directly. Propose the change on its own page and notify the owning
  seat. **Note the gap:** the product has no propose-then-publish review, so this convention
  is enforced socially, not by software. We are feeling the thing our customers will feel.
- **Strategic signal** (a competitor's real shift, not a routine release) — file a
  high-priority task naming the signal, the evidence, and the recommended action.

## Working cadence

- Competitor intelligence: weekly.
- Product improvement: weekly, aligned to the shipping rhythm.
- Anything the loops file as a task is triaged by the Head of Product before the next run,
  so the next run has a cleaner signal to work from.
