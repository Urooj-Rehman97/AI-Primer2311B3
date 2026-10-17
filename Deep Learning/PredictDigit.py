import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

#Load Dataset
(x_train, y_train),(x_test,y_test) = keras.datasets.mnist.load_data()

#Normalized
x_train = x_train /255.0
x_test = x_test / 255.0  
#0 black, 255.0 white (Convert data into 0 or 1)

#Create Model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(10, activation = 'softmax')
])

#compile
model.compile(optimizer='adam',
               loss = 'sparse_categorical_crossentropy',
               metrics= ['accuracy'] )

#train
model.fit(x_train, y_train, epochs=4)

#input
image = x_test[0]

#Test
model.evaluate(x_test, y_test)

#Prediction
prediction = model.predict(np.array([image]))

#Result
digit = np.argmax(prediction)

#Show Image
plt.imshow(image, cmap='gray')
plt.title(f"Predicted Digit: {digit}")
plt.show()
print(image)


