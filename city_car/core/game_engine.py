from pathlib import Path
from pygame import Surface

from city_car.configs.constants import SCREEN_CENTER
from city_car.core.colors import Colors
from city_car.models import Car, Position
from city_car.models.environment import Environment

from .car_keys_params import CarKeysParams


class GameEngine:
    player: Car
    environment: Environment

    def __init__(self, environ_file: Path | str):
        self.environment = Environment.from_file(environ_file)

    def initialize(self):
        self.player = Car(
            id=1,
            position=Position(*SCREEN_CENTER),
            width=40,
            height=20,
            steer_angle=0,
            color=Colors.RED,
        )

    def close(self): ...

    def tick(self, time_delta: float, car_key_params: CarKeysParams):
        self.player.move(time_delta, car_key_params, self.environment.obstacles)

    def draw(self, screen: Surface):
        for drawable in self.environment.get_all():
            drawable.draw(screen, self.player.position)

        self.player.draw(screen)
