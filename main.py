import unittest
import pandas as pd
from models import UserProfile, DiabetesRiskCalculator, HeartDiseaseRiskCalculator, RiskAssessmentSystem

    
def load_data(file_path):
    return pd.read_csv(file_path)
                       
if __name__ == "__main__": 
    dataset = load_data(r"C:\Users\naksh\OneDrive\Desktop\INST 326\finalproject\INST326\diabetes_dataset.csv")

    user = UserProfile(age = 35, ethnicity = "Hispanic", family_history = True, genetic_marker = True)


