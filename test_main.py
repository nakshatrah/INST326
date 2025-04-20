import unittest
from main import UserProfile, RiskCalculator, DiabetesRiskCalculator, HeartDiseaseRiskCalculator, RiskAssesmentSystem

class TestUserProfile(unittest.TestCase):
    def test_summary(self):
        user = UserProfile(24, "Hispanic", True, True)
        self.assertIsNone(user.get_summary()) 

    def test_risk_factors(self):
        user = UserProfile(40, "White", False, True)
        self.assertIsNone(user.has_risk_factors())

class TestDiabetesRisk(unittest.TestCase):
    def test_score(self):
        user = UserProfile(50, "Asian", True, False)
        calc = DiabetesRiskCalculator("dataset")
        self.assertIsNone(calc.calculate_score(user))

    def test_assess(self):
        user = UserProfile(60, "Black", True, True)
        calc = DiabetesRiskCalculator("dataset")
        self.assertIsNone(calc.assess(user))

class TestHeartRisk(unittest.TestCase):
    def test_score(self):
        user = UserProfile(27, "Asian", False, True)
        calc = HeartDiseaseRiskCalculator("dataset")
        self.assertIsNone(calc.calculate_score(user))

    def test_assess(self):
        user = UserProfile(55, "Hispanic", True, False)
        calc = HeartDiseaseRiskCalculator("dataset")
        self.assertIsNone(calc.assess(user))

class TestRiskAssessmentSystem(unittest.TestCase):
    def test_all(self):
        user = UserProfile(19, "Black", True, True)
        system = RiskAssesmentSystem(user, "dataset")
        self.assertIsNone(system.full_assesment())

if __name__ == '__main__':
    unittest.main() 