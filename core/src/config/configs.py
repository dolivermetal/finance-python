import logging

import yaml

log = logging.getLogger(__name__)

DATABASE_CONFIG = None
LOGGING_CONFIG = None

try:
    if DATABASE_CONFIG is None or LOGGING_CONFIG is None:
        with open("../core/resources/config.yml", "r", encoding="UTF-8") as __config_file:
            __config = yaml.safe_load(__config_file)
            DATABASE_CONFIG = __config.get("database")
            LOGGING_CONFIG = __config.get("logging")

except Exception as e:
    log.error("msg=error, e.message=%s", str(e), exc_info=e)
