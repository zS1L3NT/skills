---
name: academic-reports
description: Write, rewrite or review an academic report, assignment answer or slide deck that argues from data or a paper. Use when drafting answers, rewriting academic prose, or checking claims and flow before submission.
---

# Academic reports

A report earns its marks when every claim is **backed**, the parts tell one **story**, and the prose reads like a person who knows the subject. Work in that order. A story built on an unbacked claim fails however well it reads, so evidence is a gate, and story and voice are judgement on top of it.

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

## Story

- **Answer the question.** Map each part of each question to the sentence that answers it. Lead each answer with that sentence, then give the evidence and the limits.
- **Spine.** One point, the subpoints that establish it, then the next point. A finding from an earlier section returns where it matters later, such as data problems found at the start coming back as limits of a model.
- **Transitions.** A section opens from the last finding where the logic connects. The opener carries the link, so standalone signposts ("We next turn to...") go.
- **Relevance.** Every sentence and every figure serves the point of its section. Cut the true but off-topic sentence.
- **Concepts.** Introduce a term where the reader first needs it, in plain words, once.
- **Endings.** A paragraph ends on its last piece of evidence or its implication. Recaps and stated lessons go.
- **Labels.** Paragraph labels, if used, are short phrases saying what the paragraph does, applied consistently.
- **Slides.** One message per slide, structured text over paragraphs, and evidence legible at presentation size. A complex chart's labels say exactly what is plotted.

The story is done when every part of every question maps to an answering sentence, every transition rests on a stated finding, and every sentence and figure maps to its section's point.

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

- **Write.** Build the ledger from verified evidence, outline the spine, draft, run the voice pass, then rerun the ledger on the draft.
- **Review.** Fix the baseline, build the ledger, check the story, check the voice, all within the user's scope. Deliver every proposed edit through the `diffdoc` skill with its importance levels. Without diffdoc, give each edit an exact Find passage, its Replace text, a Comment, and a level (critical, useful or minor), grouped by section.
