# print(10/0)

try:
    print(10/0)
except:
    print("Denominator should not be zero")

print("We are learning Python....")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    div = num1 / num2
except:
    print("Denominator should not be zero.....")
else:
    print(f"Dision of given Numbers is: {div}")
finally:
    print("Finally block invokes.....")