# 📊 Telecom Customer Churn Prediction System

An end-to-end Data Analytics and Machine Learning project designed to identify telecom customers who are likely to churn. The project combines data analysis, SQL-based business insights, predictive modeling using XGBoost, an interactive Power BI dashboard, and a deployed Streamlit application for real-time predictions.

---

## 🚀 Live Demo

**Streamlit Application**
https://telecom-customer-churn-prediction-system-dz29tru4afjkcp4mw3hqv.streamlit.app/

**GitHub Repository**
https://github.com/BuildWithVansh/telecom-customer-churn-prediction-system

---

## 📌 Business Problem

Customer churn is a major challenge in the telecom industry because acquiring new customers is significantly more expensive than retaining existing ones.

The objective of this project is to:

* Identify customers at risk of churning.
* Understand key factors driving churn.
* Generate business insights for customer retention.
* Build a predictive model that supports data-driven decision making.

---

## 🛠️ Technologies Used

### Data Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Power BI
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost
* GridSearchCV

### Database

* SQL

### Deployment

* Streamlit Cloud

### Version Control

* Git & GitHub

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

**Total Customers:** 7,043

### Key Features

**Customer Information**

* Gender
* Senior Citizen
* Partner
* Dependents

**Service Information**

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies

**Account Information**

* Tenure
* Contract Type
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

**Target Variable**

* Churn

---

## 🔄 Project Workflow

Data Collection
⬇
Data Cleaning & Preprocessing
⬇
Exploratory Data Analysis
⬇
Feature Engineering
⬇
Model Training
⬇
Hyperparameter Tuning
⬇
SQL Business Analysis
⬇
Power BI Dashboard Development
⬇
Streamlit Deployment

---

## 🧹 Data Preprocessing

The following preprocessing steps were applied before model training:

* Missing value handling
* Data type correction
* One-Hot Encoding
* Feature Scaling using StandardScaler
* ColumnTransformer Pipeline
* Class imbalance handling
* Train-Test Split

---

## 🤖 Machine Learning Models

### Logistic Regression

Used as the baseline model.

### XGBoost Classifier

Used as the final model because it achieved the best overall performance.

---

## ⚙️ Hyperparameter Tuning

GridSearchCV was used to optimize the XGBoost model.

### Best Parameters

```python
learning_rate = 0.01
max_depth = 3
n_estimators = 500
```

### Best ROC-AUC Score

```text
84.91%
```

---

## 📈 Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 74.3%  |
| Precision | 51%    |
| Recall    | 82%    |
| F1 Score  | 63%    |
| ROC-AUC   | 84.91% |

### Why Recall Matters

In churn prediction, identifying customers who are likely to leave is more important than maximizing accuracy alone.

The model achieved a recall of **82%**, meaning it successfully identified most customers who were at risk of churning.

---

## 📊 Power BI Dashboard

An interactive Power BI dashboard was created to explore churn trends and customer behavior.

### Dashboard Features

* Total Customers
* Churned Customers
* Churn Rate
* Retention Rate
* Revenue Analysis
* Contract Analysis
* Payment Method Analysis
* Internet Service Analysis
* Tenure Analysis
* Dynamic Filtering

### Dashboard Preview

![Dashboard](Screenshots/dashboard.png)

---

## 💻 Streamlit Application

A web application was developed to make predictions in real time.

### Features

* Customer Information Form
* Churn Prediction
* Churn Probability Estimation
* Risk Classification
* Business Recommendations
* Interactive User Interface

### Application Screenshots

#### Customer Input Form

![App](Screenshots/streamlit_app_1.png)

#### Prediction Interface

![App](Screenshots/streamlit_app_2.png)

#### Prediction Result

![App](Screenshots/streamlit_app_3.png)

---

## 🗄️ SQL Analysis

SQL was used to perform business-focused analysis on customer churn patterns.

### Analyses Performed

* Churn Rate Analysis
* Contract Type Analysis
* Payment Method Analysis
* Revenue Analysis
* Customer Segmentation
* High-Risk Customer Identification

---

## 🔍 Key Business Insights

* Overall churn rate is 26.54%.
* Month-to-month contracts have the highest churn rate.
* Electronic Check customers churn more frequently than other payment groups.
* Fiber Optic users show higher churn behavior.
* Customers with shorter tenure are more likely to leave.
* Long-term contracts improve customer retention significantly.

---

## 💡 Business Recommendations

### Improve Contract Retention

Encourage customers to move from month-to-month plans to long-term contracts.

### Target High-Risk Customers

Use churn predictions to launch personalized retention campaigns.

### Enhance Customer Experience

Investigate service quality concerns among Fiber Optic customers.

### Payment Strategy Optimization

Offer incentives to customers using Electronic Check payment methods.

### Loyalty Programs

Reward long-term customers through discounts and loyalty benefits.

---

## 📁 Repository Structure

```text
telecom-customer-churn-prediction-system/

├── Dashboard/
├── Data/
├── Model/
├── Notebooks/
├── SQL/
├── Screenshots/
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* SHAP Explainability
* Feature Importance Dashboard
* Customer Segmentation
* Automated Retention Recommendation Engine
* API Integration
* Model Monitoring

---

## 👨‍💻 Author

### Vansh Gupta

B.Tech (Electronics & Communication Engineering)

Aspiring Data Analyst | Machine Learning Enthusiast

GitHub:
https://github.com/BuildWithVansh

LinkedIn:
https://www.linkedin.com/in/vansh-gupta-b80456276

---

⭐ If you found this project useful, consider giving the repository a star.
