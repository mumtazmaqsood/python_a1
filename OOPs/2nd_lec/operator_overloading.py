
#example of operator overloading
#adding two objects

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        st = Student(m1, m2)
        return st
    #operator orverloading greater than method
    def __gt__(self, other):
        sum_s1 = self.m1 + other.m1
        sum_s2 = self.m2 + other.m2
        if sum_s1 > sum_s2: return True
        else: return False


s1  = Student(100, 20)
s2  = Student(10, 20)
s = s1 + s2
print(s.m1, s.m2)
print(s1 > s2)