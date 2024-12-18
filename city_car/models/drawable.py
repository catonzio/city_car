from dataclasses import dataclass
from typing import Any

import pygame

from city_car.core.colors import Colors
from city_car.models.position import Position

from .entity import Entity


@dataclass
class Drawable(Entity):
    color: tuple[int, int, int] = Colors.WHITE

    def draw(self, screen: pygame.Surface, player_pos: Position):
        rect = self.to_rect(offset=player_pos)

        # if (abs(rel_pos.x) <= SCREEN_WIDTH / 2) and (
        #     abs(rel_pos.y) <= SCREEN_HEIGHT / 2
        # ):

        pygame.draw.rect(screen, self.color, rect)
        # draw_circle_alpha(
        #     screen,
        #     with_alpha(Colors.WHITE, 128),
        #     (rel_pos + (self.width / 2, self.height / 2)).to_tuple(),
        #     self.radius,
        # )

    def to_json(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "height": self.height,
            "width": self.width,
            "color": self.color,
            "position": self.position.to_json(),
            "radius": self.radius,
        }

    @staticmethod
    def from_json(json: dict[str, Any]) -> "Drawable":
        return Drawable(
            id=json["id"],
            height=json["height"],
            width=json["width"],
            color=json["color"],
            position=Position.from_json(json["position"]),
            radius=json["radius"],
        )


def draw_circle_alpha(
    surface: pygame.Surface,
    color: pygame.color.Color | tuple,
    center: tuple[float, float],
    radius: float,
):
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.circle(shape_surf, color, (radius, radius), radius)
    surface.blit(shape_surf, target_rect)
