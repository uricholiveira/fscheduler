import arrow
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from main.ext.db import db


# class CustomDataStore(SQLAlchemyJobStore):
# 	def __init__(self, instance=None):
# 		self._instance = instance
#
# 	@classmethod
# 	def get_instance(cls, ):
