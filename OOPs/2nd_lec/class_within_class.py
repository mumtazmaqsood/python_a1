
#example instance as attribute --firt example is not classwithin class example
# in below exmple there is electric car class, ec also has battery attribute but if batter details
# are in ec car class then this car fills with battery information and also other classes cannot use this
# battery class, so we have made seperate Battery class, which we are not inheriting this battery class
# bcz battery class is not in relation with
class Electric_Car:
    def __init__(self, name, engine, capcity):
        self.name = name
        self.engine = engine
        self.capcity = capcity
        self.battery = Battery("Oska", "10", "5000w", "1000 DKK")
        #Battery class instance has been created and store in self.battery

class Battery:
    def __init__(self, man, cell, watts, price):
        self.man = man
        self.cell = cell
        self.watts = watts
        self.price = price

ec = Electric_Car("Tesla", "2000c", "5")
#accessing Electric car attributes by instance name ec.name or engine etc
#but if need to access Batter class then it will work with 2 steps ec.battery.price,man,cell or watts
print(ec.battery.price)
# -------------------------------------------------------------------

#another example instance as attribute
class Student:
    def __init__(self, name, rollno, brand, cpu, ram):
        self.name = name
        self.rollno = rollno
        self.laptop = Laptop(brand, cpu, ram)
        #instance as attribute

class Laptop:
    def __init__(self, brand, cpu, ram):
        self.brand = brand
        self.cpu = cpu
        self.ram = ram

st = Student("afnan", "123", "Lenvo", "i3", "8gb")
print(st.laptop.cpu)

#inner classes example, above example implementation by using inner classes

class Student1:
    def __init__(self, name, rollno, brand, cpu, ram):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop(brand, cpu, ram)
        #object/instance has been created Laptop class

    def show(self):
        print(f"{self.rollno}: {self.name}")
        self.laptop.show()
        #laptop.show is the inner class function which has been called here

    #inner class
    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        def show(self):
            print(f"{self.brand} {self.cpu} {self.ram}")
st1 = Student1("Zanib", "258", "HP", "i5", "8gb")
st1.show()


#---------------------------------------
#electric car example by using inner class
class Electric_Car1:
    def __init__(self, name, engine, capcity):
        self.name = name
        self.engine = engine
        self.capcity = capcity
        self.battery = self.Battery("Oska", "10", "5000w", "1000 DKK")
        #Battery class instance has been created and store in self.battery

    class Battery:
        def __init__(self, man, cell, watts, price):
            self.man = man
            self.cell = cell
            self.watts = watts
            self.price = price


ec1 = Electric_Car1("Nissan", "2000c", "5")









