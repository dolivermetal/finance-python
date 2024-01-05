import logging

from core.src.config.configs import logging_config


# Configuração de Log
class LoggerConfig:

    # Carrega a configuração de log para o projeto
    @staticmethod
    def configure():
        try:
            # console = logging.StreamHandler()
            # console.setFormatter(logging.Formatter(logging_config.get("format")))
            # logging.getLogger().addHandler(console)
            logging.basicConfig(level=logging_config.get("level"), format=logging_config.get("format"))

        except Exception as e:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] - %(message)s"
            )
