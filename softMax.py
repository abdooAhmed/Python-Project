import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()
x_train = x_train/255
x_test = x_test/255
x_train_reshape = x_train.reshape(len(x_train),28*28)
print(x_train_reshape.shape)
x_text_reshape = x_test.reshape(len(x_test),28*28)
print(x_text_reshape.shape)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(100,activation='relu'),
    keras.layers.Dense(10,activation='sigmoid'),

])
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train_reshape,y_train,epochs=10)
model.evaluate(x_text_reshape,y_test)
y = model.predict(x_text_reshape)
y_label = [np.argmax(i) for i in y]
cm = tf.math.confusion_matrix(labels=y_test,predictions=y_label )
print(cm)
plt.figure(figsize=(10,7))
sb.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')