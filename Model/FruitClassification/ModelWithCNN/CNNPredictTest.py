from keras.models import load_model
import cv2
import numpy as np
from keras.preprocessing import image
from PIL import Image

classes=['Apple', 'Avocado', 'Banana', 'Grape', 'Guava', 'Lemon', 'Mango', 'Orange', 'Peach', 'Pear', 'Strawberry', 'Watermelon']
loaded_model = load_model('saved_model_h5/CNNModel.h5')

image_testing = Image.open('testImage/0_100.jpg')
print(image_testing)
image_testing = np.array(image_testing.resize((100, 100))) / 255.0

image_testing = np.expand_dims(image_testing, axis=0)
print(image_testing.shape)

output = loaded_model.predict(image_testing)
best_index = np.argmax(output)
class_name = classes[best_index]

print(output)
print(best_index)
print(class_name)