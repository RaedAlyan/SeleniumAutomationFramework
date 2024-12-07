import os
import logging
from datetime import datetime


def setup_logger(log_level=logging.INFO, log_dir='D:\\Projects\\PythonProjects\\selenium_automation_framework\\logs'):
    """
    Sets up a logger with both console and file handlers.

    :param log_level: Logging level (e.g., logging.INFO).
    :param log_dir: Directory where log files will be stored.
    :return: Configured logger instance.
    """
    logger = logging.getLogger()

    # to prevent multiple handlers from being added to the logger
    if not logger.hasHandlers():
        logger.setLevel(log_level)

        os.makedirs(log_dir, exist_ok=True)

        timestamp = datetime.now().strftime('%Y-%m-%d')
        log_file = os.path.join(log_dir, f'test_log_{timestamp}.log')

        # console_handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        # File Handler
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        # Add Handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
