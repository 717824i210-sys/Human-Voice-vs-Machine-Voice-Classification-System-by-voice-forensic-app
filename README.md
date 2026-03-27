# Human Voice vs Machine Voice Classification System
_A Voice Forensic Application by Team **THE AI ACES**_

---

## 👥 Team Information
**Team Name:** THE AI ACES  

**Team Members:**
- Dhanushya R  
- Haritha A  
- Raghumathi M  
- Ramyadevi C  

---

## 📖 Project Overview
With the rise of AI-generated voices and synthetic speech, distinguishing between **human voice recordings** and **machine-generated voices** has become crucial in fields like **forensics, cybersecurity, and media authenticity verification**.  

This project provides a **web-based application** that allows users to upload an audio file and receive a classification result:  
- **Human Voice**  
- **Machine Voice**  

along with a **confidence score**.

---

## 🎯 Objectives
- Build a forensic tool to identify whether a given audio is genuine human speech or artificially generated.  
- Provide a simple web interface for uploading and analyzing audio files.  
- Integrate machine learning models with a Flask backend and a frontend interface.  

---

## 🏗️ System Architecture

### 1. Frontend (User Interface)
- Built with **HTML, CSS, and JavaScript**.  
- Provides an upload button for `.wav` audio files.  
- Displays the classification result and confidence score.  

### 2. Backend (Flask API)
- Developed using **Flask** (Python web framework).  
- Uses **Flask-CORS** to allow communication between frontend and backend.  
- Exposes an endpoint `/predict` that accepts audio files.  

### 3. Machine Learning Model
- Audio features are extracted using **Librosa**.  
- Features are scaled using **Scikit-learn’s StandardScaler**.  
- A trained ML model (`voice_model.pkl`) predicts whether the voice is human or machine.  
- The model outputs both the **class label** and the **confidence score**.  

---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/717824i210-sys/Human-Voice-vs-Machine-Voice-Classification-System-by-voice-forensic-app.git
cd Human-Voice-vs-Machine-Voice-Classification-System-by-voice-forensic-app
