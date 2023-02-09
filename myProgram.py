class vehicle:
    pass
class vehicle:
    engine_capcity = "1,6 Turbo"

class vehicle:
    def __init__(self, number_of_wheels, types_of_tanks, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.types_of_tanks = types_of_tanks
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    def drive(self):
        print("The vehicle is in driving mode now.")
        print("electric")
vios = vehicle('4', 'petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.types_of_tanks)
print(vios.seating_capacity)
print(vios.maximum_velocity)

vios.drive()