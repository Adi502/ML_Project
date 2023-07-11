import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()      # retrieves information about the current exception being handled.
    file_name=exc_tb.tb_frame.f_code.co_filename    # retrieving the filename of the Python script where the exception occurred.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))    #creating a formatted error message string.
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        """
        The above function is a constructor that initializes an object with an error message and error
        detail.
        
        :error_message: The error message is a string that describes the error that occurred. It provides a brief explanation of what went wrong
        :error_detail: The `error_detail` parameter is a variable of type `sys`. It is used to store additional information about the error that occurred. This can include details such as the error code, error message, stack trace, and any other relevant information that can help in debugging and resolving the error
        :type error_detail: sys
        """
        super().__init__(error_message) # `super().__init__(error_message)` is calling the constructor of the parent class (`Exception`) and passing the `error_message` as an argument. This allows the parent class to initialize its own attributes and perform any necessary setup. By calling the parent class's constructor, the `CustomException` class inherits the behavior and attributes of the `Exception` class.
        self.error_message=error_message_detail(error_message,error_detail=error_detail)    # assigning the value returned by the `error_message_detail` function to the `error_message` attribute of the `CustomException` class instance.
    
    def __str__(self):
        """
        The above function returns the error message as a string.
        The `__str__` method is returning the `error_message` attribute of the object.
        """
        return self.error_message
    
