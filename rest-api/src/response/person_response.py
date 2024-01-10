from typing import Dict

from core.src.entities.person import Person


# pylint: disable=too-few-public-methods
class PersonResponse:

    def __init__(self, person: Person) -> None:
        self.id = person.id
        self.code = person.code
        self.name = person.name
        self.creation_date = person.creation_date

    def format_response(self) -> Dict:
        return {'id': self.id, 'code': self.code, 'name': self.name, 'creation_date': self.creation_date}
