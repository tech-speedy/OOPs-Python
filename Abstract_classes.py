#Abstract Class -> A class that cannot instantiated on its own; Meant to be subclasses.
#                  They can contain abstract methods, which are declared but have no implementation.
#                  Abstract Classes benefits:
#                  1. Prevents instantiation of the class itself
#                  2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")

motorcycle = Motorcycle()

motorcycle.go()
motorcycle.stop()
