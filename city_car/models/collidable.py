from dataclasses import dataclass
from typing import List

from .entity import Entity


@dataclass
class CollidableMixin(Entity):
    radius: float = 0.2

    def check_collision(self, other_entities: List[Entity]) -> bool:
        for entity in other_entities:
            if self.check_single_collision(entity):
                return True
        return False

    def check_single_collision(self, other: Entity) -> bool:
        if other == self:
            return False

        radius = (
            max(self.radius, other.radius)
            if isinstance(other, CollidableMixin)
            else self.radius
        )
        print(f"Collision {self=} -- {other=}, {radius=}")
        return self.position.equals(other.position, radius)
