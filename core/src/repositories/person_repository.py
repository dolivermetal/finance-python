from typing import List

from core.src.config.database import DatabaseManager
from core.src.entities.person import Person


# Classe responsável por efetuar a comunicação com o banco de dados nas consultas relacionadas ao objeto Person
class PersonRepository:

    # Busca todas as pessoas
    @classmethod
    def find(cls) -> List[Person]:
        with DatabaseManager() as db:
            try:
                person = (
                    db.session
                    .query(Person)
                    .all()
                )
                return person
            except Exception as e:
                db.session.rollback()
                raise e

    # Busca uma pessoa dado o seu código
    @classmethod
    def find_by_code(cls, code: str) -> Person:
        with DatabaseManager() as db:
            try:
                person = (
                    db.session
                    .query(Person)
                    .filter(Person.code == code)
                    .first()
                )
                return person
            except Exception as e:
                db.session.rollback()
                raise e

    # Cria uma entidade pessoa
    @classmethod
    def insert(cls, new_person: Person) -> None:
        with DatabaseManager() as db:
            try:
                db.session.add(new_person)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
