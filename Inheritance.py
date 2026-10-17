#Inheritance
#Single Inheritance

            # class School:
            #     def Details(self, Name, Address):
            #         self.Name = Name
            #         self.Address = Address
            #         print("School Name: "+self.Name)
            #         print("School Address: "+self.Address)


            # class Student(School):
            #     def info(self, SId, Sname, Semail):
            #         self.SId = SId
            #         self.Sname = Sname
            #         self.Semail = Semail
            #         print("Student Id: ",self.SId)
            #         print("Student Name: ",self.Sname)
            #         print("Student Email: ",self.Semail)

            # sch = School()
            # # sch.Details("Abc", "Street 4 Nazimabad")
            # # Sch.info()
            # Std = Student()
            # Std.Details("Abc", "Street 4 Nazimabad")
            # Std.info(123, "Hashir", "hashir@gmail.com")

#Multi-level Inheritance
class School:
    def Details(self, Name, Address):
        print("\n-------------- Complete Details ------------\n")
        self.Name = Name
        self.Address = Address
        print("School Name: "+self.Name)
        print("School Address: "+self.Address)

class Teacher(School):
    def TeacherDetails(self, name):
        self.name = name
        print(f"Student Name: {self.name}")


class Student(Teacher):
    def StudentDetails(self, SId, Sname, Semail):
        self.SId = SId
        self.Sname = Sname
        self.Semail = Semail
        print("Student Id: ",self.SId)
        print("Student Name: ",self.Sname)
        print("Student Email: ",self.Semail)

SchName = input("Enter Your School Name: ")
SchAdd = input("Enter complete Address of your School: ")
TeacherName = input("Enter Your Teacher Name: ")
StdId = int(input("Enter your Student Id: "))
StdName = input("Enter your full Name: ")
StdEmail = input("Enter your Email: ")
Std = Student()
# Std.Details("Abc School", "Street 4 Near Sweet shop Nazimabad")
# Std.TeacherDetails("Urooj Rehman", "3+ Years")
# Std.StudentDetails(121, "Daniyal", "daniyal@gmail.com")
Std.Details(SchName, SchAdd)
Std.TeacherDetails(TeacherName)
Std.StudentDetails(StdId, StdName, StdEmail)

#Super() 

class Flower:
    def __init__(self, name):
        self.name = name
        print(f"Flower Name: {self.name}")

class Rose(Flower):
    def __init__(self, color):
        super().__init__("Black Rose")
       
        self.color = color
        print(f"Color: {self.color}")

r1 = Rose("Black")