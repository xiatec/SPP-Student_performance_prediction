import Mygradio as gr
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def predict_math_score(gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
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
    
    return f"The predicted math score is: {results[0]:.2f}"

iface = gr.Interface(
    fn=predict_math_score,
    inputs=[
        gr.Dropdown(["male", "female"], label="Gender"),
        gr.Dropdown(["group A", "group B", "group C", "group D", "group E"], label="Race/Ethnicity"),
        gr.Dropdown(["bachelor's degree", "some college", "master's degree", "associate's degree", "high school", "some high school"], label="Parental Level of Education"),
        gr.Dropdown(["standard", "free/reduced"], label="Lunch"),
        gr.Dropdown(["none", "completed"], label="Test Preparation Course"),
        gr.Number(label="Reading Score"),
        gr.Number(label="Writing Score")
    ],
    outputs="text",
    title="Student Exam Performance Predictor",
    description="Enter student details to predict their math score."
)

if __name__ == "__main__":
    iface.launch()