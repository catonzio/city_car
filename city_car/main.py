from city_car.application import Application
from city_car.configs import SCREEN_HEIGHT, SCREEN_WIDTH
from city_car.configs.folders import MAPS_PATH


def main():
    environ_file = MAPS_PATH / "map1.json"
    application: Application = Application(
        "City Car", SCREEN_WIDTH, SCREEN_HEIGHT, environ_file
    )
    application.initialize()
    application.event_loop()
    application.close()


if __name__ == "__main__":
    main()
