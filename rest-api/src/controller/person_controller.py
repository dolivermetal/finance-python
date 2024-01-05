import logging

from flask import Blueprint, request, jsonify

from core.src.services.person_service import PersonService
from entities.person import Person
from response.person_response import PersonResponse

log = logging.getLogger(__name__)

person_blueprint = Blueprint("person", __name__)
__service = PersonService()


@person_blueprint.route('/persons', methods=['GET'])
def find_all_persons():
    try:
        log.info(f"msg=listing all persons")
        persons = __service.find_all()
        return jsonify([PersonResponse(person).format_response() for person in persons]), 200
    except Exception as e:
        log.error(f"msg=error, e.message={e}", e)
        return jsonify({"error": type(e).__name__}), 500


@person_blueprint.route('/persons/<code>', methods=['GET'])
def get_person_by_code(code):
    try:
        log.info(f"msg=find person, code={code}")
        person = __service.find_by_code(code=code)
        log.info(f"msg=person found, person={person}")
        return jsonify(PersonResponse(person).format_response()), 200
    except Exception as e:
        log.error(f"msg=error, e.message={e}")
        return jsonify({'error': type(e).__name__}), 500


@person_blueprint.route("/persons", methods=['POST'])
def create_person():
    try:
        log.info(f"msg=create person, data={request.json_data}")
        person = Person(
            id=request.json_data.get("id"),
            code=request.json_data.get("code"),
            name=request.json_data.get("name"),
            creation_date=request.json_data.get("creation_date")
        )
        __service.create_person(person)
        log.info(f"msg=person created, response={person}")
        return jsonify(PersonResponse(person).format_response()), 200
    except Exception as e:
        log.error(f"msg=error, e.message={e}", e)
        return jsonify({'error': type(e).__name__}), 500
