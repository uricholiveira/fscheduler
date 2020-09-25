from ..models import User


def get_all_users():
	"""Returns a list of existent Users"""
	try:
		return User.query.all()
	except Exception as e:
		pass
