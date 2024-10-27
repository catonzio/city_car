from dataclasses import Field, dataclass, field
from math import cos, pi, sin

from city_car.models.vector import Vector

from .collidable import CollidableMixin
from .position import Position


@dataclass
class MovableMixin(CollidableMixin):
    speed: Vector = field(default_factory=Vector.zero)  # m/s
    # acceleration: Vector = Vector.zero()  # m/s**2
    steer_angle: float = pi / 2  # in radians -- [0, pi]

    def move(self, dt: float, delta_acc: float, delta_steer: float):
        self.steer_angle += delta_steer
        self.steer_angle %= 2 * pi

        if delta_acc != 0:
            # Update speed magnitude based on delta_acc
            self.speed.value += delta_acc * dt

        # Update direction to steer the car without altering the speed magnitude
        self.speed.direction = Position(
            self.speed.value * cos(self.steer_angle), self.speed.value * sin(self.steer_angle)
        )

        self.position += self.speed.direction * dt
