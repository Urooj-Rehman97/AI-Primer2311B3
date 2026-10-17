from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Data
X = [[1],[2],[3],[4]]   #Experience
Y = [40000, 50000, 65000, 75000] #Salary

#model Training
model = LinearRegression()
model.fit(X,Y)

#Prediction
print("Prediction: ",model.predict([[5]]))
print("Prediction: ",model.predict([[3.5]]))

#Graph Visualization
plt.scatter(X,Y)
plt.plot(X, model.predict(X))

plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()
