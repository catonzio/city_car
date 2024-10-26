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

    @staticmethod
    def zero() -> "Position":
        return Position(0, 0)

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y
