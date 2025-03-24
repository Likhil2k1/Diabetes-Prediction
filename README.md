# 🌺 Diabetic Retinopathy Prediction App

A deep learning-powered web application built with **FastAPI** that predicts the stage of Diabetic Retinopathy (DR) from retinal images. Users can upload a fundus image and get an instant prediction using a trained MobileNetV2 model.

---

## 📊 DR Stage Classification

| Class | Stage              |
|-------|--------------------|
| 0     | No DR              |
| 1     | Mild               |
| 2     | Moderate           |
| 3     | Severe             |
| 4     | Proliferative DR   |

---

## 🚀 Features

- 🖼️ Upload retinal images (JPG, PNG)
- 🔍 Predict diabetic retinopathy stage using CNN (MobileNetV2)
- 📦 Ready for deployment on Render
- 🎨 Clean UI with logo & branding
- 👤 Developed by **Likhil Penujuli**

---

## 🧠 Model Info

- Architecture: **MobileNetV2**
- Image Size: `224x224`
- Framework: **TensorFlow/Keras**
- Training Accuracy: ~57%
- Validation Accuracy: ~56%

---

## 🛠️ Tech Stack

- `FastAPI` - Backend API
- `Jinja2` - HTML Template rendering
- `TensorFlow/Keras` - Model inference
- `OpenCV` - Image preprocessing
- `Uvicorn` - ASGI server
- `Render` - Cloud deployment


---

## 📂 Folder Structure

```
.
├── app/
│   ├── main.py              # FastAPI app
│   ├── model.py             # Model loading and prediction
│   ├── utils.py             # Image preprocessing
│   ├── static/logo.png      # App logo
│   └── templates/index.html # Web UI
├── model/
│   └── retina_model.h5      # Trained model
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment config
└── README.md
```

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/Likhil2k1/Diabetes-Prediction.git
cd Diabetes-Prediction
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open your browser at:  
🔗 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Future Improvements

- Use **EfficientNetB3** or **InceptionV3** for better accuracy
- Add **Grad-CAM** for explainability
- Improve validation with AUC/F1-score
- Upload directly from camera on mobile

---

## 👨‍💼 Developed By

**Likhil Penujuli**  


---

⭐ Star this repo if you like it!  
📬 PRs and contributions welcome!
