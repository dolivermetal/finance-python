from config.server import app
from core.src.config.logger import logger_configure

logger_configure()

if __name__ == '__main__':
    app.run(port=9090)
