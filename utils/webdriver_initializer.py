"""
This module is used to initialize and manage WebDriver instances for different browsers.

@author: Raed Eleyan.
@date: 03/16/2025.
@contact: raedeleyan1@gmail.com.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.core.os_manager import ChromeType
from .config_reader import ConfigReader
from .logger import Logger


class WebDriverInitializer:
    """
    This class is used to initialize WebDriver instances for different browsers.
    """

    def __init__(self):
        self.config = ConfigReader()
        self.browser = self.config.get_specified_browser().lower()
        self.logger = Logger()
        self.webdriver = None

    def initialize_webdriver(self):
        """
        Initializes and returns a WebDriver instance for the specified browser.

        :return:
        """
        try:
            if self.browser == 'chrome':
                self.logger.info('Initializing Chrome WebDriver...')
                self.webdriver = webdriver.Chrome(
                    service=ChromeService(
                        ChromeDriverManager().install()
                    )
                )
                self.logger.info('The Chrome WebDriver has been initialized successfully.')
            elif self.browser == 'firefox':
                self.logger.info('Initializing Firefox WebDriver...')
                self.webdriver = webdriver.Firefox(
                    service=FirefoxService(
                        GeckoDriverManager().install()
                    )
                )
                self.logger.info('The Firefox WebDriver has been initialized successfully.')
            elif self.browser == 'edge':
                self.logger.info('Initializing Edge WebDriver...')
                self.webdriver = webdriver.Edge(
                    service=EdgeService(
                        EdgeChromiumDriverManager().install()
                    )
                )
                self.logger.info('The Edge WebDriver has been initialized successfully.')
            elif self.browser == 'chromium':
                self.logger.info('Initializing Chromium WebDriver...')
                self.webdriver = webdriver.Chrome(
                    service=ChromeService(
                        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
                    )
                )
                self.logger.info('The Chromium WebDriver has been initialized successfully.')
            elif self.browser == 'brave':
                self.logger.info('Initializing Brave WebDriver...')
                self.webdriver = webdriver.Chrome(
                    service=ChromeService(
                        ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()
                        )
                )
                self.logger.info('The Brave WebDriver has been initialized successfully.')
            else:
                self.logger.error('Invalid browser specified at the config.json file.')
                raise KeyError(f'The browser {self.browser} is not supported.')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to '
                                     'initialize the WebDriver.') from e
