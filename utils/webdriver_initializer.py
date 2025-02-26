"""
This module provides a class to initialize and manage WebDriver instances for different browsers.

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com.
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config_loader import ConfigLoader
from selenium.common.exceptions import WebDriverException


class WebDriverInitializer:

    def __init__(self) -> None:
        """
        Initializes the WebDriverInitializer by loading the browser configuration.
        """
        self.config = ConfigLoader()
        self.browser = self.config.get_specified_browser().lower()

    def initialize_webdriver(self) -> WebDriver:
        """
        Initializes and returns a WebDriver instance for the specified browser.

        :return: an instance of the WebDriver for the specified browser.
        :raises KeyError: when the specified browser is not supported.
        :raises WebDriverException: when an error occurred while trying to initialize the WebDriver.
        """
        try:
            if self.browser == 'chrome':
                web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            elif self.browser == 'firefox':
                web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            elif self.browser == 'edge':
                web_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            else:
                raise KeyError(f'The browser {self.browser} is not supported.')
            return web_driver
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to initialize the WebDriver. Error: {e}')

