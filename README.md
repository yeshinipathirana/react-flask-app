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
* instructions
* result
* ℹ️ About

Each tab is designed to provide intuitive navigation similar to real healthcare applications.

> ⚠️ Note: The tab styling and icons were planned but could not be fully implemented due to development constraints.

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




## 🧪 Machine Learning Model

* **Algorithm:** Logistic Regression
* **Preprocessing:** StandardScaler
* **Evaluation Metrics:**

  * Accuracy
  * Classification Report
* **Model Output:**

  * Binary classification (Risk / No Risk)
  * Probability score




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







