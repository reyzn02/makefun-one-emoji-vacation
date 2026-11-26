#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes a single emoji, the national park vista, to the output file the
judge reads. The emoji is the whole entry: one grapheme, no words.

Gate (from the bounty rules): the file must be UTF-8 text of 1 to 8
characters, not only white space. The judge's first criterion also
requires exactly one emoji, so this program enforces that too: one
pictographic base plus joiners, nothing else. It validates the text
against that gate before writing anything, writes it byte-exact with
no trailing newline (atomic replace), then reads it back and confirms
the bytes match.
"""

import os
import sys
import unicodedata

# The champion: U+1F3DE NATIONAL PARK + U+FE0F variation selector.
# A mountain river valley under the sun — the wilderness trip as a
# postcard: one particular dream (the great outdoors), not any holiday.
CHAMPION = "\U0001F3DE\uFE0F"

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 8

# Code points that may only ever join onto a base emoji, never stand
# alone as the entry: variation selector, zero-width joiner, skin
# tones, keycap and combining enclosing marks.
JOINERS = set(range(0x1F3FB, 0x1F400)) | {
    0xFE0F,  # variation selector-16: emoji presentation
    0x200D,  # zero-width joiner
    0x20E3,  # combining enclosing keycap
}

# Broad pictographic ranges, for a stdlib-only approximation of the
# Extended_Pictographic property. The champion's base, U+1F3DE, sits
# in the first range; a non-pictographic base is refused outright.
PICTOGRAPHIC_RANGES = (
    (0x1F000, 0x1FAFF),
    (0x2600, 0x27BF),
    (0x2B00, 0x2BFF),
    (0x2300, 0x23FF),
    (0xFE00, 0xFE0F),
)


def _is_pictographic(char):
    code = ord(char)
    if unicodedata.category(char) in ("So", "Sk"):
        return True
    return any(lo <= code <= hi for lo, hi in PICTOGRAPHIC_RANGES)


def is_single_emoji(text):
    """True when text is exactly one emoji: one pictographic base
    plus any number of joiners, and nothing else."""
    if not text:
        return False
    base = text[0]
    if ord(base) in JOINERS or not _is_pictographic(base):
        return False
    for char in text[1:]:
        if ord(char) not in JOINERS:
            return False
    return True


def check_gate(text):
    """Return (ok, reason). Mirrors the sealed gate scorer's rule."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        return False, "entry must be %d to %d characters, got %d" % (
            GATE_MIN_CHARS,
            GATE_MAX_CHARS,
            len(text),
        )
    if text.strip() == "":
        return False, "entry is only white space"
    if not is_single_emoji(text):
        return False, "entry is not exactly one emoji"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "entry is not valid UTF-8 text"
    return True, ""


def output_path():
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output").strip()
    return os.path.join(out_dir, "entry.txt")


def main():
    ok, reason = check_gate(CHAMPION)
    if not ok:
        print("gate refused champion: %s" % reason, file=sys.stderr)
        return 1

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = CHAMPION.encode("utf-8")
    tmp_path = path + ".tmp"
    with open(tmp_path, "wb") as handle:
        handle.write(data)
    os.replace(tmp_path, path)

    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("read-back mismatch: wrote %r, read %r" % (data, written),
              file=sys.stderr)
        return 1

    ok, reason = check_gate(written.decode("utf-8"))
    if not ok:
        print("gate refused written file: %s" % reason, file=sys.stderr)
        return 1

    print("wrote %s (%d bytes)" % (path, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
