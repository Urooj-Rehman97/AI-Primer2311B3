# file = open("test.txt", "w")
# file.write("Hello Python!")
# file.close()

file = open("test.txt", "a")
file.write("\nHello Python!")
file.close()

file = open("test.txt", "r")
mydata = file.read()
print(mydata)

#line by line Read
file = open("test.txt", "r")
print(file.readline())

#shorthand
with open("test.txt", "a") as file:
    file.write("\nNew line added...")

#example
name = input("Enter Your Full Name: ")

with open("StudentList.txt" , "a") as file:
    file.write(name + "\n")
