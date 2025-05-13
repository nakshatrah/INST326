class UserProfile():
    """ This class represents a user's health profile, storing info such as age, ethnicity, familiy history, and genetic markers. 
    
    Attributes:
        age(int): The age of the user.
        Physical Activity(str): The amount of exercise teh users does
        family_history(boolean): This tells us whether or not there is a family history of diabetes or heart disease.
        genetic_marker(boolean): This tells us whether or not the user has a genetic marker for diabetes or heart disease.
        height (float): Height of the user in feet.
        weight (float): Weight of the user in pounds.
    """
    
    def __init__(self, age, physical_activity, family_history, genetic_marker, height, weight):
        """This is the usual initialization function, which sets up a UserProfile object.
        age(int): The age of the user.
        Physical Activity(str): The amount of exercise teh users does
        family_history(boolean): This tells us whether or not there is a family history of diabetes or heart disease.
        genetic_marker(boolean): This tells us whether or not the user has a genetic marker for diabetes or heart disease.
        """
        self.age = age
        self.physical_activity = physical_activity
        self.family_history = family_history
        self.genetic_marker = genetic_marker
        self.height = height
        self.weight = weight 
    
    def get_summary(self):
        """This function returns a summary of the user's profile.
        
        Args:
            None, just the self parameter that is required in all class methods.

        Returns:
            str: A summary of the user's profile in a string.
        
        """
        bmi = self.calculate_bmi()
        return (f"User Profile:\n"
                f"Age: {self.age}\n"
                f"Physical Activity: {self.physical_activity}\n"
                f"Family History: {'Yes' if self.family_history else 'No'}\n"
                f"Genetic Marker: {'Positive' if self.genetic_marker else 'Negative'}\n"
                f"Height: {self.height} ft\n"
                f"Weight: {self.weight} lbs\n")

    def has_risk_factors(self):
        """ This function will determine if the user has any risk factors based on their profile.
        
        Returns:
            boolean: This is true if the risk factors are present. If not, it is false. 
        """
        return self.family_history or self.genetic_marker


    def get_recommendtaions(self):
        reccomendations = []

        bmi = self.calculate_bmi()
        if bmi >= 30:
            reccomendations.append("Your BMI indicates obesity. Consider a weight management plan with a healthcare provider")
        elif bmi >= 25:
            reccomendations.append("You are overweight. Increasing physical activity and eating a balanced deit can help.")
        elif bmi < 18.5:
            reccomendations.append("Your BMI is low. You may benefit from a nutritionist's guidance.")

        if self.physical_activity.lower() == "low":
            reccomendations.append("Try to increase your physical activity. Even walking daily can help reduce your risk.")

        if self.family_history:
            reccomendations.append("Since you have a family history of diabetes, regular health checkups are recommended.")

        if self.genetic_marker:
            reccomendations.append("You have a genetic marker. Discuss genetic counseling or early screenings with your doctor.")

        if not reccomendations:
            reccomendations.append("Great job! Keep up your healthy lifestyle and regular checkups.")

        return reccomendations

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
        
    def calculate_bmi(self):
        height_m = self.height * 0.3048
        weight_kg = self.weight * 0.453592
        if height_m == 0:
            return 0
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 1)


class DiabetesRiskCalculator(RiskCalculator):
    """ This class calculates the risk of diabetes based on the user profile."""
    def calculate_score(self, user_profile):
        """ This method calculates a risk score for diabetes.
        
        Args:
            user_profile(UserProfile): The user's profile to be evaluated. 

        Returns: 
            int: The risk score for diabetes.
        """
        score = 0

        if user_profile.age > 45:
            score += 2
        if user_profile.family_history:
            score += 3
        if user_profile.genetic_marker:
            score += 3

        bmi = user_profile.calculate_bmi()
        if bmi >= 30:
            score += 2
        elif bmi >= 25:
            score += 1


    def assess(self, user_profile):
        """ This method assesses the risk for diabetes and returns a risk classification.
        
        Args:
            user_profile(UserProfile): The user's profile to be evaluated.
            
        Returns:
            str: The risk classification for diabetes.
        """
        score = self.calculate_score(user_profile)
        return self.classify_risk(score)


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
        self.user_profile = user_profile
        self.dataset = dataset

    def full_assesment(self):
        """ This method performs a full risk assessment for diabetes and heart disease.
        
        Returns:
            dict: A dictionary that contains the risk assessments for both diabetes and heart disease.
        """
        diabetes_calc = DiabetesRiskCalculator(self.dataset)
        

        diabetes_result = diabetes_calc.assess(self.user_profile)

        return{
            "Diabetes Risk": diabetes_result,

        }
    
    def find_similar_cases(self, top_n=5):
        """ This is a new method that we intend to add to our RiskAssessmentSystem class, it will find similar cases to that of the user based on the dataset."""
        df = self.dataset 

        similar = df[
            (df["Age"].between(self.user_profile.age - 5, self.user_profile.age + 5)) & 
            (df["Physical Activity"].str.lower() == self.user_profile.physical_activity.lower()) &
            (df["Family History"].str.lower() == ("yes" if self.user_profile.family_history else "no")) &
            (df["Genetic Markers"].str.lower() == ("positive" if self.user_profile.genetic_marker else "negative"))      
        ]

        return  similar[["Target", "Age", "Physical Activity", "Family History", "Genetic Markers"]].head(5)