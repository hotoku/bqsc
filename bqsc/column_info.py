from __future__ import annotations
from typing import Dict
from dataclasses import dataclass

from .type_map import TYPE_MAP


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

    def typehint(self) -> str:
        name = TYPE_MAP[self.type.lower()].__name__
        return f"{self.name}: Union[{name}, Sequence[{name}]]"
