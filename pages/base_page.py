"""
This Module Encapsulates Common Web Interaction and Operations.

@author: Raed Eleyan.
@date: 03/17/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (WebDriverException,TimeoutException,
                                        NoSuchElementException,ElementNotVisibleException,
                                        ElementNotInteractableException,
                                        ElementClickInterceptedException,
                                        UnexpectedTagNameException,NoSuchFrameException,
                                        NoAlertPresentException,NoSuchWindowException)
from utils.logger import Logger


class BasePage:
    """
    This Class contains common methods for all pages.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = Logger()

    def find_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        """
        Finds and returns a single WebElement.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for a WebElement to be visible.
                        Defaults to 10 seconds.
        :return: the WebElement.
        :raises TimeoutException: when the WebElement isn't found or not visible within the timeout.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotVisibleException: when a WebElement is present on the DOM,
                                            but it's not visible.
        :raises WebDriverException: when an error occurs while trying to find the WebElement.
        """
        try:
            self.logger.info(f'Finding a WebElement that has this locator: {locator}')
            web_element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
            self.logger.info(f'Successfully found the WebElement that has this locator: {locator}')
            return web_element
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to find the WebElement that has '
                              f'this locator: {locator} within {timeout} seconds.')
            raise TimeoutException(f'The WebElement that has this locator: {locator} wasn\'t '
                                   f'found or wasn\'t visible within {timeout} seconds.') from e
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} couldn\'t '
                              'be found in the DOM.')
            raise NoSuchElementException(f'No such a WebElement that has this locator: {locator} '
                                         f'in the DOM.') from e
        except ElementNotVisibleException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was present '
                              'in the DOM, but wasn\'t visible.')
            raise ElementNotVisibleException(f'The WebElement that has this locator: {locator} '
                                             'wasn\'t visible.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to find the WebElement that has '
                              f'this locator: {locator}.')
            raise WebDriverException('Unable to find the WebElement that has this '
                                     f'locator: {locator}.') from e

    def find_elements(self, locator: tuple[str, str], timeout: int = 10) -> list[WebElement]:
        """
        Finds and returns a list of WebElements.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for a list of WebElements to be visible.
                        Defaults to 10 seconds.
        :return: a list of WebElements.
        :raises TimeoutException: when no WebElements are found or not visible within the timeout.
        :raises NoSuchElementException: when the WebElements couldn't be found in the DOM.
        :raises ElementNotVisibleException: when the WebElements are present on the DOM,
                but they're not visible.
        :raises WebDriverException: when an error occurs while trying to find the WebElements.
        """
        try:
            self.logger.info(f'Finding WebElements that have this locator: {locator}')
            web_elements = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_all_elements_located(locator)
            )
            self.logger.info('Successfully found the WebElements that have this '
                             f'locator: {locator}')
            return web_elements
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to find WebElements that '
                              f'have this locator: {locator} within {timeout} seconds.')
            raise TimeoutException(f'No WebElements that have this locator: {locator} were found '
                                   f'or weren\'t visible within {timeout} seconds.') from e
        except NoSuchElementException as e:
            self.logger.error(f'The WebElements that have this locator: {locator} couldn\'t be '
                              'found in the DOM.')
            raise NoSuchElementException(f'No such WebElements that have this locator: {locator} '
                                         'found in the DOM.') from e
        except ElementNotVisibleException as e:
            self.logger.error(f'The WebElements that have this locator: {locator} were present in '
                              'the DOM, but weren\'t visible.')
            raise ElementNotVisibleException(f'The WebElements that have this locator: {locator} '
                                             'weren\'t visible.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to find the WebElements that have '
                              f'this locator: {locator}.')
            raise WebDriverException('Unable to find the WebElements that have this locator: '
                                     f'{locator}.') from e

    def click(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """
        Clicks on a WebElement.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for a WebElement to be clickable.
                        Defaults to 10 seconds.
        :raises TimeoutException: when the WebElement isn't found or not clickable
                                  within the timeout.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotInteractableException: when the WebElement is present but
                                                 not interactable.
        :raises ElementClickInterceptedException: when the element is obscured by another element.
        :raises WebDriverException: when an error occurs while trying to click on a WebElement.
        """
        try:
            self.logger.info(f'Clicking on a WebElement that has this locator: {locator}')
            web_element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
            web_element.click()
            self.logger.info('Successfully clicked on a WebElement that has '
                             f'this locator: {locator}')
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to click on a WebElement that '
                              f'has this locator: {locator} within {timeout} seconds.')
            raise TimeoutException(f'No WebElement that has this locator: {locator} was '
                                   f'found or wasn\'t clickable within {timeout} seconds.') from e
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} couldn\'t be '
                              'found in the DOM.')
            raise NoSuchElementException(f'No such a WebElement that has this locator: {locator} '
                                         'found in the DOM.') from e
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was present in '
                              'the DOM but wasn\'t interactable.')
            raise ElementNotInteractableException('The WebElement that has this locator: '
                                                  f'{locator} wasn\'t interactable.') from e
        except ElementClickInterceptedException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was obscured by '
                              'another element and couldn\'t be clicked.')
            raise ElementClickInterceptedException('The WebElement that has this locator: '
                                                   f'{locator} couldn\'t be clicked.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to click on a WebElement with '
                              f'this locator: {locator}.')
            raise WebDriverException('Unable to click on the WebElement with this locator: '
                                     f'{locator}.') from e

    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        """
        Enters text into a WebElement.

        :param locator: the locator strategy and value.
        :param text: the text to enter into a WebElement.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotInteractableException: when the WebElement is present but
                                                 not interactable.
        :raises WebDriverException: when an error occurs while trying to enter a text
                                    into a WebElement.
        """
        try:
            self.logger.info(f'Sending this text: {text} into a WebElement that has this '
                             f'locator: {locator}')
            web_element = self.find_element(locator)
            web_element.clear()
            web_element.send_keys(text)
            self.logger.info(f'Successfully sent the text: {text} into a WebElement that has '
                             f'this locator: {locator}.')
        except NoSuchElementException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} couldn\'t be '
                              'found in the DOM.')
            raise NoSuchElementException(f'No such a WebElement that has this locator: {locator} '
                                         'found in the DOM.') from e
        except ElementNotInteractableException as e:
            self.logger.error(f'The WebElement that has this locator: {locator} was present in '
                              'the DOM but wasn\'t interactable.')
            raise ElementNotInteractableException('The WebElement that has this locator: '
                                                  f'{locator} wasn\'t interactable.') from e
        except WebDriverException as e:
            self.logger.error(f'An error occurred while trying to send this text: {text} into a '
                              f'WebElement that has this locator: {locator}.')
            raise WebDriverException(f'Unable to send this text: {text} into a WebElement that has '
                                     f'this locator: {locator}.') from e

    def select_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Selects a dropdown option by a visible text.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get
                                            an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a
                                    dropdown option by a visible text.
        """
        try:
            self.logger.info('Selecting a dropdown option by this visible '
                             f'text: {text}.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_visible_text(text)
            self.logger.info('Successfully selected a dropdown option by this '
                             f'visible text: {text}.')
        except UnexpectedTagNameException as e:
            self.logger.error('The Select class didn\'t get an expected WebElement.')
            raise UnexpectedTagNameException('The Select class received an unexpected '
                                             'WebElement that has this locator '
                                             f': {locator}.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to select a dropdown option '
                              f'by this visible text: {text}.')
            raise WebDriverException('Unable to select a dropdown option by this visible '
                                     f'text: {text}.') from e

    def select_dropdown_by_value(self, locator: tuple[str, str], value: str) -> None:
        """
        Selects a dropdown option by its value attribute.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get an
                                            expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a
                                    dropdown option by a value attribute.
        """
        try:
            self.logger.info(f'Selecting a dropdown option by this value: {value}.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_value(value)
            self.logger.info('Successfully selected a dropdown option by this '
                             f'value: {value}.')
        except UnexpectedTagNameException as e:
            self.logger.error('The Select class didn\'t get an expected WebElement.')
            raise UnexpectedTagNameException('The Select class received an unexpected '
                                             'WebElement that has this locator '
                                             f': {locator}.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to select a dropdown '
                              f'option by this value: {value}.')
            raise WebDriverException('Unable to select a dropdown option by this '
                                     f'value: {value}.') from e

    def select_dropdown_by_index(self, locator: tuple[str, str], index: int) -> None:
        """
        Selects a dropdown option by its index.

        :param locator: the locator strategy and value.
        :param index: the index of the option to select.
        :raises ValueError: when the index is negative.
        :raises UnexpectedTagNameException: when the Select class didn't get
                                            an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select
                                    a dropdown option by an index.
        """
        try:
            self.logger.info(f'Selecting a dropdown option by this index: {index}.')
            self.logger.info('Checking if the index is negative or not.')
            if index < 0:
                self.logger.error('Index cannot be negative.')
                raise ValueError('Index must be a non-negative integer.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_index(index)
            self.logger.info('Successfully selected a dropdown option by this '
                             f'index: {index}.')
        except UnexpectedTagNameException as e:
            self.logger.error('The Select class didn\'t get an expected WebElement.')
            raise UnexpectedTagNameException('The Select class received an unexpected '
                                             'WebElement that has this locator '
                                             f': {locator}.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to select a dropdown '
                              f'option by this index: {index}.')
            raise WebDriverException('Unable to select a dropdown option by this '
                                     f'index{index}.') from e

    def get_all_dropdown_options(self, locator: tuple[str, str]) -> list:
        """
        Returns all options in a dropdown as a list of strings.

        :param locator: the locator strategy and value.
        :return: a list of all dropdown options.
        :raises UnexpectedTagNameException: when the Select class didn't
                                            get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to
                                    get all dropdown options.
        """
        try:
            self.logger.info('Getting all dropdown options.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            options = [option.text for option in drop_down.options]
            self.logger.info('Successfully got all dropdown options. '
                             f'Options are: {options}')
            return options
        except UnexpectedTagNameException as e:
            self.logger.error('The Select class didn\'t get an expected WebElement.')
            raise UnexpectedTagNameException('The Select class received an unexpected '
                                             'WebElement that has this locator '
                                             f': {locator}.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to get all dropdown options.')
            raise WebDriverException('Unable to get all dropdown options.') from e

    def get_selected_dropdown_option(self, locator: tuple[str, str]) -> str:
        """
        Returns the currently selected option in a dropdown.

        :param locator: the locator strategy and value.
        :return: the text of the currently selected option.
        :raises UnexpectedTagNameException: when the Select class didn't
                                            get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to get the
                                    currently selected dropdown option.
        """
        try:
            self.logger.info('Getting the currently selected dropdown option.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            self.logger.info('Successfully got the currently selected dropdown '
                             'option. The currently selected option '
                             f'is: {drop_down.first_selected_option.text}')
            return drop_down.first_selected_option.text
        except UnexpectedTagNameException as e:
            self.logger.error('The Select class didn\'t get an expected WebElement.')
            raise UnexpectedTagNameException('The Select class received an unexpected '
                                             'WebElement that has this locator'
                                             f': {locator}.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to get the currently '
                              'selected dropdown option.')
            raise WebDriverException('Unable to get the currently selected dropdown '
                                     'option.') from e

    def switch_to_iframe(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """
        Switches the WebDriver's context to the specified IFrame.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for the IFrame to be available.
                        Defaults to 10 seconds.
        :raises TimeoutException: when the IFrame is not available within the timeout.
        :raises NoSuchFrameException: when the IFrame doesn't exist.
        :raises WebDriverException: when an error occurs while trying to switch to a IFrame.
        """
        try:
            self.logger.info(f'Switching to a IFrame that has this locator: {locator}.')
            WebDriverWait(self.driver, timeout).until(
                ec.frame_to_be_available_and_switch_to_it(locator)
            )
            self.logger.info('Successfully switched to the IFrame that has '
                             f'this locator: {locator}.')
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to switch to a IFrame that '
                              f'has this locator: {locator}.')
            raise TimeoutException(f'The IFrame wasn\'t available within {timeout} '
                                   'seconds.') from e
        except NoSuchFrameException as e:
            self.logger.error(f'The IFrame that has this locator: {locator} couldn\'t be '
                              'found in the DOM.')
            raise NoSuchFrameException('No such an IFrame that has this locator: '
                                       f'{locator} in the DOM.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to switch to a IFrame that has '
                              f'this locator: {locator}.')
            raise WebDriverException('Unable to switch to IFrame that has this '
                                     f'locator: {locator}.') from e

    def switch_to_default_content(self) -> None:
        """
        Switches the WebDriver's context back to the default content (outside the IFrame).

        :raises WebDriverException: when an error occurs while trying to switch to
                                    the default content.
        """
        try:
            self.logger.info('Switching back to the default content.')
            self.driver.switch_to.default_content()
            self.logger.info('Successfully switched back to the default content.')
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to switch back to the '
                              'default content.')
            raise WebDriverException('Unable to switch back to the default '
                                     'content.') from e

    def accept_alert(self, timeout: int = 10) -> None:
        """
        Accepts an alert (clicks the "OK" button).

        :param timeout: the maximum time to wait for the alert to be present to accept.
                        Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to accept.
        :raises WebDriverException: when an error occurs while trying to accept an alert.
        """
        try:
            self.logger.info('Accepting an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.accept()
            self.logger.info('Successfully accepted the Alert.')
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to accept an Alert within '
                              f'{timeout} seconds.')
            raise TimeoutException(f'The alert wasn\'t present within {timeout} '
                                   'seconds.') from e
        except NoAlertPresentException as e:
            self.logger.error('The Alert wasn\'t present!.')
            raise NoAlertPresentException('No alert was present to accept.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to accept the Alert.')
            raise WebDriverException('Unable to accept the Alert.') from e

    def dismiss_alert(self, timeout: int = 10) -> None:
        """
        Dismisses an alert (clicks the "Cancel" button).

        :param timeout: the maximum time to wait for the alert to be present to dismiss.
                        Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to dismiss.
        :raises WebDriverException: when an error occurs while trying to dismiss an alert.
        """
        try:
            self.logger.info('Dismissing an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.dismiss()
            self.logger.info('Successfully dismissed the Alert.')
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to dismiss an '
                              f'Alert within {timeout} seconds.')
            raise TimeoutException(f'The alert was not present within {timeout} '
                                   'seconds.') from e
        except NoAlertPresentException as e:
            self.logger.error('The Alert wasn\'t present.')
            raise NoAlertPresentException('No alert was present to dismiss.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to dismiss the Alert.')
            raise WebDriverException('Unable to dismiss the Alert.') from e

    def get_alert_text(self, timeout: int = 10) -> str:
        """
        Gets the text of an alert.

        :param timeout: the maximum time to wait for the alert to be present to get its text.
                        Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to get its text.
        :raises WebDriverException: when an error occurs while trying to gett an alert text.
        """
        try:
            self.logger.info('Getting the text of an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            self.logger.info('Successfully retrieved the text of an Alert. '
                             f'The text is: {alert.text}.')
            return alert.text
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to retrieve the text of '
                              f'the Alert within {timeout} seconds.')
            raise TimeoutException(f'The alert was not present within {timeout} '
                                   'seconds.') from e
        except NoAlertPresentException as e:
            self.logger.error('The Alert wasn\'t present to get its text.')
            raise NoAlertPresentException('No alert was present.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to retrieve the text of the Alert.')
            raise WebDriverException('Unable to get the alert text.') from e

    def send_keys_to_alert(self, text: str, timeout: int = 10) -> None:
        """
        Sends text to a prompt alert.

        :param text: the text to send.
        :param timeout: the maximum time to wait for the alert to be present to send
                        keys to it. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to send keys to it.
        :raises WebDriverException: when an error occurs while trying to send keys to
                                    a prompt alert.
        """
        try:
            self.logger.info(f'Sending this text: {text} to an Alert.')
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.send_keys(text)
            self.logger.info(f'Successfully sent this text: {text} to an Alert.')
        except TimeoutException as e:
            self.logger.error('Timeout occurred while trying to send this text: '
                              f'{text} to an alert within {timeout} seconds.')
            raise TimeoutException(f'The alert wasn\'t presented within {timeout} seconds '
                                   f'to send this text: {text} to it.') from e
        except NoAlertPresentException as e:
            self.logger.error('No alert was present to send this text {text} to it.')
            raise NoAlertPresentException('No alert is presented to send this '
                                          f'text: {text} to it.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to send this '
                              f'text {text} to the alert.')
            raise WebDriverException(f'Unable to send this text: {text} to a '
                                     'prompt alert.') from e

    def get_current_window_handle(self) -> str:
        """
        Returns the handle of the current window.

        :return: the handle of the current window.
        :raises NoSuchWindowException: when the current window does not
                                       exist or is closed.
        :raises WebDriverException: when an error occurs while trying to get
                                    the current window handle.
        """
        try:
            self.logger.info('Getting the current window handle.')
            current_window_handle = self.driver.current_window_handle
            self.logger.info('Successfully retrieved the current window handle. '
                             f'The current window handle is: {current_window_handle}.')
            return current_window_handle
        except NoSuchWindowException as e:
            self.logger.error('The current window handle does not exist or is closed.')
            raise NoSuchWindowException('No such opened window to get its handle.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to retrieve the current '
                              'window handle.')
            raise WebDriverException('Unable to get the current window handle.') from e

    def get_all_window_handles(self) -> list:
        """
        Returns a list of all window handles.

        :return: a list of all window handles.
        :raises NoSuchWindowException: when no windows are opened.
        :raises WebDriverException: when an error occurs while trying to get all
                                    window handles.
        """
        try:
            self.logger.info('Getting the all window handles.')
            all_window_handles = self.driver.window_handles
            self.logger.info('Successfully retrieved the all window handles. '
                             f'The all window handles are: {all_window_handles}.')
            return all_window_handles
        except NoSuchWindowException as e:
            self.logger.error('No opened windows to retrieve their handles.')
            raise NoSuchWindowException('No windows were opened.') from e
        except WebDriverException as e:
            self.logger.error('An error occurred while trying to retrieve all window handles.')
            raise WebDriverException('Unable to get all window handles.') from e
