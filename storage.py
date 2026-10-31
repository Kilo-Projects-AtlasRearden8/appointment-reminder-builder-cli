"""Local JSON storage for appointments."""

import json
import os
import uuid
from pathlib import Path

from date_utils import parse_date, format_date


class AppointmentStore:
    """CRUD for appointments persisted in a local JSON file."""

    def __init__(self, path="appointments.json"):
        self.path = Path(path)

    def _load(self):
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
        except (json.JSONDecodeError, OSError):
            return []
        if not isinstance(data, list):
            return []
        return data

    def _save(self, appointments):
        with self.path.open("w", encoding="utf-8") as fh:
            json.dump(appointments, fh, indent=2)
            fh.write("\n")

    def list(self):
        """Return all appointments sorted by date, then provider."""
        appointments = self._load()
        return sorted(
            appointments,
            key=lambda a: (a.get("date", ""), a.get("provider", "").lower()),
        )

    def add(self, provider, date_value, notes):
        """Add an appointment and return the stored record."""
        parsed = parse_date(date_value)
        if parsed is None:
            raise ValueError(f"Invalid date: {date_value!r} (expected YYYY-MM-DD)")
        record = {
            "id": str(uuid.uuid4()),
            "provider": provider.strip(),
            "date": format_date(parsed),
            "notes": notes.strip(),
        }
        appointments = self._load()
        appointments.append(record)
        self._save(appointments)
        return record

    def delete(self, appointment_id):
        """Delete an appointment by id. Returns True if removed."""
        appointments = self._load()
        filtered = [a for a in appointments if a.get("id") != appointment_id]
        if len(filtered) == len(appointments):
            return False
        self._save(filtered)
        return True

    def clear(self):
        """Remove all appointments."""
        self._save([])
