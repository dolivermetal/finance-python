import logging

from flask import Blueprint, request, jsonify

from entities.person import Person
from exceptions.http_not_found import HttpNotFoundException
from response.http_response import HttpResponse
from response.person_response import PersonResponse
from core.src.services.person_service import PersonService

log = logging.getLogger(__name__)

person_blueprint = Blueprint("person", __name__)
__service = PersonService()


@person_blueprint.route('/persons', methods=['GET'])
def find_all_persons():
    log.info("msg=listing all persons")
    persons = __service.find_all()

    if len(persons) == 0:
        raise HttpNotFoundException("persons not found")

    http_response = HttpResponse(200, [PersonResponse(person).format_response() for person in persons])
    return jsonify(http_response.body), http_response.status_code


@person_blueprint.route('/persons/<code>', methods=['GET'])
def get_person_by_code(code):
    log.info(f"msg=find person, code={code}")
    person = __service.find_by_code(code=code)

    if person is None:
        raise HttpNotFoundException("person not found")

    log.info(f"msg=person found, person={person}")
    http_response = HttpResponse(200, PersonResponse(person).format_response())
    return jsonify(http_response.body), http_response.status_code


@person_blueprint.route("/persons", methods=['POST'])
def create_person():
    log.info(f"msg=create person, data={request.json_data}")
    person = Person(
        id=request.json_data.get("id"),
        code=request.json_data.get("code"),
        name=request.json_data.get("name"),
        creation_date=request.json_data.get("creation_date")
    )
    __service.create_person(person)
    log.info(f"msg=person created, response={person}")
    http_response = HttpResponse(200, PersonResponse(person).format_response())
    return jsonify(http_response.body), http_response.status_code
