import logging
import os
from datetime import datetime

# The code is creating a log file with a timestamp in its name.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE) #is creating the full path to the log file by joining the `log_path` and `LOG_FILE` variables using the `os.path.join()` function. This ensures that the log file will be saved in the correct directory with the correct file name.

logging.basicConfig(    # The `logging.basicConfig()` function is configuring the logging module in Python. It sets up the basic configuration for logging, including the log file name, log format, and log level.
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

