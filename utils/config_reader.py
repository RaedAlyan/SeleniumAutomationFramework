import json
from pathlib import Path
from logging import getLogger

logger = getLogger(__name__)


def load_config(config_file : str = 'config_files/config.json') -> dict:
    """
     Loads and returns the configuration from a JSON file.

    :return: A dictionary containing the configuration data.
    :raises FileNotFoundError: If the configuration file does not exist.
    """
    logger.info(f'********** {load_config.__name__}() **********')
    try:
        current_dir = Path(__file__).parent
        config_path = (current_dir / ".." / config_file).resolve()
        logger.info(f'Loading configuration from: {config_path}')
        with open(config_path) as f:
            config = json.load(f)
        logger.info('The configuration file loaded successfully.')
        return config
    except FileNotFoundError as e:
        logger.error(f'The configuration file was not found. Error: {e}')
    except Exception as e:
        logger.error(f'An error occurred while loading the configuration file. Error: {e}')
