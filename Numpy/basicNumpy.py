import numpy as np

data = np.array([10,20,30,40,50])
print(f"Atual Data: {data}")

#Vectorization
print("Data After multiplying by 3: ",data *3)
print("Data After adding 2: ",data +2)

#Builtin Methods
print("------------- BuiltIn Methods --------------")
print(np.zeros(5))
print(np.ones(5))
print(np.arange(1,10))
print(np.arange(1,10,2))
print(np.linspace(1,3,5))
print(np.linspace(1,3,6))

#Aggregate functions
print("------------- Aggregate Functions --------------")

total = np.sum(data)
print(f"Total: {total}")

average = np.mean(data)
print(f"Average: {average}")

med = np.median(data)
print(f"Median: {med}")

maximum = data.max()
minimum = data.min()
print(f"Maximum Value: {maximum}")
print(f"Maximum Value: {minimum}")

#Multidimensional Array
arr = np.array([[12,14,16],
                [13,15,17]])

#Shape, ndim, size
print("------------- Shape, ndim, size--------------")

print(f"Shape of Array: {arr.shape}") 
print(f"Shape of data: {data.shape}")

print(f"Dimension of Array: {arr.ndim}")
print(f"Dimension of data: {data.ndim}")

print(f"Size of Array: {arr.size}")
print(f"Size of data: {data.size}")


#Indexing and Slicing
print("------------- Indexing and Slicing --------------")

print(f"First value of data: {data[0]}")
print(f"Last value of data: {data[-1]}")  #-1 access last value

#Multidimensional Indexing
print(f"Last value of multidimensional Array: {arr[-1,-1]}")

#array[start:end](slicing)
print(f"First 3 values of data: {data[:3]}")
print(f"Last 3 values of data: {data[2:]}")
print(f"Middle values of data: {data[2:4]}")

#square of data
print(f"Square of given data: {data ** 2}")