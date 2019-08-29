import requests
from urllib.parse import urlparse

def url_convert(url):
    
    if not urlparse(url).scheme:
        url = "http://"+url
    print(url)
    print(urlparse(url))

url_convert("preprod.taskmonk.io")

#print(urlparse("preprod.taskmonk.io"))