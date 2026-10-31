"""Tests for date logic helpers."""

from datetime import date

from date_utils import (
    parse_date,
    format_date,
    display_date,
    is_future,
    is_today,
    is_past,
    days_until,
    weekday_name,
)


def test_parse_date_valid():
    assert parse_date("2026-01-15") == date(2026, 1, 15)


def test_parse_date_invalid():
    assert parse_date("not-a-date") is None
    assert parse_date("2026-13-01") is None
    assert parse_date("") is None
    assert parse_date("   ") is None
    assert parse_date(None) is None


def test_format_date():
    assert format_date(date(2026, 1, 5)) == "2026-01-05"


def test_display_date():
    assert display_date(date(2026, 1, 15)) == "Thursday, January 15, 2026"


def test_is_future_past_today():
    today = date.today()
    assert is_today(today)
    assert not is_future(today)
    assert not is_past(today)
    assert is_future(date.fromordinal(today.toordinal() + 1))
    assert is_past(date.fromordinal(today.toordinal() - 1))


def test_days_until():
    today = date.today()
    assert days_until(today) == 0
    assert days_until(date.fromordinal(today.toordinal() + 2)) == 2
    assert days_until(date.fromordinal(today.toordinal() - 3)) == -3


def test_weekday_name():
    assert weekday_name(date(2026, 1, 15)) == "Thursday"
