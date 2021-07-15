class Car:
    numberOfWheels = 4
    _color = "Black"
    __yearOfManufacture = 2017
class BMW(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)


car = Car()
print("Public Attribute numberOfWheels: ", car.numberOfWheels)
bmw = BMW()
print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)
