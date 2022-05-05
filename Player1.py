import socket
import json 

request =  {
   "request": "subscribe",
   "port": 8888, #Ca c'est mon port à moi sur lequel je vais écouter des requêtes.
   "name": "Sisi",
   "matricules": ["20116"]
}


with socket.socket() as s : 
    s.connect(('localhost', 3000)) #Connect prends un tuple en paramètre
    request_server = json.dumps(request).encode() #Je transforme mon dictionnaire en Json et je l'encode en binaire.
    s.send(request_server)
    
    response = s.recv(2048).decode() #Je reçoit un objet Json
    msg = json.loads(response)
    print(msg)

    