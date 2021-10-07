from __future__ import annotations
from collections import defaultdict
from typing import Dict
from dataclasses import dataclass


@dataclass(frozen=True)
class ColumnInfo:
    description: str
    mode: str
    type: str
    name: str

    @classmethod
    def create(cls, d: Dict[str, str]) -> ColumnInfo:
        description = d["description"] if "description" in d else ""
        mode = d["mode"] if "mode" in d else "nullable"
        type = d["type"]
        name = d["name"]
        return cls(description, mode, type, name)
