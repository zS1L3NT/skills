---
name: academic-reports
description: Write, rewrite or review an academic report, assignment answer or slide deck that argues from data or a paper. Use when drafting answers, rewriting academic prose, or checking claims and flow before submission.
---

# Academic reports

A report earns its marks when every claim is **backed**, the parts build one **argument**, and the prose reads like a person who knows the subject. Work in that order. An argument built on an unbacked claim fails however well it reads, so evidence is a gate, and argument and voice are judgement on top of it.

## Pick the path

- **Light path**, for rewriting a sentence or passage. Read the passage and the context around it. Keep every claim, number and caveat it carries. Verify any claim the rewrite changes, and flag evidence you cannot reach. Then apply Voice.
- **Full path**, for drafting a section or reviewing a document. Run every step below.

## Before you start

1. Fix the scope and the baseline: which parts are the user's, and which file the user names as the current version.
2. Read the assignment questions and any rubric. Every part of every question needs an answer you can point to.
3. Read any writing conventions the user or project has set, such as an instruction file, a style guide or the assignment's formatting rules. They override this skill on characters, number precision, labels and length. With none set, follow the assignment's rules.
4. Read the course material the report draws on (lecture notes, the set paper). It is the yardstick for definitions and methods.

## Evidence

Keep a **claim ledger**: one row per claim, with its location, the claim, its evidence, how you verified it, and a verdict (backed, wrong, unbacked, or unverified). A claim is any sentence a marker could answer with "how do you know?". That covers numbers, comparisons, classifications, labels such as "similar" or "typical", association and causal statements, generalisations, and descriptions of what a figure shows.

Run every check on every row:

- **Source truth.** Data claims are verified by rerunning the analysis from the raw data in a clean run, then recomputing each claim-bearing number with separately written code. Text that agrees with output from the same pipeline proves only consistency. Claims about a paper are traced to its page, table or figure.
- **Visible support.** The reader sees the comparison, count or criterion beside the claim. Every quantity a claim relies on is stated in the same paragraph or table row, or named with an exact pointer ("Table 3"). A sentence about what the mean does states the mean.
- **Criterion.** Every classification and evaluative label states the rule behind it. A variable type names its test: is there a natural order, is arithmetic meaningful, are values counted or measured. "Similar reviews" names its basis, and the basis is chosen before looking at the result.
- **Like for like.** Rebuild every percentage from its counts. Check that compared groups share the population, filters, unit and direction, and that table columns map onto real variables in the dataset.
- **Inference strength.** The evidence matches the inference. Association needs its check (a rate comparison, a test with its assumptions met). A causal claim needs a design that supports it. Check the direction too: a variable recorded after the decision (a review score, whether a sequel followed) describes the outcome rather than steering it. Generalisation stays within what the sampling supports.
- **Method fit.** Methods match the course's definitions. A method beyond the course carries a one-line reason for using it.
- **Precision match.** Text, tables and figures show the same value at the same precision.

Cut a finding whose defence needs an unsupported assumption, a construct the reader was never shown, or more space than the finding is worth, such as a chart made only to defend it.

The ledger is done when every claim in scope has a row and a verdict. State readiness only with the count ("41 of 43 claims verified, 2 unverified because ..."), and keep unverified rows visible.

## Argument

Answer each question by building a small argument from verified, in-scope evidence, and let the evidence decide the conclusion. This is the general flow, not a template for every paragraph. Use each move where the question and evidence call for it.

- **Claim (macro theme).** Open with the sentence that answers the section's question.
- **Paragraph.** One point each. The topic sentence (hyper theme) states it, the evidence is analysed, and the last sentence (hyper new) states the insight that evidence earns.
- **Warrant.** Each premise reaches the claim through an assumption a marker would accept. Every "so", "because" and "therefore" states the relation the evidence supports.
- **Progression.** Fit the paragraph to its topic sentence: **fan** gives each of its ideas its own sentences then draws them together, **linear** keeps one theme as every sentence's subject, and **zigzag** makes each sentence's new information the next sentence's subject.
- **Fair representation.** Keep the evidence's scope and qualifiers, and report conflicting findings beside supporting ones.
- **Rebuttal.** Where a marker would raise a real objection (a confounder, an outlier, repeated records), state it fairly and answer it with a check. An objection left standing qualifies the conclusion.
- **Convergence (macro new).** The conclusion combines the paragraphs' insights into a consequence for the question, using only evidence already shown in the body. Each paragraph supports, qualifies or limits that conclusion.
- **Cohesion.** One stable term per referent, "this" plus a noun for a clear referent, and certainty matched to the strength and scope of the whole claim.
- **Fallacies.** Check for straw man, equivocation, false cause, hasty generalisation, false analogy, false dilemma and slippery slope.
- **Relevance.** Every sentence and figure develops or qualifies the section's answer. Introduce a term where the reader first needs it. On slides, one message per slide, with evidence legible at presentation size.

The argument is done when every question has an answering claim, every warrant holds, every paragraph's insight feeds the conclusion, every real objection is answered or reflected in the limits, and the conclusion uses only evidence already presented.

## Voice

Humanise the structure, never the precision.

- Keep the academic terms and caveats (right-skewed, imprecise, potential confounder) and rebuild the sentence around them.
- Name the subject of every statistic: "the mean number of copies sold per game", never a bare "the average". Define the unit of analysis in plain words at first use, such as "one game is one title on one console".
- Talk to the reader with "we" and sometimes "you". Vary sentence length. Use named examples from the data, such as the best seller and its figure.
- Write in the submission register. Keep the applied criterion, and leave out textbook definitions and citations of the lecture notes unless the assignment asks for them.
- Write the shortest complete version. A rewrite that adds a missing subject or reason pays for it with a cut elsewhere, inside the length limit.
- Test each replacement on a cold reader. If they could not explain it back, rewrite it.
- For a final sweep of AI tells, use a `humanize` skill on the prose if one is available. This skill's structure (answer first, evidence beside the claim), the project's conventions and the delivery format override it where they conflict.

Voice is done when every rewrite keeps the original's meaning and caveats, names its subjects, and fits the length limit.

## Modes

- **Write.** Build the ledger from verified evidence, outline each section's point, paragraphs and conclusion, draft, run the voice pass, then rerun the ledger on the draft.
- **Review.** Fix the baseline, build the ledger, check the argument, check the voice, all within the user's scope. Deliver every proposed edit through the `diffdoc` skill with its importance levels. Without diffdoc, give each edit an exact Find passage, its Replace text, a Comment, and a level (critical, useful or minor), grouped by section.
