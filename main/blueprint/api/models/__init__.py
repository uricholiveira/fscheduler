from main.ext.bcrypt import bcrypt
from main.ext.db import db
from sqlalchemy import MetaData

import arrow
from dynaconf import settings


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


class CustomJobStore(db.Model):
	__tablename__ = 'apscheduler_jobs_custom'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	job_id = db.Column(db.String(255), unique=True)
	name = db.Column(db.String(255), unique=True)
	next_run_time = db.Column(db.DateTime, nullable=True)
	interval = db.Column(db.Time)
	days = db.Column(db.Integer, nullable=True)
	weeks = db.Column(db.Integer, nullable=True)
	start_date = db.Column(db.DateTime(True), nullable=True, default=arrow.now(settings.TIMEZONE))
	end_date = db.Column(db.DateTime(True), nullable=True)

	@property
	def seconds(self):
		return self.interval.second

	@property
	def minutes(self):
		return self.interval.minute

	@property
	def hours(self):
		return self.interval.hour


class CustomJobAudit(db.Model):
	__tablename__ = 'apscheduler_jobs_audit'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	job_id = db.Column(db.Integer, db.ForeignKey('apscheduler_jobs_custom.id'))
	event = db.Column(db.String(255), nullable=False)
	user = db.Column(db.String(255), nullable=True)
	job = db.relationship('CustomJobStore', backref=db.backref('audits', cascade="all,delete"))
	created = db.Column(db.DateTime(True), nullable=False, default=arrow.now(settings.TIMEZONE))


class CustomJobExecution(db.Model):
	__tablename__ = 'apscheduler_jobs_exec'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	job_id = db.Column(db.Integer, db.ForeignKey('apscheduler_jobs_custom.id'))
	hostname = db.Column(db.String(255), nullable=False)
	pid = db.Column(db.Integer, nullable=False)
	state = db.Column(db.String(255), nullable=False)
	created = db.Column(db.DateTime(True), nullable=False, default=arrow.now(settings.TIMEZONE))
	updated = db.Column(db.DateTime(True), nullable=True, onupdate=arrow.now(settings.TIMEZONE))
	job = db.relationship('CustomJobStore', backref=db.backref('executions', cascade="all,delete"))
