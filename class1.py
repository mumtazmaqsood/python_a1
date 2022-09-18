
#github login token 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
class Patient:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age


p1 = Patient('mumtaz', '30')

# TRY IT YOURSELF
# 9-1 Restaurant
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describle_restaurant(self):
#         print(f"Restaurant Name:{self.restaurant_name} and {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open!")
#
# restaurant = Restaurant("Flames", "Pakistani")
# restaurant1 = Restaurant("Hilton", "English")
# restaurant2 = Restaurant("Tivoli", "Danish")
# restaurant.describle_restaurant()
# restaurant.open_restaurant()
# restaurant1.describle_restaurant()
# restaurant2.describle_restaurant()


# 9-3   Users
class User:
    def __init__(self, fname, lname, age, edu):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.edu = edu

    def describle_user(self):
        print(f"User Name:{self.fname} {self.lname}"
              f"Age:{self.age}"
              f"Education:{self.edu}")
    def greet_user(self):
        print(f"Hello {self.lname} {self.fname}")

user_obj = User("Mumtaz","Maqsood", "44", "M.Sc")
user_obj1 = User("Fadia","Shafiq", "40", "M.A")
user_obj2 = User("Gul","Andam", "11", "4.th")
user_obj3 = User("Shahbaz","Maqsood", "8", "1")

user_obj.greet_user()
user_obj1.greet_user()
user_obj2.greet_user()
user_obj3.greet_user()


class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.meter = 1000
    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def get_meter(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.meter} miles on it.")
    def update_meter(self, new_milage):
        """this method update the meter value"""
        # putting the logic that nobody can decrees the meter value
        if new_milage >= self.meter:
            self.meter = new_milage
        else:
            print("You cannot change the meter reading")
    def increment_meter(self, miles):
        """Add the given amount to the meter reading."""
        self.meter += miles



car = Cars("BMW", "a4", "2022")
print("----------------------")
print(car.get_descriptive_name())
# car.get_meter()
car.update_meter(2000)
car.get_meter()
car.increment_meter(100)
print("meter reading applied after increment_meter method \n")
car.get_meter()
# -------------------------------------------------------------------------

# TRY IT YOUSERLF
# 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.no_served = 10

    def describle_restaurant(self):
        print(f"Restaurant Name:{self.restaurant_name} , {self.cuisine_type}, Guest served:{self.no_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_servered(self, no_served):
        # set the no_served value in __init()__ method
        self.no_served = no_served

    def increment_no_servered(self, new_served):
        self.no_served += new_served


restaurant = Restaurant("Flames", "Pakistani")
restaurant1 = Restaurant("Hilton", "English")
restaurant2 = Restaurant("Tivoli", "Danish")


# restaurant.no_served = 40
restaurant.set_number_servered(30)
restaurant.describle_restaurant()
restaurant.increment_no_servered(500)
restaurant.describle_restaurant()
restaurant.open_restaurant()


restaurant1.describle_restaurant()

restaurant2.set_number_servered(100)
restaurant2.describle_restaurant()







