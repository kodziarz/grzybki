from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ObjectiveWeights:
    w1: float = 0.4
    w2: float = 0.4
    w3: float = 0.2

    def __post_init__(self) -> None:
        if self.w1 < 0.0 or self.w2 < 0.0 or self.w3 < 0.0:
            raise ValueError("objective weights must be non-negative")
        if self.w1 + self.w2 + self.w3 <= 0.0:
            raise ValueError("at least one objective weight must be positive")

    def to_dict(self) -> dict[str, float]:
        return {"w1": self.w1, "w2": self.w2, "w3": self.w3}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ObjectiveWeights":
        return cls(
            w1=float(data.get("w1", 0.4)),
            w2=float(data.get("w2", 0.4)),
            w3=float(data.get("w3", 0.2)),
        )
