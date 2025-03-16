"""
This module provides a lightweight class for loading configurations from the config.json file.

@author: Raed Eleyan.
@date: 03/16/2025.
@contact: raedeleyan1@gmail.com.
"""
import json
from pathlib import Path
# Optional[data_type] is shorthand for Union[data_type, None] and is more readable.
from typing import Optional
from .logger import Logger


class ConfigReader:
    """
    Loads and provides access to configurations from a JSON file.

    This class is responsible for reading a `config.json` file, parsing its contents,
    and providing methods to retrieve specific configuration values.
    """

    def __init__(self):
        self.abs_config_path = self._get_abs_config_path()
        self.config = self._load_config()
        self.logger = Logger()

    def _get_abs_config_path(self) -> Path:
        """Gets the absolute path to the config.json file."""
        abs_config_path = Path(__file__).parent.parent / "config" / "config.json"
        self.logger.info('The absolute path of the config.json file '
                         f'is: {abs_config_path}')
        return abs_config_path

    def _load_config(self) -> dict:
        """
        Retrieves the contents of the config.json file.

        :return: the contents of the config.json file.
        :raises FileNotFoundError: when the config.json does not exist.
        :raises json.JSONDecodeError: when the config.json file contains invalid JSON format.
        """
        try:
            with open(self.abs_config_path, encoding='utf-8') as config_file:
                config_data = json.load(config_file)
            self.logger.info('The configuration is loaded successfully.')
            return config_data
        except json.JSONDecodeError as e:
            self.logger.error('The config.json file contains invalid JSON.')
            raise json.JSONDecodeError(f'Invalid JSON in the {self.abs_config_path} file',
                                       e.doc, e.pos) from e
        except FileNotFoundError as e:
            self.logger.error('The config.json file not found!')
            raise FileNotFoundError(f'The {self.abs_config_path} file doesn\'t exist!.') from e

    def get_browser_configurations(self) -> Optional[dict]:
        """
        Retrieves the browser configurations from the config.json file.

        :return: the browser configurations.
        :raises KeyError: when the "browser_configurations" option
                          doesn't exist in the config.json file.
        """
        browser_configurations = self.config.get('browser_configurations')
        if browser_configurations is None:
            self.logger.error('No browser option in the browser_configurations option!')
            raise KeyError(f'The {self.abs_config_path} file doesn\'t contain '
                           'the "browser_configurations" key.')
        self.logger.info('The browser configurations are retrieved successfully.')
        return browser_configurations

    def get_headless_mode(self) -> Optional[bool]:
        """
        Retrieves the headless mode value from "browser_configurations" option.

        :return: the headless mode.
        :raises KeyError: when the "headless_mode" option doesn't exist in
                          the "browser_configurations" option.
        """
        browser_configurations = self.get_browser_configurations()
        headless_mode = browser_configurations.get('headless')
        if headless_mode is None:
            self.logger.error('No "headless" option in the "browser_configurations" option')
            raise KeyError('The "browser_configurations" option doesn\'t '
                           'contain the headless option')
        self.logger.info('The "headless" option is retrieved successfully.'
                         f'headless mode value is: {headless_mode}')
        return headless_mode

    def get_specified_browser(self) -> Optional[str]:
        """
        Retrieves the specified browser from the "browser_configurations" option.

        :return: the specified browser.
        :raises KeyError: when the "browser" option doesn't exist in
                          the "browser_configurations" option.
        """
        browser_configurations = self.get_browser_configurations()
        specified_browser = browser_configurations.get('browser')
        if specified_browser is None:
            self.logger.error('No "browser" option in the "browser_configurations" option')
            raise KeyError('The "browser_configurations" option doesn\'t '
                           'contain the browser option')
        self.logger.info('The "browser" option is retrieved successfully.'
                         f'The specified browser is: {specified_browser}')
        return specified_browser
