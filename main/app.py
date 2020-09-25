from flask import Flask

from main.ext import config


def init_app():
	app = Flask(__name__)
	config.init_app(app)

	return app
