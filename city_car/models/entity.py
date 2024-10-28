from dataclasses import dataclass, field

from .position import Position


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
        tl_x = self.position.x - self.width / 2 - offset.x / 2
        tl_y = self.position.y - self.height / 2 - offset.y / 2
        return tl_x, tl_y, self.width, self.height
