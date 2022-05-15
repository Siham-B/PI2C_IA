# Lancement de L'IA :

Afin de lancer l'IA, vous devez prendre les fichiers game.py ainsi que IA1player.py. Une fois cette étape faite on lance le jeu avec la commande python server.py othello. Attention à bien se trouver dans le bon répertoire du serveur de jeu !
L'interface graphique de monsieur Lurkin s'affichera. 
Dans un nouveau terminal, on écrira la commande python IA1player.py. Le jeu peut maintenant commencer.


# Principe de la stratégie de l'IA :

Nous avons créé une IA capable de choisir la cellule qui peut éliminer le maximum de pions adverse. Notre stratégie repose sur 2 grands principes le kick et le save.
Grâce au possibleMove, on choisit :

- Soit de bloquer l'adversaire pour minimiser nos pertes de pions.
- Soit de tuer le maxium de pions adverse.

Le kick : pour chaque cellule où il est possible de placer un de nos pions afin d'éliminer ceux de l'adversaire ;

- Nous calculons dans les 8 directions (vers haut/bas, vers gauche/droite, sur les 2 diagonales vers le haut/bas) le nombre de pions éliminables.
- Ensuite nous prenons la cellule qui élimine le plus de pions adverse.

Le save : pour chaque cellule où il est possible de placer un de nos pions afin de bloquer l'adversaire et de sauvegarder nos pions ;

- Nous calculons dans les 8 directions (vers haut/bas, vers gauche/droite, sur les 2 diagonales vers le haut/bas) le nombre de pions sauvegardable.
- Ensuite nous prenons la cellule qui sauvegarde le plus de nos pions.

Pour finir nous comparons le nombre de pions éliminable et le nombre de pions sauvegardable du save et du kick, en fonction de ses nombres on prendra la cellule la plus optimale (qui sauvegarde ou tue le plus de pions).

# Les bibliothèques utilisés :

Nous avons utilisé le module socket afin de pouvoir établir une communication avec le serveur. 
Le module json a été importé afin de pouvoir transformer nos requêtes en objet JSON. 

__Cette I.A a été réalisé par : Boutouil Nasreddine 20212 et Boutouil Siham 20116__
