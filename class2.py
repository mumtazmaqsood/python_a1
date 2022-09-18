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