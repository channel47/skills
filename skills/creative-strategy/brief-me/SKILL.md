---
name: brief-me
description: A strategist's discovery interview for creative and marketing work — question the user about their brand, offer, and audience, then write verified context to brand/context.md for other skills to use. Use when starting creative strategy for a brand or product, when marketing output keeps coming back generic, or when the user says "brief me", "discovery session", or "build my brand context".
---

# Brief Me

Interview me about this brand until the brief would survive a skeptical creative director. Work through the territories in whatever order my answers open up: the offer and its economics (what's actually sold, price, AOV, margin room), the audience and their awareness stage, the problem and the mechanism that solves it, the proof inventory (reviews, stats, guarantees — what actually exists, not what we wish existed), competitors and the honest reason to pick us, voice, and constraints (budget, compliance, platform). For strategic framing questions, offer a recommendation to react to. For factual details such as price, margins, proof, or performance, label any suggestion as a hypothesis and require a user confirmation or source before recording it as fact.

Ask one question at a time and wait for the answer. Push back on vague answers: "busy moms" is not an audience — busy moms who have already tried what? "High quality" is not a mechanism. A claim with no proof behind it gets flagged as unsupported, not written down as fact.

If a question can be answered by looking — the live site, dossiers in `creative/`, past ads, review pages — look instead of asking.

Write the result to `brand/context.md`, organized by the territories above, with every unresolved item marked `⚠️ open`. Use one project directory per brand so this path stays canonical. This file is the shared context layer for `creative-strategist` and `ad-recon`; update it when an interview or research stage settles an open item. Close the session by listing the `⚠️ open` items — that is the agenda for next time.
