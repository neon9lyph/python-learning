import logging

config = {
    "level": logging.DEBUG,
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "handlers": [logging.FileHandler("17.log.py.log"), logging.StreamHandler()],
}

logging.basicConfig(**config)

logging.debug("This is a debug message")
