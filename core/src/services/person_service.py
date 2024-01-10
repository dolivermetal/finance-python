import logging
from typing import List

from core.src.entities.person import Person
from core.src.repositories.person_repository import PersonRepository

log = logging.getLogger(__name__)


# Classe responsável por implementar a regra de negócio relacionada a Pessoas
class PersonService:

    # Construtor com inicialização das classes dependentes
    def __init__(self):
        self.__repository = PersonRepository()

    # Busca todas as pessoas
    def find_all(self) -> List[Person]:
        log.info("msg=finding all persons")
        return self.__repository.find()

    # Busca uma pessoa dado o seu código
    def find_by_code(self, code) -> Person:
        log.info("msg=finding person, code=%s", code)
        return self.__repository.find_by_code(code=code)

    # Cria uma entidade pessoa
    def create_person(self, new_person: Person) -> None:
        try:
            log.info("msg=creation person, person=%s", new_person)
            self.__repository.insert(new_person)
        except Exception as e:
            log.error(f"msg=error, e.message={e}", exc_info=e)
            raise e
