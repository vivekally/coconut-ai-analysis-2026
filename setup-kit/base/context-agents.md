# Agents

Agents available in this instance and the rules every one of them follows.

## Standing rules for all agents

1. **Cite or abstain.** Every factual claim names its source — a page in this knowledge
   base, a connector record, or a URL you actually read. Never cite a source you did not read.
2. **Never invent a signal.** Absent evidence, file a documented context gap. A plausible
   guess presented as a finding is the worst possible output from a context layer.
3. **Say what you rejected.** Every artifact lists the alternative interpretations you
   considered and why you discarded them. This is how a reader calibrates trust.
4. **Check for duplicates first.** Read the existing task list and existing knowledge files
   before producing anything. A duplicate finding is worse than no finding.
5. **Supersede, do not overwrite.** When a fact changes, mark the previous version
   superseded and date the change. History is the product.
6. **Stay inside your grant.** A scheduled run executes as the space agent principal —
   writes at home, read-only across org-visible spaces, nothing in other private spaces. A
   manual run carries the authority of whoever started it. If a run needs a write it does not
   have, record the blocked write rather than working around it.
7. **Record what you fetched.** State the number of external sources actually retrieved in
   every artifact. A run that fetched nothing may not assert what a live page says — this is
   the one provenance rule our own product does not yet enforce for us.

## Agents

Both live as task pages under `agents/`, with their cadence in frontmatter
(`schedule`, `scheduleTz`, `scheduleEnabled`) and every execution recorded under
`agents/runs/<task>/<run-id>`.

### `agents/competitor-intelligence-loop`
Tracks the named competitor set in `competitors-list.md`. Writes one
`competitor-<name>` page per competitor and rewrites the `competitors` landscape overview on
every run. Picks first-run (full baseline) or delta-run (dated changelog of material changes
only) automatically per competitor. Sets `last-reviewed` and `appendUnique`s every URL it
read into `sources` so re-runs are idempotent.
**Cadence:** weekly. **Owner:** Head of Product.

### `agents/product-improvement-loop`
Produces exactly one validated product proposal per run, or one honest report of why no
candidate cleared the bar. Four hard gates plus a final confidence score. Writes the proposal
as a page and records the verdict in metadata (`gate-status`, `confidence`, `signal-source`)
so a view can rank runs without opening them.
**Cadence:** weekly. **Owner:** Head of Product.

## Escalation path

Any agent that finds a genuine strategic signal — not a routine release — files a
high-priority task naming the competitor or source, the evidence, and the recommended next
action. Agents do not act on strategic signals themselves.

## Explicitly out of scope for agents

- Editing pricing, positioning, or security pages directly. Propose via task.
- Contacting anyone outside the org.
- Asserting anything about Coconut's funding, headcount, or customers beyond what
  `memory` records as publicly sourced.
- Repeating claims from `docs.coconut.dev` — the five layers, VM instances, the `nut` CLI,
  the skills marketplace — as current product facts.
