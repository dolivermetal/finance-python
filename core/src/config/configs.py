import logging

import yaml

log = logging.getLogger(__name__)

database_config = None
logging_config = None

try:
    if database_config is None or logging_config is None:
        with open("../core/resources/config.yml", "r") as __config_file:
            __config = yaml.safe_load(__config_file)
            database_config = __config.get("database")
            logging_config = __config.get("logging")

except Exception as e:
    log.error(f"msg=error, e.message={e}", e)
