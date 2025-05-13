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
                       
if __name__ == "__main__": 
    dataset = load_data("diabetes_dataset.csv")

    user = UserProfile(age = 35, physical_activity = "Physical Activity", family_history = True, genetic_marker = True)

    age = int(input("Enter your age: "))
    physical_activity = input("Enter your physical activiity (Low/Moderate/High): ")
    family_history_input = input("Do you have a family history of diabetes? (yes/no): ").strip().lower()
    genetic_marker_input = input("Do you have genetic markers for diabetes? (yes/no): ").strip().lower()
    height = float(input("Enter your height in feet (ex: 5.8): "))
    weight = float(input("Enter your weight in pounds: "))

    family_history = family_history_input == "yes"
    genetic_marker = genetic_marker_input == "yes"

    user = UserProfile(age=age, physical_activity=physical_activity, family_history=family_history, genetic_marker=genetic_marker, height=height, weight=weight)

    diabetes_calculator = DiabetesRiskCalculator(dataset)
    diabetes_risk = diabetes_calculator.assess(user)

    print("\n--- Health Report ---")
    print(f"Age: {user.age}")
    print(f"Physical Activity: {user.physical_activity}")
    print(f"Diabetes Risk: {diabetes_risk}")
    print(f"BMI: {user.calculate_bmi():.2f}")
    print("\nRecommendations:")
    for rec in user.get_recommendtaions():
        print(f"- {rec}")

    system = RiskAssessmentSystem(user, dataset)
    similar_cases = system.find_similar_cases(top_n=3)
    print("\nSimilar Cases From Dataset:")

    if not similar_cases.empty:
        print(similar_cases.to_string(index=False))
    else:
        print("There were no other similar cases to your's in the dataset")


def classify_row(row):
    """
    Grabs the data from each row from the dataset

    Args:
        - row: grabs the row from the datset containing the specific attribute
    
    Returns:
        - Risk assesment Results
    """
    profile =UserProfile(
        age=row["Age"],
        physical_activity=row["Physical Activity"],
        family_history=row["Family History"].strip().lower()== "yes",
        genetic_marker=row["Genetic Markers"].strip().lower()== "positive"
    )
    return diabetes_calculator.assess(profile)

dataset["Diabetes Risk Level"]= dataset.apply(classify_row, axis=1)


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