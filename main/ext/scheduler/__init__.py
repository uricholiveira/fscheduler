from .core import FlaskScheduler

sd = FlaskScheduler()


def init_app(app):
	sd.init_app(app)
