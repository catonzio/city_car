from dataclasses import dataclass
from math import cos, pi, sin

from city_car.models.vector import Vector

from .collidable import CollidableMixin
from .position import Position


@dataclass
class MovableMixin(CollidableMixin):
    speed: Vector = Vector.zero()  # m/s
    # acceleration: Vector = Vector.zero()  # m/s**2
    steer_angle: float = pi / 2  # in radians -- [0, pi]

    def move(self, dt: float, delta_acc: float, delta_steer: float):
        self.steer_angle += delta_steer
        self.steer_angle %= 2 * pi
        # delta_accel: Vector = Vector.zero()
        # delta_accel.update(
        #     (delta_acc * cos(self.steer_angle), delta_acc * sin(self.steer_angle))
        # )
        # self.acceleration = delta_accel

        # self.acceleration.update(delta_accel.direction)
        self.speed.update(
            (
                delta_acc * cos(self.steer_angle) * dt,
                delta_acc * sin(self.steer_angle) * dt,
            )
        )

        self.position += self.speed.direction * dt
