from dataclasses import dataclass
from math import atan2, degrees, pi

from pygame import SRCALPHA, Surface
import pygame

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

        rotated = pygame.transform.rotate(temp_surface, -degrees(self.speed.angle()))

        new_rect = rotated.get_rect(center=self.to_rect()[:2])
        screen.blit(rotated, new_rect.topleft)

        end_line_pos = self.position + self.speed.normalize() * 3
        pygame.draw.line(
            screen, Colors.CYAN, self.position.to_tuple(), end_line_pos.to_tuple()
        )
