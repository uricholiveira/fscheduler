from flask_restx import Resource

from ..services.user import get_all_users
from ..utils.dto import User
from ..utils.schema import UserSerializer

api = User.api
user = User.model


@api.route('/')
class UserList(Resource):
	def get(self):
		serializer = UserSerializer(many=True)
		return serializer.dump(get_all_users())
