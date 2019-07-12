class OAuthClientCredentials:
    clientId = ""
    clientSecret = ""
    
    def __init__(self,client_id,client_secret):
        self.clientId = client_id
        self.clientSecret = client_secret
    
    def get_client_id():
        return clientId
    
    def get_client_secret():
        return clientSecret
