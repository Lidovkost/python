class NotNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]
       
    def __set__(self, instance, value):
        try:
            if value < 0:
                raise ValueError   
            instance.__dict__[self.my_attr] = value
        except ValueError:
            print(f"нельзя присвоить отрицалельное значение")

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr
        
class Road:
    _length = NotNegative()
    _width = NotNegative()
    asphalt_mass_for_1m2 = NotNegative()
    asphalt_thickness = NotNegative()
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)
        self.asphalt_mass_for_1m2 = 25
        self.asphalt_thickness = 0.05
    def asphalt_mass(self):
         """Return the mass asphalt of the road."""
         return self._length * self._width * self.asphalt_mass_for_1m2 * self.asphalt_thickness

road1 = Road(1, 5000)
road2 = Road(15, 14000)
print(f"{road1.asphalt_mass()} кг. или {road1.asphalt_mass() / 1000} т.")
print(f"{road2.asphalt_mass()} кг. или {road2.asphalt_mass() / 1000} т.")