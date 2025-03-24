from tensorflow.keras.models import load_model
import numpy as np

def load_retina_model():
    model = load_model("model/retina_model.h5")
    return model

def predict_diabetic_retinopathy(model, image_array):
    image_array = np.expand_dims(image_array, axis=0)
    prediction = model.predict(image_array)[0]
    predicted_class = int(np.argmax(prediction))
    return predicted_class