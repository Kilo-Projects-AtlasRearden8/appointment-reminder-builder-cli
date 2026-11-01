# Appointment Reminder Builder CLI

A friendly, local-first Python command-line tool for building appointment
reminder lists from a provider, a date, and some notes. It stores your
appointments in a simple JSON file on your computer and can print out handy
reminder cards or create an ICS calendar file you can import into any calendar
app.

Built by **Asdale Dynamics, LLC** (Indiana) — the indie label of Dylan Asdale,
a registered nurse turned AI author and founder of
[ASDALE DYNAMICS, LLC](https://dylanasdale.github.io). Dylan explains things
"like a friend would": plain English, step by step, never condescending. This
tool is part of a line of beginner-friendly, practical apps the LLC publishes
and sells.

## Who this is for

Anyone who juggles appointments and wants simple, printable reminders without
signing up for yet another cloud service. That includes:

- Healthcare workers keeping track of shifts and follow-ups
- Small-business owners and authors managing client meetings
- Busy individuals who prefer private, local tools
- Anyone who likes paper reminder cards they can tape to the fridge

This app is an organizational aid only — it is not medical advice.

## Features

- Add, list, delete, and clear appointments (provider, date, notes)
- Local JSON storage — no accounts, no API keys, nothing leaves your machine
- Printable reminder cards (plain text, ready to print and cut)
- ICS calendar events file you can import into any calendar app
- Tested date logic (parsing, formatting, past/future/today checks)

## What you need

Nothing special. This is standard-library Python, so there are no packages to
install and no dependencies to manage. Just Python 3.

## Get started

### 1. Grab the files

Make sure you have these files in the same folder:

- `reminder_cli.py`
- `storage.py`
- `cards.py`
- `ics_gen.py`
- `date_utils.py`

### 2. Try the help command

```bash
python3 reminder_cli.py --help
```

You should see a list of commands: `add`, `list`, `clear`, `delete`, `cards`,
and `ics`.

### 3. Add your first appointment

```bash
python3 reminder_cli.py add --provider "Dr. Ada Lopez" --date 2026-11-05 --notes "Bring insurance card and ID"
```

You'll get a confirmation with the appointment id and details.

### 4. See your appointments

```bash
python3 reminder_cli.py list
```

### 5. Print reminder cards

```bash
python3 reminder_cli.py cards --out appointment_cards.txt
```

Open `appointment_cards.txt` and print it. Each card has the provider, date,
notes, and a checkbox to mark it confirmed.

### 6. Create an ICS calendar file

```bash
python3 reminder_cli.py ics --out appointment_reminders.ics
```

Import `appointment_reminders.ics` into Google Calendar, Outlook, Apple
Calendar, or any app that understands ICS.

## Other commands

Delete one appointment by its id:

```bash
python3 reminder_cli.py delete --id <appointment-id>
```

Remove every appointment:

```bash
python3 reminder_cli.py clear
```

Keep your data in a different file with `--storage`:

```bash
python3 reminder_cli.py --storage my_appointments.json add --provider "Dr. Lee" --date 2026-12-01 --notes "Checkup"
```

## Run the tests

```bash
python3 -m pytest
```

You should see 11 passing tests covering date logic and appointment storage.

## Local-first, no secrets

This tool stores everything in a JSON file you control. It makes no network
requests, requires no keys or API tokens, and collects no personal data. Your
appointment information stays on your computer.

Please do not commit `appointments.json` (or any file holding real appointment
data) to version control.

## License

MIT License.

Copyright (c) 2026 Asdale Dynamics, LLC.

Credit: Asdale Dynamics, LLC — beginner-friendly AI education, books and
guides, and practical open-source tools. https://dylanasdale.github.io
