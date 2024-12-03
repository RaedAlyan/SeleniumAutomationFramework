import json
from logging import getLogger

logger = getLogger(__name__)


def load_config(config_file='config_files/config.json') -> dict:
    """
     Loads and returns the configuration from a JSON file.

    :return: A dictionary containing the configuration data.
    :raises FileNotFoundError: If the configuration file does not exist.
    """
    logger.info(f'********** {load_config.__name__} **********')
    try:
        logger.info(f'Loading configuration from: {config_file}')
        with open(config_file) as f:
            config = json.load(f)
        logger.info('The configuration file loaded successfully.')
        return config
    except FileNotFoundError as e:
        logger.error(f'The configuration file was not found. Error: {e}')
