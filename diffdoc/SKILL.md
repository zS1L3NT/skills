---
name: diffdoc
description: Present proposed document or text changes for human review using exact Find, Replace, and Comment entries. Use when the user asks for a diff document, Ctrl+F edits, a manual change list, or a human-in-the-loop revision workflow.
---

# Diffdoc

Keep the human in the loop for every change. Produce a change document the user can review and apply one entry at a time using Ctrl+F (Cmd+F on Mac), then select the found text and paste the replacement.

## Review contract

- By default, propose edits in the change document and leave the source untouched. A request to review, improve, rewrite, or prepare a diff through this skill authorizes proposals. Apply edits to the source only when the user explicitly asks for application, within their authorized scope.
- Make every proposed change visible, including punctuation, formatting, deletions, and moves. Give entries stable numbers so the user can accept, reject, or discuss individual changes.
- Mark optional alternatives and decisions that need the user's judgment. Keep them separate from the primary replacement so the copyable text contains one complete choice.
- If application is authorized, account for every applied change in the change document. Report anything left unresolved. Do not claim a proposal has been applied.

## Prepare the change list

1. Read the actual source and identify the baseline by filename, version, or supplied date. Respect any section boundaries. If the source is unavailable, request it before inventing Find text.
2. Draft edits against that baseline and give each one an importance level (below). Group entries under the source's own sections (question, chapter, slide), in document order. Within a section, list critical entries first, then useful, then minor, keeping document order inside each level. Keep each entry independently reviewable. Grade each fix and apply any threshold the user set before combining. Then combine retained fixes whose Find passages overlap into one replacement at their highest level, so the user does not have to find text already changed by another entry. Check that no replacement removes another entry's Find text.
3. Verify every Find string against the source. Use the smallest passage that is unique, usually a phrase or one sentence, so the user selects and pastes as little as possible. Find a whole paragraph only when the whole paragraph is rewritten. Split a paragraph with several small fixes into separate phrase-level entries, unless their Finds would overlap. When it repeats, specify the section and nearby text or expand the passage to make it unique. Use page numbers only as supplemental locators because pagination can change.
4. Deliver the numbered list with a short opening that names the baseline, scope, and application status, and counts the entries at each level. Choose where it goes (below). Do not overwrite the source to create this artifact.

When the user sends an updated source after a previous list, compare it with the previous baseline before drafting. Note which entries were applied, altered, or skipped. Treat skipped or altered entries as the user's preferences, and do not propose them again unless the user asks. If the user gives numbered notes, open the change document with a table that maps each note to the entries that address it.

When revising an earlier change list, write the revision as the next version file, preserve entry numbers where possible and mark additions or withdrawals. For a consolidated version, resolve superseded proposals against the agreed baseline and state whether numbering has changed.

## Chat or file

Follow the user's stated choice ("just output here", "give me a file"). Otherwise, judge by how the user will apply the list:

- **Chat:** a short list the user can apply in one sitting, roughly five entries or fewer with phrase-sized passages, or a quick answer inside an ongoing discussion.
- **File:** anything longer, entries with long passages or tables, a list the user will work through over time or share, or one round in a series of revisions. Save it as Markdown in the project's output or revisions folder if one exists, link it, and summarise the levels in chat.

Give each version of a change list its own file, numbered in the name (`report-diff-v1.md`, `report-diff-v2.md`), so earlier rounds stay intact for comparison. Edit an existing version in place only when the user explicitly asks to change that version.

## Importance levels

- **Critical:** a marker or reader would count it against the work. Examples are a wrong or unbacked claim, a part of the question left unanswered, a broken rule of the assignment, or a sentence that misleads.
- **Useful:** the text is correct, but this clearly improves it. Examples are support that exists but is hard to see, a gap in the flow, or a subject left unnamed.
- **Minor:** polish the user can skip at no cost, such as wording, consistency or formatting.

Grade by consequence for the reader, not by the size of the edit. A one-word fix that corrects a claim is critical, and so is missing support or an unnamed subject that makes a claim misleading or an answer incomplete. When the user sets a threshold ("critical only"), review everything, list only the entries at or above it, and state how many entries below it were left out. Skip single-word style swaps unless they change meaning.

## Entry format

Use this structure for ordinary replacements, under a heading for the source section. The labels belong outside the copyable passages.

### 1. [Critical] Short description

**Find:**

> Exact text currently in the source.

**Replace:**

> Complete replacement text to paste.

**Comment:** Briefly explain the reason and any meaningful effect on the claim, meaning, or tone.

Keep the Find text literal, including spelling, capitalization, punctuation, and meaningful whitespace. Keep mistakes in Find; fix them in Replace. Never abbreviate source text with ellipses or placeholders. Quote only text the user should select, and include unchanged surrounding text in Replace if it is needed to make Find unique.

Use blockquotes for ordinary prose. Use fenced plain-text or code blocks when leading spaces, line breaks, or literal Markdown matter. Show significant boundary whitespace explicitly in an instruction outside the block. Keep editorial notes, location hints, and formatting instructions outside the text to paste.

Start the change document with this brief usage instruction, adapted to the user's editor when known:

> Work from top to bottom. Copy each Find passage into Ctrl+F (Cmd+F on Mac), check its location, then select that passage in the document and paste the Replace passage. Read the Comment before applying it. If Find has no match, check the baseline and location before editing.

Treat Replace All as a separate, explicitly stated operation only when every occurrence has been checked and is intended to change. Otherwise identify each intended occurrence.

## Other change types

- **Insertion:** Give **Find** with an exact existing anchor, then **Insert after** or **Insert before** with the full new text. Say whether it is a new paragraph, bullet, or inline addition and whether the anchor stays.
- **Deletion:** Give **Find** with the complete text, followed by **Action: Delete this passage.** Specify whether to remove the paragraph break, bullet, or table row too. An empty Replace field is ambiguous.
- **Move:** Give the complete source passage and an exact destination anchor. Say to cut and paste before or after that anchor, preserving the passage unless a separate replacement is shown.
- **Formatting:** Give an exact Find passage or a precise table-cell location, then **Format** with the required change. For example, identify the exact words to bold. Separate formatting from the literal replacement text.
- **Tables:** Identify the table and row/column, then give Find and Replace for each changed cell. A compact Find/Replace table is suitable for short, unambiguous cell edits; retain the numbered entry and Comment.
- **Figures or other non-text elements:** Use a caption or nearby text as the Find anchor. State the exact action and link any replacement asset. Account for changed labels or captions separately.

## Final check

The list is ready when every proposed change has an entry and an importance level, every Find or anchor matches the named baseline, every replacement is complete, and applying entries in order creates no conflicting or hidden edits. Distinguish verified matches from editor-specific issues such as subscripts or line breaks that require manual selection. State application status accurately and keep unresolved choices visible.
