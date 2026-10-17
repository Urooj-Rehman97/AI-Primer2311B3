class Student:
    id = "Student12345"  #class Variable
    def __init__(self, name):   #Constructor
        self.name = name #instance Variable
    
    def __teacher(self): #__ underscore represent private
        print("Teacher Name: Urooj Rehman")
        print("Course: AI Primer")

    def details(self):
        self.__teacher()



print(Student.id)
# print(Student.name)
s1 = Student("Xyz")
print(s1.name)
# s1.teacher()
s1.details()
