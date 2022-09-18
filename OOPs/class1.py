
class Person:
    def __init__(self, fname, lname):
        print("init method called")
        self.fname = fname
        self.lname = lname

p1 = Person('Mumtaz', 'Maqsood')
print(p1.fname + p1.lname)
p2 = Person('Mumtaz1', 'Maqsood1')
print(p2.fname + p2.lname)
