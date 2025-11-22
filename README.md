MultiDisease_Prediction_AI_AZURE


![alt text](image.png)


# 🩻 Chest X-Ray Multi-Disease Classification (Streamlit + PyTorch)

This project provides an end-to-end pipeline for **multi-label chest X-ray disease prediction** using a fine-tuned **ResNet-50** model.  
A Streamlit web app is included for easy inference with an uploaded X-ray image.

---

## 📁 Project Structure
```

MULTIDISEASE_PROJECT/
│
├── app/
│   ├── app.py              # Streamlit frontend
│   ├── exception.py        # Custom exception handler
│   ├── logger.py           # Logging utility
│   ├── utils.py            # Model loading + preprocessing
│   └── __pycache__/        
│
├── data/
│   ├── final.csv
│   └── new_xray.png        # Sample test image
│
├── logs/
│   └── *.log               # Auto-generated logs
│
├── model/
│   └── best_resnet50.pth   # Saved PyTorch model checkpoint
│
├── notebooks/
│   ├── chestxray_inference.ipynb
│   └── chexnet_pytorch.ipynb
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
└── README.md               # You are here

---
```

## 🚀 Features

- Multi-label disease prediction (14 NIH classes)
- Streamlit-based interactive UI
- Custom exception and logging framework
- Dockerized for easy deployment
- CPU-compatible (no GPU required)
- Easy to extend and modify

---

## 🖥️ Running the App Locally (CPU)

###  Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

###  Install dependencies

```
pip install -r requirements.txt
```
###  Start the Streamlit app

```
streamlit run app/app.py
```
## 🖥️ 🐳 Running with Docker


### Build the image

docker build -t chestxray-app .

### Run the container

docker run -p 8501:8501 chestxray-app


