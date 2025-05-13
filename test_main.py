""" This file contains the unit tests for the risk assessment system classes. 

This module holds the test for UserProfile, DiabetesRiskCalculator, and RiskAssessmentSystem. These tests helped us validate our structure to check that the methods are functional. 
"""

import unittest
import pandas as pd
from models import UserProfile, RiskCalculator, DiabetesRiskCalculator, RiskAssessmentSystem 

class TestUserProfile(unittest.TestCase):
    """Purpose: These are the tests for the UserProfile class. The return should be "OK" if it runs properly. """
    def test_summary(self):
        user = UserProfile(30, "Moderate", True, False)
        summary = user.get_summary()
        self.assertIn("Age: 30", summary)
        self.assertIn("Physical Activity: Moderate", summary)
        self.assertIn("Family History: Yes", summary)
        self.assertIn("Genetic Marker: Negative", summary)

    def test_risk_factors(self):
        user1 = UserProfile(40, "Low", False, False)
        self.assertFalse(user1.has_risk_factors())
        user2 = UserProfile(40, "Low", True, False)
        self.assertTrue(user2.has_risk_factors())


class TestDiabetesRiskCalculator(unittest.TestCase):
    """Purpose: These are the tests for the DiabetesRiskCalculator class. The return should be "OK" if it runs properly. """
    def setUp(self):
        data = {
            "Age": [50, 33],
            "Physical Activity": ["High", "Low"],
            "Samily History": ["Yes", "No"],
            "Genetic Markers": ["Positive", "Negative"],
            "Target": [1, 0]
        }
        self.df = pd.DataFrame(data)
        self.calculator = DiabetesRiskCalculator(self.df)

    def test_score(self):
        user = UserProfile(50, "High", True, False)
        score = self.calculator.calculate_score(user)
        self.assertEqual(score, 5)

    def test_assess(self):
        user = UserProfile(60, "Low", True, False)
        result = self.calculator.assess(user)
        self.assertEqual(result, "Moderate Risk")

class TestRiskAssessmentSystem(unittest.TestCase):
    """Purpose: These are the tests for the RiskAssessmentSystem class. The return should be "OK" if it runs properly. """
    
    def setUp(self):
        data = {
            "Age": [35, 37, 50, 40, 29],
            "Physical Activity": ["Moderate", "Moderate", "Low", "High", "Moderate"],
            "Family History": ["Yes", "Yes", "No", "Yes", "Yes"],
            "Genetic Markers": ["Positive", "Positive", "Negative", "Positive", "Positive"], 
            "Target": [1, 1, 0, 1, 1]
        }
        self.df = pd.DataFrame(data)
        self.user = UserProfile(35, "Moderate", True, True)
        self.system = RiskAssessmentSystem(self.user, self.df)
    
    def test_all(self):
        results = self.system.full_assesment()
        self.assertIn("Diabetes Risk", results)
        self.assertIn(results["Diabetes Risk"], ["Low Risk", "Moderate Risk", "High Risk"])

    def test_similar_cases(self):
        similar = self.system.find_similar_cases()
        self.assertTrue(isinstance(similar, pd.DataFrame))
        self.assertFalse(similar.empty)
        self.assertIn("Physical Activity", similar.columns)
        self.assertIn("Genetic Markers", similar.columns)

if __name__ == '__main__':
    """Purpose: This is the classic statement to run the tests once the script is executed, so the tests will run if the script is run from the command line."""
    unittest.main() 