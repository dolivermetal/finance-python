import logging

from core.src.config.configs import LOGGING_CONFIG


# Carrega a configuração de log para o projeto
def logger_configure():
    try:
        # console = logging.StreamHandler()
        # console.setFormatter(logging.Formatter(logging_config.get("format")))
        # logging.getLogger().addHandler(console)
        logging.basicConfig(level=LOGGING_CONFIG.get("level"), format=LOGGING_CONFIG.get("format"))

    except KeyError:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] - %(message)s"
        )
