"""
This module provides a lightweight class for loading configurations from the config.json file.

@author: Raed Eleyan.
@date: 02/17/2025.
@contact: raedeleyan1@gmail.com.
"""
import json


class ConfigLoader:

    def __init__(self, config_path : str ='../config/config.json') -> None:
        """
        Initializes the ConfigLoader with the path to the configuration file.

        :param config_path: the path to the configuration file. Defaults to '../config/config.json'
        """
        self.config_path = config_path
        self.config = self._load_config_file()

    def _load_config_file(self) -> dict:
        """
        Loads the configuration file and returns its content as a dictionary.

        :return: the configuration data.
        :raise FileNotFoundError: if the configuration file is not found.
        """
        try:
            with open(self.config_path) as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            raise FileNotFoundError(f'The configuration file {self.config_path} was not found.')

    def get_specified_browser(self) -> str:
        """
        Retrieves the specified browser from the configuration file.

        :return: the name of the specified browser.
        """
        try:
            specified_browser = self.config['browser']
            return specified_browser
        except KeyError:
            raise KeyError('The "browser" key is missing in the configuration file.')
