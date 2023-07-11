import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

# The `@dataclass` decorator is used to automatically generate special methods for a class, such as `__init__`, `__repr__`, and `__eq__`, based on the class attributes.
@dataclass
class DataIngestionConfig:
    #Inputs for the Data Ingestion Component
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'data.csv')

# The class DataIngestion is responsible for data ingestion and has an attribute ingestion_config of type DataIngestionConfig.
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

#to read the dataset from any database/local
    def initiate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        
        try:
            df = pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as Dataframe')
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)   # creating a directory structure for the train data path.

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)   # saving the DataFrame `df` as a CSV file at the path specified by `self.ingestion_config.raw_data_path`.
            logging.info('Train test split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is complete')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion() #creates an instance of the `DataIngestion` class and assigns it to the variable `obj`.
    train_data,test_data=obj.initiate_data_ingestion()  # Its is calling the `initiate_data_ingestion()` method of the `DataIngestion` class and assigning the returned values to the variables `train_data` and `test_data`.

    data_transformation = DataTransformation()  # creating an instance of the `DataTransformation` class and assigning it to the variable `data_transformation`. This allows us to access the methods and attributes of the `DataTransformation` class using the `data_transformation` object.
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)  #calling the `initiate_data_transformation()` method of the `DataTransformation` class and assigning the returned values to the variables `train_arr` and `test_arr`. The `_` variable is used to ignore the third value returned by the method.

    modeltrainer = ModelTrainer()   # is creating an instance of the `ModelTrainer` class and assigning it to the variable `modeltrainer`. This allows us to access the methods and attributes of the `ModelTrainer` class using the `modeltrainer` object.
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr)) # is calling the `initiate_model_trainer()` method of the `ModelTrainer` class with the `train_arr` and `test_arr` variables as arguments. It then prints the return value of the method.