from dataclasses import dataclass

import pygame

from city_car.core.colors import Colors
from city_car.models.position import Position

from .entity import Entity


@dataclass
class Drawable(Entity):
    color: tuple[int, int, int] = Colors.WHITE

    def draw(self, screen: pygame.Surface, player_pos: Position):
        rect = self.to_rect()
        rect = rect[0] - player_pos.x, rect[1] - player_pos.y, *rect[2:]
        pygame.draw.rect(screen, self.color, rect)
