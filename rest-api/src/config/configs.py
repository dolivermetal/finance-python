import logging

import yaml

log = logging.getLogger(__name__)
flask_config = None

try:
    if flask_config is None:
        with open("../rest-api/resources/config.yml", "r") as config_file:
            config = yaml.safe_load(config_file)
            flask_config = config["flask"]

except Exception as e:
    log.error(f"msg=error, e.message={e}", e)
