# Coconut AI — Independent Product Analysis

An independent analysis of [Coconut AI Inc.](https://www.coconut.dev/) (coconut.dev):
what the product does, how it is actually built, who it competes with, and what could
kill it.

**Revised 18 August 2026.** Ten days after this report first ran, a second documentation
site appeared at [docs.coconut.md](https://docs.coconut.md/) describing a different product
on a different architecture. Both sites are live; the marketing navigation still links to the
older one. The report now treats the newer site as current and retires the claims built on
the older one.

**Seven of the eight tabs are public-sources-only.** The eighth — *First-hand* — comes
from attaching the Coconut MCP connector to a live beta instance and reading the object
model directly. It is quarantined on purpose so the public-sourced material stays
independently checkable.

## Live

| Page | URL | What it is |
|---|---|---|
| Analysis | **https://vivekally.github.io/coconut-ai-analysis-2026/** | Product, architecture, workflows, competitors, existential threat, stack-map fit, method |
| Competitor database | **https://vivekally.github.io/coconut-ai-analysis-2026/competitors.html** | 47 companies, searchable and tier-filterable, each with its relationship to Coconut |
| Dogfood setup guide | **https://vivekally.github.io/coconut-ai-analysis-2026/setup.html** | 10 steps to stand up a Coconut space modelling Coconut, and run both product loops against it |

Deep links: `#threat`, `#stack`, `#method` open a tab on the analysis page;
`competitors.html#c-gbrain`, `#c-glean`, `#c-hyper` open a specific company card (and clear
any active filter that would otherwise hide it); `setup.html#s7` jumps to a numbered step.

## The finding this revision turns on

Two documentation sites were live on 18 August 2026, describing incompatible object models:

| | `docs.coconut.dev` — linked from the marketing nav | `docs.coconut.md` — linked from nowhere |
|---|---|---|
| Unit | a "Coconut" = one provisioned **VM** (CPU/RAM/disk) | `org → space → page` |
| Storage | `.nut/` directory, **git-versioned** | **Postgres**, append-only revisions, *"no git lifecycle"* |
| MCP tools | `coconuts_* tasks_* knowledge_* skills_*` | `context_*`, `agent_*` |
| Retrieval | undocumented | **Postgres FTS** — no embeddings, no reranker, no vector store |
| Deployment | provision an instance | Docker Compose · Helm · Terraform |

**The newer one is what ships.** The MCP connector this report attached on 9–10 August
exposed `context_*` and `agent_*` and nothing else — the surface only `docs.coconut.md`
documents. That inference is the load-bearing judgement of the revision and is stated on the
Method tab rather than buried.

What this cannot determine from public sources: whether the split is a migration mid-flight,
a deliberate two-product strategy, or an abandoned line left standing. No migration guide,
deprecation notice, or changelog exists on either site.

## Scope and sourcing

**Public-sourced (seven tabs).** Product, Architecture, Workflows, Competitors, Existential
Threat, Stack Fit, Method. Everything traces to a public source: coconut.dev,
docs.coconut.dev, docs.coconut.md, trust.coconut.dev, the GitHub API, Y Combinator company
pages, or published reporting. First read **8–9 August 2026**; all 27 pages of the new
documentation read in full and every prior claim re-checked on **18 August 2026**.

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

## What changed on 18 August

**Retired.**

- **"Each Coconut is a VM."** Sourced correctly in August from the skills docs and the
  provisioning dialog — both still live — but contradicted by the shipped product.
- **The five-layer taxonomy** (Identity / Domain / Process / Relationships / State) appears
  nowhere in the new object model. No layer field, no layer API. Marketing narrative, not
  architecture.
- **The "hidden second product."** The `nut` CLI, git worktrees, WebSocket terminals, code
  sessions and media generation are all gone. So is the `SKILL.md` / Claude Code plugin
  marketplace dependency, which narrows the Anthropic threat considerably.
- **L09 · Orchestration** stack-map fit, revised from Direct back down to Weak — the surface
  that justified it no longer exists.

**Newly documented, and absent from the August report entirely.**

- **Webhooks** — four events, HMAC-SHA256 signed, delivery log, SSRF guard re-checked at
  delivery time after DNS resolution
- **Space templates** — a gallery merging built-in, org-maintained and opt-in remote
  catalogues, with a deep-linkable install path that survives sign-in
- **Export / import** — whole spaces as portable `coco-space-export` bundles
- **Views** — a filter builder over the same query engine agents use, with the view state in
  the URL
- **Deployment** — Docker Compose, Helm, Terraform; `api + postgres` as the enterprise artifact
- **Identity** — Google Workspace OIDC, Okta, SCIM
- **Native agents** — `COCO_NATIVE_AGENTS_MODE=native` and an "Eve" runtime container

**Sharpened.**

- **Retrieval is documented now, and it is Postgres full-text search.** The August criticism
  was that Coconut would not show its work. It has, and the answer is simpler than every
  rival's. That is defensible — state questions belong to the metadata engine, not to
  retrieval — but nobody at Coconut has written the defence down.
- **SOC 2 moved.** A Vanta Trust Center is live with ~57 continuously monitored controls, all
  passing. The only downloadable artifact is an **engagement letter**: an audit begun, not a
  report issued.
- **Layer 02 is still "Domain" on the platform page and "Product" in the FAQ**, ten days on.
- **Propose-then-publish review still has not shipped** — and is absent from a freshly
  written 27-page object model that found room for webhooks, templates and SCIM.

**Vindicated.** Four of the five First-hand findings are now confirmed by Coconut's own
documentation, in places word for word: the three content layers, the `set`/`append`/
`appendUnique` metadata semantics with a per-key audit trail and no page revision, the
automatic backlink graph, and agents as scoped principals. One detail changed underneath —
concurrency is documented as `If-Match`/ETag/`412`, not `expectedVersion`. The fifth finding,
**credit exhaustion degrading quality invisibly**, is unaddressed anywhere in the new docs.

Full conflicts log is on the Method tab.

## Diagrams

Four hand-authored inline SVGs across the analysis page:

| Diagram | Tab | Answers |
|---|---|---|
| Two products, two documentation sites | Architecture | Which architecture is which, and who points at each |
| Coco system architecture | Architecture | `org → space → page`, three doors, one ACL engine, Postgres, the agent, what is pushed outward |
| Verified object model | First-hand | What a page actually is — body, frontmatter, metadata, versions |
| Daily usage sequence | Workflows | How the drafting and correction loop runs, and where the review step is not |

Mermaid source for the sequence diagram lives in [`diagrams/`](diagrams/). The pages render
hand-authored SVG rather than Mermaid because Mermaid needs a ~2.5MB runtime and these pages
make **zero external requests**. The imported functional-architecture diagram from the June
2026 brief is retired — it described the older architecture — and its Mermaid source is kept
in `diagrams/` as a record only.

## Setup kit

[`setup-kit/`](setup-kit/) holds the source files for the setup guide: context documents,
knowledge base, and the two agent-task prompts, in two packs. **Rebuilt 18 August 2026**
against `org → space → page`: pages instead of a `.nut` directory, agent task pages instead
of Skills, `schedule` frontmatter instead of jobs, plus metadata, a view and a webhook that
the previous version could not demonstrate at all.

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
- **AI stack L11 · Application Platforms** — secondary.
- **AI stack L05 · Data Infrastructure** — partial, revised up. Explicitly not a vector database, but the metadata layer is a real typed, audited, indexed query surface.
- **AI stack L09 · Orchestration** — **revised down to weak.** The August report rated this Direct on the strength of skills, code sessions, terminals and git worktrees. None of it exists in the shipped product.
- **Robotics stack** — **no fit.** Argued explicitly rather than forced. The nearest honest adjacency is that a robotics fleet-ops team would be a *buyer*, and that the vertical slot is already occupied by Osseus.

## Caveats

- **The central judgement of this revision is an inference.** Nothing published by Coconut says which of the two documented products is current. This report follows `docs.coconut.md` because the connector it read first-hand matches that model and not the other. Strong evidence, not a statement from the company — and if it is wrong, most of the Architecture tab is wrong with it.
- What happens to anything running on the older architecture is entirely unknown.
- An engagement letter on a Trust Center indicates an audit under way. It says nothing about scope, type, or timing, and neither a completed SOC 2 nor its absence can be inferred from it.
- The new documentation describes a repository this report has no access to. Everything about the codebase is inferred from documentation that references it.
- The YC 2026 cohort is very early and moves weekly. Traction figures are point-in-time and self-reported at launch.
- No funding, leadership, or customer data is publicly available for Coconut AI Inc. beyond one named reference.

---

Not affiliated with, commissioned by, or endorsed by Coconut AI Inc.
