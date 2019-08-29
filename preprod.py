from taskmonk import TaskMonkClient
import json
import logging
from time import sleep
from taskmonk import BatchStatus
import sys
import time

level    = logging.DEBUG
format   = '  %(message)s'
handlers = [logging.FileHandler('logger.log'), logging.StreamHandler()]

logging.basicConfig(level = level, format = format, handlers = handlers)

project_id = "229"

client = TaskMonkClient("https://preprod.taskmonk.io",
    project_id = project_id, 
    client_id = 'xHBUcStrbqGiyjw3fTU66aG9ld4SgXx9',
    client_secret= 'reWLTGVZN0EFDlqEhEUVClm4D6p9OQvnpZVvPiAz41CCkhAy1lffxdQb3VK7gA4Y')




#
# Create the taxonomy
#
taxonomy_id = client.create_taxonomy('taxonomy_name') 
logging.debug('Created taxonomy %s', taxonomy_id)

#
# Upload taxonomy categories
#
upload_result = client.import_taxonomy(taxonomy_id, '/Users/sampath/taxonomy.xlsx')
logging.debug('Import taxonomy result = %s', upload_result)

#
# Create the batch with the default parameters
#
batch_id = client.create_batch("batchname8")
logging.debug('Created batch %s', batch_id)

#
#Upload Task from url
#
#upload_job_id_from_url = client.import_tasks_url(project_id,batch_id,'https://tmpupload.blob.core.windows.net/test/tmp.xlsx','Excel')
#logging.debug(upload_job_id_from_url)

#
# Upload the tasks from the csv file
#
upload_job_id = client.upload_tasks(batch_id, '/Users/sampath/pt.csv', 'CSV')
logging.debug("upload job_id = %s", upload_job_id)

time.sleep(5)

#
# Check the status of the batch
#
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
#batch_output = client.get_batch_output(batch_id, '/tmp/{}.csv'.format(batch_id), output_format='CSV', fields=[])
#logging.debug('batch_output = %s', batch_output)

batch_output = client.get_batch_output(batch_id, '/tmp/output.csv', output_format = 'CSV', fields=['product_id', 'Taxonomy_id', 'Taxonomy_Name','Taxonomy_Path', 'Comments', 'Suggestion for'])
logging.debug('batch_output = %s', batch_output)

