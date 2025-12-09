# ❤️ Heart Disease Prediction App

A web-based **Heart Disease Prediction System** built using **K-Nearest Neighbors (KNN)** and deployed using **Streamlit**. This app allows users to enter basic medical parameters and instantly check whether a person is at **risk of heart disease or not**.

---

## 🚀 Features

* ✅ User-friendly Streamlit UI
* ✅ Clear explanations for all medical inputs (0/1/2 values explained)
* ✅ KNN-based Machine Learning model
* ✅ Real-time prediction
* ✅ Deployed using Streamlit Cloud

---

## 🧠 Machine Learning Model

* Algorithm: **K-Nearest Neighbors (KNN)**
* Accuracy Achieved: **~87%**
* Trained using cleaned and preprocessed Heart Disease dataset
* Model saved using **Pickle (`.pkl`)**

---

## 📊 Input Features Used

The model takes the following **11 medical inputs**:

| Feature  | Description                                 |
| -------- | ------------------------------------------- |
| age      | Patient age                                 |
| sex      | 0 = Female, 1 = Male                        |
| cp       | Chest pain type (0–3)                       |
| trestbps | Resting blood pressure                      |
| chol     | Cholesterol level                           |
| fbs      | Fasting blood sugar (>120 mg/dl)            |
| thalach  | Maximum heart rate                          |
| exang    | Exercise induced angina                     |
| oldpeak  | Heart stress level after exercise           |
| ca       | Number of major blood vessels blocked (0–3) |
| thal     | Thalassemia scan result                     |

---

## 🛠 Tech Stack

* **Python**
* **Streamlit** (for UI)
* **Scikit-learn** (for KNN model)
* **NumPy**
* **Pandas**

---

## 📂 Project Structure

```
📦 Heart-Disease-Prediction-App
 ┣ 📄 app.py
 ┣ 📄 heart_model.pkl
 ┣ 📄 requirements.txt
 ┣ 📄 README.md
```

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/harish-kush/Heart_Disease-predictor.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```


## ✅ Output

* ✅ **Low Risk: No Heart Disease**
* ⚠️ **High Risk: Heart Disease Detected**

---

## 👨‍💻 Author

**Harish Kushwaha**


This project is for **educational purposes only** and should not be used as a medical diagnosis tool.
