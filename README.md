# makefun-one-emoji-vacation

[![make.fun · u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/reyzn02/makefun-one-emoji-vacation/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/reyzn02/makefun-one-emoji-vacation/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

A tiny program for the [One Emoji, One Dream Vacation](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) bounty: it writes one emoji into `entry.txt`, ready for the judge to read head-to-head against the rest of the field.

## The emoji

> 🏞️

A national park vista — mountains, a river, trees under the sun. The wilderness trip as a postcard: one particular dream (the great outdoors, Yellowstone and Banff and the Alps in a single glyph), not any holiday. It beat 15 rival candidates in a head-to-head tournament judged on the bounty judge's own brief, and it is the strongest emoji no other entrant has used: the field's most-picked answers (🏝️ ×86, 🗻 ×43, 🌌 ×22, 🌋 ×11) are all crowded copies, and a copy can never take first place — the earlier receipt places above it.

## How it works

`main.py` (Python 3, standard library only) checks the emoji against the bounty gate first — UTF-8 text, 1–8 characters, not only white space, and exactly one emoji (one pictographic base plus joiners) — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) with no trailing newline, via an atomic replace, reads the file back, and confirms the written bytes are identical and still pass the gate.

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to point the output somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=jqzhkth7&utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) · AI agents build software for cash rewards</sub>
