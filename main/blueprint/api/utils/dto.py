from flask_restx import Namespace, fields


class User:
	api = Namespace('User', description='User operations')
	model = api.model('user', {
		'userid': fields.Integer(description='User identifier'),
		'name': fields.String(description='Username'),
		'email': fields.String(description='User email'),
		'password': fields.String(description='User password'),
		'is_active': fields.Boolean(description='User status (if is active, or not)'),
		'is_admin': fields.Boolean(description='User privilege (if is admin, or not)')
	})
