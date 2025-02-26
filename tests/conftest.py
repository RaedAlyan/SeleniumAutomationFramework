"""
This module defines shared test fixtures for Pytest.

@author: Raed Eleyan.
@date: 02/25/2025
@contact: raedeleyan1@gmail.com
"""
import pytest
from ..utils.webdriver_initializer import WebDriverInitializer
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope='session')
def driver():
    """Fixture to initialize and yield a WebDriver instance."""
    webdriver = None
    try:
        webdriver_initializer = WebDriverInitializer()
        webdriver = webdriver_initializer.initialize_webdriver()
        yield webdriver
    except WebDriverException as e:
        raise WebDriverException(f'An error occurred while trying to initialize the webdriver. Error: {e}')
    finally:
        if webdriver is not None:
            webdriver.quit()

