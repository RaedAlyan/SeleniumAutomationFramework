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

    def is_dropdown_multiple_selections(self, locator: tuple) -> bool:
        """
        Checks if the dropdown supports multiple selections.

        :param locator: the locator strategy and value.
        :return: True if the dropdown supports multiple selections, otherwise False.
        :raises Exception: if an error occurs while checking if the dropdown supports multiple selections.
        """
        try:
            web_element = self.find_element(locator)
            dropdown = Select(web_element)
            return dropdown.is_multiple
        except Exception as e:
            raise Exception(f'An error occurred while checking the dropdown supports multiple selections. Error: {e}')

    def select_dropdown_by_visible_text(self, locator: tuple, text: str) -> None:
        """
        Selects a dropdown option by a visible text.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to select.
        :raises Exception: if an error occurs while selecting a dropdown option by a visible text.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_visible_text(text)
        except Exception as e:
            raise Exception(f'An error occurred while selecting a dropdown option by a visible text. Error: {e}')

    def select_dropdown_by_value(self, locator: tuple, value: str) -> None:
        """
        Selects a dropdown option by its value attribute.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to select.
        :raises Exception: if an error occurs while selecting a dropdown option by a value attribute.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_value(value)
        except Exception as e:
            raise Exception(f'An error occurred while selecting a dropdown option by a value. Error: {e}')

    def select_dropdown_by_index(self, locator: tuple, index: int) -> None:
        """
        Selects a dropdown option by its index.

        :param locator: the locator strategy and value.
        :param index: the index of the option to select.
        :raises Exception: if an error occurs while selecting a dropdown option by an index.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_index(index)
        except Exception as e:
            raise Exception(f'An error occurred while selecting a dropdown option by an index. Error: {e}')

    def get_all_dropdown_options(self, locator: tuple) -> list:
        """
        Returns all options in a dropdown as a list of strings.

        :param locator: the locator strategy and value.
        :return: a list of all dropdown options.
        :raises Exception: if an error occurs while getting all dropdown options.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            options = [option.text for option in drop_down.options]
            return options
        except Exception as e:
            raise Exception(f'An error occurred while getting all dropdown options. Error: {e}')

    def get_selected_dropdown_option(self, locator: tuple) -> str:
        """
        Returns the currently selected option in a dropdown.

        :param locator: the locator strategy and value.
        :return: the text of the currently selected option.
        :raises Exception: if an error occurs while getting the currently selected dropdown option.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            return drop_down.first_selected_option.text
        except Exception as e:
            raise Exception(f'An error occurred while getting currently selected dropdown option. Error: {e}')

    def deselect_all_dropdown_options(self, locator: tuple) -> None:
        """
        Deselects all selected options in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :raises InvalidArgumentException: If the dropdown is not a multi-select dropdown.
        :raises Exception: if an error occurs while deselecting all dropdown options.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_all()
        except Exception as e:
            raise Exception(f'An error occurred while deselecting all dropdown options. Error: {e}')

    def deselect_dropdown_by_index(self, locator: tuple, index: int) -> None:
        """
        Deselects a dropdown option by its index in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param index: the index of the option to deselect.
        :raises InvalidArgumentException: If the dropdown is not a multi-select dropdown.
        :raises Exception: if an error occurs while deselecting a dropdown option by an index.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_index(index)
        except Exception as e:
            raise Exception(f'An error occurred while deselecting a dropdown option by an index. Error: {e}')

    def deselect_dropdown_by_value(self, locator: tuple, value: str) -> None:
        """
        Deselects a dropdown option by its value attribute in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to deselect.
        :raises InvalidArgumentException: If the dropdown is not a multi-select dropdown.
        :raises Exception: if an error occurs while deselecting a dropdown option by a value.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_value(value)
        except Exception as e:
            raise Exception(f'An error occurred while deselecting a dropdown option by a value. Error: {e}')

    def deselect_dropdown_by_visible_text(self, locator: tuple, text: str) -> None:
        """
        Deselects a dropdown option by its visible text in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to deselect.
        :raises InvalidArgumentException: If the dropdown is not a multi-select dropdown.
        :raises Exception: if an error occurs while selecting a dropdown option by a visible text.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_visible_text(text)
        except Exception as e:
            raise Exception(f'An error occurred while selecting a dropdown option by a visible text. Error: {e}')

