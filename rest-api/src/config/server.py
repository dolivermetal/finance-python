import logging

from flask import Flask, request, jsonify

from controller.person_controller import person_blueprint
from core.src.exceptions.illegal_argument_exception import IllegalArgumentException
from exceptions.http_not_found import HttpNotFoundException
from exceptions.http_unsupported_media_type import HttpUnsupportedMediaTypeException
from response.http_response import HttpResponse
from .configs import flask_config

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config.update(flask_config)

# Registro das rotas no flask
app.register_blueprint(person_blueprint)


@app.before_request
def before_request():
    __content_type = request.headers.get("Content-Type")
    if request.method == "POST":
        if __content_type is None or __content_type != "application/json":
            raise HttpUnsupportedMediaTypeException("supported media type: application/json")

        if request.is_json:
            request.json_data = request.get_json()


@app.errorhandler(HttpUnsupportedMediaTypeException)
def unsupported_media_type_handler(e: HttpUnsupportedMediaTypeException):
    return create_response(e)


@app.errorhandler(IllegalArgumentException)
def illegal_argument_handler(e: IllegalArgumentException):
    return create_response(e)


@app.errorhandler(HttpNotFoundException)
def not_found_handler(e: HttpNotFoundException):
    return create_response(e)


@app.errorhandler(Exception)
def exception_handler(e: Exception):
    log.error(f"msg=error, e.message={e}")
    http_response = HttpResponse(500, str(e))
    return jsonify(http_response.body), http_response.status_code


def create_response(e: (HttpUnsupportedMediaTypeException | IllegalArgumentException | HttpNotFoundException)):
    log.error(f"msg=error, e.status_code={e.status_code}, e.name={e.name}, e.message={e.message}")
    http_response = HttpResponse(e.status_code, e.message)
    return jsonify(http_response.body), http_response.status_code
