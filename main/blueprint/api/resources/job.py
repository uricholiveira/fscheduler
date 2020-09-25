from flask import request, jsonify
from flask_restx import Resource

from ..services.job import get_jobs, add_job
from ..utils.dto import Job

api = Job.api
model = Job.model


@api.route('/')
class JobList(Resource):
	def get(self):
		return get_jobs()

	def post(self):
		return add_job(request.json)

