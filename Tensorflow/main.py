import keras
from keras import layers
from keras import models
from keras import optimizers
from keras.datasets import imdb
from matplotlib import pyplot as plt
import numpy as np


def sigma(x):
    return 1 / (1 + np.exp(-1 * x))

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results


(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
K = 10
z = np.random.randint(0, high=100, size=K, dtype=int)

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer=optimizers.RMSprop(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

history = model.fit(partial_x_train, partial_y_train, batch_size=512, epochs=20, validation_data=(x_val, y_val))
history_dict = history.history

train_accuracy_values = history_dict['accuracy']
val_accuracy_values = history_dict['val_accuracy']
train_loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']

accuracy = history_dict['accuracy']
epochs = range(0, len(accuracy))

plt.figure(figsize = (12, 6))
plt.plot(epochs, train_accuracy_values, 'tab:blue', label='Training Accuracy')
plt.plot(epochs, val_accuracy_values, 'tab:orange', label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.grid()
plt.legend()
plt.show()
