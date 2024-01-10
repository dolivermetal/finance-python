import logging

import yaml

log = logging.getLogger(__name__)
FLASK_CONFIG = None

try:
    if FLASK_CONFIG is None:
        with open("../rest-api/resources/config.yml", "r", encoding="UTF-8") as config_file:
            config = yaml.safe_load(config_file)
            FLASK_CONFIG = config["flask"]

except Exception as e:
    log.error("msg=error, e.message=%s", e, exc_info=e)
