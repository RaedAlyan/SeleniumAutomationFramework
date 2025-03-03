"""
This module provides a class to initialize and manage WebDriver instances for different browsers.

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com.
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.service import Service as BraveService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.os_manager import ChromeType
from config_loader import ConfigLoader
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from typing import Union


class WebDriverInitializer:

    def __init__(self) -> None:
        """
        Initializes the WebDriverInitializer by loading the browser configuration.
        """
        self.config = ConfigLoader()
        self.browser = self.config.get_specified_browser().lower()

    def _get_browser_options(self) -> Union[ChromeOptions, FirefoxOptions, EdgeOptions]:
        """
        Creates and returns browser-specific options based on the specified browser in the config.json file.

        :return: An instance of browser-specific options (e.g., ChromeOptions, FirefoxOptions, EdgeOptions).
        :raises KeyError: If the specified browser is not supported.
        """
        try:
            browser_options = self.config.get_browser_options()[self.browser]
            if self.browser == "chrome":
                options = ChromeOptions()
            elif self.browser == "firefox":
                options = FirefoxOptions()
            elif self.browser == "edge":
                options = EdgeOptions()
            elif self.browser == 'chromium':
                options = ChromeOptions()
            elif self.browser == 'brave':
                options = ChromeOptions()
            else:
                raise KeyError(f'The browser {self.browser} is not supported.')
            for option in browser_options:
                options.add_argument(option)
            return options
        except KeyError as e:
            raise KeyError(f'The browser_options option wasn\'t found in the config.json file. Error: {e}')

    def initialize_webdriver(self) -> WebDriver:
        """
        Initializes and returns a WebDriver instance for the specified browser.

        :return: an instance of the WebDriver for the specified browser.
        :raises KeyError: when the specified browser is not supported.
        :raises WebDriverException: when an error occurred while trying to initialize the WebDriver.
        """
        try:
            options = self._get_browser_options()
            if self.browser == 'chrome':
                web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            elif self.browser == 'firefox':
                web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            elif self.browser == 'edge':
                web_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            elif self.browser == 'chromium':
                web_driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(
                    chrome_type=ChromeType.CHROMIUM).install()), options=options)
            elif self.browser == 'brave':
                web_driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(
                    chrome_type=ChromeType.BRAVE).install()), options=options)
            else:
                raise KeyError(f'The browser {self.browser} is not supported.')
            return web_driver
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to initialize the WebDriver. Error: {e}')

