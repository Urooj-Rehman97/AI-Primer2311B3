import numpy as np

arr = np.array([1,2,3])
arr2 = np.array([10,20,30])

print(arr + arr2)
print(arr * arr2)

ary = np.array([[1,2,3],
                [4,5,6]])
print(ary + 10)

ary2 = np.array([[4,5,6],[1,2,3]])
print(ary + ary2)

# #reshape
ages = np.array([12,45,65,34,29,23,41,50])
new_ages = ages.reshape(4,2)
# new_ages1 = ages.reshape(-1,3)

print(ages)
print(new_ages)
# print(new_ages1)

# #Flatten / Ravel (2D array ko 1D array mconvert krta h)
print("Convert 2D array into 1D array using flatten: ",ary.flatten())
print("Convert 2D array into 1D array using ravel: ",ary.ravel())

# #Stacking
print("Vertical Stack",np.vstack((arr,arr2)))
print("Horizontal Stack",np.hstack((arr,arr2)))