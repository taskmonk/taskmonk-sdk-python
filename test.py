from taskmonk.TaskMonkClient import *
import json
import logging
from taskmonk.utils import urlConfig, apiCall, argumentlist, utilities

############ For logging to a file and console at the same time 
############ This will work for the whole code

#logging.basicConfig(level=logging.DEBUG)
level    = logging.DEBUG
format   = '  %(message)s'
handlers = [logging.FileHandler('logger.log'), logging.StreamHandler()]

logging.basicConfig(level = level, format = format, handlers = handlers)
logging.debug('Hey, this is working!')


project_id = "169"

client = TaskMonkClient("http://localhost:9000", 
    project_id = project_id, 
    client_id = 'uIUSPlDMnH8gLEIrnlkdIPRE6bZYhHpw',
    client_secret= 'zsYgKGLUnftFgkASD8pndMwn3viA0IPoGKAiw6S7aVukgMWI8hGJflFs0P2QYxTg')

batch_id = client.create_batch("batchname")
logging.debug('Created batch %s', batch_id)

upload_job_id = client.upload_tasks(batch_id, '/Users/sampath/tmp.csv', 'CSV')
logging.debug("upload job_id = %s", upload_job_id)

upload_job_progress = client.get_job_progress(upload_job_id)
logging.debug("Job Progess = %s", upload_job_progress)
