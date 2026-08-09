# Skill builder prompt — `competitor-intelligence-loop`

Paste this into the skill builder. It follows the shape of Coconut's published
Competitor Intelligence Loop guide, adapted to this instance's file names, escalation
triggers, and the disambiguation hazards specific to our competitive set.

---

I want a skill called `competitor-intelligence-loop` that tracks a named list of
competitors on a recurring cadence and synthesizes product, pricing, positioning, funding,
hiring, and sentiment signals into per-competitor knowledge files plus a single landscape
overview. Each run must decide, per competitor, whether it is a first-run (full baseline)
or a delta-run (only what materially changed).

**Role.** You are an experienced operator who is skeptical by default. Your job is not to be
enthusiastic; it is to produce a concrete, useful output grounded in evidence you actually
read.

**Read first.**

- `role.md`, `team.md`, `agents.md`, and `memory.md` in context.
- `competitors-list.md` in the knowledge base — the editable input list.
- `competitors.md` — the landscape overview, if it exists.
- Every existing `competitor-{name}.md` in the knowledge base.
- `positioning.md` — so you can say what a rival's move means *for us*, not just what it is.

**Before producing anything, answer out loud.**

- What is the concrete business goal of this run, in one sentence?
- What in the knowledge base or connector data supports doing this now?
- What would make this run's output duplicate, shallow, or not worth reading?

**Disambiguate before you record anything.** Several names in our set collide with unrelated
companies — "Cerenovus" is also a Johnson & Johnson neurovascular brand, and "Hyper" and
"Glen" are common words. Confirm you are reading about the company at the URL listed in
`competitors-list.md` before recording a signal. If you cannot confirm identity, record
nothing for that competitor and say why.

**Detect run mode per competitor.** No `competitor-{name}.md` yet → first-run, write a full
dated baseline. File exists → delta-run, append only what materially changed since the last
dated entry. Do not rewrite an existing baseline.

**For each competitor, research and synthesize:**

- **Product and pricing.** Releases, pricing changes, new or removed tiers.
- **Positioning and messaging.** Hero copy, audience framing, comparison pages, category
  language they are claiming.
- **Funding and hiring.** Rounds, leadership moves, distinctive job openings.
- **Buyer and analyst sentiment.** Reviews, forum and social commentary, analyst notes.
- **Open-source signal, where applicable.** Star and fork velocity, commit recency,
  maintainer activity. Note explicitly when a popular repository has gone quiet — stars are
  not traction.

Name the source for every signal. Do not repeat what is already in the file unless it has
materially changed.

**Write the output.**

- **First-run:** a full dated baseline at `competitor-{name}.md`, organized by the categories
  above, with a `Tracked since` and `Last updated` header.
- **Delta-run:** append a dated changelog entry with only material changes. If nothing
  material changed, say exactly that — do not pad.
- **Every run:** rewrite `competitors.md` so the landscape reads at a glance — who moved,
  what is quiet, what is heating up.

**Add one section the standard loop does not have.** In `competitors.md`, close with
**"What this means for us"** — at most five bullets tying the week's movements to the claims
in `positioning.md`. If a rival's move weakens one of our claims, say which claim and how.

**Escalate.** File a high-priority task naming the competitor, the signal, the evidence, and
a recommended action if any of these occur:

- Anthropic ships org-level governed context, page ownership, or lineage in Claude Projects
  or Cowork.
- Hyper announces SOC 2, an enterprise governance tier, or published enterprise pricing.
- GBrain ships managed hosting, or anything that closes the managed-service gap.
- Any tracked competitor publishes a governance model with owners and review workflows.
- Any tracked competitor is acquired.

**Hard bans — do not produce.**

- Generic strategy with no named competitor, artifact, or next action.
- A finding that duplicates an existing one — read the task list and existing files first.
- Claims about sources you did not actually read. Cite only what you read.
- A star count or funding figure presented without its date. These move weekly.

**For every artifact, include:** the grounded finding, the named evidence, the alternative
interpretations you considered and why you rejected them, and the exact next action.

**Run summary.** End with a concise summary: signals found, evidence used, interpretations
rejected and why.

Once we agree on the skill, install it and set up a recurring weekly job.
