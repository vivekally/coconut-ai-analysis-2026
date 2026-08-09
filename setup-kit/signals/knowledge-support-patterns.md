# ⚠️ SYNTHETIC TEST DATA — Support Patterns

> **THIS FILE IS FABRICATED. THESE ARE NOT REAL SUPPORT TICKETS.**
>
> Invented to exercise the `product-improvement-loop`. No real Coconut customer filed any
> of these. All names are fictional placeholders. Do not cite outside this test instance.
> Delete when the test is done.

**Owner:** Head of Product · **Type:** SYNTHETIC · **Period:** 2026-06-01 → 2026-08-01

---

## Volume by theme (fabricated counts)

| Theme | Tickets | Trend | Median time to resolve |
|---|---|---|---|
| "Which layer does this belong in?" | 31 | ▲ rising | 2 days (usually ends in opinion, not answer) |
| Two people edited the same page | 14 | ▲ rising | 1 day |
| "Why did this page's score change?" | 12 | flat | 3 days |
| Connector sync appears stale | 11 | ▼ falling | 4 hours |
| "How do I see what changed since Friday?" | 9 | ▲ rising | same day |
| MCP scope confusion during OAuth grant | 8 | flat | 1 hour |
| Stale flags — "can I bulk-dismiss these?" | 7 | ▲ rising | same day |
| Self-hosted install questions | 5 | flat | 2 days |

## The three that keep coming back

### 1. Layer placement (31 tickets, rising)
Almost always the same shape: a runbook, a competitor note, or a pricing decision that
plausibly belongs in two layers. Support answers with a judgment call. Different agents give
different answers. Two customers have independently asked for "a rule, not an opinion."

### 2. Silent concurrent edits (14 tickets, rising)
Two people edit the same page within a working day. Neither is notified. The owner is not
notified. It surfaces later when a number looks wrong. Version history means the data is
recoverable — the complaint is that nobody knew to look.

### 3. Unexplained score movement (12 tickets)
A conviction or fit score changes between runs and the reader cannot see which evidence
moved it. The lineage exists at page level but not at field level, so answering the ticket
requires a human to diff two versions and infer.

## Notable one-offs (fabricated)

- **2026-07-19** — A customer asked whether space agents can run against a read-replica so a
  long research job doesn't touch the live instance. No, currently.
- **2026-07-24** — A customer wanted a weekly digest of what their space agent changed. There
  is no digest; they are reading the activity feed manually.
- **2026-07-31** — A prospect asked for a "what would this look like for us" sandbox before
  signing. Declined, because standing up an instance is a VM.

## What support says internally (fabricated)

> "The layer question is the single biggest time sink and it's not a bug, it's that we ship a
> taxonomy without a decision procedure for it."

> "We could close most of the concurrent-edit tickets tomorrow if the owner just got told
> something happened."
