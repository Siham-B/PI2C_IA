import socket
import json 
import threading
import random
import game
from PI2CChampionshipRunner.games.othello.game import Game


# Requête d'inscription de chacun des joueurs
request_player1 =  {"request": "subscribe","port": 8888, "name": "Sisi","matricules": ["20116"]}
request_player2 =  {"request": "subscribe","port": 9999, "name": "Xerox","matricules": ["20212"]}

# Fonction permettant de faire inscrire n'importe quel joueur.
def Registration(request_player) : 
    with socket.socket() as s :
        s.connect(('localhost', 3000)) 
        request_server = json.dumps(request_player).encode() 
        s.send(request_server)
        response = s.recv(2048).decode() #Je reçoit un objet Json 
        msg = json.loads(response) #Je veux le lire donc je le transforme en dico
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

                elif player["name"] == "Xerox":
                    caracteristics = msg['state']
                    indexEnnemies = caracteristics["players"].index("Sisi")
                    myIndex = caracteristics["players"].index(player["name"])
                    ennemiesCellules = caracteristics['board'][indexEnnemies]
                    possibleCellules = game.possibleMoves(caracteristics)
                    myCellules = caracteristics['board'][myIndex]

                print('Depuis le Terminal',game.possibleMoves(caracteristics))
                if possibleCellules != []:
                    print("Possible")
                    kick = checkCellule(possibleCellules,ennemiesCellules,myCellules)
                    round = json.dumps({"response": "move","move": kick,"message": "Voilà bg"}).encode()
                    host.send(round)
                else:
                    round = json.dumps({"response": "move","move": None,"message": "Voilà bg"}).encode()
                    host.send(round)


# Fonction permettant de chosir la meilleure cellule
def checkCellule(possibleCellule,ennemiesCellules,myCellules):
    bord1 = [7,15,23,31,39,47,55,63]
    bord2 = [0,8,16,24,32,40,48,56]
    total = 0
    possibilities = 1
    arr = []
    for i in possibleCellule :
        a = 0 
        b = 0
        c = 0 
        d = 0 
        e = 0 
        f = 0 
        g = 0 
        h = 0
        possibilities = 1
        total = 0
        while possibilities <= 8 :
            # +1
            if possibilities == 1:
                for n in range(len(ennemiesCellules)+1):
                    cellule = i + n + 1
                    print("1 ère : " , cellule)
                    if cellule in bord2:
                        a = 0
                        break
                    elif cellule in ennemiesCellules:
                        a += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            a = 0
                            break
                # On passe à la deuxième possibilités
                print("Le a : " ,a)
                possibilities += 1
                total = total + a
            # -1
            elif possibilities == 2:
                for n in range(len(ennemiesCellules)+1):
                    cellule = i - n - 1
                    if cellule in bord1:
                        b = 0
                        break
                    elif cellule in ennemiesCellules:
                        b += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            b = 0
                            break                 
                # On passe à la troisième possibilités
                print("Le b : " ,b)
                possibilities += 1
                total = total + b
            # +8
            elif possibilities == 3:
                for n in range(1,len(ennemiesCellules)+1):
                    cellule = i + n * 8
                    print("Cellule" , cellule)
                    if cellule in ennemiesCellules:
                        c += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            c = 0
                            break                 
                # On passe à la quatrième possibilités
                print("Le c : " ,c)
                possibilities += 1
                total = total + c

                
            # -8
            elif possibilities == 4:
                for n in range(1,len(ennemiesCellules)+1):
                    cellule = i + n * -8
                    if cellule in ennemiesCellules:
                        d += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            d = 0
                            break                 
                # On passe à la cinquième possibilités
                print("Le d : " ,d)
                possibilities += 1
                total = total + d

            # +9
            elif possibilities == 5:
                for n in range(1,len(ennemiesCellules)+1):
                    cellule = i + n * 9
                    if cellule in ennemiesCellules:
                        e += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            e = 0
                            break                 
                # On passe à la sixième possibilités
                print("Le e : " ,e)
                possibilities += 1
                total = total + e
            # -9
            elif possibilities == 6:
                for n in range(1,len(ennemiesCellules)+1):
                    cellule = i + n * -9
                    if cellule in ennemiesCellules:
                        f += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            f = 0
                            break                 
                # On passe à la septième possibilités
                print("Le f : " ,f)
                possibilities += 1
                total = total + f

            # +7
            elif possibilities == 7:
                for n in range(1,len(ennemiesCellules)+1):
                    cellule = i + n * 7
                    if cellule in ennemiesCellules:
                        g += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            g = 0
                            break                 
                # On passe à la huitième possibilités
                print("Le g : " ,g)
                possibilities += 1
                total = total + g

            # -7
            elif possibilities == 8:
                for n in range(1,len(ennemiesCellules)+1):
                    cellule = i + n * -7
                    if cellule in ennemiesCellules:
                        h += 1
                    else:
                        if cellule in myCellules:
                            break
                        else:
                            h = 0
                            break                
                # On passe à la huitième possibilités
                print("Le h : " ,h)
                possibilities += 1
                total = total + h

            if possibilities == 9:
                print("Le max: ", total, " Pour la cellule", i)
                arr.append(total)
    

    print('Voila le tableau:',arr," Et voilà le max : ", max(arr))
    choice = possibleCellule[arr.index(max(arr))]
    print("La meilleure cellule est : ", choice)
    return choice


def Start_Game():
    if Registration(request_player1) == True: # Quand c'est True alors là je peux communiquer avec le serveur
        Chat(request_player1)

# Je fais chatter et inscrire mes players de façon asynchrone
thread = threading.Thread(target = Start_Game, daemon = True)
thread.start() 

while True :
    if Registration(request_player2) == True:
        Chat(request_player2)

