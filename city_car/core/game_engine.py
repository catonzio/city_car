from city_car.models import Car, Entity, Position

from .ui_state import UiState


class GameEngine:
    player: Car
    obstacles: list[Entity]

    def __init__(self):
        self.obstacles = []

    def initialize(self):
        self.player = Car(
            id=1, position=Position(x=50, y=50), width=20, height=10, speed=1
        )

    def close(self): ...

    def tick(self, time_delta: float, dx: float, dy: float, ui_state: UiState):
        fromm = self.player.position
        self.player.move(dx, dy)
        to = self.player.position
        self.player.speed = ui_state.slider_value
