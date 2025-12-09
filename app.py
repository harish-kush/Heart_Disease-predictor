import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("heart_model.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Prediction App")
st.write("Fill patient details below. All values are explained for easy understanding.")

st.markdown("---")

# ===== INPUT FIELDS WITH CLEAR MEANING =====

age = st.number_input("🧓 Age (Patient ki umar)", 1, 120, 25)

sex = st.radio(
    "👤 Gender",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.selectbox(
    "💥 Chest Pain Type",
    [0, 1, 2, 3],
    format_func=lambda x: {
        0: "Typical Chest Pain (Heart related)",
        1: "Mild Chest Pain",
        2: "Non-heart Chest Pain",
        3: "No Chest Pain"
    }[x]
)

trestbps = st.number_input(
    "🩺 Resting Blood Pressure (BP when resting)",
    80, 200, 120
)

chol = st.number_input(
    "🧈 Cholesterol Level (mg/dL)",
    100, 600, 200
)

fbs = st.radio(
    "🍬 Fasting Blood Sugar > 120 mg/dL ?",
    options=[0, 1],
    format_func=lambda x: "No (Normal)" if x == 0 else "Yes (High Sugar)"
)

thalach = st.number_input(
    "🏃 Maximum Heart Rate Achieved",
    60, 250, 150
)

exang = st.radio(
    "🏋️ Exercise se Chest Pain hota hai?",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

oldpeak = st.number_input(
    "📉 Oldpeak (Heart stress level after exercise)\n\n• 0 = No stress\n• Higher value = More heart stress",
    0.0, 10.0, 1.0
)

ca = st.selectbox(
    "🫀 Major Blood Vessels Blocked",
    [0, 1, 2, 3],
    format_func=lambda x: {
        0: "0 Vessel Blocked",
        1: "1 Vessel Blocked",
        2: "2 Vessels Blocked",
        3: "3 Vessels Blocked"
    }[x]
)

thal = st.selectbox(
    "🧪 Thalassemia (Heart Scan Result)",
    [1, 2, 3],
    format_func=lambda x: {
        1: "Normal",
        2: "Fixed Defect",
        3: "Reversible Defect"
    }[x]
)

# ✅ Same order as model training (11 FEATURES)
input_data = np.array([[age, sex, cp, trestbps, chol,
                        fbs, thalach, exang,
                        oldpeak, ca, thal]])

st.markdown("---")

# ====== PREDICTION BUTTON ======
if st.button("🔍 Predict Heart Disease"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: Person may have Heart Disease")
    else:
        st.success("✅ Low Risk: Person does NOT have Heart Disease")
