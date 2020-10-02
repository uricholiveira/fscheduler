from flask import request, jsonify
from flask_restx import Resource

from ..services.job import get_jobs, add_job, pause_job, pause_all_jobs, start_scheduler, resume_job, resume_all
from ..utils.dto import Job

api = Job.api
model = Job.model


@api.route('/')
class JobList(Resource):
	def get(self):
		return get_jobs()

	def post(self):
		return add_job(request.json)


@api.route('/start')
class JobStartAll(Resource):
	def post(self):
		return start_scheduler()


@api.route('/start/<id>')
class JobStart(Resource):
	def post(self, id: int):
		return resume_job(request.json)


@api.route('/pause')
class JobPauseAll(Resource):
	def post(self):
		return pause_all_jobs()


@api.route('/pause/<id>')
class JobPause(Resource):
	def post(self, id: int):
		return pause_job(request.json)


@api.route('/resume')
class JobResumeAll(Resource):
	def post(self):
		return resume_all()


@api.route('/resume/<id>')
class JobResume(Resource):
	def post(self, id: int):
		return resume_job(request.json)


@api.route('/shutdown')
class JobShutdown(Resource):
	def post(self):
		return pause_job(request.json)
