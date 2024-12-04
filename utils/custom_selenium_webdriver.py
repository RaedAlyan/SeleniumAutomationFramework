import os
from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement
from logger import setup_logger
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotInteractableException


class CustomSeleniumWebDriver:

    def __init__(self, driver):
        self.driver = driver
        self.logger = setup_logger()

    def get_element(self, locator: tuple) -> WebElement:
        """
        Finds a WebElement using the provided locator.

        :param locator: A tuple (By, value) for locating the WebElement.
        :return: WebElement if found.
        :raises NoSuchElementException: If the WebElement isn't found.
        :raises WebDriverException: if an error occurs while trying to find the WebElement.
        """
        self.logger.info(f'********** {self.get_element.__name__} **********')
        try:
            self.logger.info(f'Getting WebElement with this locator {locator}')
            web_element = self.driver.find_element(*locator)
            self.logger.info(f'The WebElement was get successfully with locator {locator}')
            return web_element
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement was not found with this locator {locator}. Error: {e}')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to find the WebElement. Error: {e}')

    def get_elements(self, locator: tuple) -> list[WebElement]:
        """
        Finds a list of WebElements using the provided locator.

        :param locator: A tuple (By, value) for locating a list of WebElements.
        :return: A list of WebElement objects.
        :raises NoSuchElementException: If no elements are found.
        :raises WebDriverException: If an error occurs while trying to find the WebElements.
        """
        self.logger.info(f'********** {self.get_elements.__name__} **********')
        try:
            self.logger.info(f'Getting WebElements with this locator: {locator}')
            web_elements = self.driver.find_elements(*locator)
            if web_elements:
                self.logger.info(f'Found {len(web_elements)} WebElements with this locator: {locator}.')
            else:
                self.logger.warning(f'No WebElements were found with this locator: {locator}.')
            return web_elements
        except NoSuchElementException as e:
            self.logger.error(f'No WebElements were found with this locator: {locator}. Error: {e}')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to find the WebElements. Error: {e}')

    def click(self, locator: tuple) -> None:
        """
        Clicks on a WebElement found by the locator.

        :param locator: A tuple (By, value) for locating the WebElement.
        :return: None.
        :raises ElementNotInteractableException: If the WebElement isn't interactable to be clicked.
        :raises WebDriverException: if an error occurs while trying to click the WebElement.
        """
        self.logger.info(f'********** {self.click.__name__} **********')
        try:
            self.logger.info(f'Clicking the WebElement with this locator: {locator}')
            web_element = self.get_element(locator)
            web_element.click()
            self.logger.info(f'The WebElement was clicked successfully with this locator: {locator}')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement with this locator {locator} isn\'t interactable to be clicked. '
                              f'Error: {e}')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to click the WebElement. Error: {e}')

    def type_text(self, locator: tuple, text: str) -> None:
        """
        Sends text input to a WebElement found by the locator.

        :param locator: A tuple (By, value) for locating the WebElement.
        :param text: Text to send to the WebElement.
        :return: None.
        :raises ElementNotInteractableException: If the WebElement isn't interactable to be typed.
        :raises WebDriverException: if an error occurs while trying to type the text.
        """
        self.logger.info(f'********** {self.type_text.__name__} **********')
        try:
            self.logger.info(f'Typing text "{text}" into the WebElement with this locator: {locator}')
            web_element = self.get_element(locator)
            web_element.clear()
            web_element.send_keys(text)
            self.logger.info(f'The text "{text}" typed successfully into the WebElement with this locator: {locator}')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement with this locator isn\'t interactable to be typed. Error: {e}')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to type the text into the WebElement. Error: {e}')

    def take_screenshot(self, screenshot_dir: str = 'screenshots') -> None:
        """
        Captures a screenshot of the current browser window.

        :param screenshot_dir: Directory where the screenshot will be saved.
        :return: None.
        :raises WebDriverException: if an error occurs while trying to take the screenshot.
        """
        self.logger.info(f'********** {self.take_screenshot.__name__} **********')
        try:
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f'{timestamp}.png'
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f'The screenshot was saved successfully at: {screenshot_path}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to save the screenshot. Error: {e}')

    def get_title(self) -> str:
        """
        Returns the title of the current browser window.

        :return: the title of the current browser window.
        :raises WebDriverException: if an error occurs while trying to get the title of the current browser window.
        """
        self.logger.info(f'********** {self.get_title.__name__} **********')
        try:
            self.logger.info('Fetching the page title...')
            current_page_title = self.driver.title
            self.logger.info(f'The page title was fetched successfully. Current page title: {current_page_title}')
            return current_page_title
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to get the title of the current browser window. '
                              f'Error: {e}')
