#class 1
class UserProfile():
    """ This class represents a user's health profile, storing info such as age, ethnicity, familiy history, and genetic markers. 
    
    Attributes:
        age(int): The age of the user.
        ethnicity(str): The ethnicity of the user. 
        family_history(boolean): This tells us whether or not there is a family history of diabetes or heart disease.
        genetic_marker(boolean): This tells us whether or not the user has a genetic marker for diabetes or heart disease.
    """
    
    def __init__(self, age, ethnicity, family_history, genetic_marker):
        """This is the usual initialization function, which sets up a UserProfile object.
        age(int): The age of the user.
        ethnicity(str): The ethnicity of the user. 
        family_history(boolean): This tells us whether or not there is a family history of diabetes or heart disease.
        genetic_marker(boolean): This tells us whether or not the user has a genetic marker for diabetes or heart disease.
        """
        pass

    def get_summary(self):
        """This function returns a summary of the user's profile.
        
        Args:
            None, just the self parameter that is required in all class methods.

        Returns:
            str: A summary of the user's profile in a string.
        
        """
        pass

    def has_risk_factors(self):
        """ This function will determine if the user has any risk factors based on their profile.
        
        Returns:
            boolean: This is true if the risk factors are present. If not, it is false. 
        """
        pass


#Class 2 test comment 
class RiskCalculator():
    """"""
    def __init__(self, dataset):
        pass

    def classify_risk(self, score):
        pass

#Class 3
class DiabetesRiskCalculator(RiskCalculator):
    def calculate_score(self, user_profile):
        pass


    def assess(self, user_profile):
        pass

#Class 4
class HeartDiseaseRiskCalculator(RiskCalculator):
    def calculate_score(self, user_profile):
        pass


    def assess(self, user_profile):
        pass

# Class 5
class RiskAssesmentSystem:
    def __init__(self, user_profile,dataset):
        pass

    def full_assesment(self):
        pass