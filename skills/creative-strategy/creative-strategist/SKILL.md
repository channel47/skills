---
name: creative-strategist
description: Voice-of-customer research turned into personas, ad angles, and advertorials — run as one pipeline or stage by stage. Use when the user wants to research what customers say about a product or category (reviews, Reddit, VOC, pain points, complaints), build buyer personas or customer avatars, generate ad angles or hook ideas, write an advertorial or presell page, or run the full creative strategy pipeline end to end.
---

# Creative Strategist

Four stages, each feeding the next: **Research → Personas → Angles → Advertorial**. Run only the stage the user asked for; earlier stages are prerequisites (offer to run missing ones, or accept equivalent context the user provides). All output lives in one dossier per product — `[product-slug]-dossier.md` — where each stage writes its own `# Stage: ...` section (replace the section on re-run).

**The invariant behind everything:** ads work when they use the audience's own words. Every quote is captured verbatim with a stable ID (Q1, Q2, ...), and every downstream claim — persona trait, angle, headline — cites the IDs it stands on. Never fabricate quotes, testimonials, stats, or reviews; if evidence is thin, label the output speculative and say what's missing.

Check `.claude/creative-strategist.local.md` for product context. If no clear target, ask: product or category, known competitors, open questions. After each stage, brief the user in a few lines (headline findings, biggest gap, suggested next stage) — don't dump the file.

## Quote tagging

`Q12 [🔥2 | solution-aware] "exact words" — source URL`

- Intensity: 🔥1 calm fact · 🔥2 clear emotion · 🔥3 visceral story. 🔥3 is hook material; if over ~30% of quotes land there, recalibrate — real 🔥3 is rare.
- Journey stage: pre-aware · problem-aware · solution-aware · decision · post-purchase. Pre-aware and decision quotes are scarce and valuable — flag them.

## Stage 1 — Research

Goal: 40+ high-signal verbatim quotes from 3+ source types, synthesized into creative raw material. Run the crawl in a subagent (pass it this stage plus `references/sources.md` as instructions) so the noisy fetching stays out of the main context.

Capture only quotes that are specific, emotional, comparative, decision-revealing, or assumption-breaking. Skip generic praise ("great product!"), pure logistics, incentivized reviews, and marketing-speak. Keep both sentiments. Never paraphrase.

Coverage gate: attempt all three P1 families — review sites (Trustpilot etc.), Reddit, Amazon — through the full fallback chain in `references/sources.md`; at least 2 of 3 thorough (8+ quotes each), plus at least one further source type. Log platform / access method / quote count.

Synthesize — analysis, not summary:

- Pain points ranked by frequency × intensity, each with a one-line creative implication
- Language clusters — frustration, hope, skepticism, urgency, relief — 5+ verbatim phrases each
- Objections, each with the evidence type that would overcome it
- Desires: stated vs. deeper ("I want a clean toilet" = "I want to feel like a competent adult"), with the quote that reveals the gap
- Trigger events — what flipped passive annoyance into active searching
- Competitor map: perceived strengths / weaknesses / wish-it-had, in the customers' words
- Surprising findings: 3-5 non-obvious insights. Mandatory — if nothing surprised you, you haven't gone deep enough. Contradictions between sources belong here; don't resolve them.
- Gaps: journey stages or topics with thin coverage

## Stage 2 — Personas

Cluster quotes by behavior, not demographics — demographics describe people, behavior predicts response to ads. Cluster on: journey entry point, prior-solution history (naive first-timer vs. burned veteran — often the sharpest split), and conviction pattern (what evidence converts them: peers, data, authority, risk-reversal). Merge clusters that would respond to the same ad; split where one ad would fail half the group. 2-4 personas; if two share the same hook, proof, and CTA, they're one persona.

Each persona (name encodes the tension — "The Burned Buyer", never "Sarah, 34"):

- Snapshot: entry point, solution history, demographic signals only where quotes support them
- First-person monologue tracing the decision arc — trigger → search → compare → hesitate → what would tip them — assembled from cited quotes
- Top pains by intensity, stated vs. deeper desire, objections + what overcomes each, what they've already tried and why each failed (cite IDs throughout)
- Language fingerprint: their verbatim phrases, grouped by emotional register
- Creative brief: **Lead with / Prove with / Avoid / CTA style / Best platform / Hook archetype** — one line each, concrete enough that a copywriter starts writing immediately

And one **anti-persona**: who will never convert for structural reasons (opposed philosophy, wrong category, perpetual researcher), how to recognize them in targeting, evidence quote. This is where ad spend goes to die.

## Stage 3 — Angles

Categories: pain-agitation · failed-solution ("nothing worked... until") · trigger-event (open at the moment they started searching) · identity (who they want to stop or start being) · social proof · discovery/novel mechanism · comparison · specificity (concrete number or timeframe). Skip any the data doesn't support. The strongest ads pair two: failed-solution + discovery, trigger + pain, identity + social proof, comparison + specificity.

Gates per angle: (1) **Evidence** — anchored on a 🔥3 quote plus 2+ supporting, cited by ID; (2) **Persona fit** — matches one persona's creative brief; (3) **Differentiation** — not what competitors visibly run, ideally built on a surprising finding. All three → Tier 1. Missing only 3 → Tier 2. Missing 1 or 2 → speculative or cut.

Produce 5-8 angles. Per angle: category + tier + persona + journey stage, anchor quote IDs, 3-5 hooks that are actual ad copy in cluster language (write the ad, not a description of the ad — each hook different enough to test independently), one short-form and one long-form treatment, and failure modes (where it tips into shame, fear-mongering, or clickbait; whether it attracts the anti-persona).

Close with 2-3 **angles to avoid** — obvious plays the research contradicts — and a test plan: first 3 angles × platform × budget split, with success signals and kill signals.

## Stage 4 — Advertorial

Turn the chosen angle (default: top Tier 1) into a build-ready presell page. The page earns the sale before the offer appears, moving the reader: recognition → stakes → mechanism → proof → objections answered → bridge to product. Pick the lightest archetype that fits: problem-solution, honest review, listicle, comparison, myth-busting, founder story.

Write the full copy in the persona's language fingerprint: subheads that carry the story for skimmers, short mobile paragraphs, strongest proof in the first third, biggest objection answered before the final CTA, CTA as a natural next step rather than a hard pitch.

End with a **proof ledger** — every claim rated proven / needs-source / demo-only / remove, with a publish-safe wording for each. Use placeholders like `[needs testimonial]` rather than inventing proof; in regulated categories (health, finance, kids) downgrade claims to observable facts. Add brief build notes: images needed, CTA destination, ad-to-page message match.
