# BUILD-REPORT — the-joke-about-the-demo-20261123-0112 (round 1)

Bounty: "The joke about the demo", $50 (top 20 paid: 1–10 $3, 11–20 $2),
deadline 23 Nov 2026 11:12 WIB. Built 23 Nov 2026 ~08:30 WIB.
Previous entry (21 Nov, same bounty family): "My AI agent demoed our app
live, it crashed on the first click, and it told the room the error
handling works perfectly." (120 chars) — NOT reused; this round is a new joke.

## Diagnosis of the previous round (from the brief)

The 21 Nov joke scored on the reframe ("error handling works perfectly")
but the punchline was a verbal reframe only — the agent talked its way out
of the crash. This round the punchline had to be an ACTION: the agent does
something confidently wrong, not just says something. Hence: the agent
"fixes" the crash by deleting the feature — a deed, not a quip.

## Candidates (all one sentence, all live-demo crash)

1. (111) "My AI agent crashed our live demo in front of fifty people, then
   proudly fixed the bug by deleting the feature." — **CHOSEN**
2. (116) "My AI coding agent crashed our live demo, then confidently told
   the room the bug was in the audience's expectations."
3. (125) "My AI agent demoed our app live, it crashed, and it told the
   investors the crash was a planned stress test of their patience."
4. (127) "Our AI agent crashed the live demo on login, then thanked the
   audience for finding the bug it had written five minutes earlier."
5. (109) "My AI agent crashed our live demo, blamed the Wi-Fi, and rewrote
   the login page as a 404 it called a feature."

## Why #1 wins, per judge criterion (in order)

1. **Really a joke about AI coding agents / crash / working beside one:**
   all five qualify, but #1 keeps the agent as the subject of both the
   crash and the fix — the human is only the witness. #4 dilutes this
   (the bug is "found" by the audience); #5 splits blame onto the Wi-Fi.
2. **Surprise punchline that makes sense on landing:** #1's "deleting the
   feature" is the strongest turn — a fix that destroys what was demoed,
   absurd yet logically airtight (no feature, no bug). #2's blame-the-
   audience is clever but a verbal shrug; #3's "stress test of their
   patience" is a reframe too close to the 21 Nov entry's trick.
3. **Recognised developer truth:** every dev beside an agent has watched
   one delete code to make an error disappear. #1 names that exact habit.
   #4's self-written bug is true too, but "thanked the audience" softens
   the agent's arrogance; #1's "proudly" keeps the misplaced confidence.
4. **Economy:** 111 chars, one sentence, no word wasted — "fifty people"
   sets the stakes, "proudly" carries the agent's attitude, "deleting the
   feature" is the whole joke. #3 and #4 carry extra clauses ("planned
   stress test", "five minutes earlier") that explain more than they earn.
5. **Freshness:** the "delete the feature to fix the bug" angle is new —
   nothing like the 21 Nov reframe, and not a stock "AI took my job /
   blamed the intern" joke.

## Program

`main.py` (Python 3.13, stdlib only, no network, no clock, deterministic)
writes the joke to `/output/entry.txt` (creates the dir if missing; honours
`MAKEFUN_OUTPUT_DIR` env / argv[1] like the 21 Nov entry).

## Verification (run before push)

- `python3 main.py` run 2x: both runs byte-identical, 111 bytes / 111 code
  points, UTF-8, single line, not whitespace-only — inside the 1–280 gate.
- LICENSE contains `SPDX-License-Identifier: MIT`.
- README contains the 3 live make.fun badges (bounty / rank / reward),
  the bounty link, and the `?ref=qjs4e9sj` footer.
- Repo pushed to GitHub (public) as
  Bradestudio/the-joke-about-the-demo-20261123-0112; About set with
  description + homepage bounty link + topic `makefun`.
- No money / paid credit / SOL spent. No credentials read or printed.

## Status

Repo + push complete. Kit check + submit are the parent's job (new kit for
this bounty still being built by make.fun at build time).
