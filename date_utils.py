"""Date logic helpers for the appointment reminder builder."""

from datetime import date, datetime

DATE_FORMAT = "%Y-%m-%d"
DISPLAY_FORMAT = "%A, %B %d, %Y"


def parse_date(value):
    """Parse a YYYY-MM-DD string into a date object.

    Returns None when the string is empty or not a valid date.
    """
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        return datetime.strptime(value, DATE_FORMAT).date()
    except ValueError:
        return None


def format_date(value):
    """Format a date as YYYY-MM-DD."""
    return value.strftime(DATE_FORMAT)


def display_date(value):
    """Format a date for human display (e.g. Monday, January 15, 2026)."""
    return value.strftime(DISPLAY_FORMAT)


def is_future(value):
    """Return True when the date is strictly after today."""
    return value > date.today()


def is_today(value):
    """Return True when the date is today."""
    return value == date.today()


def is_past(value):
    """Return True when the date is strictly before today."""
    return value < date.today()


def days_until(value):
    """Return the number of days from today to the date (negative if past)."""
    return (value - date.today()).days


def weekday_name(value):
    """Return the weekday name for a date."""
    return value.strftime("%A")
