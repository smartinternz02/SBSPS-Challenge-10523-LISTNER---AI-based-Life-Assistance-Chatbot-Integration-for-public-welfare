import random


class Sensor:
    def __init__(self, name):
        self.name = name

    def measure(self):
        pass


class SoilMoistureSensor(Sensor):
    def measure(self):
        # Simulate soil moisture measurement
        return random.uniform(0, 100)


class WeatherStation(Sensor):
    def measure(self):
        # Simulate weather data collection
        return {
            "temperature": random.uniform(0, 40),
            "humidity": random.uniform(0, 100),
            "wind_speed": random.uniform(0, 20),
        }


class TemperatureHumiditySensor(Sensor):
    def measure(self):
        # Simulate temperature and humidity measurement
        return {
            "temperature": random.uniform(0, 40),
            "humidity": random.uniform(0, 100),
        }


class CropHealthSensor(Sensor):
    def measure(self):
        # Simulate crop health measurement
        return "Healthy"
