#going to import inheritiance_class1 class Car
#and then create electric car

from inheritance_class1 import Car

#Electric_Car class has been created and also it inherits Car class attributes and behaviours
#also ec has its own attribute battery and behaviour charging_battery
class Electric_Car(Car):
    def __init__(self,brand, model, transmission, engine, battery):
        super().__init__(brand, model, transmission, engine)
        self.battery = battery

    def charging_battery(self):
        print(f"{self.brand} {self.model} {self.transmission} {self.engine} is charging battery {self.battery}....")
    def fuel_tank(self):
        print("Electric cars has not fuel tank")

ec = Electric_Car("Tesla", "t1", "Auto", "2000cc", "Exide")
ec.charging_battery()
#ec object also inherit fueltank method in Cars class
#this is wrong bcz electric cars has not fuel tank, so this function is going to redefine in child class
#when this methods implmentation, redefine in child class --> that is called method overiding
ec.fuel_tank()