#abstract is not support by python in order to use abstract concept
#need to use abc module
#in abstract class , only methods are created but their implmentation will be in child class through polymorshism
#all the abstract methods implementation mush have to created in child class otherwise there will be a problem
#and also object of the abstract class cannot be created

#abc module need to import to implement the abstraction
from abc import ABC, abstractmethod

# this is abstract class, cannot create its obj and also there is not methods implementation
class Computer(ABC):
    #abstract method
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def greet(self):
        pass

# try to create obj of Computer class --> it will show error
# obj_comp = Computer()
class Laptop(Computer):
    #through polymorshism abstract class methods' implementation is created here
    def process(self):
        print("It is running..")
    def greet(self):
        print("Hello .....")

laptop_obj = Laptop()
laptop_obj.process()
laptop_obj.greet()
#-------------------------------------------------
# another example
class Cars(ABC):
    @abstractmethod
    def mileage(self):
        pass
#abstract class methods implementation
class Tesla(Cars):
    def mileage(self):
        print("Tesla mileage:400 km")
class VW(Cars):
    def mileage(self):
        print("VW mileage:250 km")
class Nissan(Cars):
    def mileage(self):
        print("Nissan mileage:300 km")
class Hona(Cars):
    def mileage(self):
        print("Honda mileage:200 km")

tesla_obj = Tesla()
vw_obj = VW()
nissan_obj = Nissan()
hona_obj = Hona()
# mileage method is define in abstract class but its implementation is different class, thorugh polymorhism
tesla_obj.mileage()
vw_obj.mileage()
nissan_obj.mileage()
hona_obj.mileage()

# another example
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):print("Triangle has 3 sides")
class Pentagon(Polygon):
    def sides(self):print("Pentagon has 5 sides")
class Haxagon(Polygon):
    def sides(self): print("Haxagon has 6 sides")

t_obj = Triangle()
p_obj = Pentagon()
h_obj = Haxagon()
t_obj.sides()
p_obj.sides()
h_obj.sides()








