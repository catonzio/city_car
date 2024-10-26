from dataclasses import dataclass
import sys
from pygame import Surface, Rect, Event
import pygame
from city_car.models import Car, Entity, Position
from pygame.font import Font
from pygame_gui import UIManager
from pygame_gui.core import UIElement
from pygame_gui.elements import UIHorizontalSlider


@dataclass
class UiState:
    slider_value: float = 0


class Colors:
    RED = (83, 0, 0)
    GREEN = (35, 101, 51)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)


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


class Overlay:
    screen_width: int
    screen_height: int
    elements: dict[str, UIElement]
    gui_manager: UIManager
    state: UiState

    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.elements = {}
        self.gui_manager = UIManager((self.screen_width, self.screen_height))
        self.state = UiState()

    def initialize(self):
        speed_slider = UIHorizontalSlider(
            relative_rect=Rect((10, self.screen_height - 50), (200, 30)),
            start_value=1,
            value_range=(1, 20),
            manager=self.gui_manager,
        )
        self.elements["speed_slider"] = speed_slider

    def close(self): ...

    def update(self, time_delta: float, events: list[Event]) -> UiState:
        for event in events:
            self.gui_manager.process_events(event)
        self.gui_manager.update(time_delta)
        self.state.slider_value = self.elements["speed_slider"].get_current_value()  # type: ignore

        return self.state


class Application:
    title: str
    game_engine: GameEngine
    overlay: Overlay
    screen_width: int
    screen_height: int
    screen: Surface
    font: Font

    def __init__(self, title: str, screen_width: int, screen_height: int):
        pygame.init()
        self.title = title
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_engine = GameEngine()
        self.overlay = Overlay(self.screen_width, self.screen_height)

    def initialize(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("City Car")
        self.game_engine.initialize()
        self.overlay.initialize()
        self.font = Font(None, 36)

    def close(self):
        self.game_engine.close()
        self.overlay.close()
        pygame.quit()
        sys.exit()

    def detect_keypress(self) -> tuple[float, float]:
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1
        return dx, dy

    def draw(self, ui_state: UiState):
        self.screen.fill(Colors.GREEN)
        pygame.draw.rect(self.screen, Colors.RED, self.game_engine.player.to_rect())
        (x, y), speed = (
            self.game_engine.player.position.to_tuple(),
            ui_state.slider_value,
        )
        coordinates_text = self.font.render(
            f"({x=}, {y=}), {speed=}", True, Colors.WHITE
        )
        self.overlay.gui_manager.draw_ui(self.screen)
        self.screen.blit(coordinates_text, (10, 10))

        # Update the display
        pygame.display.flip()

    def event_loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            time_delta: float = clock.tick(30) / 1000.0
            events: list[Event] = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
                events.append(event)

            ui_state: UiState = self.overlay.update(time_delta, events)
            dx, dy = self.detect_keypress()

            self.game_engine.tick(time_delta, dx, dy, ui_state)

            self.draw(ui_state)
