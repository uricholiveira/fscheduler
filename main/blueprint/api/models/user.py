from main.ext.bcrypt import bcrypt
from main.ext.db import db


class User(db.Model):
	__tablename__ = 'user'

	userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), nullable=False)
	passw = db.Column(db.String(255), nullable=False, name='password')
	is_active = db.Column(db.Boolean, nullable=False, default=True)
	is_admin = db.Column(db.Boolean, nullable=False, default=False)

	@property
	def password(self):
		return self.passw

	@password.setter
	def password(self, value: str):
		self.password = bcrypt.generate_password_hash(value)

	def check_password(self, value: str):
		return bcrypt.check_password_hash(self.password, value)
