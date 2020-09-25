from main.ext.serializer import msl
from marshmallow import fields, EXCLUDE, post_dump


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
