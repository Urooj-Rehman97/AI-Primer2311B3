import pandas as pd

# print(pd.__version__)    check pandas version using this line of code

#Data Frame in pandas
data = {
    "Names": ["Abc", "Xyz","Mno", "Pqr"],
    "Marks": [23,56,78,90,]
}

print(data)
newData = pd.DataFrame(data)
print(newData)

#read csv files
dt = pd.read_csv("example.csv")
print(dt)

Depart = pd.read_csv("Department_Information.csv")
print(Depart)

#Built in Methods
print("------------------- Top 5 Department Information ---------------------")
Top = print(Depart.head())

print("------------------- Last 5 Department Information ---------------------")
Top = print(Depart.tail())

print("------------------- Top 5 Department Information ---------------------")
Top = print(Depart.head())

print("------------------- Summary of Department ---------------------")
Top = print(Depart.describe())

print("------------------- Summary of Students Report ---------------------")
Top = print(dt.describe())

print("------------------- Info of Department Sheet ---------------------")
Top = print(Depart.info())

#series
std = [12,34,77,98, 9]
stdData = pd.Series(std)
print("------------------- Series in Pandas ---------------------")
print(stdData)