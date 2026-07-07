# Candle of Consciousness

**Human history, seen at cosmic scale.**

This is a small hobby project inspired by [a short clip of Elon Musk](https://www.youtube.com/shorts/xaqsBWFZcHs)
making a simple but striking argument:

> The universe is ~13.8 billion years old. Recorded human civilization, if you count
> from the invention of writing, is about 5,500 years old. The cosmos is silent.
> Consciousness may be incredibly rare, and human civilization is a tiny candle
> in a vast darkness. We should do everything we can to keep it lit.

Whether or not you agree with the conclusion (Mars, multiplanetary life), the framing
is a great excuse to look at human history with fresh eyes: **everything we call
"history" fits into a rounding error of cosmic time.**

## The compression

If the age of the universe were compressed into a single calendar year
(Carl Sagan's *Cosmic Calendar*):

| Event | Real time | Cosmic calendar |
| --- | --- | --- |
| Big Bang | 13.8 billion years ago | Jan 1, 00:00 |
| Milky Way forms | ~13.6 billion years ago | early January |
| Sun & Earth form | ~4.6 billion years ago | September 2 |
| First life on Earth | ~3.8 billion years ago | September 21 |
| First animals | ~800 million years ago | December 10 |
| Dinosaurs go extinct | 66 million years ago | December 30 |
| First *Homo sapiens* | ~300,000 years ago | Dec 31, 23:52 |
| Agriculture | ~12,000 years ago | Dec 31, 23:59:32 |
| **Writing (recorded history begins)** | ~5,500 years ago | **Dec 31, 23:59:47** |
| Industrial Revolution | ~260 years ago | Dec 31, 23:59:59.4 |
| First human in space | 1961 | Dec 31, 23:59:59.86 |
| You, reading this | now | Dec 31, 24:00:00 |

Every empire, war, religion, book, and invention in recorded history happens in the
**last 13 seconds** of the cosmic year.

## What's in this repo

- [`TIMELINE.md`](TIMELINE.md): a walk through the major milestones of human history,
  each annotated with how recent it really is.
- [`data/timeline.json`](data/timeline.json): the milestones in machine-readable form,
  so you can build your own visualizations.
- [`scripts/cosmic_calendar.py`](scripts/cosmic_calendar.py): a tiny script that maps
  any point in the past onto the cosmic calendar. Try:

  ```bash
  python3 scripts/cosmic_calendar.py "5500 years ago"
  python3 scripts/cosmic_calendar.py "66 million years ago"
  ```

## The Fermi angle

The part of the clip that sticks with people is the silence. If intelligent life were
common, a civilization even a few million years older than ours (nothing, cosmically)
should be visible everywhere. It isn't. The possible explanations (we're early, we're
rare, or civilizations don't last) all lead to the same practical conclusion:
what we have is not guaranteed, and it is very, very young.

## Contributing

This is a hobby repo; corrections, new milestones, better sources, and visualizations
are all welcome. Open an issue or a PR.

## License

[MIT](LICENSE) for code, and the text content is
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
