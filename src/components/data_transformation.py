import os
import sys
from dataclasses import dataclass
from idlelib.debugobj import make_objecttreeitem
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

# The `@dataclass` decorator is used to automatically generate special methods (__init__, __repr__, etc.) for a class based on its annotated fields. In this case, the `DataTransformationConfig` class is defined as a dataclass.
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

# The class DataTransformation is used for data transformation and has a configuration object.
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        #This function is responsible for data trnasformation
        try:
            # defining lists that contain the names of the numerical and categorical columns in the dataset, respectively.
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            # The `num_pipeline` is a pipeline object that defines a sequence of steps for numerical column transformation.
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
            )

            # a pipeline object that defines a sequence of steps for transforming categorical columns in the dataset.
            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder(handle_unknown='ignore')),
                ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # The `preprocessor` object is an instance of the `ColumnTransformer` class from scikit-learn. It is used to apply different transformations to different columns of the dataset.
            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        """
        The function initiates the data transformation process by taking the paths of the training and testing data as input.
        
        train_path: The path to the training dataset file
        test_path: The test_path parameter is the file path to the test dataset. It is the location where the test dataset is stored on your computer
        """

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()    # calling the `get_data_transformer_object()` method of the `DataTransformation` class to obtain the preprocessing object.

            target_column_name="math_score" 
            numerical_columns = ["writing_score", "reading_score"]  # defining variables that store the names of the target column and numerical columns in the dataset, respectively.

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df) # applying the preprocessing object (`preprocessing_obj`) on the training and testing dataframes (`input_feature_train_df` and `input_feature_test_df`, respectively).
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)  # concatenating the transformed input features (`input_feature_train_arr`) and the target feature (`target_feature_train_df`) into a single array (`train_arr`).
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            # The `save_object()` function is used to save the preprocessing object (`preprocessing_obj`) to a file specified by the `file_path` parameter.
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)
            