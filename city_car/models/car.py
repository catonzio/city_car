from dataclasses import dataclass, field
from math import atan2, degrees, pi

import pygame
from pygame import SRCALPHA, Surface

from city_car.core.colors import Colors
from city_car.models.drawable import Drawable
from city_car.models.vector import Vector

from .movable import MovableMixin
from .position import Position


@dataclass
class Car(MovableMixin, Drawable):
    pass

    def __init__(
        self,
        id: int,
        position: Position | tuple[float, float],
        speed: Vector = Vector.zero(),
        steer_angle: float = pi / 2,
        radius: float = 0.2,
        width: float = 5,
        height: float = 5,
        color: tuple[int, int, int] = Colors.WHITE,
    ):
        position = Position(*position) if isinstance(position, tuple) else position
        MovableMixin.__init__(
            self,
            id=id,
            position=position,
            speed=speed,
            steer_angle=steer_angle,
            radius=radius,
            width=width,
            height=height,
        )
        Drawable.__init__(
            self, id=id, position=position, width=width, height=height, color=color
        )

    def draw(self, screen: Surface):
        # pygame.draw.rect(screen, self.color, self.to_rect())
        temp_surface = Surface((self.height, self.width), SRCALPHA)
        temp_surface.fill(self.color)

        rotated = pygame.transform.rotate(temp_surface, degrees(self.speed.angle()))

        x, y = screen.size
        pos = Position(x / 2, y / 2)
        new_rect = rotated.get_rect(center=pos.to_tuple())
        screen.blit(rotated, new_rect.topleft)

        end_line_pos = pos + self.speed.normalize() * 20
        pygame.draw.line(screen, Colors.CYAN, pos.to_tuple(), end_line_pos.to_tuple())
