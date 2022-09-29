
# Car class is build with brand, mode, transmission and engine attributes
# and start, stop and fueltank behaviour

class Car:
    def __init__(self, brand, model, transmission, engine):
        self.brand = brand
        self.model = model
        self.transmission = transmission
        self.engine = engine

    def start(self):
        print(f"{self.brand} {self.model} {self.transmission} {self.engine} is starting....")

    def stop(self):
        print(f"{self.brand} {self.model} {self.transmission} {self.engine} is stop....")

    def fuel_tank(self):
        print(f"{self.brand} {self.model} {self.transmission} {self.engine} is filling fuel tank....")


# creating objects
# car1 = Car("Honda", "City", "manual", "1600cc")
# car1.start()
# car1.stop()
# car1.fuel_tank()
# ------------------------------------------
# now going to make another class SportCar which almost have the same attributes
# behaviour as above Car class, now we ll inherit this Car class in our SportCar class and
# can access all its attributes and its behaviour
#         with the help of super, it takes 4 attributes to move to parent car

class Sport_Car(Car):
    def __init__(self,brand, model, transmission, engine, top_speed, seats):
        super().__init__(brand, model, transmission, engine)
        self.top_speed = top_speed
        self.seats = seats

    def current_speed(self):
        print(f"{self.brand} {self.model} {self.transmission} {self.engine} is moving with speed {self.top_speed}....")

# sp_car = Sport_Car("spoty", "civic", "auto", "3000c", "300km", "2")
# sp_car.current_speed()
