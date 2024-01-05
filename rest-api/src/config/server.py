from flask import Flask, request

from .configs import flask_config
from controller.person_controller import person_blueprint

app = Flask(__name__)
app.config.update(flask_config)

# Registro das rotas no flask
app.register_blueprint(person_blueprint)


@app.before_request
def before_request():
    __content_type = request.headers.get("Content-Type")
    if request.method == "POST" and __content_type is None and __content_type == "application/json":
        raise Exception("Unsupported Media Type")

    if request.is_json:
        request.json_data = request.get_json()
