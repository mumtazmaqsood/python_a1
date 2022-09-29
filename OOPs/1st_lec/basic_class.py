
#this is the basic layout of the class , it has attributes and methods
class SamsungGlaxy:
    # Attribute/charactertics --> variables
    ram = '4GB'
    weight = '120g'
    color = 'grey'
    processor = '4Core'
    camera = '6mpx'
    battery = '12amp'
    screen = '6*4'

    #Behaviour/Actions/Functions --> methods
    def makeCall(self):
        print("calling....")
    def recCall(self):
        print("reciving call...")
    def takePic(self):
        print("Taking pic.....")

ph_obj = SamsungGlaxy()
print(ph_obj.color)
ph_obj.recCall()


#2nd example
class Patient:
    def __init__(self, patient_id, name, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.gender = gender
        self.disease = disease

    #creating methods
    def admission(self):
        print(f"Patient:{self.name} is admitted")
    def treatment(self):
        print(f"Patient:{self.name} is treated")
    def discharge(self, bill):
        #taking bill argument and checking if bill is paid then show discharge ortherwise need to pay his dues
        if bill == True:
            print(f"Patient:{self.name} is discharged")
        else:
            print(f"Patient:{self.name} need to pay his dues")


p1 = Patient(1, "John", "M", "xx")
p2 = Patient(1, "katrina", "F", "x")

# p1.discharge(True)
# p2.discharge(False)

#we can also access through class name
#same as  p1.addmission or p1.discharge(False)
print("class name")
Patient.admission(p2)
Patient.discharge(p1, False)