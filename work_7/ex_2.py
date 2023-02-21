class Road:
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
    def asphalt_mass(self, asphalt_mass_for_1m2 = 25, asphalt_thickness = 0.05):
        return self._length * self._width * asphalt_mass_for_1m2 * asphalt_thickness
road1 = Road(20, 5000)
road2 = Road(15, 14000)
print(f"{road1.asphalt_mass()} кг. или {road1.asphalt_mass() / 1000} т.")
print(f"{road2.asphalt_mass()} кг. или {road2.asphalt_mass() / 1000} т.")
    