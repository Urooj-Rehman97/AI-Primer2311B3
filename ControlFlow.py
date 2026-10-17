#Decision Making Statement
#if, if else, if elif else
age = int(input("Enter your Age: "))
# if(age>=18):
#     print(f"Your age is {age}, you're eligible.")
# else:
#     print(f"Your age is {age}, you're not eligible.")
    
   
if(age<18):
    print(f"Your age is {age}, you're not eligible because you're too young.")
elif(age>=18 and age<=30):
    print(f"Your age is {age}, you're eligible.")
else:
    print(f"Your age is {age}, you're not eligible.") 

print("-------------------- For Loop -----------------------")
for i in range(5):
    print(i)
for i in range(5):
    print(i+1)

print("-------------------- While Loop -----------------------")

j = 1
while j<=5:
    print(j)
    j = j+1