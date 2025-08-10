#A class is a blueprint for creating objects (instances). It defines the properties (data/attributes) and behaviors (methods/functions) of an object.

class Computer:

    def config(self):
        print("i5, 8gb, 1TB")

#An object is an instance of a class. It has actual values for the attributes and can use the methods defined in the class.

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()
