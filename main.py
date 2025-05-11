import unittest
import pandas as pd
from models import UserProfile, DiabetesRiskCalculator, HeartDiseaseRiskCalculator, RiskAssessmentSystem

    
def load_data(file_path):
    return pd.read_csv(file_path)
                       
if __name__ == "__main__": 
    dataset = load_data(r"C:\Users\naksh\OneDrive\Desktop\INST 326\finalproject\INST326\diabetes_dataset.csv")

    age = int(input("Enter your age: "))
    ethnicity = input("Enter your ethnicity: ")
    family_history_input = input("Do you have a family history of diabetes or heart disease? (yes/no): ").strip().lower()
    genetic_marker_input = input("Do you have genetic markers for diabetes or heart disease? (yes/no): ").strip().lower()

    family_history = family_history_input == "yes"
    genetic_marker = genetic_marker_input == "yes"

    user = UserProfile(age=age, ethnicity=ethnicity, family_history=family_history, genetic_marker=genetic_marker)

    diabetes_calculator = DiabetesRiskCalculator(dataset)
    heart_disease_calculator = HeartDiseaseRiskCalculator(dataset)
    diabetes_risk = diabetes_calculator.assess(user)
    heart_disease_risk = heart_disease_calculator.assess(user)


    # Adding this print statement to test; need to see the results and check is the risk is calculated correctly
    print("Thanks for using our program! Here are your risk assessment results:")
    print(f"Diabetes Risk: {diabetes_risk}")
    print(f"Heart Disease Risk: {heart_disease_risk}")

    # Testing our new feature for finding similar cases below:
    system = RiskAssessmentSystem(user, dataset)
    similar_cases = system.find_similar_cases(top_n=3)
    print("\nSimilar Cases From Dataset:")
    print(similar_cases.to_string(index=False))