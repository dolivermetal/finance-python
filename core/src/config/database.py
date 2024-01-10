import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.src.config.configs import DATABASE_CONFIG

log = logging.getLogger(__name__)


class DatabaseManager:

    def __init__(self) -> None:
        log.debug("initiate database connection")
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'postgresql+psycopg2',
            DATABASE_CONFIG.get("user"),
            DATABASE_CONFIG.get("password"),
            DATABASE_CONFIG.get("host"),
            DATABASE_CONFIG.get("port"),
            DATABASE_CONFIG.get("database")
        )
        self.__engine = self.__create_engine()
        self.session = None

    def __create_engine(self):
        log.debug("creating engine")
        engine = create_engine(self.__connection_string, echo=DATABASE_CONFIG.get("echo"))
        return engine

    def get_engine(self):
        log.debug("getting engine")
        return self.__engine

    def __enter__(self):
        log.debug("open session")
        session_make = sessionmaker(bind=self.__engine, expire_on_commit=DATABASE_CONFIG.get("expire_on_commit"))
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug("closing session")
        self.session.close()
