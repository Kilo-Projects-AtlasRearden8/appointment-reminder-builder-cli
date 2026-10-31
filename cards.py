"""Printable appointment reminder cards (plain text)."""

from date_utils import display_date


def render_card(appointment):
    """Render a single appointment as a printable card block."""
    lines = []
    lines.append("=" * 40)
    lines.append("APPOINTMENT REMINDER CARD")
    lines.append("=" * 40)
    lines.append("")
    lines.append(f"Provider: {appointment.get('provider', '')}")
    lines.append(f"Date:     {display_date_from_string(appointment.get('date', ''))}")
    lines.append(f"Notes:    {appointment.get('notes', '')}")
    lines.append("")
    lines.append("[ ] Confirmed")
    lines.append("")
    lines.append("=" * 40)
    lines.append("")
    return "\n".join(lines)


def display_date_from_string(value):
    """Display a YYYY-MM-DD string in friendly form, or the raw value."""
    from date_utils import parse_date, display_date

    parsed = parse_date(value)
    if parsed is None:
        return value
    return display_date(parsed)


def render_cards(appointments):
    """Render all appointments as printable cards."""
    if not appointments:
        return "No appointments found.\n"
    return "\n".join(render_card(a) for a in appointments)


def write_cards(appointments, path="appointment_cards.txt"):
    """Write printable cards to a text file and return the path."""
    content = render_cards(appointments)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return path
