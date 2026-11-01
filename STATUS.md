# STATUS

## What was built

A local-first Python command-line tool for building appointment reminder
lists from a provider, date, and notes. It stores appointments in a local
JSON file and can generate printable reminder cards plus ICS calendar
events.

Files:
- `reminder_cli.py` — CLI entry point (add/list/clear/delete/cards/ics)
- `storage.py` — local JSON appointment store
- `cards.py` — printable reminder card renderer (plain text)
- `ics_gen.py` — ICS calendar event generator (RFC 5545 style)
- `date_utils.py` — date logic helpers (parse, format, display, past/future/today)
- `tests/test_date_utils.py` — date logic tests
- `tests/test_storage.py` — appointment store tests (add/list/delete/clear/sort/invalid date)
- `README.md` — beginner-friendly usage docs, credits Asdale Dynamics, LLC
- `LICENSE` — MIT License, Copyright (c) 2026 Asdale Dynamics, LLC
- `.gitignore` — excludes Python caches and local storage files

No external dependencies (Python standard library only). No API keys, no
network calls, no secrets or personal data. No `.github/workflows` files.

## How to run it

```bash
python3 reminder_cli.py --help

# Add an appointment
python3 reminder_cli.py add --provider "Dr. Ada Lopez" --date 2026-11-05 --notes "Bring insurance card"

# List appointments
python3 reminder_cli.py list

# Printable cards
python3 reminder_cli.py cards --out appointment_cards.txt

# ICS calendar file
python3 reminder_cli.py ics --out appointment_reminders.ics
```

Use `--storage <path>` to keep data in a different JSON file.

## Verification results

- `python3 -m py_compile` on all modules: OK
- `python3 -m pytest`: 12 passed (date logic + appointment storage)
- End-to-end CLI exercised: add, list, cards, ics all produce correct output
  (cards formatted with provider/date/notes; ICS output contains VEVENT blocks
  with UID, DTSTAMP, DTSTART, SUMMARY, DESCRIPTION)
- Invalid date produces a friendly error message and exit code 1 instead of a
  traceback
- Git initialized and committed as 7172dd2 (plain message, no
  Co-authored-by trailer). Nothing pushed, no remote created.

## Known gaps

- Cards are plain text only (no PDF rendering); print the .txt file directly
- ICS uses floating UTC DTSTAMP and all-day DATE start times; no timezone
  overrides or reminders (VALARM) yet
- Storage file path defaults to `appointments.json` in the current working
  directory; concurrent writes are not locked
- No validation beyond date format (e.g., no provider/notes length limits)
- Appointment storage tests use temp files; no real-data files are committed
