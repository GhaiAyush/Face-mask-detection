import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="😷 Face Mask Detection", layout="centered")

st.title("😷 Face Mask Detection App (YOLOv8)")
st.write("Upload an image to detect if the person is wearing a mask properly or not.")

# Load the trained YOLO model
model = YOLO("model/best.pt")

uploaded_file = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to numpy array
    img_array = np.array(image)

    # Run detection
    results = model.predict(source=img_array, conf=0.4)

    # Display annotated result
    annotated_image = results[0].plot()
    st.image(annotated_image, caption="Detection Result", use_column_width=True)

    # Show labels and confidence
    for box in results[0].boxes:
        cls = int(box.cls[0])
        conf = round(float(box.conf[0]), 2)
        label = model.names[cls]
        st.write(f"**{label}** detected with confidence **{conf}**")
