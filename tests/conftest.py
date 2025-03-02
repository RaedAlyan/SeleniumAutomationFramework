"""
This module defines shared test fixtures for Pytest.

@author: Raed Eleyan.
@date: 02/25/2025
@contact: raedeleyan1@gmail.com
"""
import pytest
from ..utils.webdriver_initializer import WebDriverInitializer
from ..utils.logger import Logger
from selenium.common.exceptions import WebDriverException


logger = Logger()

@pytest.fixture(scope='session')
def driver():
    """Fixture to initialize and yield a WebDriver instance."""
    logger.log_method_entry('The Driver Fixture')
    webdriver = None
    try:
        logger.info('Initializing WebDriver...')
        webdriver_initializer = WebDriverInitializer()
        webdriver = webdriver_initializer.initialize_webdriver()
        logger.info('WebDriver initialized successfully.')
        yield webdriver
    except WebDriverException as e:
        logger.error('Failed to initialize the WebDriver.')
        raise WebDriverException(f'An error occurred while trying to initialize the webdriver. Error: {e}')
    finally:
        if webdriver is not None:
            logger.info('Quitting WebDriver...')
            webdriver.quit()
            logger.info('WebDriver quit successfully.')

