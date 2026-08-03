import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Machine Learning Models Frontend",
    page_icon="🤖",
    layout="centered"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1{
    color:white;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------

st.title("Machine Learning Models Frontend")

# -------------------------------
# Select Model
# -------------------------------

model = st.selectbox(
    "Select Model",
    [
        "Linear Regression",
        "Logistic Regression",
        "Decision Tree Classifier",
        "Support Vector Machine",
        "K-Nearest Neighbors",
        "Naive Bayes",
        "Decision Tree Regressor",
        "Support Vector Regressor",
        "KNN Regressor"
    ]
)

st.success("Frontend Created Successfully!")

st.subheader(f"Selected Model: {model}")

st.write("Enter feature values here to make predictions.")

# -------------------------------
# Input Fields
# -------------------------------

col1, col2 = st.columns(2)

with col1:
    feature1 = st.number_input("Feature 1", key="f1")
    feature2 = st.number_input("Feature 2", key="f2")
    feature3 = st.number_input("Feature 3", key="f3")

with col2:
    feature4 = st.number_input("Feature 4", key="f4")
    feature5 = st.number_input("Feature 5", key="f5")
    feature6 = st.number_input("Feature 6", key="f6")

# -------------------------------
# Predict Button
# -------------------------------

if st.button("Predict"):
    st.success("Prediction will appear here.")

    st.write("Input Values")

    st.write({
        "Feature 1": feature1,
        "Feature 2": feature2,
        "Feature 3": feature3,
        "Feature 4": feature4,
        "Feature 5": feature5,
        "Feature 6": feature6
    })