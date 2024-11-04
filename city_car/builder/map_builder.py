from pathlib import Path
from city_car.configs.constants import CENTER_H, CENTER_W
from city_car.core.colors import Colors
from city_car.models import Obstacle, StreetTile, Environment
from city_car.models.position import Position
from city_car.configs import MAPS_PATH


class MapBuilder:
    environment: Environment

    def __init__(self):
        self.environment = Environment()

    def build(self):
        self.build_obstacles()
        self.build_street_tiles()

    def build_obstacles(self):
        obstacles: list[Obstacle] = [
            Obstacle(
                id=i,
                width=300,
                height=100,
                position=Position(x=(i * 300) + CENTER_W, y=CENTER_H + 200),
                color=Colors.BLUE,
            )
            for i in range(-10, 10)
        ]
        self.environment.obstacles.extend(obstacles)

    def build_street_tiles(self):
        street_tiles: list[StreetTile] = [
            StreetTile(
                id=i,
                width=100,
                height=100,
                position=Position(x=(i * 100) + CENTER_W, y=CENTER_H),
                color=Colors.LGREY,
                radius=0,
            )
            for i in range(-10, 10)
        ]
        self.environment.street_tiles.extend(street_tiles)

    def to_file(self, file_path: Path | str) -> None:
        self.environment.to_file(file_path)


if __name__ == "__main__":
    map_builder = MapBuilder()
    map_builder.build()

    map_builder.to_file(MAPS_PATH / "map1.json")
