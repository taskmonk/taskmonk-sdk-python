import requests
import logging
import time

url = "https://httpbin.org/ip"

proxies = {
        "http":"89.23.194.174:8080",
        "https": "89.23.194.174:8080"
    }

''' To check the inital ip address'''
# initial_ip = requests.get(url)
# print("Initial ip = %s",initial_ip.json())

''' To handle the Connection Error for example Max Entries connection error. 
    While loop is to reconnect after handling the exception and then break '''
proxy_ip = ''
while proxy_ip == '':
    try:
        proxy_ip = requests.get(url, proxies = proxies)
        print("Proxy IP = ",proxy_ip.json())
        break
    except requests.exceptions.ConnectionError:
        print("Connection refused by the server..")
        print("Sleep for 10 seconds")
        time.sleep(10)
        print("Was a nice sleep, now let me continue...")
        continue

