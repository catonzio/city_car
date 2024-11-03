import json
from typing import Any

from pathlib import Path
from city_car.models import StreetTile, Obstacle


class Environment:
    street_tiles: list[StreetTile] = []
    obstacles: list[Obstacle] =  []

    def __init__(
        self,
        street_tiles: list[StreetTile] | None = None,
        obstacles: list[Obstacle] | None = None,
    ):
        self.street_tiles = street_tiles if street_tiles else []
        self.obstacles = obstacles if obstacles else []

    def build_obstacles(self):
        obstacles: list[Obstacle] = []
        self.obstacles.extend(obstacles)

    def build_street_tiles(self):
        street_tiles: list[StreetTile] = []
        self.street_tiles.extend(street_tiles)

    def to_json(self) -> dict[str, Any]:
        return {
            "street_tiles": [st.to_json() for st in self.street_tiles],
            "obstacles": [ob.to_json() for ob in self.obstacles],
        }

    def to_file(self, file_path: Path | str) -> None:
        json_repr: dict[str, Any] = self.to_json()

        with open(file_path, "w") as f:
            f.write(json.dumps(json_repr, indent=4))

    @staticmethod
    def from_json(json: dict[str, Any]) -> "Environment":
        return Environment(
            street_tiles=json.get("street_tiles", None),
            obstacles=json.get("obstacles", None),
        )
