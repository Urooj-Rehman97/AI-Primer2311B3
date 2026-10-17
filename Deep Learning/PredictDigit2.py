import numpy as np
from tensorflow import keras
import tkinter as tk
from PIL import Image, ImageDraw
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
# image = x_test[0]

#UI Window
root = tk.Tk()
root.title("Digit Predictor")

canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

#PIL Image
image = Image.new("L", (200,200), color=255)
draw = ImageDraw.Draw(image)

#Draw Function
def paint(event):
    x1, y1 = (event.x - 8), (event.y - 8)
    x2, y2 = (event.x + 8), (event.y + 8)
    canvas.create_oval(x1,y1,x2,y2, fill="black")
    draw.ellipse([x1,y1,x2,y2], fill="black")
canvas.bind("<B1-Motion>", paint)



#Prediction Function
# prediction = model.predict(np.array([image]))
def predict():
    img = image.resize((28,28),Image.Resampling.LANCZOS)
    img_array = np.array(img)
    img_array = 255 - img_array #invert color
    img_array = img_array / 255.0
    prediction = model.predict(np.array([image]))
    digit = np.argmax(prediction)
    result_label.config(text=f"Prediction: {digit}")

btn = tk.Button(root, text="predict", command=predict)
btn.pack()

#Result Label
result_label = tk.Label(root, text="Draw a digit")
result_label.pack()
root.mainloop()

#Test
# model.evaluate(x_test, y_test)
#Result
# digit = np.argmax(prediction)

#Show Image
# plt.imshow(image, cmap='gray')
# plt.title(f"Predicted Digit: {digit}")
# plt.show()
# print(image)


