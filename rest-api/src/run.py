from config.server import app
from core.src.config.logger import LoggerConfig

LoggerConfig.configure()

if __name__ == '__main__':
    app.run(port=9090)
