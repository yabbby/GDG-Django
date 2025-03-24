class Vehicle:
    def __init__(self, make, model):
        self._make = make  # Encapsulated attribute
        self._model = model  # Encapsulated attribute

    def describe(self):
        return f"Vehicle Make: {self._make}, Model: {self._model}"


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self._num_doors = num_doors  # Encapsulated attribute

    def describe(self):
        return f"Car Make: {self._make}, Model: {self._model}, Number of Doors: {self._num_doors}"


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def describe(self):
        return f"Bike Make: {self._make}, Model: {self._model}"


# Demonstration of polymorphism
def vehicle_description(vehicle):
    print(vehicle.describe())


# Example Usage
car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "MT-07")

vehicle_description(car)  # Output: Car Make: Toyota, Model: Camry, Number of Doors: 4
vehicle_description(bike)  # Output: Bike Make: Yamaha, Model: MT-07