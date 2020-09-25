from flask import Blueprint
from flask_restx import Api

from .resources.user import api as user_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc')


def init_app(app):
	api.add_namespace(user_ns, path='/user')
	app.register_blueprint(blueprint)
