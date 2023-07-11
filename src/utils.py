import os 
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):    #The function `save_object` saves an object to a file using the pickle library.
                                    #param file_path: The file path where the object will be saved. This should include the file name and extension (e.g., "data.pkl")
                                    #The `obj` parameter is the object that you want to save to a file. It can be any Python object that is serializable, meaning it can be converted into a byte stream and saved to a file.
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)        #dill.dump helps to create the pkl file

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    """
    The function `evaluate_models` trains and evaluates multiple machine learning models using grid
    search and returns a report of the test scores.
    
    :param X_train: The training data features
    :param y_train: The target variable for the training set. It is the variable that you are trying to
    predict or model
    :param X_test: The test set features (input variables) used to evaluate the models
    :param y_test: The parameter `y_test` is the true target values for the test set. It is a
    1-dimensional array or list containing the actual values of the target variable for the test data
    :param models: The "models" parameter is a dictionary that contains different machine learning
    models. The keys of the dictionary represent the names of the models, and the values represent the
    actual model objects
    :param param: The `param` parameter is a dictionary that contains the hyperparameters for each
    model. The keys of the dictionary are the names of the models, and the values are dictionaries of
    hyperparameters for each model
    :return: a dictionary called "report" which contains the test model scores for each model in the
    input list of models.
    """
    try:
        report = {}
#This trains and evaluates multiple machine learning models using grid search and returns a report of the test scores.
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
 
# The function `load_object` loads an object from a file using the `dill` library and raises a CustomException` if an error occurs.

    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)   
        