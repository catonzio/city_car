from dataclasses import dataclass, field

from city_car.configs.constants import SCREEN_HEIGHT, SCREEN_WIDTH

from .position import Position


def to_relative(position: Position, player_position: Position) -> Position:
    return Position(
        position.x - player_position.x + SCREEN_WIDTH / 2,
        position.y - player_position.y + SCREEN_HEIGHT / 2,
    )


@dataclass
class Entity:
    id: int = 0
    position: Position = field(default_factory=Position.zero)
    width: float = 0
    height: float = 0
    radius: float = 20

    def __init__(
        self,
        id: int,
        position: Position | tuple[float, float] = Position.zero(),
        width: float = 0,
        height: float = 0,
        radius: float = 10,
    ):
        self.id = id
        self.position = Position(*position) if isinstance(position, tuple) else position
        self.width = width
        self.height = height
        self.radius = radius

    def to_rect(
        self, offset: Position | None = None
    ) -> tuple[float, float, float, float]:
        offset = offset if offset else Position.zero()
        relative: Position = to_relative(self.position, offset)
        tl_x = relative.x - self.width / 2
        tl_y = relative.y - self.height / 2
        return tl_x, tl_y, self.width, self.height
