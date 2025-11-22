import streamlit as st
import torch
from utils import load_model, predict_image
from exception import XRAYException
from logger import logger
import sys
from config import WEIGHT_PATH

st.set_page_config(
    page_title="Chest X-Ray Disease Predictor",
    layout="wide",     # <<— THIS makes the page full-width
)


DEVICE = torch.device("cpu")


@st.cache_resource
def get_model():
    try:
        return load_model(WEIGHT_PATH, DEVICE)
    except Exception as e:
        st.error("❌ Failed to load model. Check logs.")
        raise XRAYException(e, sys)


model = get_model()

st.title("🩻 Chest X-Ray Disease Predictor (NIH14)")
st.write("Upload a chest X-ray image to obtain disease probabilities.")

uploaded = st.file_uploader("Upload X-ray", type=["jpg", "jpeg", "png"])

if uploaded:

    # ---------- TWO COLUMN LAYOUT ----------
    col1, col2 = st.columns([1, 1])

    # LEFT COLUMN → SHOW IMAGE
    with col1:
        
        st.image(uploaded, use_container_width=True,caption="Uploaded Image")


    # Save temp image
    temp_path = "temp.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded.getbuffer())

    # RIGHT COLUMN → RESULTS
    with col2:
        try:
            with st.spinner("Running inference..."):
                preds = predict_image(model, temp_path, DEVICE)

            st.subheader("📊 Prediction Probabilities")
            for cls, p in preds.items():
                st.write(f"{cls}: **{p:.4f}**")

            st.subheader("🔥 Positive Findings (p > 0.5)")
            positives = {c: p for c, p in preds.items() if p > 0.5}

            if positives:
                for k, v in positives.items():
                    st.write(f"✔ {k}: **{v:.3f}**")
            else:
                st.write("No strong findings detected.")

        except XRAYException as e:
            logger.error(f"Main inference error: {str(e)}")
            st.error("❌ Something went wrong during prediction. Check logs.")
