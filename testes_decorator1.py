""" criacao de um decorator personalizado """
import sys
import logging

def log(func):
    """
    Log what function is called
    """
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # add file handler
        fh = logging.StreamHandler(sys.stdout)
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.debug(f"Running function: {name}")
        result = func(*args, **kwargs)
        logger.debug(f"Result: {result}")
        return func
    return wrap_log

@log
def double_function(a):
    """
    Double the input parameter
    """
    return a*2

if __name__ == "__main__":
    value = double_function(2)

##############################################