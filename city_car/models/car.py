from dataclasses import dataclass
from math import pi

from .movable import MovableMixin
from .position import Position


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
