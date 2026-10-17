#Functions
#Function without Parameter
print("-------------------- Functions ------------------")
print("-------------------- Function without Parameter ------------------")
def greetings():
    print("Hello Python....")

greetings()

print("-------------------- Function with Parameter ------------------")
#
#Keyword Parameter
#default

def add(a,b):
    sum = a+b
    print(f"Sum of given numbers: {sum}")

add(12,8)
# add()

#Keyword Parameter
def info(name, age):
    print(f"Hello {name} you're {age} years old")

info(age = 12, name= "Abc")
# info()

#Default Parameter
def user(name = "Guest User"):
    print(f"Welcome {name}")

user()
user("Urooj Rehman")

def sub(x,y):
    return x -y

subtract = sub(12,5)
print(f"Subtraction of given Numbers: {subtract}")
