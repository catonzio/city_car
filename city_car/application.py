import sys

import pygame
from pygame import Surface
from pygame.event import Event
from pygame.font import Font

from city_car.core import Colors, GameEngine, Overlay, UiState


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
