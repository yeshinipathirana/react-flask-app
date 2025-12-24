# react flask app



---

# 🫀 Heart Disease Prediction Mobile Application

## 📌 Project Overview

This project is a **Heart Disease Prediction System** developed as an academic project using **Machine Learning**, **Flask backend**, and **React Native (Expo)** frontend. The system predicts the likelihood of heart disease based on clinical input parameters using the **UCI Cleveland Heart Disease dataset**.

The application follows a **real-world healthcare mobile app design**, including user guidance, ethical disclaimers, and modular navigation.

---

## 🎯 Objectives

* To apply machine learning techniques for heart disease risk prediction
* To deploy the trained model via a RESTful API
* To build a mobile-friendly user interface using React Native
* To follow ethical guidelines for health-related applications

---

## 🧠 Dataset

* **Name:** UCI Cleveland Heart Disease Dataset
* **Source:** Kaggle (UCI Repository version)
* **Target Variable:** `target`

  * `1` → Presence of heart disease
  * `0` → No heart disease

---

## 🏗️ System Architecture

```
User (Mobile App)
        |
        |  HTTP POST (JSON)
        v
React Native (Expo)
        |
        |  REST API
        v
Flask Backend
        |
        |  Trained ML Model
        v
Prediction Result
```

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask (REST API)
* Scikit-learn (Logistic Regression)
* Pandas, NumPy
* Joblib (Model persistence)

### Frontend

* React Native
* Expo Router
* Expo Go (Android testing)
* AsyncStorage (Local data storage – planned)

---

## 📱 Mobile Application Features

### 1️⃣ Bottom Tab Navigation (Planned)

The mobile application is designed to include a **professional bottom tab navigation bar** using Expo Router Tabs.

**Planned Tabs:**

* 🏠 Home
* 📝 Predict
* 📊 History
* ℹ️ About

Each tab is designed to provide intuitive navigation similar to real healthcare applications.

> ⚠️ Note: The tab styling and icons were planned but could not be fully implemented due to development constraints.

---

### 2️⃣ Icons for Navigation (Planned)

Each tab is designed to include meaningful icons to enhance usability:

| Tab     | Icon (Planned)        |
| ------- | --------------------- |
| Home    | 🏠 Home icon          |
| Predict | ❤️ Pulse / Heart icon |
| History | ⏱ Time icon           |
| About   | ℹ️ Information icon   |

Icons were planned using **Ionicons from @expo/vector-icons**.

---

### 3️⃣ Prediction History (Planned Feature)

The application design includes a **prediction history feature**, allowing users to:

* View previous prediction results
* See probability scores
* View date and time of prediction
* Clear history when required

**Planned Storage Method:**

* Local storage using `AsyncStorage`

> ⚠️ Due to time and environment limitations, this feature is documented as a planned enhancement.

---

### 4️⃣ Image Integration (Planned)

The UI design includes healthcare-related images such as:

* Heart illustration on Home screen
* Result status visual indicators (Low/High Risk)

Images are stored in:

```
assets/images/
```

> Images are included for visual enhancement and user engagement.

---

## 🧪 Machine Learning Model

* **Algorithm:** Logistic Regression
* **Preprocessing:** StandardScaler
* **Evaluation Metrics:**

  * Accuracy
  * Classification Report
* **Model Output:**

  * Binary classification (Risk / No Risk)
  * Probability score

---

## 🔐 Ethical Considerations

* The application **does NOT provide medical advice**
* Predictions are for **educational purposes only**
* Users are advised to consult qualified healthcare professionals
* Clear disclaimers are included in the UI design

---

## ▶️ How to Run the Project

### Backend

```bash
cd backend
venv\Scripts\activate   # Windows
python app.py
```

### Frontend

```bash
cd mobile
npx expo start -c
```

Open the app using **Expo Go** on an Android device.

---

## 📘 Limitations

* Prediction history and icons are documented but not fully implemented
* Model accuracy depends on dataset limitations
* Application is not intended for clinical diagnosis

---

## 🚀 Future Enhancements

* Full implementation of prediction history
* Enhanced UI with charts and animations
* User authentication
* Cloud deployment of backend
* APK generation for Play Store

---

## 🎓 Academic Declaration

This project was developed **solely for academic and educational purposes** as part of coursework requirements. All datasets and libraries used are publicly available.

---

## 👨‍💻 Author

**Student Project – Machine Learning & Mobile Application Development**

---

### ✅ Viva Tip (You can say this confidently)

> “Some advanced UI and persistence features were designed and documented
> but not fully implemented due to time constraints. However, the system
> architecture and codebase fully support future integration.”

---

If you want, next I can:

* Rewrite this README in **more academic tone**
* Add **screenshots placeholders**
* Create a **submission-ready PDF**
* Prepare **viva Q&A from this project**

Just tell me 👍


