import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Set relative paths
model_folder = 'Model\ModelWithCNN'
dataset_folder = 'Dataset\FruitClassification'


# Get the absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
common_parent_dir = os.path.dirname(os.path.dirname(current_dir))
dataset_path = os.path.join(common_parent_dir, 'Dataset', 'FruitClassification')
labels = os.listdir(dataset_path+'/Test')
print(dataset_path)

# Image dimensions and batch size
img_height = 100
img_width = 100
batch_size = 32

# TEST
test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(os.path.join(dataset_path, 'Test'),
                                            target_size = (img_height, img_width),
                                            batch_size = 50,
                                            class_mode = 'sparse')
from keras.models import load_model

loaded_model = load_model('saved_model_h5/CNNModel.h5')
score = loaded_model.evaluate(test_set, return_dict=True, verbose=0)
print(score)


