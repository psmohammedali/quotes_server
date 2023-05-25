import socket
import requests
import quotes_title
import random
import json
import conf

server_obj = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5556
server_obj.bind((host,port))
server_obj.listen()
conn_obj, _ = server_obj.accept()
if conn_obj:
    conn_obj.send(b'b')
    request_data = conn_obj.recv(1024)
    while request_data:
        category = random.choice(quotes_title.title_list)
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': conf.key})
        response = json.loads(response.text)
        quotes = response[0]["quote"].encode('utf-8')
        
        conn_obj.send(quotes)
        if request_data == b'stop':
            conn_obj.close()
            break
        request_data = conn_obj.recv(1024)

