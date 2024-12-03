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
