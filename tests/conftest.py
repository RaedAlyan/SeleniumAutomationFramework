import pytest
from utils.logger import setup_logger
from utils.config_reader import load_config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from utils.random_data_generator import RandomDataGenerator

logger = setup_logger()


@pytest.fixture(scope='class')
def driver():
    """
    Initializes and yields the WebDriver based on the specified browser in the config file.
    :return:
    """
    logger.info(f'********** {driver.__name__}() **********')
    web_driver = None
    try:
        logger.info('Starting setup stage ...')
        browser = _get_specified_browser()
        web_driver = _initialize_web_driver(browser)
        web_driver.maximize_window()
        yield web_driver
    except WebDriverException as e:
        logger.error(f'An error occurred while initializing the web driver. Error: {e}')
    finally:
        logger.info('The tearDown stage is finishing ...')
        if web_driver is not None:
            web_driver.quit()
        logger.info('The tearDown stage finished successfully.')


def _get_specified_browser() -> str:
    """
    Gets the specified browser type from the config.json file.

    :return: the browser specified in the configuration.
    :raises ValueError: if the browser isn't found.
    :raises Exception: if An error occurred while loading the config.json file.
    """
    logger.info(f'********** {_get_specified_browser.__name__}() **********')
    try:
        logger.info('Loading config file...')
        config = load_config()
        logger.info('Getting the specified browser from the config.json')
        browser = config['browser'].lower()
        logger.info(f'The specified browser is {browser}')
        return browser
    except KeyError as e:
        logger.error(f'Missing "browser" key in the config.json file. Error: {e}')
    except Exception as e:
        logger.error(f'An error occurred while loading the config.json file. Error: {e}')


def _initialize_web_driver(browser) -> WebDriver:
    """
    Initializes the WebDriver based on the specified browser.

    :param browser: the browser type (e.g., 'chrome', 'firefox', 'edge').
    :return: the initialized webdriver object.
    :raises ValueError: if the browser isn't supported.
    :raises Exception: if an error occurred while initializing the webdriver.
    """
    logger.info(f'********** {_initialize_web_driver.__name__}() **********')
    try:
        if browser == 'chrome':
            return _initialize_chrome_driver()
        elif browser == 'firefox':
            return _initialize_firefox_driver()
        elif browser == 'edge':
            return _initialize_edge_driver()
        else:
            logger.error('Specified browser is not supported.')
            raise ValueError(f'Unsupported browser: {browser}')
    except ValueError as e:
        logger.error(f'Unsupported browser: {browser}. Error: {e}')
    except Exception as e:
        logger.error(f'An error occurred while initializing the webdriver. Error: {e}')


def _initialize_chrome_driver() -> WebDriver:
    """
    Initializes a Chrome WebDriver instance.

    :return: the initialized chrome webdriver object.
    :raises WebDriverException: if an error occurred while initializing the chrome webdriver.
    """
    logger.info(f'********** {_initialize_chrome_driver.__name__}() **********')
    try:
        logger.info('Initializing Chrome WebDriver...')
        chrome_webdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        logger.info('The chrome webdriver initialized successfully.')
        return chrome_webdriver
    except WebDriverException as e:
        logger.error(f'An error occurred while initializing the chrome webdriver. Error: {e}')


def _initialize_firefox_driver():
    """
    Initializes a Firefox WebDriver instance.

    :return: the initialized firefox webdriver object.
    :raises WebDriverException: if an error occurred while initializing the firefox webdriver.
    """
    logger.info(f'********** {_initialize_firefox_driver.__name__}() **********')
    try:
        logger.info('Initializing Firefox WebDriver...')
        firefox_webdriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        logger.info('The Firefox webdriver is initialized successfully.')
        return firefox_webdriver
    except WebDriverException as e:
        logger.error(f'An error occurred while initializing the Firefox webdriver. Error: {e}')


def _initialize_edge_driver():
    """
    Initializes an Edge WebDriver instance.

    :return: the initialized edge webdriver object.
    :raises WebDriverException: if an error occurred while initializing the edge webdriver.
    """
    logger.info(f'********** {_initialize_edge_driver.__name__}() **********')
    try:
        logger.info('Initializing Edge WebDriver')
        edge_webdriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        logger.info('The Edge webdriver is initialized successfully.')
        return edge_webdriver
    except WebDriverException as e:
        logger.error(f'An error occurred while initializing the edge webdriver. Error: {e}')


@pytest.fixture(scope='session')
def generated_data():
    faker = RandomDataGenerator()
    data = {
        "first_name": faker.generate_random_first_name(),
        "last_name": faker.generate_random_last_name(),
        "email": faker.generate_random_email(),
        "password": faker.generate_random_password(),
    }
    return data
