def with_alpha(
    color: tuple[int, int, int], alpha: int = 255
) -> tuple[int, int, int, int]:
    return (*color, alpha)


class Colors:
    RED = (83, 0, 0)
    GREEN = (35, 101, 51)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    LGREY = (107, 107, 107)
    DGREY = (36, 36, 36)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
