#DataStructures
#List
#Tuples
#Dictionary
#sets
import Functions

print("----------------- List ------------------")
#List (Ordered, Mutable(values can be changeable), Allow duplicate values, built in methods, List access by indexing)
numbers = [1,2,3,4,5,5]
print(numbers)
print(numbers[1])
numbers[1] = 6
print("------------ List After replace existing value -------------")
print(f"New List: {numbers}")

print("------------------ List Built-in Methods ----------------------")
numbers.append(7)
print(f"After adding new Numbers: {numbers}")

numbers.remove(4)
print(f"After removing a number: {numbers}")

print("--------------------- Accessing List using Loop --------------------")
names = ["Shaheryar", "Ebad", "Ukasha", "Umer"]

print("----------- Student List ----------------")
for n in names:
    print(n)


print("----------------- Tuples ------------------")
#Tuples (Immutable (value can not be change or add))

ages=(23,56,78,90, 23)
# ages[0] = 43
# ages.append(26)
print(ages)

print("----------------- Sets ------------------")

#sets (duplicate values not allowed, automatically remove duplicate values )
oddNumbers = {1,3,5,7,9,11}
wholeNumbers = {1,2,3,4,5,6,7,8,9,10}
print(oddNumbers)

#sets operation
#union
print("----------------- Union ------------------")

print(oddNumbers.union(wholeNumbers))

print("----------------- Intersection ------------------")
print(oddNumbers.intersection(wholeNumbers))

print("----------------- Dictionary ------------------")

student ={
    "id": "101",
    "name": "Abc",
    "email":"abc?@gmail.com"
}

print(f"Student Name: {student}")
print(f"Student Name: {student["name"]}")

student["email"] = "abc123@gmail.com"
print(f"Student Name: {student}")



