from dataclasses import Field, dataclass, field
from math import cos, pi, sin
from typing import Sequence
from xml.dom.minidom import Entity

from city_car.configs.constants import HANDBRAKE
from city_car.core.car_keys_params import CarKeysParams
from city_car.models.vector import Vector

from .collidable import CollidableMixin
from .position import Position


@dataclass
class MovableMixin(CollidableMixin):
    speed: Vector = field(default_factory=Vector.zero)  # m/s
    steer_angle: float = pi / 2  # in radians -- [0, pi]
    retro: bool = False

    def move(
        self,
        dt: float,
        car_key_params: CarKeysParams,
        obstacles: Sequence[CollidableMixin] | None = None,
    ):
        if car_key_params.retro and abs(self.speed.value) < 0.2:
            self.retro = not self.retro

        self.steer_angle += car_key_params.steer
        self.steer_angle %= 2 * pi

        if car_key_params.acceleration > 0:
            # Update speed magnitude based on car_key_params.delta_acceleration
            da: float = car_key_params.acceleration * dt
            self.speed.value = self.speed.value + (da if not self.retro else -da)
        if car_key_params.handbrake > 0:
            if abs(self.speed.value) < HANDBRAKE:
                self.speed.value = 0
            else:
                da: float = car_key_params.handbrake * dt
                self.speed.value = self.speed.value - (da if not self.retro else -da)

        # Update direction to steer the car without altering the speed magnitude
        self.speed.direction = Position(
            self.speed.value * cos(self.steer_angle),
            self.speed.value * sin(self.steer_angle),
        )

        dp = self.speed.direction * dt
        self.position += dp

        if obstacles:
            if self.check_collision(obstacles):
                print(f"Before: {self.position=} {self.speed=}")
                self.position -= dp
                self.speed.set_direction((0, 0))
                print(f"After: {self.position=} {self.speed=}")
