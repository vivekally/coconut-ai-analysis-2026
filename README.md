# Coconut AI — Independent Product Analysis

An independent analysis of [Coconut AI Inc.](https://www.coconut.dev/) (coconut.dev):
what the product does, how it is actually built, who it competes with, and what could
kill it.

**Seven of the eight tabs are public-sources-only.** The eighth — *First-hand* — comes
from attaching the Coconut MCP connector to a live beta instance and reading the object
model directly. It is quarantined on purpose so the public-sourced material stays
independently checkable.

## Live

| Page | URL | What it is |
|---|---|---|
| Analysis | **https://vivekally.github.io/coconut-ai-analysis-2026/** | Product, architecture, workflows, competitors, existential threat, stack-map fit, method |
| Competitor database | **https://vivekally.github.io/coconut-ai-analysis-2026/competitors.html** | 47 companies, searchable and tier-filterable, each with its relationship to Coconut |
| Dogfood setup guide | **https://vivekally.github.io/coconut-ai-analysis-2026/setup.html** | 10 steps to stand up a Coconut instance modelling Coconut, and run both product loops against it |

Deep links: `#threat`, `#stack`, `#method` open a tab on the analysis page;
`competitors.html#c-gbrain`, `#c-glean`, `#c-hyper` open a specific company card (and clear
any active filter that would otherwise hide it); `setup.html#s7` jumps to a numbered step.

## Scope and sourcing

**Public-sourced (seven tabs).** Product, Architecture, Workflows, Competitors,
Existential Threat, Stack Fit, Method. Everything traces to a public source read
**8–9 August 2026**: coconut.dev, docs.coconut.dev, the GitHub API, Y Combinator company
pages, or published reporting.

**First-hand (one tab).** Drawn from the Coconut MCP connector against a live beta
instance, **9–10 August 2026**. Covers the shipped tool surface, the object model, and one
observed product behaviour.

What that tab deliberately excludes: **any page contents, any seeded or customer data,
and anything identifying an organization or user.** No writes were made to the instance.
Structure and behaviour only. Ignore that one tab and the rest of the document stands as
a strictly public-sourced analysis.

Every company in the database carries a verification flag describing how well *this
report* confirmed it, not how good the company is:

- **verified** — confirmed 8 Aug 2026 against a primary source (GitHub API, the company's own site, a YC company page, a funding announcement)
- **reported** — consistent secondary sourcing (Tracxn, Sacra, trade press), no primary confirmation
- **thin** — single-source or inherited from prior research and not re-confirmed. A lead, not a fact.

Current split: 23 verified, 15 reported, 9 thin.

## Findings that corrected prior research

This report re-verified rather than inherited. The material corrections:

- **Context layer 02 is now "Domain," not "Product"** — and Coconut's own FAQ still says Product. The conflict is on their site, not between sources.
- **Pricing tiers are Team / Company / Enterprise**, not Starter / Growth / Enterprise.
- **Each "Coconut" is a VM running Claude Code**, per the skills docs. This reframes the architecture and was absent from every prior diagram.
- **Glean is at $300M ARR** (May 2026), not $200M. Up from ~$100M fifteen months earlier.
- **Dust raised a $40M Series B** in May 2026 led by Abstract and Sequoia — prior research listed it only as "VC-backed."
- **GBrain has 28,015 stars**, not ~23.6K. Mem0 has 62,829, not 41K.
- **Propose-then-publish review is marked "coming soon"** — the load-bearing beam of the governance pitch.
- **No SOC 2 claim appears anywhere on the public site.**
- **The agent runtime is selectable** (Claude / Gemini / Codex), not Claude-only — a correction to this report's own first version, logged in the conflicts table.

From first-hand access:

- **The published API reference describes a tool surface that no longer exists.** The shipped connector exposes `context_*` and `agent_*`; not one documented tool name appears, and there is no `knowledge_*` namespace at all.
- **Three content layers per page** — body, frontmatter, and typed metadata — where metadata patches carry their own audit trail *without* creating a page revision. Better designed than any public page explains.
- **Real optimistic concurrency** (`expectedVersion`), an automatic link graph with backlinks and broken-target flagging, and run records carrying model, token usage, turn count, and an opt-in reasoning transcript.
- **Credit exhaustion degrades quality invisibly.** When agent credits run out, runs fall back to a no-retrieval path whose output is structurally indistinguishable from a researched run. The quality gates interrogate reasoning, not whether evidence was fetched — so a well-argued case from fabricated premises passes all of them.

Full conflicts log is on the Method tab.

## Setup kit

[`setup-kit/`](setup-kit/) holds the source files for the setup guide: context documents,
knowledge base, and the two skill-builder prompts, in two packs.

**Pack A** (`setup-kit/base/`) is public facts only. **Pack B** (`setup-kit/signals/`) is
**fabricated** customer feedback, support tickets, and churn notes — invented so the Product
Improvement Loop has a signal to work with, because by design it refuses to invent one. No
real Coconut customer said any of it and every company named in it is fictional. `build.py`
fails the build if any Pack B file loses its warning header.

The sequencing is the exercise: load Pack A, run the loop, and a correctly-built product
files *"No signal this run — context gap"* rather than guessing. Then load Pack B and run
again for a real proposal.

## Build

`data/competitors.json` is the single source of truth. `build.py` validates it, writes
a CSV export, and injects the JSON inline into `competitors.html` so the published page
makes **zero external requests**.

```bash
python3 build.py
```

Idempotent — safe to run repeatedly. Validation fails the build on a missing required
field, a duplicate or non-kebab-case id, an unknown tier, an invalid confidence or
threat value, a negative or missing funding figure, or a relative URL.

To add or edit a company, edit `data/competitors.json` and re-run the build. Never edit
the injected JSON inside `competitors.html` directly.

The same build renders `setup.html` from `setup-kit/setup.template.html`, inlining every
`__FILE__<path>__` placeholder. Edit the kit files, never the generated page.

## Conventions

Follows the house format used across the AI Intelligence reports:

- Single-file, self-contained, zero external requests. Favicon is an emoji data URI; citation links are the only outbound URLs.
- Charter serif body, monospace for figures and labels.
- Three-way theming: `:root` vars + `prefers-color-scheme` + `data-theme` overrides, persisted under the `coconut-analysis-theme` localStorage key.
- Hash-linked tabs with a `hashchange` listener.
- A published conflicts log where sources disagree.

This repo is **standalone** — it is not part of the numbered AI Intelligence suite and
carries no suite bar. It links out to
[01 · AI Stack](https://vivekally.github.io/ai-stack-report/) and
[05 · Robotics Stack](https://vivekally.github.io/ai-robotics-stack-2026/) where relevant.

## Stack-map positions argued here

- **AI stack L10 · Middleware & APIs** — primary. The `MCP servers / connectors` sub-layer currently has no companies named; Coconut is the cleanest candidate for the first entry.
- **AI stack L09 · Orchestration** — stronger than previously assessed, because of the VM-runs-Claude-Code finding.
- **AI stack L11 · Application Platforms** — secondary.
- **Robotics stack** — **no fit.** Argued explicitly rather than forced. The nearest honest adjacency is that a robotics fleet-ops team would be a *buyer*, and that the vertical slot is already occupied by Osseus.

## Caveats

- The YC 2026 cohort is very early and moves weekly. Traction figures are point-in-time and self-reported at launch.
- The VM-per-instance reading is inferred from documentation language, not confirmed by the company.
- Absence of a SOC 2 claim on a public site is not proof of absence of SOC 2.
- No funding, leadership, or customer data is publicly available for Coconut AI Inc. beyond one named reference.

---

Not affiliated with, commissioned by, or endorsed by Coconut AI Inc.
