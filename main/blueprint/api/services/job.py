import logging
from main.ext.scheduler import sd

from ..models import CustomJobStore


def start_scheduler():
	try:
		sd.start()
		return {'status': 'success', 'message': 'Scheduler started!'}
	except Exception as e:
		return {'status': 'error', 'message': e}

def resume_all():
	try:
		sd.resume()
		return {'status': 'success', 'message': 'All jobs has resumed!'}
	except Exception as e:
		return {'status': 'error', 'message': e}


def resume_job(data):
	try:
		sd.resume_job(job_id=data['id'])
		job = 'Aaaa'
		return {'status': 'success', 'message': f'Job: {job} has resumed!'}
	except Exception as e:
		return {'status': 'error', 'message': e}


def get_jobs():
	jobs = sd.get_jobs()
	return [{'id': job.id, 'name': job.name} for i, job in enumerate(jobs)]


def say():
	print('Hello World!')


def add_job(data):
	try:
		sd.add_job(data['job_file'], 'interval', seconds=data['seconds'], name=data['job_name'])
		return {'status': 'success', 'message': 'Job added!'}
	except Exception as e:
		return {'status': 'error', 'message': e}


def pause_job(data):
	try:
		sd.pause_job(job_id=data["id"])
		return {'status': 'success', 'message': 'Job added!'}
	except Exception as e:
		return {'status': 'error', 'message': e}


def pause_all_jobs():
	try:
		sd.pause()
		return {'status': 'success', 'message': 'Job added!'}
	except Exception as e:
		return {'status': 'error', 'message': e}
# def modify_job(data, id)
