import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        # This method is used to make predictions on a set of input features.
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scale = preprocessor.transform(features)
            preds = model.predict(data_scale)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:   #represents custom data with attributes such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score.
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int, ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        # The block of code is creating a dictionary called `custom_data_input_dict` that
        # represents the custom data attributes. Each attribute is a key-value pair in the dictionary,
        # where the key is the attribute name (e.g., "gender", "race_ethnicity") and the value is a
        # list containing the corresponding attribute value.
        try:
            custom_data_input_dict = {
                "gender" : [self.gender],
                "race_ethnicity" : [self.race_ethnicity],
                "parental_level_of_education" : [self.parental_level_of_education],
                "lunch" : [self.lunch],
                "test_preparation_course" : [self.test_preparation_course],
                "reading_score" : [self.reading_score],
                "writing_score" : [self.writing_score], 
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)