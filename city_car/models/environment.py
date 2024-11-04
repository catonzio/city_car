import json
from typing import Any

from pathlib import Path
from city_car.models import StreetTile, Obstacle
from city_car.models.drawable import Drawable


class Environment:
    street_tiles: list[StreetTile] = []
    obstacles: list[Obstacle] = []

    def __init__(
        self,
        street_tiles: list[StreetTile] | None = None,
        obstacles: list[Obstacle] | None = None,
    ):
        self.street_tiles = street_tiles if street_tiles else []
        self.obstacles = obstacles if obstacles else []

    def get_all(self) -> list[Drawable]:
        result: list[Drawable] = []
        result.extend(self.street_tiles)
        result.extend(self.obstacles)
        return result

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
        street_tiles: list | None = json.get("street_tiles", None)
        obstacles: list | None = json.get("obstacles", None)

        return Environment(
            street_tiles=[StreetTile.from_json(st) for st in street_tiles]
            if street_tiles
            else None,
            obstacles=[Obstacle.from_json(st) for st in obstacles]
            if obstacles
            else None,
        )

    @staticmethod
    def from_file(file_path: Path | str) -> "Environment":
        with open(file_path, "r") as f:
            json_repr: dict[str, Any] = json.load(f)
        return Environment.from_json(json_repr)
