import streamlit as st
from student.modeling.predict import getpred
import numpy as np

# Student exam score prediction app
st.title("Student Exam Score Prediction")
st.write("This app predicts the exam score of students based on various factors.")

# Create a form
with st.form(key="prediction_form"):
    st.write("Please enter the following details:")

    # Input fields for each factor
    Hours_Studied = st.number_input(
        "Hours Studied", min_value=0.0, max_value=24.0, step=0.1
    )
    Attendance = st.number_input(
        "Attendance (%)", min_value=0.0, max_value=100.0, step=0.1
    )
    bool_Extracurricular_Activities = st.selectbox(
        "Participates in Extracurricular Activities?", [0, 1]
    )
    Sleep_Hours = st.number_input(
        "Sleep Hours", min_value=0.0, max_value=24.0, step=0.1
    )
    Previous_Scores = st.number_input(
        "Previous Scores", min_value=0.0, max_value=100.0, step=0.1
    )
    bool_Internet_Access = st.selectbox("Has Internet Access?", [0, 1])
    Tutoring_Sessions = st.number_input("Tutoring Sessions", min_value=0, step=1)
    School_Type_Private = st.selectbox("Private School?", [0, 1])
    School_Type_Public = st.selectbox("Public School?", [0, 1])
    Physical_Activity = st.number_input(
        "Physical Activity (hours/week)", min_value=0.0, step=0.1
    )
    numeric_Parental_Education_Level = st.number_input(
        "Parental Education Level (numeric)", min_value=0.0, step=0.1
    )
    numeric_Distance_from_Home = st.number_input(
        "Distance from Home (km)", min_value=0.0, step=0.1
    )
    numeric_Parental_Involvement = st.number_input(
        "Parental Involvement (numeric)", min_value=0.0, step=0.1
    )
    numeric_Access_to_Resources = st.number_input(
        "Access to Resources (numeric)", min_value=0.0, step=0.1
    )
    numeric_Motivation_Level = st.number_input(
        "Motivation Level (numeric)", min_value=0.0, step=0.1
    )
    numeric_Family_Income = st.number_input(
        "Family Income (numeric)", min_value=0.0, step=0.1
    )
    numeric_Teacher_Quality = st.number_input(
        "Teacher Quality (numeric)", min_value=0.0, step=0.1
    )
    numeric_Peer_Influence = st.number_input(
        "Peer Influence (numeric)", min_value=0.0, step=0.1
    )
    numeric_Learning_Disabilities = st.number_input(
        "Learning Disabilities (numeric)", min_value=0.0, step=0.1
    )

    # create a ndarray with the variables
    input_data = [
        Hours_Studied,
        Attendance,
        bool_Extracurricular_Activities,
        Sleep_Hours,
        Previous_Scores,
        bool_Internet_Access,
        Tutoring_Sessions,
        School_Type_Private,
        School_Type_Public,
        Physical_Activity,
        numeric_Parental_Education_Level,
        numeric_Distance_from_Home,
        numeric_Parental_Involvement,
        numeric_Access_to_Resources,
        numeric_Motivation_Level,
        numeric_Family_Income,
        numeric_Teacher_Quality,
        numeric_Peer_Influence,
        numeric_Learning_Disabilities,
    ]

    # Convert it into a 2D numpy array
    X_input = np.array([input_data])

    # Submit button
    submit_button = st.form_submit_button(label="Predict")

# Handle form submission
if submit_button:
    st.write("Form submitted! Use the input values for prediction.")
    prediction = getpred(X_input)
    st.markdown(f"Predicted Exam Score: {prediction}")

import os

os.getcwd()
