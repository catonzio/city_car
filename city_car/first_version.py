import pygame
import sys

import pygame_gui

from city_car.models import Car, Position

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Car")

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Square properties
square_size = 30
car = Car(id=1, position=Position(x=50, y=50), speed=5)

# Font for displaying coordinates
font = pygame.font.Font(None, 36)

# Pygame GUI manager
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# Slider for speed control
speed_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((10, SCREEN_HEIGHT - 50), (200, 30)),
    start_value=1,
    value_range=(1, 20),
    manager=manager,
)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(30) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Update GUI manager
        manager.process_events(event)

    manager.update(time_delta)

    # Get the speed from the slider and update car's speed
    car.speed = speed_slider.get_current_value()

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car.move(-car.speed, 0)
    if keys[pygame.K_RIGHT]:
        car.move(car.speed, 0)
    if keys[pygame.K_UP]:
        car.move(0, -car.speed)
    if keys[pygame.K_DOWN]:
        car.move(0, +car.speed)

    # Ensure the square stays within the screen bounds
    square_x = max(0, min(SCREEN_WIDTH - square_size, car.position.x))
    square_y = max(0, min(SCREEN_HEIGHT - square_size, car.position.y))

    # Fill the screen with green
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    manager.draw_ui(screen)

    # Display the coordinates
    coordinates_text = font.render(f"({square_x}, {square_y})", True, WHITE)
    screen.blit(coordinates_text, (10, 10))

    # Update the display
    pygame.display.flip()
    # pygame.time.Clock().tick(30)  # Limit the frame rate
