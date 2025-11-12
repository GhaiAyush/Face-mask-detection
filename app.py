import os
# 🩵 Fix for Streamlit Cloud: prevent cv2 GUI loading (libGL.so.1 missing)
os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"] = "0"
os.environ["OPENCV_LOG_LEVEL"] = "ERROR"
os.environ["FORCE_HEADLESS"] = "1"
import streamlit as st
try:
    from ultralytics import YOLO
except ImportError:
    import cv2
    raise RuntimeError("OpenCV failed to load. Please ensure headless mode is enforced.")

from PIL import Image
import numpy as np

st.set_page_config(page_title="😷 Face Mask Detection", layout="centered")

st.title("😷 Face Mask Detection App (YOLOv8)")
st.write("Upload an image to detect if the person is wearing a mask properly, incorrectly, or not at all.")

# Load trained YOLOv8 model
model = YOLO("model/best.pt")

uploaded_file = st.file_uploader("📸 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # ✅ Convert RGBA → RGB (remove alpha channel)
    if image.mode == "RGBA":
        image = image.convert("RGB")

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to numpy array
    img_array = np.array(image)

    # ✅ Run YOLO prediction
    results = model.predict(source=img_array, conf=0.4)

    # ✅ Display annotated result (works headlessly)
    annotated_image = results[0].plot()
    st.image(annotated_image, caption="Detection Result", use_column_width=True)

    # ✅ Show class labels and confidence
    if results[0].boxes is not None:
        for box in results[0].boxes:
            cls = int(box.cls[0])
            conf = round(float(box.conf[0]), 2)
            label = model.names[cls]
            st.write(f"**{label}** detected with confidence **{conf}**")
    else:
        st.warning("No mask detected in the image.")
