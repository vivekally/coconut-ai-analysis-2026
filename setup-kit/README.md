# Setup Kit — source files for the dogfood guide

These are the raw files rendered into [`setup.html`](../setup.html) by `build.py`.
Edit them here, never in the generated page.

**Published guide:** https://vivekally.github.io/coconut-ai-analysis-2026/setup.html

## Layout

```
setup-kit/
├── setup.template.html      the guide, with __FILE__<path>__ placeholders
├── base/                    PACK A — public facts only
│   ├── context-role.md      → nut context update role
│   ├── context-team.md      → nut context update team
│   ├── context-agents.md    → nut context update agents
│   ├── context-memory.md    → nut context update memory
│   ├── knowledge-product.md
│   ├── knowledge-market.md
│   ├── knowledge-positioning.md
│   ├── knowledge-constraints.md
│   └── knowledge-competitors-list.md   input to the competitor loop
├── signals/                 PACK B — FABRICATED. See warning below.
│   ├── knowledge-feedback.md
│   ├── knowledge-support-patterns.md
│   └── knowledge-churn-notes.md
└── skills/                  skill-builder prompts
    ├── competitor-intelligence-loop.md
    └── product-improvement-loop.md
```

## ⚠️ About `signals/`

**Every file in `signals/` is fabricated.** No real Coconut customer said any of it. Every
company named in it — Northwind Capital, Kestrel Logistics, Ardent Health Partners,
Meridian Freight, Talbot & Rowe, Halcyon Systems, Vantage Partners — is fictional.

It exists because the Product Improvement Loop refuses to invent a signal, so without
seeded feedback data it correctly reports a context gap and stops. Pack B gives it
something concrete to work with so the rest of the machine can be exercised.

The *frictions* described are extrapolated from publicly observable gaps (no public SOC 2
claim, review workflow marked coming soon, undocumented retrieval, a VM-per-instance
architecture, a collided brand name). The *evidence* is a dramatization.

**`build.py` fails the build** if any file in `signals/` loses its `SYNTHETIC` marker or its
explicit "not real / fabricated" warning within the first 600 characters. That guard exists
because these files live in a public repo next to a public-sources-only analysis, and the
two must never be confusable.

## Two packs, in order

The sequencing is the point of the exercise:

1. Load **Pack A** only.
2. Run `product-improvement-loop`. It should file **"No signal this run — context gap."**
   That is the correct result — the discipline being enforced.
3. Save that output. Then load **Pack B**.
4. Run it again. Now it should produce a validated proposal.

If step 2 produces a confident proposal with an invented user, that is the most
informative result the exercise can yield, and worth capturing in full.

## Build

```bash
python3 build.py
```

Reads every `__FILE__<path>__` placeholder in `setup.template.html`, inlines the referenced
file HTML-escaped, and writes `setup.html`. Idempotent. Fails loudly on a missing file, an
unresolved placeholder, or a missing synthetic warning.

## Adapting this for a different company

Replace the contents of `base/`, keeping the file names. The two skill prompts reference
`competitors-list.md`, `product.md`, `constraints.md`, and `positioning.md` by name — keep
those or update the prompts to match. Delete `signals/` entirely and use real customer data;
that is the whole point of the loop.
