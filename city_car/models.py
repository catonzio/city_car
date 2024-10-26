from dataclasses import dataclass
from math import pi
from typing import List


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


@dataclass
class Entity:
    id: int = 0
    position: Position = Position.zero()
    width: float = 0
    height: float = 0

    def __init__(
        self,
        id: int,
        position: Position | tuple[float, float] = Position.zero(),
        width: float = 0,
        height: float = 0,
    ):
        self.id = id
        self.position = Position(*position) if isinstance(position, tuple) else position
        self.width = width
        self.height = height

    def to_rect(self) -> tuple[float, float, float, float]:
        tl_x = self.position.x - self.width / 2
        tl_y = self.position.y - self.height / 2
        return tl_x, tl_y, self.width, self.height


# Collision Mixin
@dataclass
class CollidableMixin(Entity):
    radius: float = 0.2

    def check_collision(self, other_entities: List[Entity]) -> bool:
        for entity in other_entities:
            if self.check_single_collision(entity):
                return True
        return False

    def check_single_collision(self, other: Entity) -> bool:
        if other == self:
            return False

        radius = (
            max(self.radius, other.radius)
            if isinstance(other, CollidableMixin)
            else self.radius
        )
        print(f"Collision {self=} -- {other=}, {radius=}")
        return self.position.equals(other.position, radius)


# Movement Mixin
@dataclass
class MovableMixin(CollidableMixin):
    speed: float = 0  # m/s
    acceleration: float = 0  # m/s**2
    steer_angle: float = pi / 2  # in radians -- [0, pi]

    def move(self, dx: float, dy: float, ref_sys: Position | None = None):
        ref_sys = ref_sys if ref_sys else Position(0, 0)
        self.position.x += dx * self.speed
        self.position.y += dy * self.speed


# Car Entity inheriting both mixins and Entity
@dataclass
class Car(MovableMixin):
    def __init__(
        self,
        id: int,
        position: Position | tuple[float, float],
        speed: float = 0.0,
        acceleration: float = 0.0,
        steer_angle: float = pi / 2,
        radius: float = 0.2,
        width: float = 5,
        height: float = 5,
    ):
        position = Position(*position) if isinstance(position, tuple) else position
        super().__init__(
            id=id,
            position=position,
            speed=speed,
            acceleration=acceleration,
            steer_angle=steer_angle,
            radius=radius,
            width=width,
            height=height,
        )
