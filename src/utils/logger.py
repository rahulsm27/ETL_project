import logging
import socket


logging.basicConfig(filename='logs.log',level=logging.INFO, format = "%(asctime)s %(name)s %(levelname)s %(message)s")

def get_logger(name:str) -> logging.Logger :
    """
    Configures a logging module to be used by all
    
    """

    return logging.getLogger(f"{socket.gethostname()}{name}")