from dataclasses import dataclass
import pygame

from city_car.core.colors import Colors
from .entity import Entity


@dataclass
class Drawable(Entity):
    color: tuple[int, int, int] = Colors.WHITE

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.to_rect())
