#Inheritance in Python is a core concept of Object-Oriented Programming (OOP) that allows one class (called the child or subclass) to inherit attributes and methods from another class (called the parent or superclass).

#Parent Class: The base class that contains common attributes and methods.
#Child Class: The derived class that inherits from the parent class.
#Code Reusability: Inheritance promotes reuse of existing code
#super() function: Used to call methods from the parent class inside the child class.

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
