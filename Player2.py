import socket
import json 

request =  {
   "request": "subscribe",
   "port": 9999, 
   "name": "Xerox",
   "matricules": ["20212"]
}


with socket.socket() as s : 
    s.connect(('localhost', 3000)) 
    request_server = json.dumps(request).encode() 
    s.send(request_server)
    
    response = s.recv(2048).decode() 
    msg = json.loads(response)
    print(msg)
