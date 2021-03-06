from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    api = Api(app)

    from server.resources import t
    api.add_resource(t.App, '/')
    return app
