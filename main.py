from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

model_folder = 'Model/FruitClassification/ModelWithCNN/saved_model_h5'  # change the path on the cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, model_folder, 'CNNModel.h5')
#print(model_folder)
loaded_model = load_model(model_path)
classes=['Apple', 'Avocado', 'Banana', 'Grape', 'Guava', 'Lemon', 'Mango', 'Orange', 'Peach', 'Pear', 'Strawberry', 'Watermelon']

def preprocess_image(file_path):
    img = image.load_img(file_path, target_size=(100, 100))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error": "No selected file"})

        if file:
            # Save the uploaded file temporarily
            filename = secure_filename(file.filename)
            file_path = os.path.join("temp", filename)
            file.save(file_path)

            # Preprocess the image
            input_data = preprocess_image(file_path)

            # Make predictions using the loaded model
            predictions = loaded_model.predict(input_data)

            predicted_class = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class])

            return jsonify({"class": classes[predicted_class], "confidence": confidence})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
