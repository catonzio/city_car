from dataclasses import dataclass


@dataclass
class Position:
    x: float
    y: float

    def equals(self, other: "Position", radius: float):
        # xs = self.x - radius <= other.x <= self.x + radius
        # ys = self.y - radius <= other.y <= self.y + radius
        # return xs and ys
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= radius**2

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: "Position | float | int"):
        if isinstance(other, Position):
            return Position(self.x * other.x, self.y * other.y)
        elif isinstance(other, float | int):
            return Position(self.x * other, self.y * other)
        return NotImplemented

    @staticmethod
    def zero() -> "Position":
        return Position(0, 0)

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y

    def __str__(self) -> str:
        return f"({self.x:.3f}, {self.y:.3f})"
