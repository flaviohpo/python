''' usando a funcao get_logger(...) '''
import logging
from re import DEBUG

logger = logging.getLogger('meu_logger')

logger.setLevel(DEBUG)
logger.debug()