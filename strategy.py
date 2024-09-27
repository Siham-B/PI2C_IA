# Fonction permettant de répertorier le nombre de pions tué par cellule et de choisir le plus grand nombre
def kickPions(possibleCellule,ennemiesCellules,myCellules):
    bord1 = [7,15,23,31,39,47,55,63]
    bord2 = [0,8,16,24,32,40,48,56]
    total = 0
    possibilities = 1
    kickTab = []
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
                kickTab.append(total)
    

    print('Voila le tableau de kick:',kickTab," et voilà le max kick : ", max(kickTab))
    choice = possibleCellule[kickTab.index(max(kickTab))]
    print("La meilleure cellule pour tuer est : ", choice)
    return choice, max(kickTab)

# Fonction permettant de répertorier le nombre de pions sauvegardé par cellule et de choisir le plus grand nombre
def savePions(possibleCellule,ennemiesCellules,myCellules):
    bord1 = [7,15,23,31,39,47,55,63]
    bord2 = [0,8,16,24,32,40,48,56]
    total = 0
    possibilities = 1
    saveTab = []
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
                    if cellule in bord2:
                        a = 0
                        break
                    elif cellule in myCellules:
                        a += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    elif cellule in myCellules:
                        b += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    if cellule in myCellules:
                        c += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    if cellule in myCellules:
                        d += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    if cellule in myCellules:
                        e += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    if cellule in myCellules:
                        f += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    if cellule in myCellules:
                        g += 1
                    else:
                        if cellule in ennemiesCellules:
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
                    if cellule in myCellules:
                        h += 1
                    else:
                        if cellule in ennemiesCellules:
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
                saveTab.append(total)
    

    print('Voila le tableau:',saveTab," Et voilà le max sauvegarder : ", max(saveTab))
    choice = possibleCellule[saveTab.index(max(saveTab))]
    print("La meilleure cellule est : ", choice)
    return choice,max(saveTab)


# Fonction permettant de choisir la meilleure cellule entre les fonctions savePions et kickPions
def bestChoice(possibleCellules,ennemiesCellules,myCellules):
    celluleKick,maxKick = kickPions(possibleCellules,ennemiesCellules,myCellules)
    celluleSave,maxSave = savePions(possibleCellules,ennemiesCellules,myCellules)
    
    if maxKick > maxSave:
        print("On choisit de kick")
        return celluleKick
    elif maxSave > maxKick:
        print("On choisit de save")
        return celluleSave
    else:
        print("Egalité, on choisit de kick")
        return celluleKick

