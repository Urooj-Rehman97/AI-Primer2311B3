import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder #Step 2
from sklearn.model_selection import train_test_split #import for step 3
from sklearn.preprocessing import StandardScaler  #import for step 4
from sklearn.linear_model import LogisticRegression #import for step 5 and 6
from sklearn.metrics import accuracy_score

#Step 1 dataset
data = {
    "Age": [24,56, np.nan, 45, 23, 34, np.nan, 33,23, 40],
    "Salary": [45000, np.nan, 50000, 25000, 30000, np.nan, 80000, np.nan, 67000, 60000],
    "Gender": ["Male", "Female","Female","Male", np.nan, np.nan, "Male","Female","Female","Male"],
    "City": ["Karachi","Karachi","Islamabad",np.nan, "Lahore","Karachi","Islamabad","Lahore","Karachi",np.nan],
    "Purchased": [0,1,1,1,1,0,1,1,1,0]
}

dt = pd.DataFrame(data)
print("--------------------Original Data------------------")
print(dt)

#handle missing values
dt["Age"] = dt["Age"].fillna(dt["Age"].mean())
dt["Salary"] = dt["Salary"].fillna(dt["Salary"].mean())
dt["Gender"] = dt["Gender"].fillna(dt["Gender"].mode()[0])
dt["City"] = dt["City"].fillna(dt["City"].mode()[0])

print("--------------------Data After handle Missing Values------------------")
print(dt)

#Step 2
#LabelEncoder handle categorical data 
#Example Pass / Fail, Male / Female

le = LabelEncoder()
dt["Gender"] = le.fit_transform(dt["Gender"])
print("-------------------- Label Encoding ------------------")
print(dt)

#One Hot Encoding ( Separate Columns)
dt = pd.get_dummies(dt, columns=["City"])
print("-------------------- One Hot Encoding ------------------")
print(dt)

#Step 3 --------assigning x and y

x = dt.drop("Purchased", axis=1)
y = dt["Purchased"]


# X_train, X-test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state = 42)
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=42
)

print("\n------------------------------- Output Training and Testing Data --------------------------------------\n")
print("X Train Data: \n",X_train)
print("X Test Data: \n",X_test)
print("Y Train Data: \n",y_train)
print("Y Test Data: \n",y_test)

#Step 4 ---------------Scaling (handle data)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

#Step 5 ----------------------- model Train

model = LogisticRegression()   #Declare Model
model.fit(X_train, y_train)    #Model training

#Step 6 ------------------------ prediction

pred = model.predict(X_test)
print("Prediction: ",pred)

#Step 7 ---------------- Check Accuracy
accuracy = accuracy_score(y_test, pred)
print("Accuracy: ", accuracy)