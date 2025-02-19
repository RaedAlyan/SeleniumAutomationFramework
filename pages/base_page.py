"""

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium.common import InvalidArgumentException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        """
        Initializes the BasePage with the WebDriver instance.

        :param driver: the WebDriver instance.
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Navigates to the specified URL

        :param url: the URL to navigate to.
        :raises Exception: if an error occurs while navigating to the specified URL.
        """
        try:
            self.driver.get(url)
        except Exception as e:
            raise Exception(f'An error occurred while navigating to the {url}. Error: {e}')

    def find_element(self, locator: tuple) -> WebElement:
        """
        Finds and returns a single web element.

        :param locator: the locator strategy and value.
        :return: the web element.
        :raises Exception: if an error occurs while finding the element.
        """
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            raise Exception(f'An error occurred while finding the web element with this locator: {locator}. Error: {e}')

    def find_elements(self, locator: tuple) -> list[WebElement]:
        """
        Finds and returns a list of web elements.

        :param locator: the locator strategy and value.
        :return: a list of web elements.
        :raises Exception: if an error occurs while finding the elements.
        """
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            raise Exception(
                f'An error occurred while finding the web_elements with this locator: {locator}. Error: {e}')

    def get_current_url(self) -> str:
        """
        Returns the current URL of the browser.

        :return: the current URL.
        :raises Exception: if an error occurs while getting the current URL.
        """
        try:
            return self.driver.current_url
        except Exception as e:
            raise Exception(f'An error occurred while getting the current URL. Error: {e}')

    def go_back(self) -> None:
        """
        Navigates back to the previous page in the browser history.

        :raises Exception: if an error occurs while navigating to the previous page.
        """
        try:
            self.driver.back()
        except Exception as e:
            raise Exception(f'An error occurred while navigating to the previous page. Error: {e}')

    def go_forward(self) -> None:
        """
        Navigates forward to the next page in the browser history.

        :raises Exception: if an error occurs while navigating to the next page.
        """
        try:
            self.driver.forward()
        except Exception as e:
            raise Exception(f'An error occurred while navigating to the next page. Error: {e}')

    def refresh(self) -> None:
        """
        Refreshes the current page.

        :raises Exception: if an error occurs while refreshing the page.
        """
        try:
            self.driver.refresh()
        except Exception as e:
            raise Exception(f'An error occurred while refreshing the page. Error: {e}')

    def get_title(self) -> str:
        """
        Returns the title of the current page.

        :return: the title of the current page.
        :raises Exception: if an error occurs while getting the title of the current page.
        """
        try:
            return self.driver.title
        except Exception as e:
            raise Exception(f'An error occurred while getting title of the current page. Error: {e}')

    def click(self, locator: tuple) -> None:
        """
        Clicks on a web element.

        :param locator: the locator strategy and value.
        :raises Exception: if an error occurs while clicking on a web element.
        """
        try:
            web_element = self.find_element(locator)
            web_element.click()
        except Exception as e:
            raise Exception(f'An error occurred while clicking on the web element with this {locator}. Error: {e}')

    def send_keys(self, locator: tuple, text: str) -> None:
        """
        Enters text into a web element.

        :param locator: the locator strategy and value.
        :param text: the text to enter into a web element.
        :raises Exception: if an error occurs while entering text into a web element.
        """
        try:
            web_element = self.find_element(locator)
            web_element.clear()
            web_element.send_keys(text)
        except Exception as e:
            raise Exception(f'An error occurred while entering text into a web element. Error: {e}')

    def quit(self) -> None:
        """
        Closes all browser windows and ends the WebDriver session.

        :raises Exception: if an error occurs while quiting the WebDriver session.
        """
        try:
            self.driver.quit()
        except Exception as e:
            raise Exception(f'An error occurred while quiting the WebDriver session.')

    def close(self) -> None:
        """
        Closes the current browser window.

        :raises Exception: if an error occurs while closing the current window.
        """
        try:
            self.driver.close()
        except Exception as e:
            raise Exception(f'An error occurred while closing the current window. Error: {e}')