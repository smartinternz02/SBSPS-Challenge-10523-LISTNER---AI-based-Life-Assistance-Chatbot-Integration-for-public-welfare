from sensors import SoilMoistureSensor, WeatherStation, TemperatureHumiditySensor, CropHealthSensor
from drones import Drone
from farm import Farm
from ai_assistant import AIAssistant

if __name__ == "__main__":
    farm = Farm()
    soil_sensor = SoilMoistureSensor("SoilSensor1")
    weather_station = WeatherStation("WeatherStation1")
    drone = Drone("Drone1")

    farm.add_sensor(soil_sensor)
    farm.add_sensor(weather_station)
    farm.add_drone(drone)

    assistant = AIAssistant(farm)

    # Simulate the components in action
    soil_moisture_data = soil_sensor.measure()
    weather_data = weather_station.measure()
    drone.fly()
    drone_capture = drone.capture_imagery()

    assistant.analyze_data(soil_moisture_data, weather_data, drone_capture)
    assistant.control_irrigation()
    assistant.detect_pests_and_diseases()
    assistant.automate_harvesting()
