from dataclasses import dataclass

from .position import Position


@dataclass
class Entity:
    id: int = 0
    position: Position = Position.zero()
    width: float = 0
    height: float = 0

    def __init__(
        self,
        id: int,
        position: Position | tuple[float, float] = Position.zero(),
        width: float = 0,
        height: float = 0,
    ):
        self.id = id
        self.position = Position(*position) if isinstance(position, tuple) else position
        self.width = width
        self.height = height

    def to_rect(self) -> tuple[float, float, float, float]:
        tl_x = self.position.x - self.width / 2
        tl_y = self.position.y - self.height / 2
        return tl_x, tl_y, self.width, self.height
