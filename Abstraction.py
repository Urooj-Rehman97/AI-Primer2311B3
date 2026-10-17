from abc import ABC, abstractmethod

class Person:
    @abstractmethod
    def intro(self):
        pass

class Student(Person):
    def intro(self):
        print("\nI'm a student...")

class Teacher(Person):
    def intro(self):
        print("\nI'm a Teacher")

p1 = Person()
p1.intro()

s1 = Student()
s1.intro()

t1 = Teacher()
t1.intro()
