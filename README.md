<p align="center">
  <img src="assets/FruityFit.png" alt="fruityfit-logo" height="400" />
</p>

<h1 align="center">FruityFit</h1>

<div align="center">
CH2-PS327
</div>

## CH2-PS327 Contributors

| Name  | Bangkit-ID | Learning Path  | 
| :---: | :---: | :---: |
|  Evander Gabriel  | M239BSY0797  | Machine Learning  |
|  Christopher Ade Wiyanto  | M239BSY1097  | Machine Learning  |
|  Sonya Oktavia  | M200BSX1152  | Machine Learning  |
| Danar Hadi Bachtiar | C253BSY3294 | Cloud Computing |
| Muhamad Arya Al Ghifari Wibowo | C134BSY3568  | Cloud Computing |
| Melisa Wijaya | A239BSX2324 | Mobile Development |
| Adam Rayhant Laksono | A009BSY2477  | Mobile Development |


## Machine Learning
### 1. Fruit Classifications

<p align="center">
  <img src="assets/Fruit-Classification-Accuracy.jpeg" alt="" height="400" />
  <img src="assets/Fruit-Classification-Loss.jpeg" alt="" height="400" />
</p>

### Steps
1. Collect dataset
2. Make 2 folders for test and train
3. Make folders in each folders as much classes and name it.
4. Use ImageDataGenerator to augment the images dataset 
5. Tensorflow to build the ML model using CNN 
6. Make the REST API using Flask

### 2. Fruit Freshness Classifications

<p align="center">
  <img src="assets/Fresh-Accu.jpeg" alt="" height="400" />
  <img src="assets/Fresh-Loss.jpeg" alt="" height="400" />
</p>

### Steps
1. Collect dataset
2. Make 2 folders for test and train
3. Make 2 folders in each folder because we want binary and name it True or False.
4. Use ImageDataGenerator to augment the images dataset 
5. Tensorflow to build the ML model using CNN 
6. Save to SavedModel then convert to tensorflow.lite

### 3. Chatbot
<p align="center">
  <img src="assets/Botie.png" alt="" height="400" />
</p>
Botie employs text classification to predict future events and utilizes various Google products, such as Generative AI, Palm API, TensorFlow, and a custom search API. In addition to typical chatbot functions, Botie examines user history to provide personalized juice recommendations based on individual preferences and nutritional requirements

### Steps

1. Gather data
2. Create separate directories for testing and training
3. Generate JSON for the data
4. Apply NLTK preprocessing for text data
5. Utilize NLTK for data augmentation and manipulation
6. Saved it to class blueprint for advanced deployment
7. Construct a class blueprint for 2 generative ai and web scraping
8. Make one class to combine 3 class before for deployment
9. Save as a SavedModel and convert to H5
10. deployed in flask server
