from dataclasses import dataclass

from city_car.models.collidable import CollidableMixin
from city_car.models.drawable import Drawable


@dataclass
class Obstacle(CollidableMixin, Drawable):
    pass
