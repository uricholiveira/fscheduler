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


class Job:
	api = Namespace('Job', description='User operations')
	model = api.model('job', {
		'job_id': fields.Integer(description='Job id'),
		'job_name': fields.String(description='Job name, if None = job.id'),
		'job_file': fields.String(description='File name that contains a job, example: "job.py"'),
		'seconds': fields.Integer(description='Interval in seconds'),
		'minutes': fields.Integer(description='Interval in minutes'),
		'hours': fields.Integer(description='Interval in hours'),
		'days': fields.Integer(description='Interval in days'),
		'weeks': fields.Integer(description='Interval in weeks'),
		'start_date': fields.Date(description='Start date'),
		'end_date': fields.Date(description='End date')
	})
