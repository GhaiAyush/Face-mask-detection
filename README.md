

# 😷 Face Mask Detection using YOLOv8

> Real-time detection of **with mask**, **without mask**, and **incorrectly worn mask** using YOLOv8 — wrapped in a beautiful Streamlit web app!

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/Framework-YOLOv8-orange?logo=ultralytics)
![HuggingFace](https://img.shields.io/badge/Deploy-HuggingFace_Spaces-yellow?logo=huggingface&logoColor=black)

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
git clone https://github.com/GhaiAyush/Face-mask-detection.git
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
## 📸 Live Demo

Try the app instantly on HuggingFace:

👉 **https://huggingface.co/spaces/ayushghai/face-mask-detection**

No installation needed — upload an image or capture live with your webcam!

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

## 👥 Team & Contributions

> A passionate and collaborative effort led by **Ayush Ghai**, driving the entire project lifecycle — from architecture design and model training to testing and deployment.

| 👤 **Member**      | 💼 **Role**                         | 🧠 **Contributions**                                                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⭐ **Ayush Ghai**  | **Lead Developer & Project Head**    | - Conceived and led the complete SafetySnap project lifecycle.<br>- Designed overall system architecture integrating YOLOv8 with Streamlit.<br>- Managed model training, fine-tuning, and optimization for real-time PPE detection.<br>- Handled backend logic, data flow, and performance tuning.<br>- Conducted model evaluation, testing, and debugging.<br>- Supervised UI/UX design and guided deployment preparation.<br>- Created technical documentation and handled project presentation. |
| **Sumit Agrawal**  | **Frontend & Deployment Engineer**   | - Deployed the Streamlit application on Streamlit Cloud.<br>- Worked on Streamlit UI for image upload and detection result display.<br>- Designed responsive layouts for a better visual experience.<br>- Assisted in final testing and integration for production deployment. |

---

## 🌟 Acknowledgements

- Dataset by [andrewmvd](https://www.kaggle.com/andrewmvd) on Kaggle  
- Huge thanks to **Ultralytics** for YOLOv8  
- **Streamlit** for making deployment so easy  
- Google Colab for free GPUs ❤️  

---

💬 **Enjoyed this project? Give it a ⭐ and share with friends!**

