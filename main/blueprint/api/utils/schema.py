from marshmallow import fields, EXCLUDE, post_dump

from main.ext.serializer import msl


class UserSerializer(msl.SQLAlchemyAutoSchema):
	class Meta:
		unknown = EXCLUDE

	id = fields.Integer(required=False)
	name = fields.String(required=True)
	email = fields.String(required=True)
	password = fields.String(required=True)
	is_active = fields.Boolean(required=False)
	is_admin = fields.Boolean(required=False, dump_only=True)

	@post_dump()
	def wrapper(self, data, many, *args, **kwargs):
		return {'data': data}


class JobSerializer(msl.SQLAlchemyAutoSchema):
	class Meta:
		unknown = EXCLUDE

	id = fields.Integer(required=False)
	job_id = fields.String(required=False)
	name = fields.String(required=True)
	next_run_time = fields.DateTime(required=False)
	interval = fields.Time(required=True)
	days = fields.Integer(required=False)
	weeks = fields.Integer(required=False)
	start_date = fields.DateTime(required=False)
	end_date = fields.DateTime(required=False)

	@post_dump()
	def wrapper(self, data, many, *args, **kwargs):
		return {'data': data}
