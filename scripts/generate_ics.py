#!/usr/bin/env python3
"""Generate replicability-training.ics from _data/schedule.csv and _data/mentoring.csv."""

import argparse
import csv
from pathlib import Path

TIMEZONE = "America/New_York"

VTIMEZONE = """BEGIN:VTIMEZONE
TZID:America/New_York
X-LIC-LOCATION:America/New_York
BEGIN:DAYLIGHT
TZOFFSETFROM:-0500
TZOFFSETTO:-0400
TZNAME:EDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0400
TZOFFSETTO:-0500
TZNAME:EST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE"""

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}


def escape(text):
    return text.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;")


def parse_date(date_str, year):
    month_str, day_str = date_str.split()
    return year, MONTHS[month_str], int(day_str)


def parse_time_range(time_str):
    # e.g. "8:00-9:00" or "17:30- 18:30"
    start_str, end_str = [t.strip() for t in time_str.split("-")]
    start_h, start_m = (int(x) for x in start_str.split(":"))
    end_h, end_m = (int(x) for x in end_str.split(":"))
    return (start_h, start_m), (end_h, end_m)


def load_mentoring(path, year):
    dates = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("day"):
                continue
            day_num = row["day"].replace("Day", "").strip()
            dates[f"Day{day_num}"] = {
                "date": parse_date(row["date"], year),
                "topic": row["topic"],
            }
    return dates


def load_schedule_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_events(schedule_rows, mentoring, stamp):
    events = []
    for row in schedule_rows:
        time_str = row["Time"].strip()
        if not time_str or "self-paced" in time_str:
            continue
        (sh, sm), (eh, em) = parse_time_range(time_str)
        for day_key, day_info in mentoring.items():
            summary = row.get(day_key, "").strip()
            if not summary:
                continue
            year, month, day = day_info["date"]
            uid = f"repl-training-{day_key.lower()}-{sh:02d}{sm:02d}@replicability-training"
            events.append(
                f"""BEGIN:VEVENT
UID:{uid}
DTSTAMP:{stamp}
DTSTART;TZID={TIMEZONE}:{year:04d}{month:02d}{day:02d}T{sh:02d}{sm:02d}00
DTEND;TZID={TIMEZONE}:{year:04d}{month:02d}{day:02d}T{eh:02d}{em:02d}00
SUMMARY:{escape(f"Replicability Training {day_key.replace('Day', 'Day ')}: {summary}")}
DESCRIPTION:{escape(day_info["topic"])}
END:VEVENT"""
            )
    return events


def generate(schedule_path, mentoring_path, year, stamp):
    mentoring = load_mentoring(mentoring_path, year)
    schedule_rows = load_schedule_rows(schedule_path)
    events = build_events(schedule_rows, mentoring, stamp)
    body = "\n".join(events)
    return f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Replicability Training//EN
CALSCALE:GREGORIAN
{VTIMEZONE}
{body}
END:VCALENDAR
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schedule", default="_data/schedule.csv", type=Path)
    parser.add_argument("--mentoring", default="_data/mentoring.csv", type=Path)
    parser.add_argument("--output", default="assets/replicability-training.ics", type=Path)
    parser.add_argument("--year", type=int, default=None, help="Year for the training dates (default: current year)")
    parser.add_argument("--stamp", default=None, help="DTSTAMP value, e.g. 20260813T000000Z (default: now)")
    args = parser.parse_args()

    from datetime import datetime, timezone

    year = args.year or datetime.now().year
    stamp = args.stamp or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    ics = generate(args.schedule, args.mentoring, year, stamp)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(ics, encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
