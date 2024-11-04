from dataclasses import dataclass
from typing import Any

from city_car.models.collidable import CollidableMixin
from city_car.models.drawable import Drawable


@dataclass
class Obstacle(CollidableMixin, Drawable):
    @staticmethod
    def from_json(json: dict[str, Any]) -> "Obstacle":
        parent: Drawable = Drawable.from_json(json)

        return Obstacle(
            id=parent.id,
            position=parent.position,
            width=parent.width,
            height=parent.height,
            radius=parent.radius,
            color=parent.color,
        )
