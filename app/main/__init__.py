from flask import Flask
from flask_cors import CORS
from ..db.db import mongo

from .config import config_by_name



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)

    mongo.init_app(app)

    return app