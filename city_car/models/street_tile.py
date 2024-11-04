from dataclasses import dataclass, field
from typing import Any

from pygame import Surface
from city_car.models.drawable import Drawable
from city_car.models.position import Position


@dataclass
class Strip(Drawable):
    def draw(self, screen: Surface, player_pos: Position):
        super().draw(screen, player_pos)

    @staticmethod
    def from_json(json: dict[str, Any]) -> "StreetTile":
        parent: Drawable = Drawable.from_json(json)

        return StreetTile(
            id=parent.id,
            position=parent.position,
            width=parent.width,
            height=parent.height,
            radius=parent.radius,
            color=parent.color,
        )


@dataclass
class StreetTile(Drawable):
    strips: list[Strip] = field(default_factory=list)

    def __post_init__(self):
        # TODO add strips initialization
        pass

    def draw(self, screen: Surface, player_pos: Position):
        super().draw(screen, player_pos)

        for strip in self.strips:
            strip.draw(screen, player_pos)

    def to_json(self) -> dict[str, Any]:
        parent: dict[str, Any] = super().to_json()
        parent["strips"] = [s.to_json() for s in self.strips]
        return parent

    @staticmethod
    def from_json(json: dict[str, Any]) -> "StreetTile":
        parent: Drawable = Drawable.from_json(json)

        return StreetTile(
            id=parent.id,
            position=parent.position,
            width=parent.width,
            height=parent.height,
            radius=parent.radius,
            color=parent.color,
        )
