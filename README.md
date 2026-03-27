# 🎧 Human Voice vs Machine Voice Classification System
🚀 An Intelligent Offline AI Solution to Detect Human vs AI-Generated Voices  

---

## 👥 Team Information
**Team Name:** THE AI ACES  

**Team Members:**
- Dhanushya R  
- Haritha A  
- Raghumathi M  
- Ramyadevi C  

---

## 🌟 Overview
This project is a **Voice Forensic Application** designed to distinguish between **Human Voice** and **Machine-Generated Voice**.  
It uses **Machine Learning** and **Audio Signal Processing** techniques to analyze speech patterns and classify audio files with confidence scores.  
The system also supports **live audio input**, **sentiment analysis**, and generates **forensic reports**.  

---

## 📊 Dataset & Preprocessing
- **Dataset Path:** `C:\Users\dhanu\THE AI ACES\human-nonhuman`  
- **Human Audio Samples:** 1001  
- **Machine Audio Samples:** 1000  
- **Total Samples:** 2001  
- **Feature Shape:** `(2001, 8000)`  
- **Labels Shape:** `(2001,)`  
- **Format:** `.wav`  

✅ Preprocessing Completed Successfully.  
Features extracted using **MFCCs** and normalized for training.  

---

## 🧪 Model Training & Results
We trained and evaluated multiple models. Below are the results:

| Model                | Accuracy  | Precision | Recall   | Example Prediction | Confidence | Final Decision   |
|-----------------------|-----------|-----------|----------|--------------------|------------|-----------------|
| Logistic Regression   | 0.7656    | 0.7903    | 0.7277   | Human Voice        | 0.68       | Needs Review    |
| SVM                   | 0.8628    | 0.8930    | 0.8267   | Human Voice        | 0.88       | High Confidence |
| Random Forest         | 0.8204    | 0.8532    | 0.7772   | Human Voice        | 0.67       | Needs Review    |
| KNN                   | 0.8254    | 0.8707    | 0.7673   | Machine Voice      | 0.80       | Needs Review    |
| Decision Tree         | 0.7107    | 0.7171    | 0.7029   | Human Voice        | 1.00       | High Confidence |

---

### 🏆 Best Performing Model
- **SVM (Support Vector Machine)**  
- **Accuracy:** 0.8628  
- **Precision:** 0.8930  
- **Recall:** 0.8267  
- ✅ Selected as the final model for deployment.  

---

## 🎤 Real-Time Monitoring
The system supports **live audio input** via microphone:  

- 🚨 **Alert:** Machine Voice Detected! Confidence: 93.19%  
- ✅ **Human Voice:** Confidence: 72.57%  
- **File Example:** `C:\Users\dhanu\THE AI ACES\human-nonhuman\human\bloqRTe69CA3IAitQ-0_0NldbEsEKhus.mp3`  
- **Deepfake Detector Result:** ✅ Likely Genuine Human Voice  
- 📄 **Report Generated:** `forensic_report.pdf`  

---

## 🖥️ Application Features
- Upload `.wav` audio file  
- Automatic preprocessing and feature extraction  
- Classification as **Human Voice** or **Machine Voice**  
- Confidence score display  
- Real-time monitoring with microphone input  
- Sentiment analysis integration  
- Forensic report generation (`forensic_report.pdf`)  

---

## ⚙️ Tech Stack
- 🐍 Python  
- 📊 Scikit-learn  
- 🎧 Librosa  
- 🌐 Flask  
- 🤖 TensorFlow / Keras  
- 🛠️ Joblib  

---

## 🚀 Getting Started
### 🛠️ Installation
```bash
pip install -r requirements.txt

## 🚀 Run the Project
## ▶️ Training
```bash
python train.py

##Start backend
python app.py

🌐 Open in Browser
http://127.0.0.1:5000

📁 Project Structure
voice-forensic-app/
│── dataset/             # Audio dataset (human-nonhuman)
│── models/              # Trained models
│── backend/
│   ├── app.py           
│   ├── voice_model.pkl  # Saved ML model
│   ├── voice_scaler.pkl # Saved scaler
│── train.py             # Training script
│── requirements.txt     # Dependencies
│── utils.py             # Helper functions


