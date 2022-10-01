#Multilevel inheritance example
# class C inherits class B and Class B inherit class A : A --> B --> C

class A:
    def feature1(self):
        print("Feature 1")
    def feature2(self):
        print("Feature 2")

class B(A):
    def feature3(self):
        print("Feature 3")
    def feature4(self):
        print("Feature 4")

class C(B):
    def feature5(self):
        print("Feature 5")
    def feature6(self):
        print("Feature 6")

#class C has all the features that has class A, B and C that is called multilevel inheritance
c_obj = C()
c_obj.feature1()
#----------------------------------------------------------------------------------------------

#implemented multiple inheritance
# class D(A, B):
#     def featureD(self):
#         print("Feature D")
#     def featureD1(self):
#         print("Feature D1")
#
# d_obj = D()
# d_obj.feature1()

#Constructor in inheritance & method resolution order
class AB:
    def __init__(self):
        print("class ab init method")
    def feature1(self):
        print("Feature 1")
    def feature2(self):
        print("Feature 2")

class BC(AB):
    def featurebc1(self):
        print("Feature bc1")
    def featurebc2(self):
        print("Feature bc2")
bc_obj = BC()
bc_obj.featurebc1()




