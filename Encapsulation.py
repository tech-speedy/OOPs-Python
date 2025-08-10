#Encapsulation -> It is one of the key features of object oriented programming.
#                 Encapsulation refers to the bundling of attributes and methods inside a single class.
#                 It prvents outer class from accessing and changing attributes and methods of a class.
#                 This also helps to achieve data hiding.

#                 we denote private attributes using underscore as the prefix i.e. single (_) or double(__)

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

comp1 = Computer()
comp1.sell()

comp1.setMaxPrice(1000)
comp1.sell()
