from main.ext.scheduler import sd


def get_jobs():
	jobs = sd.get_jobs()
	return [{'id': job.id, 'name': job.name} for i, job in enumerate(jobs)]


def say():
	print('Hello World!')


def add_job(data):
	try:
		sd.add_job(data['job_file'], 'interval', seconds=data['seconds'], id=data['job_id'], name=data['job_name'])
		return {'status': 'success', 'message': 'Job added!'}
	except Exception as e:
		return {'status': 'error', 'message': e}
