import socket

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from dynaconf import settings


class FlaskScheduler(BackgroundScheduler):
	def __init__(self, app=None, db=None, **options):
		super().__init__(**options)
		self._hostname = socket.gethostname().lower()
		self._app = app
		self._db = db

	@property
	def app(self):
		return self._app

	@app.setter
	def app(self, value):
		self._app = value

	@property
	def db(self):
		return self._db

	@db.setter
	def db(self, value):
		self._db = value

	@property
	def hostname(self):
		return self._hostname

	def load_config(self):
		options = dict()

		jobstores = {
			'default': SQLAlchemyJobStore(engine=self.db.get_engine(self.app), tablename='apscheduler_jobs_custom'),
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

		options['jobstores'] = jobstores
		options['executors'] = executors
		options['job_defaults'] = job_defaults
		options['timezone'] = timezone

		self.configure(**options)

	def init_app(self, app, db):
		self.app = app
		self.db = db
		self.load_config()
		self.start()
