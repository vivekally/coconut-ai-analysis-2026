# Product — What Coconut Is

**Owner:** Head of Product · **Last verified:** 2026-08-08 · **Source:** coconut.dev,
docs.coconut.dev

## One sentence

Coconut connects an organization's scattered documents, tools, and undocumented know-how
into one living, governed source that any AI tool draws from through a permission-aware
MCP connector.

## The problem, as we state it

Organizational AI context fails three ways at once:

- **Fragmented** — AI tools do not share context, so every session starts from zero.
- **Stale** — context goes out of date the moment things change.
- **Inconsistent** — without a shared source, output varies by tool, team, and session.

The distinction we draw against enterprise search: search helps people *find* information;
a context layer gives AI the knowledge to *act* on it.

## The five layers

| # | Layer | Holds | Investor-firm example |
|---|---|---|---|
| 01 | Identity | Who you are, what you are trying to do — mission, goals, OKRs | Fund thesis, mandate, criteria |
| 02 | Domain | What you work on and the language around it | Focus areas, markets, portfolio, live deals |
| 03 | Process | How work gets done — templates, frameworks, checklists | Sourcing, diligence, the IC process |
| 04 | Relationships | Stakeholder maps, who owns what, landmines | Founders, co-investors, LPs |
| 05 | State | Current initiatives, recent decisions, open questions, metrics | Same |

**Known inconsistency:** the platform page calls layer 02 "Domain"; the FAQ still calls it
"Product". Both live as of 2026-08-08.

## What is genuinely differentiated

- **Page metadata as a query surface.** Typed key-value data alongside every page — scores,
  stages, dates, owners, sources — queryable across a space. "Every deal in diligence with
  conviction above 0.7, ranked" is one query, not a re-keyed spreadsheet. Prose carries
  judgment; metadata carries facts that churn.
- **Lineage, not overwrite.** A changed decision supersedes rather than overwrites. Every
  page versioned, any two versions diffable, rollback in one step.
- **Space agents as principals.** Each space has an agent with standing instructions running
  on a schedule — folding transcripts into memos, appending sources, flagging stale coverage.
  Read-only outside explicit grants, every run recorded.

## Surfaces

Coconut Studio, Control Plane, VS Code / Cursor extension, `nut` CLI, iOS app, REST
`/api/v1`, WebSocket, MCP server at `app.coconut.dev/mcp` (26 tools, OAuth-scoped), and an
A2A agent card.

## Architecture note

Each "Coconut" is an instance — per the skills documentation, a VM with the `nut` CLI
installed and a `.nut/` directory for state, where an agent loop reads `SKILL.md` and
executes `nut` subcommands. The `.nut` directory is git-versioned and holds `context/`,
`knowledge/`, `skills/`, `jobs/`, `tasks/`, `mcp/`, `resources/`, `chats/`, `config.json`.

## Deployment and security

AWS. AES-256 at rest, TLS 1.2+ in transit, RBAC, MFA, least privilege, audit logging,
regular penetration testing. Three models: multi-tenant SaaS, single-tenant hosted,
self-hosted. Assurance artifacts under NDA.

**Gap:** no SOC 2 claim appears on the public site.

## Pricing

Three contact-sales tiers, no public figures: **Team** (first pilot), **Company**
(multi-team), **Enterprise** (org-wide, SSO/SCIM, procurement support).

## Shipped vs promised

- **Shipped:** 1.0 (2026-06-03), versioning, lineage, rollback, ownership, RBAC, MCP with
  OAuth scopes, connectors, space agents, skills, jobs.
- **Marked "coming soon":** propose-then-publish review — the tiered-propagation workflow
  where low-risk updates flow automatically and high-impact changes require confirmation.
