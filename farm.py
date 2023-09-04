class Farm:
    def __init__(self):
        self.sensors = []
        self.drones = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_drone(self, drone):
        self.drones.append(drone)
