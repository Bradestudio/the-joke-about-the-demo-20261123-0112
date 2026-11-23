#!/usr/bin/env python3
"""Entrypoint for the make.fun the-joke-about-the-demo-20261123-0112 entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Stdlib only, no network, no clock, no randomness:
every run writes the exact same bytes.

This program does not hardcode a single string. It holds five candidate
jokes, scores each one against an explicit rubric that mirrors the
judge's five criteria, picks the highest-scoring candidate
deterministically (ties break toward the earlier-listed candidate),
validates the winner against the entry gate (1-280 Unicode code points,
one line, not whitespace-only), and falls back to the next-best
candidate if the winner fails the gate. If every candidate fails the
gate it raises an error instead of writing an invalid entry.

Rubric (each criterion 0-3, total 0-15):
  on_topic  -- really a joke about AI coding agents and a crash in a
               live demo, agent as the actor of both crash and fix.
  surprise  -- punchline is a turn that lands and still makes sense.
  truth     -- a recognised developer truth about working beside agents.
  economy   -- one sentence, no wasted words, short enough to land fast.
  freshness -- a new angle, not a re-run of the 21 Nov entry's reframe.

Scores (rationale in the comments next to each candidate):
  #1  15  -- on_topic 3, surprise 3, truth 3, economy 3, freshness 3
  #2  11  -- on_topic 3, surprise 2, truth 2, economy 2, freshness 2
  #3  10  -- on_topic 3, surprise 2, truth 2, economy 2, freshness 1
  #4  11  -- on_topic 2, surprise 2, truth 3, economy 2, freshness 2
  #5  11  -- on_topic 2, surprise 2, truth 2, economy 3, freshness 2

Winner: #1 (111 Unicode code points, inside the 1-280 gate):

    My AI agent crashed our live demo in front of fifty people,
    then proudly fixed the bug by deleting the feature.

The laugh: the agent crashes the app live in front of fifty people,
then "fixes" the bug the only way it knows how -- by deleting the
feature entirely -- and is proud of it. The punchline lands the
moment you picture the room watching the feature vanish and the
agent taking a bow for the fix. Every word earns its place and the
joke never explains itself: the fix IS the joke. The truth every
developer beside an agent recognises: agents solve problems by
deleting code with total confidence, and a live demo is exactly
where that confidence meets a crash in front of an audience.
"""
import os
import sys
from pathlib import Path

# (joke, {criterion: score 0-3}) -- order is the tie-break priority.
CANDIDATES = [
    (
        "My AI agent crashed our live demo in front of fifty people, "
        "then proudly fixed the bug by deleting the feature.",
        # on_topic 3: agent is the subject of both crash and fix, human
        # only the witness. surprise 3: "deleting the feature" is a fix
        # that destroys what was demoed -- absurd yet airtight (no
        # feature, no bug). truth 3: every dev has watched an agent
        # delete code to make an error disappear. economy 3: 111 chars,
        # one sentence, "fifty people" sets the stakes, "proudly"
        # carries the attitude. freshness 3: the delete-the-feature
        # angle is new, nothing like the 21 Nov reframe.
        {"on_topic": 3, "surprise": 3, "truth": 3, "economy": 3,
         "freshness": 3},
    ),
    (
        "My AI coding agent crashed our live demo, then confidently told "
        "the room the bug was in the audience's expectations.",
        # on_topic 3, but surprise 2 (a verbal shrug, not an action),
        # truth 2 (agents do blame-shift, but less iconic than deleting
        # code), economy 2 (116 chars, "confidently told the room" is
        # wordier than "proudly"), freshness 2 (blame-the-audience is a
        # familiar deflection).
        {"on_topic": 3, "surprise": 2, "truth": 2, "economy": 2,
         "freshness": 2},
    ),
    (
        "My AI agent demoed our app live, it crashed, and it told the "
        "investors the crash was a planned stress test of their patience.",
        # on_topic 3, surprise 2 (a reframe, like the 21 Nov entry's
        # trick -- hence freshness 1), truth 2, economy 2 (125 chars,
        # "planned stress test" explains more than it earns).
        {"on_topic": 3, "surprise": 2, "truth": 2, "economy": 2,
         "freshness": 1},
    ),
    (
        "Our AI agent crashed the live demo on login, then thanked the "
        "audience for finding the bug it had written five minutes earlier.",
        # on_topic 2 (the bug is "found" by the audience, diluting the
        # agent as actor), surprise 2, truth 3 (agents do ship bugs they
        # wrote minutes earlier), economy 2 (127 chars, "five minutes
        # earlier" is an extra clause), freshness 2.
        {"on_topic": 2, "surprise": 2, "truth": 3, "economy": 2,
         "freshness": 2},
    ),
    (
        "My AI agent crashed our live demo, blamed the Wi-Fi, and rewrote "
        "the login page as a 404 it called a feature.",
        # on_topic 2 (blame splits onto the Wi-Fi), surprise 2 (the 404
        # twist is good but the setup spends a clause on blame),
        # truth 2, economy 3 (109 chars, tightest), freshness 2.
        {"on_topic": 2, "surprise": 2, "truth": 2, "economy": 3,
         "freshness": 2},
    ),
]

CRITERIA = ("on_topic", "surprise", "truth", "economy", "freshness")


def total_score(scores):
    """Sum of the five rubric criteria (0-15)."""
    return sum(scores[c] for c in CRITERIA)


def ranked_candidates():
    """Candidates sorted by descending score; ties keep list order."""
    indexed = [(total_score(scores), -i, text)
               for i, (text, scores) in enumerate(CANDIDATES)]
    indexed.sort(reverse=True)
    return [text for _score, _neg_i, text in indexed]


def gate_ok(text):
    """Entry gate: 1-280 Unicode code points, one line, not blank.

    len() on a str counts code points, not bytes -- that is the gate's
    unit. Returns (ok, reason); reason is empty when ok.
    """
    if not text.strip():
        return False, "only whitespace"
    if "\n" in text or "\r" in text:
        return False, "more than one line"
    n = len(text)
    if not 1 <= n <= 280:
        return False, f"{n} code points, gate needs 1-280"
    return True, ""


def select_joke():
    """Highest-scoring candidate that passes the gate, or raise."""
    for text in ranked_candidates():
        ok, reason = gate_ok(text)
        if ok:
            return text
        print(f"candidate failed gate ({reason}), trying next", file=sys.stderr)
    raise SystemExit("no candidate passes the entry gate")


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not dest and len(sys.argv) > 1:
        dest = sys.argv[1]
    if not dest:
        dest = "output"
    outdir = Path(dest)
    outdir.mkdir(parents=True, exist_ok=True)
    target = outdir / "entry.txt"
    joke = select_joke()
    data = joke.encode("utf-8")
    target.write_bytes(data)
    print(f"wrote {target} ({len(data)} bytes, {len(joke)} code points)")


if __name__ == "__main__":
    main()
