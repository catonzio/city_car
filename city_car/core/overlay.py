from pygame import Rect
from pygame.event import Event
from pygame_gui import UIManager
from pygame_gui.core import UIElement
from pygame_gui.elements import UIHorizontalSlider

from .ui_state import UiState


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
