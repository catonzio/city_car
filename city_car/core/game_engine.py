from pygame import Surface

from city_car.core.colors import Colors
from city_car.models import Car, Obstacle, Position

from .car_keys_params import CarKeysParams


class GameEngine:
    player: Car
    obstacles: list[Obstacle]

    def __init__(self):
        self.obstacles = []

    def initialize(self):
        self.player = Car(
            id=1,
            position=Position(x=250, y=250),
            width=40,
            height=20,
            steer_angle=0,
            color=Colors.RED,
        )
        self.obstacles.extend(
            [
                Obstacle(
                    2,
                    position=Position(100, 100),
                    width=30,
                    height=20,
                    color=Colors.BLUE,
                ),
                Obstacle(
                    3,
                    position=Position(700, 500),
                    width=30,
                    height=20,
                    color=Colors.BLUE,
                ),
                Obstacle(
                    4,
                    position=Position(100, 500),
                    width=30,
                    height=20,
                    color=Colors.BLUE,
                ),
                Obstacle(
                    5,
                    position=Position(700, 100),
                    width=30,
                    height=20,
                    color=Colors.BLUE,
                ),
            ]
        )

    def close(self): ...

    def tick(self, time_delta: float, car_key_params: CarKeysParams):
        self.player.move(
            time_delta, car_key_params.delta_acceleration, car_key_params.delta_steer
        )

    def draw(self, screen: Surface):
        self.player.draw(screen)

        for obstacle in self.obstacles:
            obstacle.draw(screen, self.player.position)
