"""Shared models used by the API."""
from typing import Any

import mongoengine as db


class Time(db.EmbeddedDocument):
    """A class representing an HH:MM time in 24-hour format."""

    hour: int = db.IntField(min_value=0, max_value=23, required=True)
    minute: int = db.IntField(min_value=0, max_value=59, required=True)
