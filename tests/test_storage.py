"""Tests for the local JSON appointment store."""

import os
import tempfile

from storage import AppointmentStore


def test_store_add_and_list():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "appointments.json")
        store = AppointmentStore(path)
        record = store.add("Dr. Ada Lopez", "2026-11-05", "Bring insurance card")
        appointments = store.list()
        assert len(appointments) == 1
        assert appointments[0]["provider"] == "Dr. Ada Lopez"
        assert appointments[0]["date"] == "2026-11-05"
        assert appointments[0]["notes"] == "Bring insurance card"
        assert record["id"] == appointments[0]["id"]


def test_store_rejects_invalid_date():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "appointments.json")
        store = AppointmentStore(path)
        try:
            store.add("Dr. Ada Lopez", "not-a-date", "notes")
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError for invalid date")
        assert store.list() == []


def test_store_delete():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "appointments.json")
        store = AppointmentStore(path)
        record = store.add("Dr. Ada Lopez", "2026-11-05", "notes")
        assert store.delete(record["id"]) is True
        assert store.delete(record["id"]) is False
        assert store.list() == []


def test_store_clear():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "appointments.json")
        store = AppointmentStore(path)
        store.add("Dr. Ada Lopez", "2026-11-05", "notes")
        store.add("Dr. Ben Cho", "2026-11-12", "notes")
        store.clear()
        assert store.list() == []


def test_store_sorted_by_date_then_provider():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "appointments.json")
        store = AppointmentStore(path)
        store.add("Dr. Ben Cho", "2026-11-12", "later")
        store.add("Dr. Ada Lopez", "2026-11-05", "earlier")
        appointments = store.list()
        assert appointments[0]["provider"] == "Dr. Ada Lopez"
        assert appointments[1]["provider"] == "Dr. Ben Cho"
