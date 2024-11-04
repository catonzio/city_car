from pathlib import Path
import sys
from math import degrees

import pygame
from pygame import Surface
from pygame.event import Event
from pygame.font import Font

from city_car.configs.constants import ACCELERATION, HANDBRAKE, TURN_ANGLE
from city_car.core import Colors, GameEngine, Overlay, UiState
from city_car.core.car_keys_params import CarKeysParams
from city_car.models.car import Car
from city_car.models.position import Position


class Application:
    title: str
    game_engine: GameEngine
    overlay: Overlay
    screen_width: int
    screen_height: int
    screen: Surface
    font: Font

    def __init__(
        self,
        title: str,
        screen_width: int,
        screen_height: int,
        environ_file: Path | str,
    ):
        pygame.init()
        self.title = title
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_engine = GameEngine(environ_file)
        self.overlay = Overlay(self.screen_width, self.screen_height)
        self.screen_center: Position = Position(screen_width / 2, screen_height / 2)

    def initialize(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("City Car")
        self.game_engine.initialize()
        self.overlay.initialize()
        self.font = Font(None, 24)

    def close(self):
        self.game_engine.close()
        self.overlay.close()
        pygame.quit()
        sys.exit()

    def detect_keypress(self) -> CarKeysParams:
        acceleration, steer, handbrake, retro = 0, 0, 0, False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            steer -= TURN_ANGLE
        if keys[pygame.K_RIGHT]:
            steer += TURN_ANGLE
        if keys[pygame.K_UP]:
            acceleration += ACCELERATION
        if keys[pygame.K_DOWN]:
            handbrake += HANDBRAKE
        if keys[pygame.K_r]:
            retro = True

        # print(f"{acceleration=}, {steer=}, {handbrake=}, {retro=}")
        return CarKeysParams(
            acceleration=acceleration, steer=steer, handbrake=handbrake, retro=retro
        )

    def draw_grid(self):
        blockSize = 25  # Set the size of the grid block
        for x in range(0, self.screen_width, blockSize):
            for y in range(0, self.screen_height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, Colors.LGREY, rect, 1)
            #     if y == 100:
            #         break
            # if x == 100:
            #     break

    def draw(self, ui_state: UiState):
        # draw background
        self.screen.fill(Colors.GREEN)
        # draw grid
        # self.draw_grid()

        self.game_engine.draw(self.screen)

        # render the text
        player: Car = self.game_engine.player
        coordinates_text = self.font.render(
            f"{player.position}, s: {player.speed} speed: {player.speed.value:.3f} sa: {degrees(player.steer_angle):.3f}, retro: {player.retro:.1f}",
            True,
            Colors.DGREY,
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
            car_keys_params: CarKeysParams = self.detect_keypress()

            self.game_engine.tick(time_delta, car_keys_params)

            self.draw(ui_state)
