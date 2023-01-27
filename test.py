


# def say_something():
#     what_to_say = 'Hi'
#     now_say_it(what_to_say)
#
# def now_say_it(content):
#     print(content)
#
# say_something()

# def outerfun():
#     global a
#     a = 20
#     def innerfun():
#         global a
#         a = 30
#         print('a',a)
#
# a = 10
# outerfun()
# print('a',a)


# d = {'a', 'b', 'c'}
# while d:
#     print(d.popitem())
# print('Done')


# class Parent:
#     def __init__(self):
#         self.x = 1
#     def change(self):
#         self.x = 10
# class Child(Parent):
#     def change(self):
#         self.x = self.x + 1
#         return self.x
# def main():
#     obj = Child()
#     print(obj.change())
#
# main()


# print("Hello" + 2 + "world")

# data = 50
# try:
#     data = data / 0
# except ZeroDivisionError:
#     print('cannot div by 0')
#
# try:
#     data = data / 5
# except:
#     print("inside except block")

# class Dog:
#     def walk(self):
#         return "wlaking"
#     def speak(self):
#         return "woowoo"
# class Jack(Dog):
#     def talk(self):
#         return super().speak()
# bobo = Jack()
# bobo.talk()

# class ABC():
#     def __init__(self):
#         self.a = 'A'
# obj1 = ABC()
# print(obj1.a)
# obj1.b  ="pak"
# print(obj1.b)

# class student:
#     def __init__(self):
#         self.marks = 97
#         self.cgpa  =8.7
#     def display(self):
#         print(self.marks)
# obj = student()
# print(obj.cgpa)



# def abc(*l, x, y, z):
#     return x+y+z+sum(l)
#
#
# # abc(z=1, x=2, y=3, 1,3,4)
# abc(1,3,4, x=1, y=10, z=20 )
# abc(1,3,4, z=1, x=10, y=20 )
# abc(5,5,5, 1,2,3)

# a = ['a','b','c','d','e']
# while a:
#     if len(a) < 3:
#         break
#     print(a.pop(), end="")
# print("Done")

class Sales:
    def __init__(self, id):
        self.id = id
        id = 100

val = Sales(123)
print(val.id)





















