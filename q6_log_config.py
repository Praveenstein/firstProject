import logging.config
import json

LOGGER = logging.getLogger(__name__)


with open("log.json", 'r') as file_object:
    config_data = json.load(file_object)

logging.config.dictConfig(config_data)
LOGGER.debug("Testing Debug")
LOGGER.info("Testing Info")
