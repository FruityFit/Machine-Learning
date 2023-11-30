from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = FastAPI()
model_folder = 'Model\ModelWithCNN\saved_model_h5' #change if its different
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, model_folder, 'CNNModel.h5')
print(model_path)
loaded_model = load_model(model_path)


def preprocess_image(file_path):
    img = image.load_img(file_path, target_size=(100, 100))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        file_path = f"temp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Preprocess the image
        input_data = preprocess_image(file_path)

        # Make predictions using the loaded model
        predictions = loaded_model.predict(input_data)

        # Example: Assuming it's a classification task and returning the class with the highest probability
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class])

        return JSONResponse(content={"class": predicted_class, "confidence": confidence}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn

    # uvicorn.run(app, host="127.0.0.1", port=8000)
