from tensorflow import keras #Keras Library is useed for deeplearning

#dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#normalized (data ko 0 or 1 m convert krna)
x_train = x_train /255.0
x_test = x_test /255.0

#0 black
#255 white (1)

#Create Model
model = keras.Sequential([.
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#Compile'
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']

)

#model train
model.fit(x_train,y_train, epochs = 3)

#evaluate
model.evaluate(x_test,y_test)



