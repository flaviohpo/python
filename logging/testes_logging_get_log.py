import logging

logger = logging.getLogger(__name__) 
formatter = logging.Formatter('%(asctime)s;%(levelname)s;%(message)s')

file_handler = logging.FileHandler('logger.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

# caso queira printar no console o log também:
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)