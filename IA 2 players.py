import socket
import json 
import threading
import random
import game
from PI2CChampionshipRunner.games.othello.game import Game
from strategy import bestChoice


# Requête d'inscription de chacun des joueurs
request_player1 =  {"request": "subscribe","port": 8888, "name": "Sisi","matricules": ["20116"]}
request_player2 =  {"request": "subscribe","port": 9999, "name": "Xerox","matricules": ["20212"]}

# Fonction permettant de faire inscrire n'importe quel joueur.
def Registration(request_player) : 
    with socket.socket() as s :
        s.connect(('localhost', 3000)) 
        request_server = json.dumps(request_player).encode() 
        s.send(request_server)
        # Réception objet JSON
        response = s.recv(2048).decode()
        # Transformation objet JSON en dictionnaire python
        msg = json.loads(response)
        print(msg)
        if  msg == {"response": "ok"}: 
            return True 
        else:
            return False

# Fonction permettant de communiquer avec le serveur.
def Chat(player) : 
    with socket.socket() as s :
        s.bind(('0.0.0.0', player['port'])) 
        s.listen()
        while True : 
            host, adress = s.accept()
            msg = (json.loads(host.recv(2048).decode()))
            print(msg)
            if msg == {"request" : "ping"} : 
                rep = {"response" : "pong"} 
                host.send(json.dumps(rep).encode())
            if msg != {"request" : "ping"} :
                if player["name"] == "Sisi":
                    caracteristics = msg['state']
                    indexEnnemies = caracteristics['players'].index("Xerox")
                    myIndex = caracteristics["players"].index(player["name"])
                    ennemiesCellules = caracteristics['board'][indexEnnemies]
                    possibleCellules = game.possibleMoves(caracteristics)
                    myCellules = caracteristics['board'][myIndex]
                    print('Cellule possible à jouer : ',game.possibleMoves(caracteristics))
                    if possibleCellules != []:
                        print("C'est possible de jouer !")
                        choice = bestChoice(possibleCellules,ennemiesCellules,myCellules)
                        round = json.dumps({"response": "move","move": choice,"message": "Voilà bg"}).encode()
                        host.send(round)
                    else:
                        print("C'est impossible de jouer !")
                        round = json.dumps({"response": "move","move": None,"message": "Voilà bg"}).encode()
                        host.send(round)

                elif player["name"] == "Xerox":
                    caracteristics = msg['state']
                    possibleCellules = game.possibleMoves(caracteristics)
                    print('Depuis le Terminal',game.possibleMoves(caracteristics))
                    if possibleCellules != []:
                        print("C'est possible de jouer !")
                        round = json.dumps({"response": "move","move": random.choice(possibleCellules),"message": "Voilà bg"}).encode()
                        host.send(round)
                    else:
                        print("C'est impossible de jouer")
                        round = json.dumps({"response": "move","move": None,"message": "Voilà bg"}).encode()
                        host.send(round)


def Start_Game():
    # Quand c'est True alors là je peux communiquer avec le serveur
    if Registration(request_player1) == True:
        Chat(request_player1)

# Je fais chatter et inscrire mes players de façon asynchrone
thread = threading.Thread(target = Start_Game, daemon = True)
thread.start() 

while True :
    if Registration(request_player2) == True:
        Chat(request_player2)

