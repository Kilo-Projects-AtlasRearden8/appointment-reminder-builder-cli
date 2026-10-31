# Appointment Reminder Builder CLI

A local-first Python command-line tool for building appointment reminder lists
from a provider, date, and notes. It stores appointments in a local JSON file
and can generate printable reminder cards plus ICS calendar events.

Built and maintained by **Asdale Dynamics, LLC** (Indiana), the indie label of
Dylan Asdale — registered nurse turned AI author and founder of
[ASDALE DYNAMICS, LLC](https://dylanasdale.github.io). Part of a line of
beginner-friendly, practical tools the LLC publishes and sells.

## Who this is for

Anyone who juggles appointments and wants simple, printable reminder cards and
calendar events without signing up for another cloud service. Healthcare
workers, small-business owners, authors, and busy individuals who prefer local,
private tools. This app is an organizational aid only — it is not medical
advice.

## Features

- Add, list, delete, and clear appointments (provider, date, notes)
- Local JSON storage — no accounts, no API keys, nothing leaves your machine
- Printable reminder cards (plain text, ready to print and cut)
- ICS calendar events file you can import into any calendar app
- Tested date logic (parsing, formatting, past/future/today checks)

## Install

No installation required. This is standard-library Python — no dependencies.

```bash
python3 reminder_cli.py --help
```

## Usage

Add an appointment:

```bash
python3 reminder_cli.py add --provider "Dr. Ada Lopez" --date 2026-11-05 --notes "Bring insurance card"
```

List appointments:

```bash
python3 reminder_cli.py list
```

Generate printable cards:

```bash
python3 reminder_cli.py cards --out appointment_cards.txt
```

Generate an ICS calendar file:

```bash
python3 reminder_cli.py ics --out appointment_reminders.ics
```

Delete an appointment by id:

```bash
python3 reminder_cli.py delete --id <appointment-id>
```

Clear all appointments:

```bash
python3 reminder_cli.py clear
```

Use `--storage <path>` to keep your data in a different JSON file.

## Tests

```bash
python3 -m pytest
```

7 tests covering date parsing, formatting, display, past/future/today checks,
day offsets, and weekday names.

## Local-first, no secrets

This tool stores everything in a JSON file you control. It makes no network
requests, requires no keys, and collects no personal data. Do not commit
`appointments.json` or any other storage file containing real data.

## License

MIT License.

Copyright (c) 2026 Asdale Dynamics, LLC.

Credit: Asdale Dynamics, LLC — beginner-friendly AI education, books and
guides, and practical open-source tools. https://dylanasdale.github.io
