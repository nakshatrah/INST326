import unittest 
import pandas as pd
import matplotlib.pyplot as plt
from models import UserProfile, DiabetesRiskCalculator, RiskAssessmentSystem 

    
def load_data(file_path):
    """
    Loads a CSV file containing the diabetes dataset into the Dataframe

    Args:
        - file_path: path to CSV file
    
    Returns: 
        - The dataframe containing the loaded data
    """
    return pd.read_csv(file_path)

def classify_row(row, diabetes_calculator):
    """
    Classifies the risk level for each row of user data

    Args:
        - row: a row from the dataset containing user information
        - diabetes_calculator(DiabetesRiskCalculator): An instance of the calculator used to asses the risk

    Returns:
        - A string of the diabetes risk classification
    """
    profile = UserProfile(
        age=row["Age"],
        height=5.5,
        weight=150,
        physical_activity=row["Physical Activity"],
        family_history=row["Family History"].strip().lower() == "yes",
        genetic_marker=row["Genetic Markers"].strip().lower() == "positive",)
    return diabetes_calculator.assess(profile)
                       
if __name__ == "__main__": 
    dataset = load_data("diabetes_dataset.csv")

    age = int(input("Enter your age: "))
    physical_activity = input("Enter your physical activiity (Low/Moderate/High): ")
    family_history_input = input("Do you have a family history of diabetes? (yes/no): ").strip().lower()
    genetic_marker_input = input("Do you have genetic markers for diabetes? (yes/no): ").strip().lower()
    height = float(input("Enter your height in feet (ex: 5.8): "))
    weight = float(input("Enter your weight in pounds: "))

    family_history = family_history_input == "yes"
    genetic_marker = genetic_marker_input == "yes"

    height_inches = height * 12
    bmi = (weight / (height_inches ** 2)) * 703

    user = UserProfile(age=age, physical_activity=physical_activity, family_history=family_history, genetic_marker=genetic_marker, height=height, weight=weight)

    diabetes_calculator = DiabetesRiskCalculator(dataset)
    diabetes_risk = diabetes_calculator.assess(user)

    print("\n--- Health Report ---")
    print(f"Age: {user.age}")
    print(f"Physical Activity: {user.physical_activity}")
    print(f"Diabetes Risk: {diabetes_risk}")
    print(f"BMI: {user.calculate_bmi():.2f}")
    print("\nRecommendations:")
    for rec in user.get_recommendations():
        print(f"- {rec}")

    system = RiskAssessmentSystem(user, dataset)
    similar_cases = system.find_similar_cases(top_n=3)
    print("\nSimilar Cases From Dataset:")

    if not similar_cases.empty:
        print(similar_cases.to_string(index=False))
    else:
        print("There were no other similar cases to your's in the dataset")

dataset["Diabetes Risk Level"] = dataset.apply(lambda row: classify_row(row, diabetes_calculator), axis=1)


risk_counts= dataset["Diabetes Risk Level"].value_counts()



risk_counts.plot(
    kind="bar",
    stacked="True",
    color=["green","red","blue"],
    edgecolor="black",
    figsize=(8,5)
)


plt.title=("Diabetes Risk by Physical Activity Level")
plt.xlabel("Physical Activity Level")
plt.ylabel("Number of people")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()