# Before & After Prompt Examples

Real-world examples of prompt transformations demonstrating optimization techniques.

---

## Example 1: Data Extraction (Medical Records)

### Before (Weak)
```
Summarize this patient record for the doctor.
```

### Problems
- No format specification
- No indication of what's important
- No structure for the summary
- Inconsistent results across records

### After (Optimized)
```
You are a medical records analyst preparing concise summaries for physicians before follow-up appointments.

<patient_record>
{patient_record_content}
</patient_record>

<instructions>
Analyze the patient record and create a structured summary covering:
1. Patient demographics (name, age)
2. Key diagnoses in chronological order
3. Current medications with purposes
4. Recent concerns requiring follow-up
5. Recommended action items for this visit
</instructions>

<output_format>
<summary>
**Patient:** [Name], [Age]

**Key Diagnoses:**
- [Diagnosis] ([Year])
- [Continue as needed]

**Current Medications:**
- [Medication]: [Purpose]

**Recent Concerns:**
- [Concern 1]
- [Concern 2]

**Action Items:**
1. [Priority action]
2. [Secondary action]
</summary>
</output_format>

<example>
<patient_record>
John Smith, DOB 1968. Diagnosed hypertension 2015, managed with lisinopril 10mg.
Depression diagnosed 2018, currently on sertraline 50mg. Last visit noted elevated
A1C at 6.2, discussed lifestyle modifications. Patient reports occasional dizziness.
</patient_record>

<summary>
**Patient:** John Smith, 56

**Key Diagnoses:**
- Hypertension (2015)
- Depression (2018)
- Pre-diabetic indicators (2024)

**Current Medications:**
- Lisinopril 10mg: Blood pressure management
- Sertraline 50mg: Depression

**Recent Concerns:**
- Elevated A1C (6.2) suggesting pre-diabetic state
- Occasional dizziness (may be medication-related)

**Action Items:**
1. Review A1C and discuss diabetes prevention plan
2. Assess dizziness - check BP and medication timing
</summary>
</example>
```

### Techniques Applied
| Technique | How | Impact |
|-----------|-----|--------|
| Role prompting | Medical analyst context | Sets expertise and tone |
| XML structure | Tagged sections | Clear data/instruction separation |
| Output format | Exact markdown template | Consistent, scannable output |
| Example | Full input/output pair | Demonstrates expected detail level |

---

## Example 2: Customer Support Classification

### Before (Weak)
```
Read this customer message and tell me what it's about and how urgent it is.
```

### Problems
- No classification criteria
- "Urgent" is undefined
- Output format unspecified
- No handling for edge cases

### After (Optimized)
```
You are a customer support triage system. Classify incoming messages by category and priority.

<message>
{customer_message}
</message>

<instructions>
Classify this customer message using the criteria below.

Priority Levels:
- URGENT: System outage, security concern, or revenue-blocking issue
- HIGH: Order problem, refund request, or time-sensitive question
- MEDIUM: Product question, feature request, or general complaint
- LOW: Feedback, general inquiry, or non-time-sensitive request

Categories:
- billing: Payment, refund, subscription issues
- technical: Product bugs, errors, how-to questions
- shipping: Order status, delivery problems
- account: Login, settings, profile issues
- feedback: Suggestions, praise, general comments
- other: Doesn't fit above categories
</instructions>

<output_format>
{
  "priority": "URGENT|HIGH|MEDIUM|LOW",
  "category": "billing|technical|shipping|account|feedback|other",
  "summary": "One sentence summary (max 100 chars)",
  "requires_human": true|false,
  "reasoning": "Brief explanation of classification"
}
</output_format>

<examples>
<example>
<message>YOUR SITE IS DOWN I CANT PAY FOR MY ORDER THIS IS RIDICULOUS</message>
<output>
{
  "priority": "URGENT",
  "category": "technical",
  "summary": "Customer unable to complete payment due to website outage",
  "requires_human": true,
  "reasoning": "Site outage blocking revenue; all-caps indicates high frustration"
}
</output>
</example>

<example>
<message>Hi, just wondering if you ship to Canada? Thanks!</message>
<output>
{
  "priority": "LOW",
  "category": "shipping",
  "summary": "International shipping availability inquiry",
  "requires_human": false,
  "reasoning": "Simple factual question, polite tone, not time-sensitive"
}
</output>
</example>

<example>
<message>cancel my subscription immediately or i will dispute the charge with my bank</message>
<output>
{
  "priority": "HIGH",
  "category": "billing",
  "summary": "Subscription cancellation with chargeback threat",
  "requires_human": true,
  "reasoning": "Chargeback threat requires immediate human intervention"
}
</output>
</example>
</examples>

<edge_cases>
- If message is empty or contains only symbols: {"priority": "LOW", "category": "other", "summary": "Unclassifiable input", "requires_human": true, "reasoning": "Message content uninterpretable"}
- If message contains multiple issues: Classify by the HIGHEST priority issue and note others in reasoning
- If language is unclear: Set requires_human to true with reasoning "Language barrier or unclear message"
</edge_cases>
```

### Techniques Applied
| Technique | How | Impact |
|-----------|-----|--------|
| Explicit criteria | Priority and category definitions | Consistent classification |
| JSON output | Exact schema with types | Programmatically parseable |
| Multiple examples | 3 diverse cases (urgent, low, threatening) | Covers classification spectrum |
| Edge cases | Empty, multi-issue, unclear | Handles production realities |
| requires_human flag | Boolean for escalation | Enables workflow automation |

---

## Example 3: Code Review

### Before (Weak)
```
Review this code and tell me what's wrong with it.
```

### Problems
- No review criteria
- No severity levels
- Output structure undefined
- No positive feedback guidance

### After (Optimized)
```
You are a senior software engineer conducting a code review. Focus on correctness, security, performance, and maintainability.

<code language="{language}">
{code_to_review}
</code>

<context>
{optional_context_about_the_code}
</context>

<instructions>
Review the code for issues in these categories (in priority order):
1. **Security**: Vulnerabilities, injection risks, sensitive data exposure
2. **Correctness**: Bugs, logic errors, edge cases not handled
3. **Performance**: Inefficiencies, unnecessary operations, scaling concerns
4. **Maintainability**: Readability, naming, code organization, missing docs

For each issue found:
- Identify the specific location (line/function)
- Explain the problem clearly
- Suggest a fix with code when applicable
- Assign severity: CRITICAL, HIGH, MEDIUM, LOW

Also note 1-2 things done well (if any).
</instructions>

<output_format>
## Code Review Summary

**Overall Assessment:** [APPROVE / REQUEST_CHANGES / NEEDS_DISCUSSION]
**Issue Count:** [X critical, Y high, Z medium, W low]

### Issues

#### [SEVERITY] [Category]: [Brief Title]
**Location:** [file:line or function name]
**Problem:** [Explanation]
**Suggestion:**
```{language}
[Fixed code]
```

[Repeat for each issue]

### Positive Notes
- [Something done well]
- [Another positive aspect, if applicable]

### Summary
[One paragraph overall assessment and priority recommendations]
</output_format>

<review_guidelines>
- Do NOT flag style preferences unless they harm readability
- Do NOT suggest refactors unrelated to the categories above
- If no issues found, say "No significant issues found" with overall APPROVE
- Prioritize security issues above all others
- Include line numbers when referencing specific code
</review_guidelines>
```

### Techniques Applied
| Technique | How | Impact |
|-----------|-----|--------|
| Role + expertise | Senior engineer persona | Sets review depth expectation |
| Prioritized categories | Ordered 1-4 by importance | Focuses on high-impact issues |
| Structured output | Markdown with clear sections | Actionable, readable reviews |
| Severity levels | CRITICAL to LOW | Enables prioritization |
| Negative instructions | What NOT to flag | Prevents pedantic reviews |
| Balanced feedback | Positive notes required | Constructive, not demoralizing |

---

## Example 4: Call Summarization

### Before (Weak)
```
Summarize this call transcript.
```

### Problems
- No structure for summary
- No guidance on what matters
- Inconsistent detail levels
- No handling for incomplete calls

### After (Optimized)
```
You are a customer service analyst summarizing call transcripts for quality assurance.

<transcript>
{call_transcript}
</transcript>

<instructions>
Before generating the summary, analyze the transcript in <thinking> tags:
- What was the customer's main issue?
- How was it resolved (if at all)?
- What follow-up is required?
- Are there any ambiguities or unclear points?

Then provide a structured summary in <summary> tags.
</instructions>

<output_format>
<thinking>
[Your analysis here - this section is for reasoning only]
</thinking>

<summary>
{
  "customer_issue": "Brief description of the problem (max 100 chars)",
  "resolution": "How the issue was addressed (max 150 chars)",
  "follow_up_required": true|false,
  "follow_up_details": "What needs to happen next (or null if none)",
  "customer_sentiment": "positive|neutral|negative|frustrated",
  "call_quality_notes": "Any notable observations about the call handling",
  "status": "RESOLVED|PENDING|ESCALATED|INCOMPLETE"
}
</summary>
</output_format>

<guidelines>
- Omit all personally identifiable information (names, phone numbers, emails)
- Keep each text field under its character limit
- Maintain professional, neutral tone
- Focus on facts, not interpretation
</guidelines>

<insufficient_data_criteria>
If ANY of these conditions are met:
- Transcript has fewer than 5 exchanges
- Customer's issue is completely unclear
- Call is garbled, incomplete, or hindered by language barrier

Return ONLY:
<summary>
{"status": "INSUFFICIENT_DATA"}
</summary>
</insufficient_data_criteria>

<examples>
<example>
<transcript>
Agent: Thank you for calling TechCorp support, how can I help?
Customer: Yeah my internet keeps dropping every few hours.
Agent: I'm sorry to hear that. Let me check your connection status... I see some intermittent issues. I'll reset your connection from here.
Customer: Okay.
Agent: Done. Can you check if it's working now?
Customer: Yeah it's back. Hope it stays this time.
Agent: If it happens again, call us back and we'll schedule a technician.
Customer: Alright thanks.
</transcript>

<thinking>
Main issue: Intermittent internet connectivity dropping every few hours.
Resolution: Agent performed remote connection reset.
Follow-up: Conditional - customer should call back if issue recurs for technician visit.
Sentiment: Neutral to slightly skeptical ("Hope it stays this time").
No ambiguities, straightforward troubleshooting call.
</thinking>

<summary>
{
  "customer_issue": "Internet connection dropping intermittently every few hours",
  "resolution": "Remote connection reset performed by agent",
  "follow_up_required": false,
  "follow_up_details": null,
  "customer_sentiment": "neutral",
  "call_quality_notes": "Efficient troubleshooting, appropriate escalation path offered",
  "status": "RESOLVED"
}
</summary>
</example>

<example>
<transcript>
Agent: Support, how can I--
Customer: Hello? Hello?
Agent: Yes I'm here, how--
[call disconnects]
</transcript>

<thinking>
The call was disconnected before any issue could be discussed. Fewer than 5 meaningful exchanges and no customer issue was articulated.
</thinking>

<summary>
{"status": "INSUFFICIENT_DATA"}
</summary>
</example>
</examples>
```

### Techniques Applied
| Technique | How | Impact |
|-----------|-----|--------|
| Chain of thought | `<thinking>` tags before summary | Better analysis, debuggable |
| Structured JSON | Exact field schema | Consistent, parseable output |
| Character limits | Per-field constraints | Predictable output size |
| Status flags | RESOLVED/PENDING/INSUFFICIENT | Classification without forced content |
| Insufficient data handling | Explicit criteria + minimal response | Graceful degradation |
| Multiple examples | Success + edge case | Shows both paths |

---

## Example 5: Content Moderation

### Before (Weak)
```
Check if this content is appropriate.
```

### Problems
- "Appropriate" is undefined
- No categories of violations
- No confidence levels
- Binary output misses nuance

### After (Optimized)
```
You are a content moderation system. Evaluate user-generated content for policy compliance.

<content>
{user_content}
</content>

<policies>
Prohibited content includes:
1. **Hate speech**: Attacks on protected groups based on race, religion, gender, etc.
2. **Violence**: Threats, glorification of violence, graphic descriptions of harm
3. **Adult content**: Sexually explicit material, nudity descriptions
4. **Harassment**: Targeted attacks, doxxing, bullying of individuals
5. **Spam/Scam**: Unsolicited commercial content, phishing attempts
6. **Misinformation**: Demonstrably false claims about health, elections, emergencies
</policies>

<instructions>
Evaluate the content against each policy category. For each potential violation:
- Identify which policy it violates
- Quote the specific problematic text
- Assign confidence: HIGH (clear violation), MEDIUM (likely violation), LOW (borderline)

If no violations found, indicate content is compliant.
</instructions>

<output_format>
{
  "decision": "APPROVE|REMOVE|REVIEW",
  "violations": [
    {
      "policy": "policy_name",
      "evidence": "exact quoted text",
      "confidence": "HIGH|MEDIUM|LOW",
      "explanation": "why this violates policy"
    }
  ],
  "flags": ["hate_speech", "violence", ...],
  "requires_human_review": true|false,
  "reasoning": "Overall assessment summary"
}
</output_format>

<decision_criteria>
- REMOVE: Any HIGH confidence violation in hate_speech, violence, adult_content, or harassment
- REVIEW: Any MEDIUM confidence violation, or LOW in sensitive categories
- APPROVE: No violations or only LOW confidence in spam/misinformation
</decision_criteria>

<edge_cases>
- Content in non-English: Flag for human review with note about language
- Quoted/reported content: Evaluate the quoted portion, note if clearly attributed
- Sarcasm/satire: If clearly satirical, mark as LOW confidence with context
- Empty content: Return APPROVE with note "No content to evaluate"
</edge_cases>
```

### Techniques Applied
| Technique | How | Impact |
|-----------|-----|--------|
| Policy definitions | 6 numbered categories | Clear, auditable criteria |
| Evidence quoting | Exact text in output | Explainable decisions |
| Confidence levels | HIGH/MEDIUM/LOW | Nuanced assessment |
| Decision tree | Explicit REMOVE/REVIEW/APPROVE rules | Consistent automation |
| Edge cases | Language, satire, quotes | Handles real-world complexity |
| Requires human flag | Boolean for escalation | Enables hybrid workflow |

---

## Pattern Summary

### Optimization Transforms by Problem Type

| Original Problem | Solution Pattern |
|------------------|------------------|
| "Summarize this" | Add structure + format + length limits + example |
| "Check this for X" | Define X explicitly + severity levels + examples |
| "Help with Y" | Add constraints + output format + scope limits |
| "Analyze Z" | Add criteria + structured output + reasoning steps |
| No examples | Add 2-3 diverse input/output pairs |
| Inconsistent output | Add exact format spec + edge case handling |
| Too verbose | Add word limits + structured sections |
| Missing cases | Add edge case handlers + status flags |
