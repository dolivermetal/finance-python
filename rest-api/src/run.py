import core.src.config.logger as logger
from config.server import app

logger.configure()

if __name__ == '__main__':
    app.run(port=9090)
