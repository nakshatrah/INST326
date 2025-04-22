""" This file contains the unit tests for the risk assessment system classes. 

This module holds the test for UserProfile, DiabetesRiskCalculator, HeartDiseaseRiskCalculator, and RiskAssessmentSystem. These tests helped us validate our structure to check that the methods are functional. 
"""

import unittest
from main import UserProfile, RiskCalculator, DiabetesRiskCalculator, HeartDiseaseRiskCalculator, RiskAssessmentSystem

class TestUserProfile(unittest.TestCase):
    """Purpose: These are the tests for the UserProfile class. The return should be "OK" if it runs properly. """
    def test_summary(self):
        user = UserProfile(24, "Hispanic", True, True)
        self.assertIsNone(user.get_summary()) 

    def test_risk_factors(self):
        user = UserProfile(40, "White", False, True)
        self.assertIsNone(user.has_risk_factors())

class TestDiabetesRisk(unittest.TestCase):
    """Purpose: These are the tests for the DiabetesRiskCalculator class. The return should be "OK" if it runs properly. """
    def test_score(self):
        user = UserProfile(50, "Asian", True, False)
        calc = DiabetesRiskCalculator("dataset")
        self.assertIsNone(calc.calculate_score(user))

    def test_assess(self):
        user = UserProfile(60, "Black", True, True)
        calc = DiabetesRiskCalculator("dataset")
        self.assertIsNone(calc.assess(user))

class TestHeartRisk(unittest.TestCase):
    """Purpose: These are the tests for the HeartDiseaseRiskCalculator class. The return should be "OK" if it runs properly. """
    def test_score(self):
        user = UserProfile(27, "Asian", False, True)
        calc = HeartDiseaseRiskCalculator("dataset")
        self.assertIsNone(calc.calculate_score(user))

    def test_assess(self):
        user = UserProfile(55, "Hispanic", True, False)
        calc = HeartDiseaseRiskCalculator("dataset")
        self.assertIsNone(calc.assess(user))

class TestRiskAssessmentSystem(unittest.TestCase):
    """Purpose: These are the tests for the RiskAssessmentSystem class. The return should be "OK" if it runs properly. """
    def test_all(self):
        user = UserProfile(19, "Black", True, True)
        system = RiskAssessmentSystem(user, "dataset")
        self.assertIsNone(system.full_assesment())

if __name__ == '__main__':
    """Purpose: This is the classic statement to run the tests once the script is executed, so the tests will run if the script is run from the command line."""
    unittest.main() 