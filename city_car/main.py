from city_car.application import Application


def main():
    application: Application = Application("City Car", 800, 600)
    application.initialize()
    application.event_loop()
    application.close()


if __name__ == "__main__":
    main()
