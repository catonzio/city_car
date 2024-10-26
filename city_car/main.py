from city_car.application import Application

if __name__ == "__main__":
    application: Application = Application("City Car", 800, 600)
    application.initialize()
    application.event_loop()
    application.close()
