# ⚠️ SYNTHETIC TEST DATA — Customer Feedback

> **THIS FILE IS FABRICATED. IT IS NOT REAL CUSTOMER FEEDBACK.**
>
> Every quote, person, and company name below is invented to exercise the
> `product-improvement-loop`, which by design refuses to run without a concrete signal.
> **No real Coconut customer said any of this.** All names are fictional placeholders.
>
> Do not cite this file outside this test instance. Do not quote it to anyone. Do not
> treat any name here as a real person or company. Delete it when the test is done.
>
> The *frictions* described are extrapolated from publicly observable gaps
> (SOC 2 an engagement letter rather than a report, review workflow still unshipped,
> retrieval that is plain Postgres full-text search, two contradictory documentation sites,
> a heavily collided brand name). The *evidence* is not
> real — it is a plausible dramatization written to give the loop something to bite on.

**Owner:** Head of Product · **Type:** SYNTHETIC · **Created:** 2026-08-08

---

## Pilot: Northwind Capital (fictional, mid-size VC, 22 seats)

**2026-07-14 — Partner, sourcing**
> "The Monday list is genuinely the thing. I stopped rebuilding the sheet. But I don't
> trust a conviction score I can't see the reasoning for. When it says 0.72 I want to know
> which three sentences in the memo moved it, and right now I have to open the page and read
> the whole thing to reconstruct it."

**2026-07-22 — Analyst**
> "Two of us updated the same portfolio page in the same afternoon and I only found out
> because the numbers looked wrong on Thursday. Nobody was told. There's an owner on the
> page but the owner doesn't get asked anything — being the owner doesn't seem to *do*
> anything yet."

**2026-07-29 — Partner, sourcing**
> "Half our diligence context is in the data room, not in Drive or Slack. Right now
> somebody exports and re-uploads. That's the step where things go stale."

## Pilot: Kestrel Logistics (fictional, ops team, 40 seats)

**2026-06-30 — Director of Operations**
> "Setup took our team about three weeks, not the days we were promised, and almost all of
> it was arguing about which space a thing belonged in, and whether a fact was frontmatter or
> metadata. Is a runbook Process or
> Domain? We had the same argument four times. In the end one person just decided and nobody
> else agrees with the result."

**2026-07-18 — Ops lead**
> "The stale flags work. Nobody looks at them. There's no moment in anybody's week where
> looking at decay flags is the thing you're doing, so they just accumulate and now the
> number is big enough that it's easier to ignore."

## Evaluation: Ardent Health Partners (fictional, did not convert)

**2026-07-08 — Security review**
> "We can't take this past the security questionnaire without SOC 2. Self-hosted helps but
> our reviewers still want a report to point at. This isn't a judgment about your
> engineering, it's that the form has a field and we can't leave it empty."

**2026-07-11 — Platform architect**
> "I asked how retrieval ranks and got 'Postgres full-text search.' No reranker, no
> embeddings, and no explanation of why not. I evaluated
> another vendor the same week who walked me through their reranker. I'm not saying yours is
> worse — I'm saying I can't tell, and I have to write a recommendation."

## Inbound, unqualified

**2026-07-25 — via demo request form**
> "Is this the appointment scheduling one? I think I have the wrong Coconut."

**2026-08-01 — prospect, first call**
> "My CTO's first question was whether we could just run GBrain. I didn't have a good
> answer beyond 'someone maintains this one.'"

---

## Cross-cutting patterns (synthesized, still synthetic)

1. **Ownership is nominal.** Owners are assigned but the owner role currently carries no
   obligation and no notification. Two pilots hit the same silent-conflict problem.
2. **Decay flags have no moment.** Freshness detection works; there is no ritual that
   consumes it, so the backlog grows until it is ignored.
3. **Structure is the onboarding tax.** Space boundaries and the frontmatter/metadata split
   are what teams argue about, and
   the argument is unresolved rather than settled.
4. **Two mechanical enterprise blockers:** no SOC 2 *report* (an engagement letter is not one),
   and retrieval that is never defended.
5. **Score opacity.** Metadata scores are trusted less than they should be because the
   evidence behind a number is not visible at the point the number is read.
