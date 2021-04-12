#!/usr/bin/python

import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()
# Simple Logger
logging.basicConfig(filename="/logs/app__init__.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # Testing logger
    logger.info("Flask App Configured")
    logger.info("DB Initialized")

    # Temporary route
    @app.route('/')
    def hello_world():
        return 'Hello World !! Its working and reloading too !!'

    return app