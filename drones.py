class Drone:
    def __init__(self, name):
        self.name = name

    def fly(self):
        # Simulate drone flight
        print(f"{self.name} is flying")

    def capture_imagery(self):
        # Simulate image capture
        print(f"{self.name} captured imagery")
        return "Imagery data"
