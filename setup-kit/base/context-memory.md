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

### Ongoing — Model-agnostic distribution, and a selectable runtime
Our context serves Claude, ChatGPT, Copilot, and Gemini. Our own runtime is selectable rather
than fixed. Keep the two claims separate in external messaging and overstate neither; a
technical evaluator will check both.

### 2026-08-18 — A second documentation site went live, describing different software
`docs.coconut.md` documents Coco: `org → space → page` over Postgres, append-only revisions,
**"no git lifecycle"**, `context_*`/`agent_*` MCP tools, Postgres full-text search, and
Compose/Helm/Terraform deployment. `docs.coconut.dev` is still live, still describes VM
instances and a git-versioned `.nut` directory, and is still what the marketing nav links to.
A live MCP connector attached on 2026-08-09 matched the *new* model and nothing in the old
one. **Treat `docs.coconut.md` as current and `docs.coconut.dev` as historical.** What happens
to anything running on the older architecture is not documented anywhere.

## Known open questions

- **Propose-then-publish review still has not shipped.** Marked "coming soon" on the platform
  page, and absent from all 27 pages of the new documentation — no review endpoint, no proposal
  object, no approval state on a page. Until it ships the governance wedge is partly a promise.
- **SOC 2 is in flight, not landed.** `trust.coconut.dev` is live with ~57 continuously
  monitored controls, all passing, but the only downloadable artifact is an engagement letter.
  Dust and Mem0 advertise completed Type II.
- **Layer 02 is named "Domain" on the platform page and "Product" in the FAQ.** Still true ten
  days after first being noticed — and the taxonomy itself appears nowhere in the shipped
  object model.
- **Retrieval is now documented, and it is Postgres full-text search.** No embeddings, no
  vector store, no reranker. That is a defensible bet — that enterprise questions are state
  questions the metadata engine answers exactly — but nobody has written the defence down, so
  evaluators score it as a missing feature.
- **We publish two contradictory documentation sites** and point customers at the older one.
  For a company selling one consistent governed source of truth, this is the thesis failing in
  public on its own website.

## Naming hazard

"Coconut" collides with Coconut Software (banking), Coconut tax software, coconut.co (video
encoding), and a Meta research paper. We now run six hostnames across two TLDs — coconut.dev,
docs.coconut.dev, app.coconut.dev, trust.coconut.dev, docs.coconut.md, app.coconut.md — where
the **top-level domain, not the subdomain**, tells you which product you are reading about.
Any research task about "Coconut" must disambiguate the company *and* the TLD first, or it
will return the wrong company or the wrong architecture.

## Provenance

All of the above traces to coconut.dev, docs.coconut.dev, docs.coconut.md,
trust.coconut.dev, the GitHub API, or published reporting, read 2026-08-08 and re-verified
2026-08-18. Nothing here comes from private beta access.
