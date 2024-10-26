from dataclasses import dataclass
from math import pi

from .collidable import CollidableMixin
from .position import Position


@dataclass
class MovableMixin(CollidableMixin):
    speed: float = 0  # m/s
    acceleration: float = 0  # m/s**2
    steer_angle: float = pi / 2  # in radians -- [0, pi]

    def move(self, dx: float, dy: float, ref_sys: Position | None = None):
        ref_sys = ref_sys if ref_sys else Position(0, 0)
        self.position.x += dx * self.speed
        self.position.y += dy * self.speed
