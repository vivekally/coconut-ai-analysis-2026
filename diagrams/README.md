# Diagram sources

Mermaid source for the diagrams rendered on the site. The published pages carry
hand-authored inline SVG instead of rendering these at runtime, because Mermaid needs a
~2.5MB library and the pages are built to make **zero external requests**. These files are
kept so the source of truth is editable and portable.

| File | Rendered on |
|---|---|
| `architecture-functional.mmd` | `index.html` → Architecture tab, second diagram |
| `daily-usage-sequence.mmd` | `index.html` → Workflows tab |
| `daily-usage-sequence-pm.mmd` | merged into the above; kept for reference |

## Corrections applied when rendering

`architecture-functional.mmd` is reproduced from the June 2026 Notion brief. Two claims in
it were corrected on the published SVG rather than carried forward:

- **Context layer 02** is labelled `Product` in the source. The platform page says
  **Domain**; the FAQ still says Product. The rendered diagram shows the conflict.
- **Canonical Store** was an inference in the original brief and is still undocumented. The
  rendered diagram marks it as inferred rather than asserting it.
