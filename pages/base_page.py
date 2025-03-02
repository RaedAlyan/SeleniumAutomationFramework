"""
This Module Encapsulates Common Web Interaction and Operations.

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com
"""
from ..utils.logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (WebDriverException, TimeoutException, NoSuchElementException,
                                        ElementNotVisibleException, ElementNotInteractableException,
                                        UnexpectedTagNameException, ElementClickInterceptedException,
                                        NoSuchFrameException, NoAlertPresentException, NoSuchWindowException,
                                        InvalidArgumentException)


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        """
        Initializes the BasePage with the WebDriver instance.

        :param driver: the WebDriver instance.
        """
        self.driver = driver
        self.logger = Logger()

    def navigate_to(self, url: str) -> None:
        """
        Navigates to the specified URL

        :param url: the URL to navigate to.
        :raises WebDriverException: when an error occurs while trying to navigate to the specified URL.
        """
        self.logger.log_method_entry(self.navigate_to.__name__)
        try:
            self.logger.info(f'Navigating to this URL: {url}')
            self.driver.get(url)
            self.logger.info(f'Successfully navigated to this URL: {url}')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to navigate to this URL: {url}. Error: {e}')
            raise WebDriverException(f'Failed to navigate to this URL: {url}.')

    def find_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Finds and returns a single WebElement.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for a WebElement to be visible. Defaults to 10 seconds.
        :return: the WebElement.
        :raises TimeoutException: when the WebElement isn't found or not visible within the timeout.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotVisibleException: when a WebElement is present on the DOM, but it's not visible.
        :raises WebDriverException: when an error occurs while trying to find the WebElement.
        """
        self.logger.log_method_entry(self.find_element.__name__)
        try:
            self.logger.info(f'Finding a WebElement that has this locator: {locator}')
            web_element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
            self.logger.info(f'Successfully found the WebElement that has this locator: {locator}')
            return web_element
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to find the WebElement that has this locator: {locator} '
                              f'within {timeout} seconds. Error: {e}')
            raise TimeoutException(f'The WebElement that has this locator: {locator} wasn\'t found or wasn\'t visible '
                                   f'within {timeout} seconds.')
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} couldn\'t be found in the DOM. '
                              f'Error: {e}')
            raise NoSuchElementException(f'No such a WebElement that has this locator: {locator} in the DOM.')
        except ElementNotVisibleException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was present in the DOM, but wasn\'t '
                              f'visible. Error: {e}')
            raise ElementNotVisibleException(f'The WebElement that has this locator: {locator} wasn\'t visible.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to find the WebElement that has this locator: {locator}.'
                              f' Error: {e}')
            raise WebDriverException(f'Unable to find the WebElement that has this locator: {locator}.')

    def find_elements(self, locator: tuple[str, str], timeout: int = 10) -> list[WebElement]:
        """
        Finds and returns a list of WebElements.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for a list of WebElements to be visible. Defaults to 10 seconds.
        :return: a list of WebElements.
        :raises TimeoutException: when no WebElements are found or not visible within the timeout.
        :raises NoSuchElementException: when the WebElements couldn't be found in the DOM.
        :raises ElementNotVisibleException: when the WebElements are present on the DOM, but they're not visible.
        :raises WebDriverException: when an error occurs while trying to find the WebElements.
        """
        self.logger.log_method_entry(self.find_elements.__name__)
        try:
            self.logger.info(f'Finding WebElements that have this locator: {locator}')
            web_elements = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_all_elements_located(locator)
            )
            self.logger.info(f'Successfully found the WebElements that have this locator: {locator}')
            return web_elements
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to find WebElements that have this locator: {locator} '
                              f'within {timeout} seconds. Error: {e}.')
            raise TimeoutException(f'No WebElements that have this locator: {locator} were found or weren\'t visible '
                                   f'within {timeout} seconds.')
        except NoSuchElementException as e:
            self.logger.error(f'The WebElements that have this locator: {locator} couldn\'t be found in the DOM. '
                              f'Error: {e}')
            raise NoSuchElementException(f'No such WebElements that have this locator: {locator} found in the DOM.')
        except ElementNotVisibleException as e:
            self.logger.error(f'The WebElements that have this locator: {locator} were present in the DOM, but weren\'t'
                              f' visible. Error: {e}')
            raise ElementNotVisibleException(f'The WebElements that have this locator: {locator} weren\'t visible.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to find the WebElements that have this locator: '
                              f'{locator}. Error: {e}')
            raise WebDriverException(f'Unable to find the WebElements that have this locator: {locator}.')

    def get_current_url(self) -> str:
        """
        Returns the current URL of the browser.

        :return: the current URL.
        :raises WebDriverException: when an error occurs while trying to get the current URL.
        """
        self.logger.log_method_entry(self.get_current_url.__name__)
        try:
            self.logger.info('Getting the current URL')
            current_url = self.driver.current_url
            self.logger.info(f'Successfully got the current URL: {current_url}')
            return current_url
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to get the current URL. Error: {e}')
            raise WebDriverException('Unable to get the current URL.')

    def go_back(self) -> None:
        """
        Navigates back to the previous page in the browser history.

        :raises WebDriverException: when an error occurs while trying to navigate to the previous page.
        """
        self.logger.log_method_entry(self.go_back.__name__)
        try:
            self.logger.info('Navigating back to the previous page')
            self.driver.back()
            self.logger.info('Successfully navigated back to the previous page')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to navigate to the previous page. Error: {e}')
            raise WebDriverException('Unable to navigate to the previous page.')

    def go_forward(self) -> None:
        """
        Navigates forward to the next page in the browser history.

        :raises WebDriverException: when an error occurs while trying to navigate to the next page.
        """
        self.logger.log_method_entry(self.go_forward.__name__)
        try:
            self.logger.info('Navigating forward to the next page')
            self.driver.forward()
            self.logger.info('Successfully navigated forward to the next page')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to navigate to the next page. Error: {e}')
            raise WebDriverException('Unable to navigate to the next page')

    def refresh(self) -> None:
        """
        Refreshes the current page.

        :raises WebDriverException: when an error occurs while trying to refresh the current page.
        """
        self.logger.log_method_entry(self.refresh.__name__)
        try:
            self.logger.info('Refreshing the current page')
            self.driver.refresh()
            self.logger.info('Successfully refreshed the current page')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to refresh the current page. Error: {e}')
            raise WebDriverException('Unable to refresh the current page.')

    def get_title(self) -> str:
        """
        Returns the title of the current page.

        :return: the title of the current page.
        :raises WebDriverException: when an error occurs while trying to get the title of the current page.
        """
        self.logger.log_method_entry(self.get_title.__name__)
        try:
            self.logger.info('Getting the title of the current page')
            title = self.driver.title
            self.logger.info(f'Successfully got the title of the current page. The title is: {title}')
            return title
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to get the title of the current page. Error: {e}')
            raise WebDriverException('Unable to get the title of the current page.')

    def click(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """
        Clicks on a WebElement.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for a WebElement to be clickable. Defaults to 10 seconds.
        :raises TimeoutException: when the WebElement isn't found or not clickable within the timeout.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises ElementClickInterceptedException: when the element is obscured by another element.
        :raises WebDriverException: when an error occurs while trying to click on a WebElement.
        """
        self.logger.log_method_entry(self.click.__name__)
        try:
            self.logger.info(f'Clicking on a WebElement that has this locator: {locator}')
            web_element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
            web_element.click()
            self.logger.info(f'Successfully clicked on a WebElement that has this locator: {locator}')
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to click on a WebElement that has this locator: {locator}'
                              f' within {timeout} seconds. Error: {e}')
            raise TimeoutException(f'No WebElement that has this locator: {locator} was found or wasn\'t clickable '
                                   f'within {timeout} seconds.')
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} couldn\'t be found in the DOM. '
                              f'Error: {e}')
            raise NoSuchElementException(f'No such a WebElement that has this locator: {locator} found in the DOM.')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was present in the DOM but wasn\'t '
                              f'interactable. Error: {e}')
            raise ElementNotInteractableException(f'The WebElement that has this locator: {locator } wasn\'t '
                                                  'interactable.')
        except ElementClickInterceptedException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was obscured by another element and '
                              f'couldn\'t be clicked. Error: {e}')
            raise ElementClickInterceptedException(f'The WebElement that has this locator: {locator} couldn\'t be '
                                                   'clicked.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to click on a WebElement with this locator: {locator}. '
                              f'Error: {e}')
            raise WebDriverException(f'Unable to click on the WebElement with this {locator}.')

    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        """
        Enters text into a WebElement.

        :param locator: the locator strategy and value.
        :param text: the text to enter into a WebElement.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to enter a text into a WebElement.
        """
        self.logger.log_method_entry(self.send_keys.__name__)
        try:
            self.logger.info(f'Sending this text: {text} into a WebElement that has this locator: {locator}')
            web_element = self.find_element(locator)
            web_element.clear()
            web_element.send_keys(text)
            self.logger.info(f'Successfully sent the text: {text} into a WebElement that has this locator: {locator}.')
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} couldn\'t be found in the DOM. '
                              f'Error: {e}')
            raise NoSuchElementException(f'No such a WebElement that has this locator: {locator} found in the DOM.')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was present in the DOM but wasn\'t '
                              f'interactable. Error: {e}')
            raise ElementNotInteractableException(f'The WebElement that has this locator: {locator} wasn\'t '
                                                  'interactable.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to send this text: {text} into a WebElement that has '
                              f'this locator: {locator}. Error: {e}')
            raise WebDriverException(f'Unable to send this text: {text} into a WebElement that has this locator: '
                                     f'{locator}.')

    def quit(self) -> None:
        """
        Closes all browser windows and ends the WebDriver session.

        :raises WebDriverException: when an error occurs while trying to quit the WebDriver session.
        """
        self.logger.log_method_entry(self.quit.__name__)
        try:
            self.logger.info(f'Closing all browser windows and ending the WebDriver session.')
            self.driver.quit()
            self.logger.info(f'Successfully closed all browser windows and ending the WebDriver session.')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to close all browser windows and ending the WebDriver '
                              f'session. Error: {e}')
            raise WebDriverException('Unable to close all browser windows and ending the WebDriver session.')

    def close(self) -> None:
        """
        Closes the current browser window.

        :raises WebDriverException: when an error occurs while trying to close the current window.
        """
        self.logger.log_method_entry(self.close.__name__)
        try:
            self.logger.info('Closing the current browser window.')
            self.driver.close()
            self.logger.info(f'Successfully closed the current browser window.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to close the current window. Error: {e}')
            raise WebDriverException('Unable to close the current window.')

    def is_dropdown_multiple_selections(self, locator: tuple[str, str]) -> bool:
        """
        Checks if the dropdown supports multiple selections.

        :param locator: the locator strategy and value.
        :return: True if the dropdown supports multiple selections, otherwise False.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to check if the dropdown supports multiple
                                    selections or not.
        """
        self.logger.log_method_entry(self.is_dropdown_multiple_selections.__name__)
        try:
            self.logger.info(f'Checking if the dropdown supports multiple selections.')
            web_element = self.find_element(locator)
            dropdown = Select(web_element)
            if dropdown.is_multiple:
                self.logger.info(f'The dropdown supports multiple selections.')
            else:
                self.logger.info(f'The dropdown doesn\'t support multiple selections.')
            return dropdown.is_multiple
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to check if the dropdown supports multiple selections '
                              f'or not. Error: {e}')
            raise WebDriverException('Unable to check if the dropdown supports multiple selections or not.')

    def select_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Selects a dropdown option by a visible text.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a dropdown option by a visible text.
        """
        self.logger.log_method_entry(self.select_dropdown_by_visible_text.__name__)
        try:
            self.logger.info(f'Selecting a dropdown option by this visible text: {text}.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_visible_text(text)
            self.logger.info(f'Successfully selected a dropdown option by this visible text: {text}.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to select a dropdown option by this visible text: '
                              f'{text}. Error: {e} ')
            raise WebDriverException(f'Unable to select a dropdown option by this visible text: {text}.')

    def select_dropdown_by_value(self, locator: tuple[str, str], value: str) -> None:
        """
        Selects a dropdown option by its value attribute.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a dropdown option by a value attribute.
        """
        self.logger.log_method_entry(self.select_dropdown_by_value.__name__)
        try:
            self.logger.info(f'Selecting a dropdown option by this value: {value}.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_value(value)
            self.logger.info(f'Successfully selected a dropdown option by this value: {value}.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to select a dropdown option by this value: {value}. '
                              f'Error: {e}')
            raise WebDriverException(f'Unable to select a dropdown option by this value: {value}.')

    def select_dropdown_by_index(self, locator: tuple[str, str], index: int) -> None:
        """
        Selects a dropdown option by its index.

        :param locator: the locator strategy and value.
        :param index: the index of the option to select.
        :raises ValueError: when the index is negative.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a dropdown option by an index.
        """
        self.logger.log_method_entry(self.select_dropdown_by_index.__name__)
        try:
            self.logger.info(f'Selecting a dropdown option by this index: {index}.')
            self.logger.info('Checking if the index is negative or not.')
            if index < 0:
                self.logger.error('Index cannot be negative.')
                raise ValueError('Index must be a non-negative integer.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_index(index)
            self.logger.info(f'Successfully selected a dropdown option by this index: {index}.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to select a dropdown option by this index: {index}. '
                              f'Error: {e}')
            raise WebDriverException(f'Unable to select a dropdown option by this index{index}.')

    def get_all_dropdown_options(self, locator: tuple[str, str]) -> list:
        """
        Returns all options in a dropdown as a list of strings.

        :param locator: the locator strategy and value.
        :return: a list of all dropdown options.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to get all dropdown options.
        """
        self.logger.log_method_entry(self.get_all_dropdown_options.__name__)
        try:
            self.logger.info(f'Getting all dropdown options.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            options = [option.text for option in drop_down.options]
            self.logger.info(f'Successfully got all dropdown options. Options are: {options}')
            return options
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to get all dropdown options. Error: {e}')
            raise WebDriverException(f'Unable to get all dropdown options.')

    def get_selected_dropdown_option(self, locator: tuple[str, str]) -> str:
        """
        Returns the currently selected option in a dropdown.

        :param locator: the locator strategy and value.
        :return: the text of the currently selected option.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to get the currently selected dropdown option.
        """
        self.logger.log_method_entry(self.get_selected_dropdown_option.__name__)
        try:
            self.logger.info(f'Getting the currently selected dropdown option.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            self.logger.info('Successfully got the currently selected dropdown option. The currently selected option '
                             f'is: {drop_down.first_selected_option.text}')
            return drop_down.first_selected_option.text
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to get the currently selected dropdown option. '
                              f'Error: {e}')
            raise WebDriverException('Unable to get the currently selected dropdown option.')

    def deselect_all_dropdown_options(self, locator: tuple[str, str]) -> None:
        """
        Deselects all selected options in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :raises InvalidArgumentException: If the dropdown is not a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to deselect all dropdown options.
        """
        self.logger.log_method_entry(self.deselect_all_dropdown_options.__name__)
        try:
            self.logger.info('Deselecting all selected options in a multi-select dropdown.')
            self.logger.info('Checking if the dropdown is a multi-select dropdown or not.')
            if not self.is_dropdown_multiple_selections(locator):
                self.logger.error('The dropdown isn\'t a multi-select dropdown.')
                raise InvalidArgumentException('The dropdown isn\'t supported the multi-select option.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_all()
            self.logger.info('Successfully deselected all selected options in the multi-select dropdown.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to deselect all selected options in the multi-select '
                              f'dropdown. Error: {e}')
            raise WebDriverException(f'Unable to deselect all selected options in the multi-select dropdown.')

    def deselect_dropdown_by_index(self, locator: tuple[str, str], index: int) -> None:
        """
        Deselects a dropdown option by its index in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param index: the index of the option to deselect.
        :raises InvalidArgumentException: when the dropdown isn't a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to deselect a dropdown option by an index.
        """
        self.logger.log_method_entry(self.deselect_dropdown_by_index.__name__)
        try:
            self.logger.info(f'Deselecting an option in the multi-select dropdown by this index: {index}.')
            self.logger.info('Checking if the dropdown supports multiple selections or not.')
            if not self.is_dropdown_multiple_selections(locator):
                self.logger.error('The dropdown doesn\'t support the multi-select option.')
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_index(index)
            self.logger.info(f'Successfully deselected a dropdown option by the index: {index}.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to deselect a dropdown option by this index: {index}. '
                              f'Error: {e}.')
            raise WebDriverException(f'Unable to deselect a dropdown option by this index: {index}.')

    def deselect_dropdown_by_value(self, locator: tuple[str, str], value: str) -> None:
        """
        Deselects a dropdown option by its value attribute in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to deselect.
        :raises InvalidArgumentException: when the dropdown isn't a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to deselect a dropdown option by a value.
        """
        self.logger.log_method_entry(self.deselect_dropdown_by_value.__name__)
        try:
            self.logger.info(f'Deselecting an option in the multi-select dropdown by this value: {value}.')
            self.logger.info('Checking if the dropdown supports multiple selections or not.')
            if not self.is_dropdown_multiple_selections(locator):
                self.logger.error('The dropdown doesn\'t support the multi-select option.')
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_value(value)
            self.logger.info(f'Successfully deselected an option by the value: {value}.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to deselect an option by this value: {value}. '
                              f'Error: {e}')
            raise WebDriverException(f'Unable to deselect a dropdown option by this value: {value}.')

    def deselect_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Deselects a dropdown option by its visible text in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to deselect.
        :raises InvalidArgumentException: If the dropdown isn't a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: if an error occurs while trying to select a dropdown option by a visible text.
        """
        self.logger.log_method_entry(self.deselect_dropdown_by_visible_text.__name__)
        try:
            self.logger.info(f'Deselecting an option in the multi-select dropdown by this visible text: {text}.')
            self.logger.info('Checking if the dropdown supports multiple selections or not.')
            if not self.is_dropdown_multiple_selections(locator):
                self.logger.error('The dropdown doesn\'t support the multi-select option.')
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_visible_text(text)
            self.logger.info(f'Successfully deselected an option by the visible text: {text}.')
        except UnexpectedTagNameException as e:
            self.logger.error(f'The Select class didn\'t get an expected WebElement. Error: {e}')
            raise UnexpectedTagNameException('The Select class received an unexpected WebElement that has this '
                                             f'locator: {locator}.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to deselect an option by this visible text: {text}. '
                              f'Error: {e}')
            raise WebDriverException(f'Unable to select a dropdown option by this visible text: {text}.')

    def switch_to_iframe(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """
        Switches the WebDriver's context to the specified IFrame.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for the IFrame to be available. Defaults to 10 seconds.
        :raises TimeoutException: when the IFrame is not available within the timeout.
        :raises NoSuchFrameException: when the IFrame doesn't exist.
        :raises WebDriverException: when an error occurs while trying to switch to a IFrame.
        """
        self.logger.log_method_entry(self.switch_to_iframe.__name__)
        try:
            self.logger.info(f'Switching to a IFrame that has this locator: {locator}.')
            WebDriverWait(self.driver, timeout).until(
                ec.frame_to_be_available_and_switch_to_it(locator)
            )
            self.logger.info(f'Successfully switched to the IFrame that has this locator: {locator}.')
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to switch to a IFrame that has this locator: {locator}. '
                              f'Error: {e}.')
            raise TimeoutException(f'The IFrame wasn\'t available within {timeout} seconds.')
        except NoSuchFrameException as e:
            self.logger.error(f'The IFrame that has this locator: {locator} couldn\'t be found in the DOM. Error: {e}.')
            raise NoSuchFrameException(f'No such an IFrame that has this locator: {locator} in the DOM.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to switch to a IFrame that has this locator: {locator}. '
                              f'Error: {e}.')
            raise WebDriverException(f'Unable to switch to IFrame that has this locator: {locator}.')

    def switch_to_default_content(self) -> None:
        """
        Switches the WebDriver's context back to the default content (outside the IFrame).

        :raises WebDriverException: when an error occurs while trying to switch to the default content.
        """
        self.logger.log_method_entry(self.switch_to_default_content.__name__)
        try:
            self.logger.info('Switching back to the default content.')
            self.driver.switch_to.default_content()
            self.logger.info(f'Successfully switched back to the default content.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to switch back to the default content. Error: {e}.')
            raise WebDriverException('Unable to switch back to the default content.')

    def accept_alert(self, timeout: int = 10) -> None:
        """
        Accepts an alert (clicks the "OK" button).

        :param timeout: the maximum time to wait for the alert to be present to accept. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to accept.
        :raises WebDriverException: when an error occurs while trying to accept an alert.
        """
        self.logger.log_method_entry(self.accept_alert.__name__)
        try:
            self.logger.info('Accepting an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.accept()
            self.logger.info(f'Successfully accepted the Alert.')
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to accept an Alert within {timeout} seconds. Error: {e}.')
            raise TimeoutException(f'The alert wasn\'t present within {timeout} seconds.')
        except NoAlertPresentException as e:
            self.logger.error(f'The Alert wasn\'t present!. Error: {e}.')
            raise NoAlertPresentException(f'No alert was present to accept.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to accept the Alert. Error: {e}.')
            raise WebDriverException(f'Unable to accept the Alert.')

    def dismiss_alert(self, timeout: int = 10) -> None:
        """
        Dismisses an alert (clicks the "Cancel" button).

        :param timeout: the maximum time to wait for the alert to be present to dismiss. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to dismiss.
        :raises WebDriverException: when an error occurs while trying to dismiss an alert.
        """
        self.logger.log_method_entry(self.dismiss_alert.__name__)
        try:
            self.logger.info('Dismissing an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.dismiss()
            self.logger.info(f'Successfully dismissed the Alert.')
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to dismiss an Alert within {timeout} seconds. '
                              f'Error: {e}.')
            raise TimeoutException(f'The alert was not present within {timeout} seconds.')
        except NoAlertPresentException as e:
            self.logger.error(f'The Alert wasn\'t present. Error: {e}.')
            raise NoAlertPresentException(f'No alert was present to dismiss.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to dismiss the Alert. Error: {e}.')
            raise WebDriverException(f'Unable to dismiss the Alert.')

    def get_alert_text(self, timeout: int = 10) -> str:
        """
        Gets the text of an alert.

        :param timeout: the maximum time to wait for the alert to be present to get its text. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to get its text.
        :raises WebDriverException: when an error occurs while trying to gett an alert text.
        """
        self.logger.log_method_entry(self.get_alert_text.__name__)
        try:
            self.logger.info('Getting the text of an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            self.logger.info(f'Successfully retrieved the text of an Alert. The text is: {alert.text}.')
            return alert.text
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to retrieve the text of the Alert within {timeout} '
                              f'seconds. Error: {e}.')
            raise TimeoutException(f'The alert was not present within {timeout} seconds.')
        except NoAlertPresentException as e:
            self.logger.error(f'The Alert wasn\'t present to get its text. Error: {e}.')
            raise NoAlertPresentException(f'No alert was present.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to retrieve the text of the Alert. Error: {e}.')
            raise WebDriverException(f'Unable to get the alert text.')

    def send_keys_to_alert(self, text: str, timeout: int = 10) -> None:
        """
        Sends text to a prompt alert.

        :param text: the text to send.
        :param timeout: the maximum time to wait for the alert to be present to send keys to it. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to send keys to it.
        :raises WebDriverException: when an error occurs while trying to send keys to a prompt alert.
        """
        self.logger.log_method_entry(self.send_keys_to_alert.__name__)
        try:
            self.logger.info(f'Sending this text: {text} to an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.send_keys(text)
            self.logger.info(f'Successfully sent this text: {text} to an Alert.')
        except TimeoutException as e:
            self.logger.error(f'Timeout occurred while trying to send this text: {text} to an alert within {timeout} '
                              f'seconds. Error: {e}.')
            raise TimeoutException(f'The alert wasn\'t presented within {timeout} seconds to send this text: {text} to '
                                   'it.')
        except NoAlertPresentException as e:
            self.logger.error(f'No alert was present to send this text {text} to it. Error: {e}.')
            raise NoAlertPresentException(f'No alert is presented to send this text: {text} to it.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to send this text {text} to the alert. Error: {e}.')
            raise WebDriverException(f'Unable to send this text: {text} to a prompt alert.')

    def get_current_window_handle(self) -> str:
        """
        Returns the handle of the current window.

        :return: the handle of the current window.
        :raises NoSuchWindowException: when the current window does not exist or is closed.
        :raises WebDriverException: when an error occurs while trying to get the current window handle.
        """
        self.logger.log_method_entry(self.get_current_window_handle.__name__)
        try:
            self.logger.info('Getting the current window handle.')
            current_window_handle = self.driver.current_window_handle
            self.logger.info('Successfully retrieved the current window handle. The current window handle is: '
                             f'{current_window_handle}.')
            return current_window_handle
        except NoSuchWindowException as e:
            self.logger.error(f'The current window handle does not exist or is closed. Error: {e}.')
            raise NoSuchWindowException('No such opened window to get its handle.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to retrieve the current window handle. Error: {e}.')
            raise WebDriverException('Unable to get the current window handle.')

    def get_all_window_handles(self) -> list:
        """
        Returns a list of all window handles.

        :return: a list of all window handles.
        :raises NoSuchWindowException: when no windows are opened.
        :raises WebDriverException: when an error occurs while trying to get all window handles.
        """
        self.logger.log_method_entry(self.get_all_window_handles.__name__)
        try:
            self.logger.info('Getting the all window handles.')
            all_window_handles = self.driver.window_handles
            self.logger.info('Successfully retrieved the all window handles. The all window handles are: '
                             f'{all_window_handles}.')
            return all_window_handles
        except NoSuchWindowException as e:
            self.logger.error(f'No opened windows to retrieve their handles. Error: {e}.')
            raise NoSuchWindowException(f'No windows were opened.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to retrieve all window handles. Error: {e}.')
            raise WebDriverException('Unable to get all window handles.')

    def switch_to_window(self, handle: str) -> None:
        """
        Switches the WebDriver's context to the specified window.

        :param handle: the handle of the window to switch to.
        :raises NoSuchWindowException: when the specified window doesn't exist or is closed.
        :raises WebDriverException: when an error occurs while trying to switch to a window.
        """
        self.logger.log_method_entry(self.switch_to_window.__name__)
        try:
            self.logger.info(f'Switching to the {handle} window.')
            self.driver.switch_to.window(handle)
            self.logger.info(f'Successfully switched to this {handle} window.')
        except NoSuchWindowException as e:
            self.logger.error(f'The {handle} window does not exist or is closed. Error: {e}.')
            raise NoSuchWindowException('The specified window didn\'t exist or was closed.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to switch {handle} window. Error: {e}.')
            raise WebDriverException(f'Unable to switch to this {handle} window.')

    def perform_hover_over_element_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a hover over a WebElement ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a hover over a WebElement ActionChain.
        """
        self.logger.log_method_entry(self.perform_hover_over_element_action_chain.__name__)
        try:
            self.logger.info(f'Performing an hover over this WebElement that has this locator: {locator}.')
            web_element = self.find_element(locator)
            ActionChains(self.driver).move_to_element(web_element).perform()
            self.logger.info(f'Successfully performed an hover over the WebElement that has this locator: {locator}.')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} isn\'t interactable to perform the '
                              f'hover over a WebElement ActionChain. Error: {e}.')
            raise ElementNotInteractableException(f'The WebElement was present but wasn\'t interactable to perform the '
                                                  f'hover over a WebElement ActionChain.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to perform a hover over ActionChain over this WebElement'
                              f' that has this locator: {locator}. Error: {e}.')
            raise WebDriverException('Unable to perform the hover over ActionChain over this WebElement that has this '
                                     f'locator: {locator}.')

    def perform_drag_and_drop_action_chain(self, source_locator: tuple[str, str],
                                           target_locator: tuple[str, str]) -> None:
        """
        Performs a drag and drop ActionChain.

        :param source_locator: the locator strategy and value for the source element.
        :param target_locator: the locator strategy and value for the target element.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a drag and drop ActionChain.
        """
        self.logger.log_method_entry(self.perform_drag_and_drop_action_chain.__name__)
        try:
            self.logger.info(f'Performing the drag and drop ActionChain with this source WebElement that has this '
                             f'locator: {source_locator}, and this target WebElement that has this locator: '
                             f'{target_locator}.')
            source_web_element = self.find_element(source_locator)
            target_web_element = self.find_element(target_locator)
            ActionChains(self.driver).drag_and_drop(source_web_element, target_web_element).perform()
            self.logger.info(f'Successfully performed the drag and drop ActionChain with this source WebElement that '
                             f'has this locator: {source_locator}, and this target WebElement that has this locator: '
                             f'{target_locator}.')
        except ElementNotInteractableException as e:
            self.logger.error(f'One of these WebElements (The source WebElement that has this locator: {source_locator}'
                              f', and the target WebElement that has this locator: {target_locator}), was present but '
                              f'wasn\'t interactable to perform the drag and drop ActionChain. Error: {e}.')
            raise ElementNotInteractableException(f'One of these WebElements (The source WebElement that has this '
                                                  f'locator: {source_locator}, and the target WebElement that has this '
                                                  f'locator: {target_locator}) wasn\'t interactable to perform the '
                                                  f'drag and drop ActionChain. ')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to perform the drag and drop ActionChain with these '
                              f'WebElements: (The source WebElement that has this locator: {source_locator}, and the '
                              f'target WebElement that has this locator: {target_locator}). Error: {e}.')
            raise WebDriverException('Unable to perform the drag and drop ActionChain with these WebElements: (The '
                                     f'source WebElement that has this locator: {source_locator}, and the target '
                                     f'WebElement that has this locator: {target_locator}).')

    def perform_double_click_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a double click ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a double click ActionChain.
        """
        self.logger.log_method_entry(self.perform_double_click_action_chain.__name__)
        try:
            self.logger.info(f'Performing the double click ActionChain on this WebElement that has this locator: '
                             f'{locator} ')
            web_element = self.find_element(locator)
            ActionChains(self.driver).double_click(web_element).perform()
            self.logger.info(f'Successfully performed the double click ActionChain on this WebElement that has this '
                             f'locator: {locator} ')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was not interactable to perform the '
                              f'double click ActionChain. Error: {e}.')
            raise ElementNotInteractableException(f'The WebElement that has this locator: {locator} was present but '
                                                  f'wasn\'t interactable to perform the double click ActionChain.')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to perform the double click ActionChain on this '
                              f'WebElement that has this locator: {locator}. Error: {e}.')
            raise WebDriverException('Unable to perform the double click ActionChain on this WebElement that has this '
                                     f'locator: {locator}.')

    def perform_right_click_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a right click (context click) ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a right click ActionChain.
        """
        self.logger.log_method_entry(self.perform_right_click_action_chain.__name__)
        try:
            self.logger.info('Performing the right click ActionChain on this WebElement that has this locator: '
                             f'{locator} ')
            web_element = self.find_element(locator)
            ActionChains(self.driver).context_click(web_element).perform()
            self.logger.info('Successfully performed the right click ActionChain on this WebElement that has this '
                             f'locator: {locator} ')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was not interactable to perform the '
                              f'right click ActionChain. Error: {e}.')
            raise ElementNotInteractableException(f'The WebElement that has this locator: {locator} was present but '
                                                  f'wasn\'t interactable to perform the right click ActionChain.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to perform the right click ActionChain on this '
                              f'WebElement that has this locator: {locator}. Error: {e}.')
            raise WebDriverException('Unable to perform the right click ActionChain on this WebElement that has this '
                                     f'locator: {locator}.')

    def perform_click_and_hold_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a click and hold ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a click and hold ActionChain.
        """
        self.logger.log_method_entry(self.perform_click_and_hold_action_chain.__name__)
        try:
            self.logger.info('Performing the click and hold ActionChain on this WebElement that has this locator: '
                             f'{locator}.')
            web_element = self.find_element(locator)
            ActionChains(self.driver).click_and_hold(web_element).perform()
            self.logger.info(f'Successfully performed the click and hold ActionChain on this WebElement that has this '
                             f'locator: {locator}.')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was not interactable to perform the '
                              f'click and hold ActionChain. Error: {e}.')
            raise ElementNotInteractableException(f'The WebElement that has this locator: {locator} was present but '
                                                  f'wasn\'t interactable to perform the click and hold ActionChain.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to perform the click and hold ActionChain on this '
                              f'WebElement that has this locator: {locator}. Error: {e}.')
            raise WebDriverException('Unable to perform the click and hold ActionChain on this WebElement that has '
                                     f'this locator: {locator}.')

    def perform_release_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a release ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a release ActionChain.
        """
        self.logger.log_method_entry(self.perform_release_action_chain.__name__)
        try:
            self.logger.info(f'Performing the release ActionChain on this WebElement that has this locator: {locator}')
            web_element = self.find_element(locator)
            ActionChains(self.driver).release(web_element).perform()
            self.logger.info(f'Successfully performed the release ActionChain on this WebElement that has this '
                             f'locator: {locator}')
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} wasn\'t interactable to perform the '
                              f'release ActionChain. Error: {e}.')
            raise ElementNotInteractableException(f'The WebElement that has this locator: {locator} was present but '
                                                  f'wasn\'t interactable to perform the release ActionChain.')
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to perform the release ActionChain on this WebElement '
                              f'that has this locator: {locator}. Error: {e}.')
            raise WebDriverException('Unable to perform the release ActionChain on this WebElement that has this '
                                     f'locator: {locator}.')

    def perform_send_keys_action_chain(self, *keys: str) -> None:
        """
        Sends key combinations (e.g., Ctrl+C, Ctrl+V).

        :param keys: the keys to send.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to send keys.
        """
        self.logger.log_method_entry(self.perform_send_keys_action_chain.__name__)
        try:
            self.logger.info(f'Performing the send keys ActionChain by sending these keys: {keys}')
            ActionChains(self.driver).send_keys(*keys).perform()
            self.logger.info(f'Successfully performed the send keys ActionChain by sending these keys: {keys}')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to perform the send keys ActionChain by sending these '
                              f'keys: {keys}. Error: {e}.')
            raise WebDriverException(f'Unable to send these keys: {keys}')
