from .coree import FlaskScheduler
from ..db import db

sd = FlaskScheduler()


def init_app(app):
	sd.init_app(app, db)
