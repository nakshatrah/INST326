import unittest
from main import UserProfile, RiskCalculator, DiabetesRiskCalculator, HeartDiseaseRiskCalculator, RiskAssesmentSystem

class TestUserProfile(unittest.TestCase):
    def test_summary(self):
        user = UserProfile(24, "Hispanic", True, True)
        self.assertIsNone(user.get_summary()) 
    
if __name__ == '__main__':
    unittest.main() 