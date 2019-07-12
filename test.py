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

class Test:

    def main(self):
        projectId = "240"
        #logging.debug(access_token_response.status_code)
        # Initialize the taskmonk client witht he oauth credentials and projectId

        client = TaskMonkClient("http://localhost:9000")

        # upload_tasks = client.uploadTasks(projectId,"/home/dang/Downloads/Primenow_Excel_50.xlsx","batchName")
        # logging.debug(upload_tasks)

        # project_info = client.getProjectInfoByID(projectId)
        # logging.debug(project_info)

        # project_users = client.getProjectUsers(projectId)
        # logging.debug(project_users)

        # job_progress = client.getJobProgress(projectId,10)
        # logging.debug(job_progress)

        # batch_status = client.getBatchStatus(projectId,10)
        # logging.debug(batch_status)

        

        # import_task_url = client.importTasksUrl(projectId=projectId)
        # logging.debug(import_task_url)

        createBatch = client.create_batch("batchName","127")
        logging.debug(createBatch)


logging.debug('Hello')
test = Test()
test.main()
