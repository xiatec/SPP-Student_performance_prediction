import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def main():
    st.title("Student Exam Performance Predictor")

    # Input fields
    gender = st.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox("Parental Level of Education", 
        ["bachelor's degree", "some college", "master's degree", "associate's degree", "high school", "some high school"])
    lunch = st.selectbox("Lunch", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.number_input("Reading Score", min_value=0, max_value=100)
    writing_score = st.number_input("Writing Score", min_value=0, max_value=100)

    if st.button("Predict Math Score"):
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )
        pred_df = data.get_data_as_data_frame()
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        st.success(f"The predicted math score is: {results[0]:.2f}")

if __name__ == "__main__":
    main()