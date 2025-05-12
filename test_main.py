""" This file contains the unit tests for the risk assessment system classes. 

This module holds the test for UserProfile, DiabetesRiskCalculator, and RiskAssessmentSystem. These tests helped us validate our structure to check that the methods are functional. 
"""

import unittest
import pandas as pd
from models import UserProfile, RiskCalculator, DiabetesRiskCalculator, RiskAssessmentSystem

sample_data = pd.DataFrame([
    {
        "Target": "Type 1 Diabetes",
        "Genetic Markers": "Positive",
        "Autoantibodies": "Negative",
        "Family History": "Yes",
        "Environmental Factors": "Present",
        "Insulin Levels": 35,
        "Age": 36,
        "BMI": 24,
        "Physical Activity": "High",
        "Dietary Habits": "Healthy",
        "Blood Pressure": 120,
        "Cholesterol Levels": 180,
        "Waist Circumference": 32,
        "Blood Glucose Levels": 100,
        "Ethnicity": "Hispanic"
    },
    {
        "Target": "Type 2 Diabetes",
        "Genetic Markers": "Negative",
        "Family History": "No",
        "Age": 60,
        "Ethnicity": "Black"
    }
])

class TestUserProfile(unittest.TestCase):
    """Purpose: These are the tests for the UserProfile class. The return should be "OK" if it runs properly. """
    def test_summary(self):
        user = UserProfile(24, "Hispanic", True, True)
        summary = user.get_summary()
        self.assertIn("Age: 24", summary)
        self.assertIn("Family History: Yes", summary)

    def test_risk_factors(self):
        user1 = UserProfile(40, "White", False, False)
        self.assertFalse(user1.has_risk_factors())
        user2 = UserProfile(40, "White", True, False)
        self.assertTrue(user2.has_risk_factors())


class TestDiabetesRiskCalculator(unittest.TestCase):
    """Purpose: These are the tests for the DiabetesRiskCalculator class. The return should be "OK" if it runs properly. """
    def test_score(self):
        user = UserProfile(50, "Asian", True, False)
        calc = DiabetesRiskCalculator(sample_data)
        score = calc.calculate_score(user)
        self.assertEqual(score, 5)

    def test_assess(self):
        user = UserProfile(60, "Black", True, True)
        calc = DiabetesRiskCalculator(sample_data)
        result = calc.assess(user)
        self.assertEqual(result, "High Risk")

class TestHeartRiskCalculator(unittest.TestCase):
    """Purpose: These are the tests for the HeartDiseaseRiskCalculator class. The return should be "OK" if it runs properly. """
    def test_score(self):
        user = UserProfile(55, "Hispanic", True, False)
        calc = HeartDiseaseRiskCalculator(sample_data)
        score = calc.calculate_score(user)
        self.assertEqual(score, 4)

    def test_assess(self):
        user = UserProfile(30, "Hispanic", False, True)
        calc = HeartDiseaseRiskCalculator(sample_data)
        result = calc.assess(user)
        self.assertEqual(result, "Low Risk")

class TestRiskAssessmentSystem(unittest.TestCase):
    """Purpose: These are the tests for the RiskAssessmentSystem class. The return should be "OK" if it runs properly. """
    def test_all(self):
        user = UserProfile(19, "Black", True, True)
        system = RiskAssessmentSystem(user, sample_data)
        results = system.full_assesment()
        self.assertIn("Diabetes Risk", results)
        self.assertIn("Heart Disease Risk", results)

    def test_similar_cases(self):
        user = UserProfile(36, "Hispanic", True, True)
        system = RiskAssessmentSystem(user, sample_data)
        similar = system.find_similar_cases()
        self.assertFalse(similar.empty)
        self.assertIn("Target", similar.columns)

if __name__ == '__main__':
    """Purpose: This is the classic statement to run the tests once the script is executed, so the tests will run if the script is run from the command line."""
    unittest.main() 