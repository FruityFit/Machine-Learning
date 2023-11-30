import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np
import matplotlib.pyplot as plt


# Set relative paths
model_folder = 'Model\FruitClassification\ModelWithCNN'
dataset_folder = 'Dataset\FruitClassification'

# Get the absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, model_folder, 'model.py')
common_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
dataset_path = os.path.join(common_parent_dir, 'Dataset', 'FruitClassification')
labels = os.listdir(dataset_path+'/Training')
num_classes = len(labels)

# Image dimensions and batch size
img_height = 100
img_width = 100
batch_size = 50

# Configure ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    vertical_flip=True,
    validation_split=0.2
)

# Flow from directory for training set
train_generator = train_datagen.flow_from_directory(
    os.path.join(dataset_path, 'Training'),
    target_size=(img_height, img_width),
    class_mode='sparse',
    batch_size=batch_size,
    subset='training'
)

# Flow from directory for validation set
validation_generator = train_datagen.flow_from_directory(
    os.path.join(dataset_path, 'Training'),
    target_size=(img_height, img_width),
    class_mode='sparse',
    batch_size=batch_size,
    subset='validation'
)

model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape=(img_height, img_width, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), input_shape=(img_height, img_width, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), input_shape=(img_height, img_width, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model.summary()

# Train the model
epochs = 10
history = model.fit(
    train_generator,
    steps_per_epoch=(train_generator.n// batch_size) + 1,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=(validation_generator.n// batch_size) + 1,
    verbose = 1
)


print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

model.save('saved_model_h5/CNNModel.h5')