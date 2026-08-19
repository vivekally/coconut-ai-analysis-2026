# Product — What Coconut Is

**Owner:** Head of Product · **Last verified:** 2026-08-18 · **Source:** coconut.dev,
docs.coconut.md, docs.coconut.dev, trust.coconut.dev

## One sentence

Coconut connects an organization's scattered documents, tools, and undocumented know-how
into one living, governed source that any AI tool draws from through a permission-aware
MCP connector.

## Read this first: we document two products

As of 2026-08-18 two documentation sites are live and they describe different software.

| | `docs.coconut.dev` | `docs.coconut.md` |
|---|---|---|
| Unit | a Coconut = one provisioned VM | `org → space → page` |
| Storage | `.nut/` directory, git-versioned | Postgres |
| Versioning | git branches and worktrees | append-only revisions, **"no git lifecycle"** |
| MCP tools | `coconuts_* tasks_* knowledge_* skills_*` | `context_* agent_*` |
| Retrieval | "indexed and available" | Postgres full-text search + metadata query |
| Deployment | provision an instance | Docker Compose, Helm, Terraform |

**The second one is what ships.** A live MCP connector attached on 2026-08-09 exposed
`context_*` and `agent_*` and nothing else. The marketing nav still links to the first.
Treat any claim sourced only to `docs.coconut.dev` as historical.

## The problem, as we state it

Organizational AI context fails three ways at once: **fragmented** (tools do not share
context), **stale** (it ages the moment things change), **inconsistent** (output varies by
tool, team, and session).

The distinction we draw against enterprise search: search helps people *find* information;
a context layer gives AI the knowledge to *act* on it. As of the new documentation the
mechanism behind that is a **query** engine, not a retrieval engine.

## The object model

- **Org → space → page.** A space groups pages around a purpose, carries its own members and
  visibility (`private` or `org`), and has **exactly one agent**. Every user also has a
  personal space.
- **A page has three content layers.** Markdown **body** (narrative), **frontmatter**
  (travels with the revision), and **metadata** (stored alongside, queryable, patchable
  without creating a revision).
- **Reserved prefixes.** `agents/` holds the agent's instructions, task pages and run
  records; `templates/` holds page templates. Both hidden from listings and search.
- **Three doors, one ACL engine.** Browser at `/pages/:space/:path`, HTTP with
  `Accept: text/markdown`, MCP at `POST /mcp`. Identical authorization outcomes.

## What is genuinely differentiated

- **Metadata as a query surface.** Any JSON value. `set` upserts, `append` extends arrays
  atomically, `appendUnique` makes re-running agents idempotent. Per-key audit trail.
  Operators `eq neq exists missing gt gte lt lte contains`, AND-ed, with `orderBy`.
- **Views.** `/views` is a filter builder over the *same* engine agents use, with the whole
  view state in the URL — a tuned query is a shareable link and a team dashboard.
- **Agents as scoped principals.** Scheduled runs execute as the space agent principal;
  manual runs execute with the requesting user's authority.
- **Automatic link graph.** Backlinks, broken-target flags and a space-wide broken-link
  report, indexed from Markdown bodies on every write.

## Newer capabilities

| Capability | What it is |
|---|---|
| Webhooks | Four page/metadata events, HMAC-SHA256 signed, retries with backoff, delivery log, SSRF guard re-checked after DNS resolution |
| Space templates | A gallery merging built-in, org-maintained and opt-in remote catalogues; "Use this template" provisions a whole space |
| Export / import | Whole spaces as portable JSON bundles (`coco-space-export` v1), the same format space templates are built from |
| Deployment | Docker Compose, Helm chart, Terraform for AWS. Enterprise artifact is `api + postgres` |
| Identity | Google Workspace OIDC first-class, Okta profile, SCIM baseline |
| Native agents | `COCO_NATIVE_AGENTS_MODE=native` plus an "Eve" runtime container, gated by per-org entitlements |

## Vertical blueprints

Five, each a metadata schema plus a saved view plus a connector: private-equity deal
pipeline, B2B SaaS account research, SRE runbooks, legal contract repository, manufacturing
supplier audit. Every one is the same three primitives dressed for a buyer.

## The five layers

Identity / Domain / Process / Relationships / State appear on the platform page and
**nowhere in the shipped object model**. There is no layer field and no layer API. Treat the
taxonomy as sales narrative, not architecture.

**Known inconsistency, still live:** the platform page calls layer 02 "Domain"; the FAQ calls
it "Product". Both live as of 2026-08-18, ten days after first being noticed.

## Deployment and security

AES-256 at rest, TLS 1.2+ in transit, RBAC, MFA, least privilege, audit logging, regular
penetration testing. The security page now describes two models, managed or self-hosted.
Secrets — webhook signing keys, connector credentials, model keys — are encrypted under a
required 32-byte `COCO_SETTINGS_ENCRYPTION_KEY`; without it webhook creation returns `503`
rather than storing plaintext.

**SOC 2 status:** a Vanta Trust Center is live at `trust.coconut.dev` with roughly 57
continuously monitored controls, all passing. The only downloadable artifact is an
**engagement letter** — an audit begun, not a report issued.

## Pricing

Three contact-sales tiers, no public figures: **Team** (first pilot), **Company**
(multi-team), **Enterprise** (org-wide, SSO/SCIM, procurement support).

## Shipped vs promised

- **Shipped:** append-only revisions, `If-Match`/ETag concurrency, metadata with per-key
  audit, full-text search, link graph, space agents with schedules and run records,
  connectors, webhooks, templates, export/import, SCIM.
- **Still missing:** **propose-then-publish review.** Marked "coming soon" on the platform
  page and absent entirely from 27 pages of new documentation — no review endpoint, no
  proposal object, no approval state on a page.
