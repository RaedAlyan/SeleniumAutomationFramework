"""

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium.common import InvalidArgumentException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (WebDriverException, TimeoutException, NoSuchElementException,
                                        ElementNotVisibleException, ElementNotInteractableException,
                                        UnexpectedTagNameException, ElementClickInterceptedException,
                                        NoSuchFrameException, NoAlertPresentException, NoSuchWindowException)


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
        :raises WebDriverException: when an error occurs while trying to navigate to the specified URL.
        """
        try:
            self.driver.get(url)
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while navigating to this URL: {url}. Error: {e}')

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
        try:
            web_element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(locator)
            )
            return web_element
        except TimeoutException as e:
            raise TimeoutException(f'Timeout! The WebElement was not found or not visible within {timeout} seconds. '
                                   f'Error: {e}')
        except NoSuchElementException as e:
            raise NoSuchElementException(f'The WebElement could not be found in the DOM. Error: {e}')
        except ElementNotVisibleException as e:
            raise ElementNotVisibleException(f'The WebElement was present on the DOM, but was not visible. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to find the WebElement with this locator: '
                                     f'{locator}. Error: {e}')

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
        try:
            web_elements = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_all_elements_located(locator)
            )
            return web_elements
        except TimeoutException as e:
            raise TimeoutException(f'Timeout! No WebElements were found or not visible within {timeout} seconds. '
                                   f'Error: {e}')
        except NoSuchElementException as e:
            raise NoSuchElementException(f'The WebElements could not be found in the DOM. Error: {e}')
        except ElementNotVisibleException as e:
            raise ElementNotVisibleException('The WebElements were present on the DOM, but were not visible. '
                                             f'Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to find the WebElements with this locator: '
                                     f'{locator}. Error: {e}')

    def get_current_url(self) -> str:
        """
        Returns the current URL of the browser.

        :return: the current URL.
        :raises WebDriverException: when an error occurs while trying to get the current URL.
        """
        try:
            return self.driver.current_url
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to get the current URL. Error: {e}')

    def go_back(self) -> None:
        """
        Navigates back to the previous page in the browser history.

        :raises WebDriverException: when an error occurs while trying to navigate to the previous page.
        """
        try:
            self.driver.back()
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to navigate to the previous page. Error: {e}')

    def go_forward(self) -> None:
        """
        Navigates forward to the next page in the browser history.

        :raises WebDriverException: when an error occurs while trying to navigate to the next page.
        """
        try:
            self.driver.forward()
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to navigate to the next page. Error: {e}')

    def refresh(self) -> None:
        """
        Refreshes the current page.

        :raises WebDriverException: when an error occurs while trying to refresh the current page.
        """
        try:
            self.driver.refresh()
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to refresh the current page. Error: {e}')

    def get_title(self) -> str:
        """
        Returns the title of the current page.

        :return: the title of the current page.
        :raises WebDriverException: when an error occurs while trying to get the title of the current page.
        """
        try:
            return self.driver.title
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to get the title of the current page. Error: {e}')

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
        try:
            web_element = WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable(locator)
            )
            web_element.click()
        except TimeoutException as e:
            raise TimeoutException(f'Timeout! No WebElements were found or not clickable within {timeout} seconds. '
                                   f'Error: {e}')
        except NoSuchElementException as e:
            raise NoSuchElementException(f'The WebElements could not be found in the DOM. Error: {e}')
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except ElementClickInterceptedException as e:
            raise ElementClickInterceptedException('The WebElement is obscured by another element and can not be '
                                                   f'clicked. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to click on the WebElement with this {locator}. '
                                     f'Error: {e}')

    def send_keys(self, locator: tuple[str, str], text: str) -> None:
        """
        Enters text into a WebElement.

        :param locator: the locator strategy and value.
        :param text: the text to enter into a WebElement.
        :raises NoSuchElementException: when the WebElement couldn't be found in the DOM.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to enter a text into a WebElement.
        """
        try:
            web_element = self.find_element(locator)
            web_element.clear()
            web_element.send_keys(text)
        except NoSuchElementException as e:
            raise NoSuchElementException(f'The WebElements could not be found in the DOM. Error: {e}')
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to enter a text into a WebElement. Error: {e}')

    def quit(self) -> None:
        """
        Closes all browser windows and ends the WebDriver session.

        :raises WebDriverException: when an error occurs while trying to quit the WebDriver session.
        """
        try:
            self.driver.quit()
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to quit the WebDriver session. Error: {e}')

    def close(self) -> None:
        """
        Closes the current browser window.

        :raises WebDriverException: when an error occurs while trying to close the current window.
        """
        try:
            self.driver.close()
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to close the current window. Error: {e}')

    def is_dropdown_multiple_selections(self, locator: tuple[str, str]) -> bool:
        """
        Checks if the dropdown supports multiple selections.

        :param locator: the locator strategy and value.
        :return: True if the dropdown supports multiple selections, otherwise False.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to check if the dropdown supports multiple
                                    selections or not.
        """
        try:
            web_element = self.find_element(locator)
            dropdown = Select(web_element)
            return dropdown.is_multiple
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to check the dropdown supports multiple selections'
                                     f' or not. Error: {e}')

    def select_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Selects a dropdown option by a visible text.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a dropdown option by a visible text.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_visible_text(text)
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to select a dropdown option by a visible text. '
                                     f'Error: {e}')

    def select_dropdown_by_value(self, locator: tuple[str, str], value: str) -> None:
        """
        Selects a dropdown option by its value attribute.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a dropdown option by a value attribute.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_value(value)
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to select a dropdown option by a value. '
                                     f'Error: {e}')

    def select_dropdown_by_index(self, locator: tuple[str, str], index: int) -> None:
        """
        Selects a dropdown option by its index.

        :param locator: the locator strategy and value.
        :param index: the index of the option to select.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to select a dropdown option by an index.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.select_by_index(index)
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to select a dropdown option by an index. '
                                     f'Error: {e}')

    def get_all_dropdown_options(self, locator: tuple[str, str]) -> list:
        """
        Returns all options in a dropdown as a list of strings.

        :param locator: the locator strategy and value.
        :return: a list of all dropdown options.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to get all dropdown options.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            options = [option.text for option in drop_down.options]
            return options
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to get all dropdown options. Error: {e}')

    def get_selected_dropdown_option(self, locator: tuple[str, str]) -> str:
        """
        Returns the currently selected option in a dropdown.

        :param locator: the locator strategy and value.
        :return: the text of the currently selected option.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to get the currently selected dropdown option.
        """
        try:
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            return drop_down.first_selected_option.text
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to get the currently selected dropdown option. '
                                     f'Error: {e}')

    def deselect_all_dropdown_options(self, locator: tuple[str, str]) -> None:
        """
        Deselects all selected options in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :raises InvalidArgumentException: If the dropdown is not a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to deselect all dropdown options.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_all()
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to deselect all dropdown options. Error: {e}')

    def deselect_dropdown_by_index(self, locator: tuple[str, str], index: int) -> None:
        """
        Deselects a dropdown option by its index in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param index: the index of the option to deselect.
        :raises InvalidArgumentException: when the dropdown isn't a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to deselect a dropdown option by an index.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_index(index)
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to deselect a dropdown option by an index. '
                                     f'Error: {e}')

    def deselect_dropdown_by_value(self, locator: tuple[str, str], value: str) -> None:
        """
        Deselects a dropdown option by its value attribute in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param value: the value attribute of the option to deselect.
        :raises InvalidArgumentException: when the dropdown isn't a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: when an error occurs while trying to deselect a dropdown option by a value.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_value(value)
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to deselect a dropdown option by a value. '
                                     f'Error: {e}')

    def deselect_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Deselects a dropdown option by its visible text in a multi-select dropdown.

        :param locator: the locator strategy and value.
        :param text: the visible text of the option to deselect.
        :raises InvalidArgumentException: If the dropdown isn't a multi-select dropdown.
        :raises UnexpectedTagNameException: when the Select class didn't get an expected WebElement.
        :raises WebDriverException: if an error occurs while trying to select a dropdown option by a visible text.
        """
        try:
            if not self.is_dropdown_multiple_selections(locator):
                raise InvalidArgumentException('The dropdown is not a multi-select dropdown.')
            web_element = self.find_element(locator)
            drop_down = Select(web_element)
            drop_down.deselect_by_visible_text(text)
        except UnexpectedTagNameException as e:
            raise UnexpectedTagNameException(f'The Select class did not get an expected WebElement. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to select a dropdown option by a visible text. '
                                     f'Error: {e}')

    def switch_to_iframe(self, locator: tuple[str, str], timeout: int = 10) -> None:
        """
        Switches the WebDriver's context to the specified IFrame.

        :param locator: the locator strategy and value.
        :param timeout: the maximum time to wait for the IFrame to be available. Defaults to 10 seconds.
        :raises TimeoutException: when the IFrame is not available within the timeout.
        :raises NoSuchFrameException: when the IFrame doesn't exist.
        :raises WebDriverException: when an error occurs while trying to switch to a IFrame.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.frame_to_be_available_and_switch_to_it(locator)
            )
        except TimeoutException as e:
            raise TimeoutException(f'The IFrame was not available within {timeout} seconds. Error: {e}')
        except NoSuchFrameException as e:
            raise NoSuchFrameException(f'The IFrame did not exist. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to switch to a frame. Error: {e}')

    def switch_to_default_content(self) -> None:
        """
        Switches the WebDriver's context back to the default content (outside the IFrame).

        :raises WebDriverException: when an error occurs while trying to switch to the default content.
        """
        try:
            self.driver.switch_to.default_content()
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to switch to a default content. Error: {e}')

    def accept_alert(self, timeout: int = 10) -> None:
        """
        Accepts an alert (clicks the "OK" button).

        :param timeout: the maximum time to wait for the alert to be present to accept. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to accept.
        :raises WebDriverException: when an error occurs while trying to accept an alert.
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.accept()
        except TimeoutException as e:
            raise TimeoutException(f'The alert was not present within {timeout} seconds. Error: {e}')
        except NoAlertPresentException as e:
            raise NoAlertPresentException(f'No alert was present to accept. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to accept an Alert. Error: {e}')

    def dismiss_alert(self, timeout: int = 10) -> None:
        """
        Dismisses an alert (clicks the "Cancel" button).

        :param timeout: the maximum time to wait for the alert to be present to dismiss. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to dismiss.
        :raises WebDriverException: when an error occurs while trying to dismiss an alert.
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.dismiss()
        except TimeoutException as e:
            raise TimeoutException(f'The alert was not present within {timeout} seconds. Error: {e}')
        except NoAlertPresentException as e:
            raise NoAlertPresentException(f'No alert was present to dismiss. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to dismiss an Alert. Error: {e}')

    def get_alert_text(self, timeout: int = 10) -> str:
        """
        Gets the text of an alert.

        :param timeout: the maximum time to wait for the alert to be present to get its text. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to get its text.
        :raises WebDriverException: when an error occurs while trying to gett an alert text.
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            return alert.text
        except TimeoutException as e:
            raise TimeoutException(f'The alert was not present within {timeout} seconds. Error: {e}')
        except NoAlertPresentException as e:
            raise NoAlertPresentException(f'No alert was present to get its text. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to get the alert text. Error: {e}')

    def send_keys_to_alert(self, text: str, timeout: int = 10) -> None:
        """
        Sends text to a prompt alert.

        :param text: the text to send.
        :param timeout: the maximum time to wait for the alert to be present to send keys to it. Defaults to 10 seconds.
        :raises TimeoutException: when the alert is not present within the timeout.
        :raises NoAlertPresentException: when no alert is present to send keys to it.
        :raises WebDriverException: when an error occurs while trying to send keys to a prompt alert.
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present()
            )
            alert.send_keys(text)
        except TimeoutException as e:
            raise TimeoutException(f'The alert was not present within {timeout} seconds. Error: {e}')
        except NoAlertPresentException as e:
            raise NoAlertPresentException(f'No alert was present to send keys to it. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to send keys to a prompt alert. Error: {e}')

    def get_current_window_handle(self) -> str:
        """
        Returns the handle of the current window.

        :return: the handle of the current window.
        :raises NoSuchWindowException: when the current window does not exist or is closed.
        :raises WebDriverException: when an error occurs while trying to get the current window handle.
        """
        try:
            current_window_handle = self.driver.current_window_handle
            return current_window_handle
        except NoSuchWindowException as e:
            raise NoSuchWindowException(f'The current window did not exist or was closed. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to get the current window handle. Error: {e}')

    def get_all_window_handles(self) -> list:
        """
        Returns a list of all window handles.

        :return: a list of all window handles.
        :raises NoSuchWindowException: when no windows are opened.
        :raises WebDriverException: when an error occurs while trying to get all window handles.
        """
        try:
            all_window_handles = self.driver.window_handles
            return all_window_handles
        except NoSuchWindowException as e:
            raise NoSuchWindowException(f'No windows were opened. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while getting all window handles. Error: {e}')

    def switch_to_window(self, handle: str) -> None:
        """
        Switches the WebDriver's context to the specified window.

        :param handle: the handle of the window to switch to.
        :raises NoSuchWindowException: when the specified window doesn't exist or is closed.
        :raises WebDriverException: when an error occurs while trying to switch to a window.
        """
        try:
            self.driver.switch_to.window(handle)
        except NoSuchWindowException as e:
            raise NoSuchWindowException(f'The specified window did not exist or was closed. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to switch to a window. Error: {e}')

    def perform_hover_over_element_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a hover over a WebElement ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a hover over a WebElement ActionChain.
        """
        try:
            web_element = self.find_element(locator)
            ActionChains(self.driver).move_to_element(web_element).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to perform the hover over A WebElement '
                                     f'ActionChain. Error: {e}')

    def perform_drag_and_drop_action_chain(self, source_locator: tuple[str, str],
                                           target_locator: tuple[str, str]) -> None:
        """
        Performs a drag and drop ActionChain.

        :param source_locator: the locator strategy and value for the source element.
        :param target_locator: the locator strategy and value for the target element.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a drag and drop ActionChain.
        """
        try:
            source_web_element = self.find_element(source_locator)
            target_web_element = self.find_element(target_locator)
            ActionChains(self.driver).drag_and_drop(source_web_element, target_web_element).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to perform the drag and drop ActionChain. '
                                     f'Error: {e}')

    def perform_double_click_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a double click ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a double click ActionChain.
        """
        try:
            web_element = self.find_element(locator)
            ActionChains(self.driver).double_click(web_element).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to perform the double click ActionChain. '
                                     f'Error: {e}')

    def perform_right_click_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a right click (context click) ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a right click ActionChain.
        """
        try:
            web_element = self.find_element(locator)
            ActionChains(self.driver).context_click(web_element).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to perform the right click ActionChain. '
                                     f'Error: {e}')

    def perform_click_and_hold_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a click and hold ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a click and hold ActionChain.
        """
        try:
            web_element = self.find_element(locator)
            ActionChains(self.driver).click_and_hold(web_element).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException('An error occurred while trying to perform the click and hold ActionChain. '
                                     f'Error: {e}')

    def perform_release_action_chain(self, locator: tuple[str, str]) -> None:
        """
        Performs a release ActionChain.

        :param locator: the locator strategy and value.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to perform a release ActionChain.
        """
        try:
            web_element = self.find_element(locator)
            ActionChains(self.driver).release(web_element).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to perform the release ActionChain. Error: {e}')

    def perform_send_keys_action_chain(self, *keys: str) -> None:
        """
        Sends key combinations (e.g., Ctrl+C, Ctrl+V).

        :param keys: the keys to send.
        :raises ElementNotInteractableException: when the WebElement is present but not interactable.
        :raises WebDriverException: when an error occurs while trying to send keys.
        """
        try:
            ActionChains(self.driver).send_keys(*keys).perform()
        except ElementNotInteractableException as e:
            raise ElementNotInteractableException(f'The WebElement was present but not interactable. Error: {e}')
        except WebDriverException as e:
            raise WebDriverException(f'An error occurred while trying to send keys. Error: {e}')