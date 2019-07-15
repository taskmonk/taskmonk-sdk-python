from taskmonk import TaskMonkClient
import json
import logging
from time import sleep
from taskmonk import BatchStatus

level    = logging.DEBUG
format   = '  %(message)s'
handlers = [logging.FileHandler('logger.log'), logging.StreamHandler()]

logging.basicConfig(level = level, format = format, handlers = handlers)

project_id = "456"

client = TaskMonkClient("http://localhost:9000", 
    project_id = project_id, 
    client_id = 'uIUSPlDMnH8gLEIrnlkdIPRE6bZYhHpw',
    client_secret= 'zsYgKGLUnftFgkASD8pndMwn3viA0IPoGKAiw6S7aVukgMWI8hGJflFs0P2QYxTg')




# #
# # Create the taxonomy
# #
# taxonomy_id = client.create_taxonomy('taxonomy_name') 
# logging.debug('Created taxonomy %s', taxonomy_id)

# #
# # Upload taxonomy categories
# #
# upload_result = client.import_taxonomy(taxonomy_id, '/home/dang/Downloads/taxonomy.xlsx')
# logging.debug('Import taxonomy result = %s', upload_result)

#
# Create the batch with the default parameters
#
batch_id = client.create_batch("batchname")
logging.debug('Created batch %s', batch_id)

import_task_from_url = client.import_tasks_url(project_id,batch_id,'https://drive.google.com/file/d/1WvklGqLHnJUy3hXmzA30nM-DLq3Yw6pj/view?usp=sharing','Excel')
logging.debug(import_task_from_url)

#
# Upload the tasks from the csv file
#
upload_job_id = client.upload_tasks(batch_id, '/Users/sampath/tmp.csv', 'CSV')
logging.debug("upload job_id = %s", upload_job_id)

#
# Check the progress of the upload job
#
upload_job_progress = client.get_job_progress(upload_job_id)
logging.debug("Job Progess = %s", upload_job_progress)

#
# Wait till the upload job is complete
#
while (not client.is_job_complete(upload_job_id)):
	logging.debug("waiting for job to complete")
	sleep(1)
logging.debug("Upload tasks is complete")

# #
# # Check the status of the batch
# #
batch_status = client.get_batch_status(batch_id)
logging.debug("Batch Status = %s", batch_status)

#
# Wait till the batch is completed by the annotation partners
#
while (not client.is_batch_complete(batch_id)):
	logging.debug("waiting for batch to complete")
	sleep(1)

logging.debug("Batch annotation is complete")

#
# Get batch output
# 
batch_output = client.get_batch_output(batch_id, '/tmp/output.csv', output_format = 'CSV')
logging.debug('batch_output = %s', batch_output)

completed = batch_status['completed']
total = batch_status['total']
batchComplete = client.isBatchComplete(BatchStatus(0,0,completed,total))
logging.debug(batchComplete)
