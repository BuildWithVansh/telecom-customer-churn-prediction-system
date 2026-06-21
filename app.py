import streamlit as st
import pandas as pd
import joblib

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# =========================
# Load Model
# =========================
model = joblib.load("Model/best_xgb_model.pkl")

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.title("📊 Telecom Churn Project")

    st.markdown("""
    ### Model Information

    **Algorithm:** XGBoost

    **ROC-AUC Score:** 84.91%

    **Developer:** Vansh Gupta

    **Project Type:** Customer Churn Prediction
    """)

# =========================
# Title
# =========================
st.title("📊 Customer Churn Prediction System")
st.markdown("Predict whether a telecom customer is likely to churn.")

# =========================
# Customer Inputs
# =========================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox("Gender", ["Male", "Female"])

    SeniorCitizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

with col2:

    DeviceProtection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    TechSupport = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )

# =========================
# Customer Summary
# =========================
st.subheader("📋 Customer Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:
    st.metric("Contract", Contract)

with summary_col2:
    st.metric("Internet", InternetService)

with summary_col3:
    st.metric("Monthly Charges", f"₹{MonthlyCharges}")

# =========================
# Prediction
# =========================

if st.button("🚀 Predict Churn"):

    data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges]
    })

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    st.subheader("📈 Prediction Results")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    st.progress(int(probability * 100))

    if probability < 0.30:
        risk = "🟢 Low Risk"

    elif probability < 0.70:
        risk = "🟡 Medium Risk"

    else:
        risk = "🔴 High Risk"

    st.info(f"Risk Level: {risk}")

    if prediction == 1:

        st.error(
            f"⚠️ Customer Likely To Churn\n\nProbability: {probability:.2%}"
        )

    else:

        st.success(
            f"✅ Customer Likely To Stay\n\nProbability Of Churn: {probability:.2%}"
        )

    st.subheader("💡 Recommended Action")

    if probability > 0.70:

        st.warning("""
        High Risk Customer

        • Offer Discount
        • Contact Customer Personally
        • Provide Loyalty Benefits
        • Upgrade Service Package
        """)

    elif probability > 0.40:

        st.info("""
        Medium Risk Customer

        • Send Promotional Offers
        • Improve Customer Support
        • Provide Retention Benefits
        """)

    else:

        st.success("""
        Low Risk Customer

        • Customer is likely to stay.
        • Continue regular engagement.
        """)

# =========================
# Footer
# =========================
st.markdown("---")
st.caption(
    "Developed by Vansh Gupta | XGBoost + Streamlit + Power BI + SQL"
)
