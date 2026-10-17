#import
from sklearn.tree import DecisionTreeClassifier

#Data
x = [[45],[56],[78],[90],[50]]  #marks x input
y = [0,1,1,1,0] # 0-Fail / 1-Pass y output

#model Train
model = DecisionTreeClassifier()
model.fit(x,y)  #fit is used to train model

#Prediction
print("Prediction",model.predict([[60]]))
print("Prediction",model.predict([[47]]))
print("Prediction",model.predict([[51]]))

