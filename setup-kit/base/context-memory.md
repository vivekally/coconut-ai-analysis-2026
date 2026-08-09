# Memory

Long-lived notes that should survive across sessions. Everything here is drawn from
public sources as of 8 August 2026 and carries its provenance. Add dated entries over
time; do not silently rewrite history — supersede it.

## Standing facts

- **Entity.** Coconut AI Inc., footer copyright 2026. Public GitHub organization
  `lovelybunch`, created 2025-08-28 — the company is roughly twelve months old.
- **Access.** Invite-only and demo-gated. The docs front page states this plainly.
- **Version.** Coconut 1.0 tagged 2026-06-03 in the public `coconut-releases` repository.
- **Team size.** LinkedIn reports 2–10 employees. Unverified beyond that, and self-reported
  LinkedIn ranges are unreliable.
- **Public customer reference.** One: Ari Franklin, Group PM at Kohl's. No case studies, no
  scale metrics.
- **Funding.** No publicly disclosed rounds. Crunchbase and PitchBook return same-name
  companies, not this entity.

## Decisions and their reasoning

### 2026-06-03 — Shipped 1.0
Single release tag in the public releases repository. Everything before this was private beta.

### Ongoing — Governance chosen as the wedge
We compete against free open source below us and platform-native memory above us. Neither
can credibly offer owners, lineage, tiered review, and decay signals. That is the position
we defend. It follows that anything which weakens the governance story costs us more than
it costs a competitor.

### Ongoing — Model-agnostic distribution, not model-agnostic runtime
Our context serves Claude, ChatGPT, Copilot, and Gemini. Our own agent loop is Claude Code
and the AI chat endpoint defaults to Claude Sonnet 4.5. Both statements are true. Keep them
separate in external messaging; conflating them is a credibility risk if a technical
evaluator notices.

## Known open questions

- **Propose-then-publish review is marked "coming soon"** on the platform page while the FAQ
  describes tiered propagation in the present tense. Until it ships, the governance wedge is
  partly a promise.
- **No SOC 2 claim appears anywhere on the public site.** Competitors with narrower scope
  (Dust, Mem0) advertise SOC 2 Type II.
- **Layer 02 is named "Domain" on the platform page and "Product" in the FAQ.** Two names for
  one layer, live simultaneously, on the site of a company selling consistency.
- **Unit economics of a VM per instance** are unexamined here. Per-tenant cost scales with
  tenants rather than usage, which is an awkward shape for seat pricing and makes a free
  tier expensive.
- **Retrieval method is undocumented.** We say knowledge is "indexed and available for
  retrieval" and stop. At least one direct competitor publishes its full retrieval
  architecture.

## Naming hazard

"Coconut" collides with Coconut Software (banking), Coconut tax software, coconut.co (video
encoding), and a Meta research paper. We are at coconut.dev, Studio at app.coconut.md,
Control Plane at app.coconut.dev. Any research task about "Coconut" must disambiguate first
or it will return the wrong company.

## Provenance

All of the above traces to coconut.dev, docs.coconut.dev, the GitHub API, or published
reporting, read 2026-08-08. Nothing here comes from private beta access.
