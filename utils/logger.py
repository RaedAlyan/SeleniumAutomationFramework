"""
This module is used to create and manage loggers with console and file handlers.

@author: Raed Eleyan.
@date: 03/16/2025
@contact: raedeleyan1@gmail.com
"""
import os
import logging
from datetime import datetime


class Logger:
    """
    This class is used to create and manage loggers with console and file handlers.
    """

    def __init__(self, log_level=logging.INFO, log_file_path='logs'):
        # create a logger.
        self.logger = logging.getLogger(__name__)

        # set the log level.
        self.logger.setLevel(log_level)

        # create a log format.
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Create logs directory if it doesn't exist
        if not os.path.exists(log_file_path):
            os.makedirs(log_file_path)

        # console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)

        # file handler
        log_file_name = os.path.join(log_file_path,
                                     f'app_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log')
        file_handler = logging.FileHandler(log_file_name)
        file_handler.setFormatter(log_format)

        # avoid duplicate handlers
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message):
        """Log a critical message."""
        self.logger.critical(message)
