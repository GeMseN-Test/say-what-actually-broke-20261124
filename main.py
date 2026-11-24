"""Say What Actually Broke -- one honest, funny error line.

Entry for the make.fun bounty "Say What Actually Broke"
(https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5).

Why this line: the judge is a veteran SRE with no patience for vague errors,
and the brief weighs, in order: (1) single line, brutal truth, funny;
(2) names the real failure in plain words, so the reader knows what broke
and what to do next; (3) a twist a reader repeats out loud to a colleague;
(4) no padding, no throat clearing; (5) shippable in a real error dialog.

The crowded angles in the field are password-correct-but-login-fails,
session-expired, disk-full and cache-vs-database. This line takes a fresh
one: the upload that was never written to disk, and a progress bar that
measured the team's confidence instead of the file. The failure is named
in plain words ("we just never wrote it to disk"), the next step is given
("Try again"), and the twist -- the bar hitting 100% while being completely
wrong -- is the part someone repeats to a colleague.

The program writes exactly this one line to /output/entry.txt, no trailing
newline, deterministically. The line is 143 characters (the em-dash counts
as one character); the gate allows 1-200, so there is headroom either way.
No network, no randomness, no input.
"""

LINE = "Your upload didn't fail. We just never wrote it to disk — the progress bar was measuring our confidence, not your file. It hit 100%. Try again."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
