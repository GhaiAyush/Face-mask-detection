

# 😷 Face Mask Detection using YOLOv8

> Real-time detection of **with mask**, **without mask**, and **incorrectly worn mask** using YOLOv8 — wrapped in a beautiful Streamlit web app!

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/Framework-YOLOv8-orange?logo=ultralytics)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📸 Demo

<div align="center">
  <table>
    <tr>
      <td><strong>Input Image</strong></td>
      <td><strong>Detection Result</strong></td>
    </tr>
    <tr>
      <td><img src="assets/input_sample.jpg" alt="Input" width="400"/></td>
      <td><img src="assets/output_sample.jpg" alt="Output" width="400"/></td>
    </tr>
  </table>
</div>

---

## 🧩 Project Structure

```
face-mask-detection/
│
├── model/
│   └── best.pt                  # Trained YOLOv8 model weights
│
├── notebook/
│   └── train_model.ipynb        # Complete training notebook (Google Colab)
│
├── assets/                      # Screenshots & demo images
├── app.py                       # Streamlit web application
├── requirements.txt
├── data.yaml                    # Dataset configuration
└── README.md
```

---

## 🚀 Features

- Accurate 3-class detection: `with_mask` ✅ · `without_mask` 🚫 · `mask_weared_incorrect` ⚠️  
- Simple & interactive Streamlit web interface  
- Upload image or use webcam (optional)  
- Lightning-fast inference with YOLOv8 nano  
- Trained on free Google Colab GPU  
- One-click deployment on Streamlit Cloud  

---

## 🧰 Technologies Used

| Component       | Technology                                                                 |
|-----------------|----------------------------------------------------------------------------|
| Model           | [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)           |
| Programming     | Python 3.10+                                                               |
| Web Framework   | [Streamlit](https://streamlit.io)                                          |
| Training Platform | Google Colab (Tesla T4 GPU)                                              |
| Dataset         | [Face Mask Detection ~12K Images](https://www.kaggle.com/datasets/andrewmvd/face-mask-detection) |

---

## 🧑‍💻 How It Works

1. Downloaded the popular Kaggle Face Mask dataset (~12K annotated images)  
2. Converted XML annotations → YOLO TXT format  
3. Trained **YOLOv8n** (nano) model for **25 epochs** on Google Colab  
4. Exported `best.pt` and integrated into a user-friendly Streamlit app  

**Training Command Used:**
```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Load pretrained nano model
results = model.train(data="data.yaml", epochs=25, imgsz=640, batch=16)
```

---

## ⚙️ Local Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/face-mask-detection.git
cd face-mask-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

## ☁️ Live Demo (Deployed on Streamlit Cloud)

🎯 **Try it instantly here:**

👉 [**Face Mask Detection Web App**](https://face-mask-detection-fnw4hnxdvtpk6vcaukxw2z.streamlit.app/)

No installation required — just upload an image and see real-time mask detection results directly in your browser! 🚀


---

## ☁️ Deploy on Streamlit Cloud (Free!)

1. Push this repo to GitHub  
2. Go to [https://share.streamlit.io](https://share.streamlit.io)  
3. Connect GitHub → Select this repo  
4. Set main file as `app.py` → Deploy!  

Live in under 60 seconds!

---

## 🏆 Model Details

- **Architecture**: YOLOv8n (nano – fastest & lightweight)  
- **Epochs**: 25  
- **Image Size**: 640×640  
- **Classes**: `with_mask`, `without_mask`, `mask_weared_incorrect`  
- **Hardware**: Google Colab Tesla T4 GPU  

---

| 👤 **Member**        | 💼 **Role**                       | 🧠 **Contributions**                                                                                                                                                                                                                                                                     |
| -------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ayush Ghai**       | **Lead Developer & Project Head** | - Designed overall system architecture<br>- Managed YOLOv8 model training pipeline<br>- Fine-tuned model parameters & performance metrics<br>- Conducted testing, evaluation, and validation of detections<br>- Guided UI-UX improvements for better user flow                           |
| **Tarun Kodi**     | **AI & Backend Developer**        | - Integrated YOLOv8 inference engine with Streamlit<br>- Optimized model loading & prediction pipeline<br>- Structured the project folder for modularity<br>- Configured deployment on Streamlit Cloud<br>- Enhanced README and documentation for GitHub                                 |
| **Gowri Shankar** | **Frontend & UI Engineer**        | - Designed Streamlit web interface for better accessibility<br>- Developed layout for image upload and result display<br>- Created responsive interface for both desktop & mobile<br>- Handled UI testing and bug fixes<br>- Added visual assets and icons for professional presentation |


---

## 🪪 License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

---

## 🌟 Acknowledgements

- Dataset by [andrewmvd](https://www.kaggle.com/andrewmvd) on Kaggle  
- Huge thanks to **Ultralytics** for YOLOv8  
- **Streamlit** for making deployment so easy  
- Google Colab for free GPUs ❤️  

---

💬 **Enjoyed this project? Give it a ⭐ and share with friends!**

