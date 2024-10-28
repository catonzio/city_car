from city_car.application import Application
from city_car.configs import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    application: Application = Application("City Car", SCREEN_WIDTH, SCREEN_HEIGHT)
    application.initialize()
    application.event_loop()
    application.close()


if __name__ == "__main__":
    main()
