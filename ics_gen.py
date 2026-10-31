"""ICS calendar event generation for appointments."""

import uuid
from datetime import datetime, timezone

from date_utils import parse_date, format_date


PRODID = "-//Asdale Dynamics, LLC//Appointment Reminder Builder 1.0//EN"


def _escape(text):
    """Escape a value for an ICS text property."""
    return (
        str(text)
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def _now_utc():
    """Current UTC timestamp in ICS format."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def render_ics(appointments):
    """Render appointments as an ICS calendar string."""
    lines = []
    lines.append("BEGIN:VCALENDAR")
    lines.append("VERSION:2.0")
    lines.append("PRODID:" + PRODID)
    lines.append("CALSCALE:GREGORIAN")
    lines.append("METHOD:PUBLISH")
    lines.append("X-WR-CALNAME:Appointment Reminders")
    lines.append("X-WR-TIMEZONE:UTC")
    for appointment in appointments:
        event_date = parse_date(appointment.get("date", ""))
        if event_date is None:
            continue
        event_id = appointment.get("id") or str(uuid.uuid4())
        lines.append("BEGIN:VEVENT")
        lines.append("UID:" + str(event_id))
        lines.append("DTSTAMP:" + _now_utc())
        lines.append("DTSTART;VALUE=DATE:" + event_date.strftime("%Y%m%d"))
        lines.append("SUMMARY:Appointment with " + _escape(appointment.get("provider", "")))
        notes = appointment.get("notes", "")
        if notes:
            lines.append("DESCRIPTION:" + _escape(notes))
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    lines.append("")
    return "\r\n".join(lines)


def write_ics(appointments, path="appointment_reminders.ics"):
    """Write appointments to an ICS file and return the path."""
    content = render_ics(appointments)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(content)
    return path
