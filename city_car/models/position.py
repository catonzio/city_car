from dataclasses import dataclass
from math import sqrt


@dataclass
class Position:
    x: float
    y: float

    def equals(self, other: "Position", radius: float):
        d = self.dist(other)
        return d <= radius * 2

    def __add__(self, other: "Position | tuple | float | int"):
        if isinstance(other, float) or isinstance(other, int):
            rother: Position = Position(other, other)
        else:
            rother: Position = (
                other if isinstance(other, Position) else Position(*other)
            )
        return Position(self.x + rother.x, self.y + rother.y)

    def __sub__(self, other: "Position | tuple | float | int"):
        if isinstance(other, float) or isinstance(other, int):
            rother: Position = Position(other, other)
        else:
            rother: Position = (
                other if isinstance(other, Position) else Position(*other)
            )
        return Position(self.x - rother.x, self.y - rother.y)

    def __mul__(self, other: "Position | float | int"):
        if isinstance(other, Position):
            return Position(self.x * other.x, self.y * other.y)
        elif isinstance(other, float | int):
            return Position(self.x * other, self.y * other)
        return NotImplemented

    def dist(self, other: "Position | tuple[float, float]") -> float:
        if isinstance(other, Position):
            return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        elif isinstance(other, tuple):
            return sqrt((self.x - other[0]) ** 2 + (self.y - other[1]) ** 2)
        return NotImplemented

    def dot(self, other: "Position | tuple[float, float]") -> "Position":
        if isinstance(other, Position):
            return Position(self.x * other.x, self.y * other.y)
        elif isinstance(other, tuple):
            return Position(self.x * other[0], self.y * other[1])
        return NotImplemented

    @staticmethod
    def zero() -> "Position":
        return Position(0, 0)

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def __str__(self) -> str:
        return f"({self.x:.3f}, {self.y:.3f})"

    def __repr__(self) -> str:
        return f"({self.x:.3f}, {self.y:.3f})"
