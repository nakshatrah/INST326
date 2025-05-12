import unittest
import pandas as pd
import matplotlib.pyplot as plt
from models import UserProfile, DiabetesRiskCalculator, RiskAssessmentSystem 

    
def load_data(file_path):
    ##ADD DOCSTRINGs
    return pd.read_csv(file_path)
                       
if __name__ == "__main__": 
    dataset = load_data("diabetes_dataset.csv")

    user = UserProfile(age = 35, ethnicity = "Hispanic", family_history = True, genetic_marker = True)

    age = int(input("Enter your age: "))
    ethnicity = input("Enter your ethnicity: ")
    family_history_input = input("Do you have a family history of diabetes? (yes/no): ").strip().lower()
    genetic_marker_input = input("Do you have genetic markers for diabetes? (yes/no): ").strip().lower()

    family_history = family_history_input == "yes"
    genetic_marker = genetic_marker_input == "yes"

    user = UserProfile(age=age, ethnicity=ethnicity, family_history=family_history, genetic_marker=genetic_marker)

    diabetes_calculator = DiabetesRiskCalculator(dataset)
    diabetes_risk = diabetes_calculator.assess(user)


    # User's results are outputted
    print("\nThanks for using our program! Here are your risk assessment results:")
    print(f"Diabetes Risk: {diabetes_risk}")

    # Finds similar cases to the user
    system = RiskAssessmentSystem(user, dataset)
    similar_cases = system.find_similar_cases(top_n=3)
    print("\nSimilar Cases From Dataset:")

    if not similar_cases.empty:
        print(similar_cases.to_string(index=False))
    else:
        print("There were no other similar cases to your's in the dataset")


def classify_row(row):
    ### ADDD DOCSTRINGS
    profile =UserProfile(
        age=row["Age"],
        ethnicity=row["Ethnicity"],
        family_history=row["Family History"].strip().lower()== "yes",
        genetic_marker=row["Genetic Markers"].strip().lower()== "positive"
    )
    return diabetes_calculator.assess(profile)

dataset["Diabetes Risk Level"]= dataset.apply(classify_row, axis=1)
ethnicity_counts= dataset["Diabetes Risk Level"].value_counts()
plt.figure(figsize=(8,5))
ethnicity_counts.plot(kind="bar", color="skyblue", edgecolor="black")

plt.title=("Diabetes Risk Distribution")
plt.xlabel("Risk Level")
plt.ylabel("Number of people")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()