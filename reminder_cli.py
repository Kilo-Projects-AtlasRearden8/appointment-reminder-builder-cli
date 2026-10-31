"""Command-line interface for building appointment reminder lists.

Local-first Python CLI. Stores appointments in a JSON file and can
emit printable reminder cards and ICS calendar events.
"""

import argparse
import sys

from cards import write_cards
from ics_gen import write_ics
from storage import AppointmentStore


def build_parser():
    parser = argparse.ArgumentParser(
        prog="reminder_cli.py",
        description="Build appointment reminder lists from provider, date, and notes.",
    )
    parser.add_argument(
        "--storage",
        default="appointments.json",
        help="Path to the local JSON storage file (default: appointments.json)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Add an appointment")
    add_p.add_argument("--provider", required=True, help="Provider name")
    add_p.add_argument("--date", required=True, help="Appointment date (YYYY-MM-DD)")
    add_p.add_argument("--notes", default="", help="Appointment notes")

    sub.add_parser("list", help="List all appointments")

    sub.add_parser("clear", help="Remove all appointments")

    del_p = sub.add_parser("delete", help="Delete an appointment by id")
    del_p.add_argument("--id", required=True, help="Appointment id")

    cards_p = sub.add_parser("cards", help="Generate printable reminder cards")
    cards_p.add_argument(
        "--out", default="appointment_cards.txt", help="Output file (default: appointment_cards.txt)"
    )

    ics_p = sub.add_parser("ics", help="Generate ICS calendar events file")
    ics_p.add_argument(
        "--out", default="appointment_reminders.ics", help="Output file (default: appointment_reminders.ics)"
    )

    return parser


def cmd_add(args, store):
    record = store.add(args.provider, args.date, args.notes)
    print(f"Added appointment {record['id']}: {record['provider']} on {record['date']}")


def cmd_list(args, store):
    appointments = store.list()
    if not appointments:
        print("No appointments.")
        return
    for a in appointments:
        print(f"{a['id']}  {a['date']}  {a['provider']}  {a['notes']}")


def cmd_clear(args, store):
    store.clear()
    print("All appointments cleared.")


def cmd_delete(args, store):
    removed = store.delete(args.id)
    if removed:
        print(f"Deleted appointment {args.id}.")
    else:
        print(f"No appointment found with id {args.id}.")


def cmd_cards(args, store):
    appointments = store.list()
    path = write_cards(appointments, args.out)
    print(f"Wrote {len(appointments)} card(s) to {path}")


def cmd_ics(args, store):
    appointments = store.list()
    path = write_ics(appointments, args.out)
    print(f"Wrote {len(appointments)} event(s) to {path}")


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "clear": cmd_clear,
    "delete": cmd_delete,
    "cards": cmd_cards,
    "ics": cmd_ics,
}


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    store = AppointmentStore(args.storage)
    handler = COMMANDS[args.command]
    handler(args, store)


if __name__ == "__main__":
    main()
