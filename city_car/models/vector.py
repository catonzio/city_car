from dataclasses import dataclass
from math import atan2, sqrt

from city_car.models.position import Position


@dataclass
class Vector:
    direction: Position
    value: float

    @staticmethod
    def zero() -> "Vector":
        return Vector(Position(0, 0), 0)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.direction + other.direction, self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.direction - other.direction, self.value - other.value)
        return NotImplemented

    def update(self, delta: Position | tuple[float, float]):
        delta = Position(*delta) if isinstance(delta, tuple) else delta
        self.set_direction(self.direction + delta)

    def set_direction(self, direction: Position | tuple[float, float]):
        self.direction = (
            Position(*direction) if isinstance(direction, tuple) else direction
        )
        self.value = sqrt(self.direction.x**2 + self.direction.y**2)

    def angle(self):
        return atan2(self.direction.x, self.direction.y)

    def normalize(self) -> Position:
        magnitude: float = (self.direction.x**2 + self.direction.y**2) ** (1 / 2)
        if magnitude == 0:
            return Position.zero()
        return Position(self.direction.x / magnitude, self.direction.y / magnitude)

    def __str__(self) -> str:
        return str(self.direction)

    def __repr__(self) -> str:
        return str(self.direction)
