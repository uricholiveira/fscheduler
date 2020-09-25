import logging
import socket
import warnings

from apscheduler.events import EVENT_ALL
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from dynaconf import settings


class FlaskScheduler(BackgroundScheduler):
	def __init__(self, app=None, **options):
		super().__init__(**options)
		self._hostname = socket.gethostname().lower()
		self._app = app

	@property
	def hostname(self):
		return self._hostname

	@property
	def app(self):
		return self._app

	@app.setter
	def app(self, value):
		self.app = value

	def load_config(self):
		options = dict()

		jobstores = {
			'default': SQLAlchemyJobStore(url=settings.SQLALCHEMY_DATABASE_URI)
		}
		executors = {
			'default': ThreadPoolExecutor(settings.JOB_EXECUTORS),
			'processpool': ProcessPoolExecutor(settings.JOB_PROCESS_POOL)
		}
		job_defaults = {
			'default': settings.JOB_COALESCE,
			'max_instances': settings.JOB_MAX_INSTANCES
		}
		timezone = settings.TIMEZONE

		setattr(options, 'jobstores', jobstores)
		setattr(options, 'executors', executors)
		setattr(options, 'job_defaults', job_defaults)
		setattr(options, 'timezone', timezone)

		self.configure(**options)

	def init_app(self, app):
		self.app = app
		self.load_config()
