from utils import urlConfig, apiCall, argumentlist, utilities
from utils.jsonUtils import json2obj
import base64
import gzip
import json
import requests
import logging
#from apiKeycredentials import *

argsList = argumentlist.argsList
argumentVerifier = utilities.argumentVerifier

class Error(Exception):
   pass

class InvalidArguments(Error):
   pass


class TaskMonkClient:
    baseURL = urlConfig.BASE_URL
    token = None
    #oAuthClient

    def __init__(self, base_url=urlConfig.BASE_URL):
        self.baseURL = base_url
        #self.apiKey = api_key
        self.token = self.refreshToken()
    
    def refreshToken(self):
        #token_url = "http://localhost:9000/api/oauth2/token" 
        token_url = self.baseURL + '/api/oauth2/token'
        params =  {
            'grant_type': 'client_credentials',
            'client_id': 'uIUSPlDMnH8gLEIrnlkdIPRE6bZYhHpw',
            'client_secret':'zsYgKGLUnftFgkASD8pndMwn3viA0IPoGKAiw6S7aVukgMWI8hGJflFs0P2QYxTg'
        }
        headers = {'accept': 'application/json'}
        access_token_response = requests.post(token_url, params= params,headers = headers)
        #logging.debug(access_token_response.text)
        parsed = access_token_response.json()
        accessToken = parsed['access_token']
        logging.debug(accessToken)
        #logging.debug(access_token_response.status_code)
        return accessToken
    
    def getTokenResponse(self):
        if self.token is None:
            self.token = self.refreshToken
        #logging.debug(self.token)
        return self.token

    def getProjectInfoByID(self, projectId=None):
        try:
            if argumentVerifier([projectId, self.apiKey]):
                raise InvalidArguments
        except InvalidArguments:
            logging.debug('invalid arguments')
            return json.dumps(argsList['getProjectInfoByID'])
    
        url = self.baseURL + urlConfig.URLS['Project'] + '/' + projectId
        response = apiCall.get(self.token,url, {}, 10)
    
        return json2obj(response).response
    
    def getProjectUsers(self, projectId):
        url = self.baseURL + urlConfig.URLS['Project'] + '/' + projectId + '/users'
        response = apiCall.get(url, {}, 10)
        return response
    
    # def uploadTasks1(projectId, batchId, files=None, self.apiKey=None):
    #     url = self.baseURL + urlConfig.URLS['Project'] + '/' + projectId + '/import/tasks/batch/' + batchId
    #     # files = {'files': open('/Users/prashanth/Downloads/2095.14_Input.xls', 'rb')}
    #     # content = "encoded", batch_name = batchName, priority = Some(priority), comments = Some(comments))
    #     response = apiCall.fileUpload(self.apiKey, url, files , 30)
    #     return response
    
    def getJobProgress(self, projectId, jobId):
        url = self.baseURL + urlConfig.URLS['Project'] + '/' +projectId + '/job/' + jobId + '/status'
        response = apiCall.get(self.token,url, {}, 10)
        return json2obj(response).response
    
    def getBatchStatus(self, projectId, batchId):
        url = self.baseURL + urlConfig.URLS['Project'] + '/' + projectId + '/batch/' + batchId + '/status'
        response = apiCall.get(self.token,url, {}, 10)
        return response
    
    def uploadTasks(self,  projectId=None, batchId=None,file=None):
        url = self.baseURL + urlConfig.URLS['Project'] + projectId + "/batch/" + batchId + "/tasks/import"
    
        try:
            if argumentVerifier([projectId, file, batch_name, token]):
                raise InvalidArguments
        except InvalidArguments:
            logging.debug('invalid arguments', projectId, file)
            return json.dumps(argsList['uploadTasks']) 
    
        try:
            if file.endswith('.gz'):
                fileContent = open(file, 'rb').read()
                encoded = base64.b64encode(fileContent)
            else:
                fileContent = open(file, 'rb').read()
                with gzip.open('file.txt.gz', 'wb') as f:
                    f.write(fileContent)
                fileContent = open('file.txt.gz', 'rb').read()
                encoded = base64.b64encode(fileContent)
    
        except:
            return json.dumps({
                "response": None,
                "error": "failed to decode file, file format supported .gzip .xls .xlsx"
            })
    
        # notifications = []
        # if notification_email:
        #     notification = {}
        #     notification['notificationType'] = "Email"
        #     metaData = {'email_address': notification_email}
        #     notification['metaData'] = metaData
        #     notifications.append(notification)

        # payload = {
        #   "batch_name": "batchName",
        #   "priority": 0,
        #   "comments": "string",
        #   "notifications":  notifications
        # }
    
        response = apiCall.post(self.token,url,fileContent, 60)
    
        return json2obj(response).response
    
    
    def importTasksUrl(self, projectId=None, fileUrl=None):
    
        try:
            if argumentVerifier([projectId, fileUrl, token]):
                raise InvalidArguments
        except InvalidArguments:
            logging.debug('invalid arguments')
            return json.dumps(argsList['importTasksUrl'])
    
        url = self.baseURL + urlConfig.URLS['Project'] + '/' + projectId + '/import/tasks/url'
    
        data = json.dumps({
            "fileUrl": fileUrl,
            "batch_name": "batch_name"
        })
    
        response = apiCall.post(self.token,url, data , 30)
        logging.debug(response)
        return response
    
    def create_batch(self,batchName='',projectId=None):

        url = self.baseURL + urlConfig.URLS['Project'] + '/' + projectId + '/batch'
        batch = {
            "batch_name": "string",
            "priority": 0,
            "comments": "string",
            "notifications": [
                {
                "notificationType": "Email",
                "metaData": {}
                }
            ]
        }
        data = json.dumps(batch)
        response = apiCall.post(self.token,url,data,30)
        logging.debug(response)
        return response






        
