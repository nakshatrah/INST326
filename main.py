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
        self.age = age
        self.ethnicity = ethnicity
        self.family_history = family_history
        self.genetic_marker = genetic_marker
    
    def get_summary(self):
        """This function returns a summary of the user's profile.
        
        Args:
            None, just the self parameter that is required in all class methods.

        Returns:
            str: A summary of the user's profile in a string.
        
        """
        return (f"User Profile:\n"
                f"Age: {self.age}\n"
                f"Ethnicity: {self.ethnicity}\n"
                f"Family History: {'Yes' if self.family_history else 'No'}\n"
                f"Genetic Marker: {'Positive' if self.genetic_marker else 'Negative'}\n")

    def has_risk_factors(self):
        """ This function will determine if the user has any risk factors based on their profile.
        
        Returns:
            boolean: This is true if the risk factors are present. If not, it is false. 
        """
        return self.family_history or self.genetic_marker


#Class 2 test comment 
class RiskCalculator():
    """ This class calculates the health risk based on a dataset.

    Attributes: 
        dataset(any type): The dataset that is entered; this is used to calculate the risk. 
    """
    def __init__(self, dataset):
        """ This function is the initialization function that's meant to set up a RiskCalculator.

        Args:
            dataset(any type): The dataset used in the risk calculation.
        """
        self.dataset = dataset

    def classify_risk(self, score):
        """ This function classifies the risk based on a score. 
        
        Args:
            score(int): The risk score that is calculated.

        Returns:
            str: A string that describes the risk level.
        """
        if score >= 7:
            return "High Risk"
        elif score >= 4:
            return "Moderate Risk"
        else:
            return "Low Risk"

#Class 3
class DiabetesRiskCalculator(RiskCalculator):
    """ This class calculates the risk of diabetes based on the user profile."""
    def calculate_score(self, user_profile):
        """ This method calculates a risk score for diabetes.
        
        Args:
            user_profile(UserProfile): The user's profile to be evaluated. 

        Returns: 
            int: The risk score for diabetes.
        """
        pass


    def assess(self, user_profile):
        """ This method assesses the risk for diabetes and returns a risk classification.
        
        Args:
            user_profile(UserProfile): The user's profile to be evaluated.
            
        Returns:
            str: The risk classification for diabetes.
        """
        pass

#Class 4
class HeartDiseaseRiskCalculator(RiskCalculator):
    """ This class calculates the risk of heart disease based on the user profile."""
    def calculate_score(self, user_profile):
        """ This methods calculates a risk score for hear disease based on the user profile, similarly to our previous DiabetesRiskCalculator function.
        
        Args: 
            user_profile(UserProfile): The user's profile to be evaluated. 

        Returns:
            int: The risk score for heart disease.
        """
        pass


    def assess(self, user_profile):
        """ This method assesses the risk for heart disease and returns a risk classification.
        
        Args: 
            user_profile(UserProfile): The user's profile to be assessed.
            
        Returns:
            str: The risk classification for heart disease."""
        pass

# Class 5
class RiskAssessmentSystem:
    """ This class is the main system for risk assessment; It coordinates the entire health risk assessment for the individual using our program.
    
    Attributes: 
        user_profile(UserProfile): The user's profile being evaluated.
        dataset(any type): The dataset used in the risk calculation.
    """
    
    def __init__(self, user_profile,dataset):
        """This function is the initialization function that's meant to set up a RiskAssessmentSystem.
        
        Args:
            user_profile(UserProfile): The user's profile being evaluated.
            dataset(any type): The dataset used for the user's assessment for the user. This 
        """
        pass

    def full_assesment(self):
        """ This method performs a full risk assessment for diabetes and heart disease.
        
        Returns:
            dict: A dictionary that contains the risk assessments for both diabetes and heart disease.
        """
        pass