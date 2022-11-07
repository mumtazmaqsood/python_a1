#data.txt memeber are open, same Car has been inherited in ec1
#in this class make getter and setter method, so that user should not change its attribute values
#if want to see or need to change the value, it should go through methods


from inheritance_class1 import Car

class Electric_Car1(Car):
    def __init__(self,brand, model, transmission, engine, battery):
        super().__init__(brand, model, transmission, engine)
        self.battery = battery

    def charging_battery(self):
        print(f"{self.brand} {self.model} {self.transmission} {self.engine} is charging battery {self.battery}....")
    def fuel_tank(self):
        print("Electric cars has not fuel tank")

    def get_battery(self):
        print(f"{self.brand} {self.model} has this battery:{self.battery}")

    def set_battery(self, new_battery):
        self.battery = new_battery

#now by creating getter and setter method, user can access and change battery description by proper channel
ec2 = Electric_Car1("Nissan", "e1", "auto", "2000c","APS")
ec2.get_battery()
ec2.set_battery("Exoide")
ec2.get_battery()

#another exmple
class Student:
    def __init__(self, roll_no, name, course, insitute):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.insitute = insitute

    def get_rollno(self):
        print(f"{self.name} has this rollno:{self.roll_no}")
    def set_rollno(self, new_rollno):
        self.roll_no = new_rollno
        print(f"Roll no has been set: {self.name} has this rollno:{self.roll_no}")

    def get_course(self):
        print(f"Student: {self.name} is registered in this course:{self.course}")
    def set_course(self, new_course):
        course = ["iot", "block chain", "metaverse", "cloudcomp", "ai"]
        if new_course in course:
            self.course = new_course
        else:
            print(f"{new_course} is not avaible")


st = Student(10, "John", "IT", "MIT")
st.get_rollno()
st.set_rollno(20)
st.get_rollno()
st.get_course()
st.set_course("devops")
st.get_course()











