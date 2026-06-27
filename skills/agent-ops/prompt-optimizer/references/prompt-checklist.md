# Prompt Optimization Checklist

Quick validation checklist for optimized prompts. Run through each section before finalizing.

---

## Clarity (Is it Unambiguous?)

- [ ] **Single interpretation** - Could this instruction be misread? Test by imagining someone unfamiliar with the context reading it.
- [ ] **No vague qualifiers** - Replace "good", "appropriate", "relevant", "some", "various" with specific criteria.
- [ ] **Defined terminology** - Technical terms either defined or contextually clear.
- [ ] **Action verbs** - Instructions use clear action verbs (analyze, list, extract, compare) not passive voice.
- [ ] **Quantified where possible** - "several" → "3-5", "brief" → "2-3 sentences", "short" → "under 100 words"

**Quick Test:** Read the prompt aloud. Any hesitation points are likely ambiguous.

---

## Completeness (Is Anything Missing?)

- [ ] **Goal stated explicitly** - The first sentence explains what to accomplish.
- [ ] **All inputs provided** - Data or context the model needs is included or clearly referenced.
- [ ] **Output format specified** - Exact structure (JSON, markdown, bullets, prose) defined.
- [ ] **Length/scope bounded** - Word counts, item limits, or scope constraints included.
- [ ] **Success criteria clear** - What makes a "good" response is defined or demonstrable.

**Quick Test:** Could someone complete this task without asking clarifying questions?

---

## Structure (Is it Well-Organized?)

- [ ] **XML tags used** - Sections delineated with semantic tags (`<input>`, `<instructions>`, `<output_format>`).
- [ ] **Long content first** - Documents, data, or transcripts placed before instructions.
- [ ] **Logical flow** - Context → Instructions → Format → Examples → Edge Cases
- [ ] **Grouped related items** - Similar instructions or constraints together, not scattered.
- [ ] **Numbered steps** - Multi-step processes use numbered lists.

**Quick Test:** Can you quickly locate any specific instruction by scanning?

---

## Examples (Are There Demonstrations?)

- [ ] **Examples included** - At least 1-2 input/output pairs for non-trivial tasks.
- [ ] **Diversity covered** - Examples show different scenarios, not just the "happy path".
- [ ] **Edge case shown** - At least one example demonstrates unusual/tricky input handling.
- [ ] **Format demonstrated** - Examples match the exact output format specified.
- [ ] **Realistic content** - Examples use plausible data, not obvious placeholders like "foo/bar".

**Quick Test:** Would someone understand the task just from the examples alone?

---

## Constraints (Are Boundaries Set?)

- [ ] **Scope defined** - What IS and IS NOT in scope clearly stated.
- [ ] **Negative instructions** - "Do NOT" list for common failure modes.
- [ ] **Length limits** - Max words/characters for output sections if relevant.
- [ ] **Format requirements** - Required fields, forbidden patterns, naming conventions.
- [ ] **Behavior boundaries** - What to do when uncertain, when to refuse, when to ask for clarification.

**Quick Test:** Can you identify at least 3 things the model should NOT do?

---

## Edge Cases (Are Special Cases Handled?)

- [ ] **Empty/missing input** - Behavior defined for null, empty, or missing data.
- [ ] **Ambiguous input** - Instructions for when input is unclear or multi-interpretable.
- [ ] **Out-of-scope requests** - How to handle requests beyond the prompt's purpose.
- [ ] **Error conditions** - What to return when task cannot be completed.
- [ ] **Status flags** - Classification system for different output types (SUCCESS, ERROR, INSUFFICIENT_DATA).

**Quick Test:** What happens if you feed this prompt garbage? Is that handled?

---

## Production Readiness (For Critical Use Cases)

- [ ] **Chain of thought** - `<thinking>` tags for complex reasoning tasks.
- [ ] **Separable output** - Final answer easily extractable (regex-friendly tags).
- [ ] **Guardrails** - Safety constraints for customer-facing or sensitive applications.
- [ ] **Consistent refusal** - Single, exact phrase for out-of-scope or inappropriate requests.
- [ ] **No meta-commentary** - No references to "context", "training", or "as an AI".
- [ ] **Tested at scale** - Validated on diverse inputs, not just a few examples.

---

## Common Issues Quick-Fix Reference

| Issue | Red Flag | Fix |
|-------|----------|-----|
| Vague output | "Give me a summary" | Specify format: "3 bullet points, max 50 words each" |
| No examples | Complex format, no demos | Add 2-3 input/output pairs in `<examples>` |
| Missing context | References undefined terms | Add `<context>` section with background |
| Unbounded scope | "Help with anything" | Add explicit scope limits and out-of-scope handling |
| Format ambiguity | "Return the results" | Specify: JSON, markdown, plain text with structure |
| No error handling | Only handles success | Add `<edge_cases>` with error conditions |
| Over-verbose prompts | Repetitive instructions | Consolidate, use structured sections |
| Buried constraints | Limits hidden in paragraphs | Extract to dedicated `<constraints>` section |

---

## Scoring (Optional Self-Assessment)

Rate the prompt on each dimension (1-5):

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Clarity | /5 | 1.5x | |
| Completeness | /5 | 1.5x | |
| Structure | /5 | 1.0x | |
| Examples | /5 | 1.0x | |
| Constraints | /5 | 1.0x | |
| Edge Cases | /5 | 1.0x | |
| **Total** | | | **/40** |

- **35-40**: Production-ready
- **28-34**: Good, minor improvements possible
- **20-27**: Needs work, likely inconsistent results
- **<20**: Major revision required

---

## Final Verification

Before delivering an optimized prompt, confirm:

1. [ ] Read the prompt from the user's perspective - does it make sense?
2. [ ] Mentally simulate 3 different inputs - would outputs be consistent?
3. [ ] Identify the weakest part - is it acceptable or needs one more pass?
4. [ ] Format is copy-paste ready - no placeholders marked as `[TODO]`?
