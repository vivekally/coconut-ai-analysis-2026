# Diagram sources

Mermaid source for diagrams rendered on the site. The published pages carry hand-authored
inline SVG instead of rendering these at runtime, because Mermaid needs a ~2.5MB library and
the pages are built to make **zero external requests**. These files are kept so the source of
truth stays editable and portable.

| File | Rendered on | Status |
|---|---|---|
| `daily-usage-sequence.mmd` | `index.html` → Workflows tab | Current — relabelled 18 Aug 2026 |
| `daily-usage-sequence-pm.mmd` | merged into the above | Kept for reference |
| `architecture-functional.mmd` | — | **Retired 18 Aug 2026** |

## Retired: `architecture-functional.mmd`

Reproduced from the June 2026 Notion brief, this described the product documented at
`docs.coconut.dev`: five context layers over a per-org VM. The documentation published at
[docs.coconut.md](https://docs.coconut.md/) describes different software — `org → space →
page` over Postgres, append-only revisions, *"no git lifecycle"* — and a live MCP connector
read on 9 August 2026 matched that model, not this one.

The diagram is kept as a record of what was published, not as a description of the product.
Its slot on the Architecture tab is now taken by two current hand-authored SVGs:

- **Two products, two documentation sites** — the row-by-row comparison of both architectures
- **Coco system architecture** — `org → space → page`, the three doors, one ACL engine,
  Postgres, the space agent, and what is pushed outward

Neither has Mermaid source; sequence and comparison layouts render acceptably in Mermaid, but
these two are box-and-label diagrams where hand-authored SVG is both smaller and cleaner.

## Corrections applied when rendering `daily-usage-sequence.mmd`

The structure is the June 2026 brief's; the labels were replaced on 18 August 2026:

- **The connector resolves pages and metadata queries** rather than assembling five context
  layers. The five-layer taxonomy appears nowhere in the shipped object model.
- **The correction path has no review step.** The original diagram showed a user opening a
  Task — a change proposal an owner reviewed before it propagated. No proposal object exists:
  a correction is a `PUT` with an `If-Match` header, and if the ETag is current it lands.
