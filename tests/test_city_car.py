import pytest
from city_car.models import Position, Car, Entity


# Sample Test Data
@pytest.fixture
def car():
    return Car(id=1, position=(0, 0), speed=5)


@pytest.fixture
def other_car():
    return Car(id=2, position=(5, 5), speed=5)


@pytest.fixture
def obstacle():
    return Entity(id=3, position=(3, 3))


@pytest.fixture
def fat_car():
    return Car(id=3, position=(10, 10), radius=6)


def test_car_initial_position(car):
    assert car.position == Position(0, 0)


def test_car_move(car):
    car.move(1, 1)  # Move diagonally
    assert car.position.x == 5
    assert car.position.y == 5


def test_car_collision_with_another_car(car, other_car):
    assert not car.check_collision([other_car])  # Initially no collision
    car.position = Position(5, 5)  # Set position to collide
    assert car.check_collision([other_car])  # Should detect collision now


def test_car_collision_with_obstacle(car, obstacle):
    assert not car.check_collision([obstacle])  # Initially no collision
    obstacle.position = Position(5, 5)  # Move obstacle to the car's position
    car.position = Position(5, 5)  # Set car's position to collide
    assert car.check_collision([obstacle])  # Should detect collision now


def test_car_speed(car):
    car.move(1, 0)  # Move horizontally
    assert car.position.x == 5
    assert car.position.y == 0  # Since only horizontal movement was made


def test_car_collision_with_fatcar(car, fat_car):
    car.speed = 1
    car.move(6, 6)
    assert car.check_collision([fat_car])
    car.move(-2, -2)
    assert not car.check_collision([fat_car])
