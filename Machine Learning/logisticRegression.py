from sklearn.linear_model import LogisticRegression

#Data
X = [[50], [60], [70],[80]]   #Marks, X (input)
Y = [0,1,1,1]  # 0 = fail, 1= pass , Y (OutPut)

#Model
model = LogisticRegression()

#Train
model.fit(X,Y)

#Prediction
print("Prediction: ",model.predict([[40]]))
print("Prediction: ",model.predict([[55]]))
