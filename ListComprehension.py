#List Comprehension

numbers = []
print(f"Numbers: {numbers}")
for i in range(5):
    numbers.append(i)

print(f"Numbers: {numbers}")

#shorthand ListComprehension

numbers = [i for i in range(5)] 
print(f"Numbers: {numbers}")

#Take input from user than store even Numbers using List Comprehension

n = int(input("Enter any Number: "))
evenNumbers = []
for i in range(n):
    if(i %2 == 0):
        evenNumbers.append(i)

print(f"Even Numbers: {evenNumbers}")

#shorhand
evenNum = [i for i in range(n) if i %2 == 0]
print(f"Even Numbers: {evenNum}")

#Take number of subjects from user then take marks for each subject and stor in List


