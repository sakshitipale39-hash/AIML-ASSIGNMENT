# 🤖 Machine Learning Multi-Model Prediction System

## 📌 Project Overview

This project is developed as part of the Applied Machine Learning (AML) assignment.

It includes:

- Classification Models
- Regression Models
- Streamlit Web Application
- Model Saving using Joblib

The application allows users to select any trained Machine Learning model and make predictions using a simple web interface.

---

# 📂 Project Structure

```
AML_PROJECT/
│
├── app.py
├── README.md
├── requirements.txt
│
├── heart(7).csv
├── insurancee(8).csv
│
├── models/
│   ├── logistic.pkl
│   ├── decision_tree_classifier.pkl
│   ├── svm_classifier.pkl
│   ├── knn_classifier.pkl
│   ├── naive_bayes.pkl
│   ├── linear_regression.pkl
│   ├── decision_tree_regressor.pkl
│   ├── svr.pkl
│   ├── knn_regressor.pkl
│   ├── heart_scaler.pkl
│   ├── insurance_scaler.pkl
│   ├── heart_columns.pkl
│   └── insurance_columns.pkl
```

---

# 📊 Datasets Used

## Classification Dataset

Heart Disease Dataset

Target Variable

```
HeartDisease
```

Features

- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope

---

## Regression Dataset

Medical Insurance Dataset

Target Variable

```
charges
```

Features

- age
- sex
- bmi
- children
- smoker
- region

---

# 🧠 Classification Models

- Logistic Regression
- Decision Tree Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes

Evaluation Metrics

- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1 Score

---

# 📈 Regression Models

- Linear Regression
- Decision Tree Regressor
- Support Vector Regressor
- KNN Regressor

Evaluation Metric

- R² Score

---

# 💾 Saved Models

Classification

- logistic.pkl
- decision_tree_classifier.pkl
- svm_classifier.pkl
- knn_classifier.pkl
- naive_bayes.pkl

Regression

- linear_regression.pkl
- decision_tree_regressor.pkl
- svr.pkl
- knn_regressor.pkl

---

# ⚙️ Libraries Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

# 🚀 Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

# 🌐 Frontend Features

✔ Dark Theme

✔ Model Selection Dropdown

✔ Classification Prediction

✔ Regression Prediction

✔ User Friendly Interface

✔ Prediction Button

---

# 📌 Workflow

1. Load Dataset

2. Data Cleaning

3. Encoding

4. Feature Scaling

5. Train Test Split

6. Train Machine Learning Models

7. Evaluate Models

8. Save Models (.pkl)

9. Build Streamlit Frontend

10. Make Predictions

---

# 📊 Machine Learning Algorithms

Classification

- Logistic Regression
- Decision Tree
- SVM
- KNN
- Naive Bayes

Regression

- Linear Regression
- Decision Tree Regressor
- SVR
- KNN Regressor

---

# 👩‍💻 Developed By

**Name:** Sakshi Tipale

**Course:** Applied Machine Learning (AML)

**Project:** Multi-Model Machine Learning Prediction System

---

# ⭐ Thank You
