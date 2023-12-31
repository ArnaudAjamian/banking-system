import logging
import os

# create a 'logs' directory (if one does not already exist)
log_dir = 'logs'
os.makedirs(log_dir, exist_ok = True)

# instantiate logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')


# instantiate -- file handler
# create a file handler to write log messages to a file inside the 'logs' directory
log_file = os.path.join(log_dir, 'banking_system_log.log')
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

# instantiate -- console handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# add both handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)