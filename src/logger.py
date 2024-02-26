import logging
import os
from datetime import datetime

# Generating the name for the log file using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Getting the path for the log directory within the current working directory
log_path = os.path.join(os.getcwd(), "logs")

# Creating the log directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Creating the full path for the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configuring the basic logging settings
logging.basicConfig(level=logging.INFO,  # Setting the logging level to INFO
                    filename=LOG_FILEPATH,  # Setting the log file path
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"  # Setting the log message format
                    )