from flask_marshmallow import Marshmallow

msl = Marshmallow()


def init_app(app):
	msl.init_app(app)
