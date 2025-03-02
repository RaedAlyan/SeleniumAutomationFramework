"""
This module provides a lightweight class for loading configurations from the config.json file.

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com.
"""
import json
from logger import Logger


class ConfigLoader:

    def __init__(self, config_path : str ='../config/config.json') -> None:
        """
        Initializes the ConfigLoader with the path to the configuration file.

        :param config_path: the path to the configuration file. Defaults to '../config/config.json'
        """
        self.config_path = config_path
        self.config = self._load_config_file()
        self.logger = Logger()

    def _load_config_file(self) -> dict:
        """
        Loads the configuration file and returns its content as a dictionary.

        :return: the configuration data.
        :raise FileNotFoundError: if the configuration file is not found.
        """
        self.logger.log_method_entry(self._load_config_file.__name__)
        try:
            self.logger.info(f'Loading configuration file from {self.config_path}')
            with open(self.config_path) as config_file:
                config_data = json.load(config_file)
                self.logger.info(f'The configuration file has been loaded from {self.config_path} successfully.')
                return config_data
        except FileNotFoundError:
            self.logger.error('The configuration file wasn\'t found.')
            raise FileNotFoundError(f'The configuration file {self.config_path} was not found.')

    def get_specified_browser(self) -> str:
        """
        Retrieves the specified browser from the configuration file.

        :return: the name of the specified browser.
        """
        self.logger.log_method_entry(self.get_specified_browser.__name__)
        try:
            self.logger.info(f'Retrieving the specified browser from the configuration file')
            specified_browser = self.config['browser']
            self.logger.info(f'The specified browser which is : {specified_browser} has been retrieved from '
                             f'{self.config_path} successfully.')
            return specified_browser
        except KeyError as e:
            self.logger.error('No "browser" key in the configuration file.')
            raise KeyError(f'The "browser" key is missing in the configuration file. Error: {e}')
