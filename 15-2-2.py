from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Езда на автомобиле")

class Motorcycle(Vehicle):
    def go(self):
        print("Езда на мотоцикле")

def go_temp(vehicle):
    vehicle.go()

car = Car()
motorcycle = Motorcycle()

go_temp(car)         # Выводит "Езда на автомобиле"
go_temp(motorcycle)  # Выводит "Езда на мотоцикле"

for t_v in (car, motorcycle):
    t_v.go()