#!/usr/bin/env python3
"""Map any point in the past onto the Cosmic Calendar.

The Cosmic Calendar (Carl Sagan) compresses the 13.8-billion-year age of the
universe into a single calendar year: the Big Bang is January 1 at 00:00 and
the present moment is December 31 at midnight. On this scale, 1 second is
about 437 years.

Usage:
    python3 cosmic_calendar.py "5500 years ago"
    python3 cosmic_calendar.py "66 million years ago"
    python3 cosmic_calendar.py "4.6 billion years ago"
    python3 cosmic_calendar.py            # prints the events from data/timeline.json
"""

import json
import re
import sys
from pathlib import Path

UNIVERSE_AGE_YEARS = 13_800_000_000
YEAR_SECONDS = 365 * 24 * 3600
SECONDS_PER_YEAR_AGO = YEAR_SECONDS / UNIVERSE_AGE_YEARS  # cosmic seconds per real year

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

MULTIPLIERS = {"thousand": 1e3, "million": 1e6, "billion": 1e9}


def parse_years_ago(text: str) -> float:
    """Parse strings like '66 million years ago' or '5500 years ago'."""
    m = re.match(r"\s*([\d,.]+)\s*(thousand|million|billion)?\s*(years?)?(\s*ago)?\s*$",
                 text.strip(), re.IGNORECASE)
    if not m:
        raise ValueError(f"Could not parse: {text!r}")
    value = float(m.group(1).replace(",", ""))
    if m.group(2):
        value *= MULTIPLIERS[m.group(2).lower()]
    return value


def to_cosmic(years_ago: float) -> str:
    """Return the cosmic-calendar date/time for a moment `years_ago` in the past."""
    seconds_from_year_end = years_ago * SECONDS_PER_YEAR_AGO
    seconds_from_year_start = YEAR_SECONDS - seconds_from_year_end

    day_of_year = int(seconds_from_year_start // (24 * 3600))
    remainder = seconds_from_year_start - day_of_year * 24 * 3600

    month, day = 0, day_of_year + 1
    for i, days in enumerate(MONTH_DAYS):
        if day <= days:
            month = i
            break
        day -= days

    hours = int(remainder // 3600)
    minutes = int(remainder % 3600 // 60)
    seconds = remainder % 60

    if seconds_from_year_end < 60:
        return f"{MONTH_NAMES[month]} {day}, {hours:02d}:{minutes:02d}:{seconds:06.3f}"
    return f"{MONTH_NAMES[month]} {day}, {hours:02d}:{minutes:02d}:{int(seconds):02d}"


def main() -> None:
    if len(sys.argv) > 1:
        years_ago = parse_years_ago(" ".join(sys.argv[1:]))
        print(f"{years_ago:,.0f} years ago  ->  Cosmic Calendar: {to_cosmic(years_ago)}")
        return

    data_path = Path(__file__).resolve().parent.parent / "data" / "timeline.json"
    events = json.loads(data_path.read_text())["events"]
    width = max(len(e["name"]) for e in events)
    for e in events:
        print(f"{e['name']:<{width}}  {to_cosmic(e['years_ago'])}")


if __name__ == "__main__":
    main()
