from datetime import datetime

from sqlalchemy import Column, String, BigInteger, DateTime

from core.src.config.base import Base
from core.src.exceptions.invalid_data import InvalidDataException


class Person(Base):
    __tablename__ = "person"
    __table_args__ = {"schema": "finance", "extend_existing": True}

    id = Column(BigInteger, primary_key=True, name="idt_person")
    code = Column(String, name="cod_person")
    name = Column(String, name="nam_person")
    creation_date = Column(DateTime(timezone=True), name="dat_creation", default=datetime.now())

    def __init__(self, id: BigInteger, code: String, name: String, creation_date: datetime):
        self.id = id
        self.code = code
        self.name = name
        self.creation_date = creation_date
        self.validate()

    def __repr__(self):
        return f"Person(id={self.id}, code={self.code}, name={self.name}, creation_date={self.creation_date})"

    def validate(self):
        if not self.code:
            raise InvalidDataException("code can't be null or empty")

        if not self.name:
            raise InvalidDataException("name can't be null or empty")
