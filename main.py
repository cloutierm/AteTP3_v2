#Cree par Maximilien Cloutier
#Cree en 2023
#Code du TP3

import random
import sys


vies = 20
victoires = 0
winstreak = 0
defaites = 0


#La fonction pour les regles du jeu et le contexte
def regles():
   print("\nBienvenue dans le donjon. Vous allez devoir combattre des monstres de differents niveaux pour affronter le boss du donjon. \n"
         "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. \n"
         "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. \n"
         "La partie se termine lorsque les points de vie de l’usager tombent sous 0. \n"
         "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie. \n"
         "\nVoici votre premier monstre")


#Tu es dans un donjon et tu combats des monstres, potentionellement un boss, et tu dois survivre le plus longtemps
def jeu():
   global vies
   global victoires
   global winstreak
   global defaites
   choix = 0
   #Code pour le combat du boss
   while vies > 0 and choix != 4:
       #Si le joueur a eu assez de victoires, il peut combattre le boss
       if victoires == 10 or winstreak == 5:
           print("\nVous avez battu assez de monstres. \n"
                 "Le boss a beaucoup plus de vies que les monstres normaux.\n"
                 "Il va falloir lui infliger 35 dégats pour le vaincre.\n"
                 "Vous avez 3 boucliers, 1 potion de vie et 1 épée que vous avez trouvé dans la salle.\n"
                 "Les boucliers vous permettent de bloquer 1 attaque du boss.\n"
                 "La potion de vie vous donne 3 ponits de vie. \n"
                 "L'épée vous donne 2 degats bonus\n")
           vies_boss = 35
           boucliers = 3
           potion_vie = 1
           #Le combat contre le boss continue tant que vous ou le boss n'êtes pas mort
           while vies_boss > 0 and vies > 0:

               force_boss = random.randint(1, 10)
               print("Le boss vous attaque avec une puissance de", force_boss)
               choix2 = input("Vieullez choisir une action:\n"
                              "1- Attaquer le boss\n"
                              "2- Bloquer l'attaque du boss\n"
                              "3- Utiliser la potion de vie\n")
               #Attauqer le boss
               if choix2 == "1":
                   print("Vous attaquer le boss")
                   attaque3 = random.randint(3, 8)
                   attaque4 = random.randint(3, 8)
                   attaque_totale2 = attaque3 + attaque4
                   print("Votre attaque a une puissance de", attaque3, "et", attaque4)
                   print("Votre attaque a une puissance totale de", attaque_totale2)
                   print("Le boss perd", attaque_totale2, "point(s) de vie")
                   vies_boss = vies_boss - attaque_totale2
                   print("Vies du boss:", vies_boss)
                   print("Le boss vous fait", force_boss, "degats")
                   vies = vies - force_boss
                   print("Vies:", vies)
               #Bloquer l'attauqe du boss
               elif choix2 == "2":

                   if boucliers <= 0:
                       print("Vous n'avez plus de bouclier.\n"
                             "Vous bloquer rien.\n"
                             "Le boss vous attque.\n")
                       print("Le boss vous fait", force_boss, "degats")
                       vies = vies - force_boss
                       print("Vies:", vies)
                   else:
                       boucliers -= 1
                       print("Vous utiliser un bouclier.\n"
                             "Il vous reste", boucliers, "bouclier(s)")
               #Utiliser la potion de vie
               elif choix2 == "3":

                   if potion_vie <= 0:
                       print("Vous buvez une potion vide.\n"
                             "Rien ne se passe.\n"
                             "Le boss vous attque.\n")
                       print("Le boss vous fait", force_boss, "degats")
                       vies = vies - force_boss
                       print("Vies:", vies)

                   else:
                       print("Vous utiliser une potion de vie")
                       vies = vies +5
                       potion_vie = 0
                       print("Vies:", vies)
               #Le joueur ne fait rien ou le choix est mauvais
               else:
                   print("Vous ne faites rien.\n"
                         "le boss vous attque.\n")
                   print("Le boss vous fait", force_boss, "degats")
                   vies = vies - force_boss
                   print("Vies:", vies)

           if vies_boss <= 0:
               print("Bravo!!!!! Vous avez battu le boss"
                     "")
               victoires = 0
               winstreak = 0

       force_ennemis = random.randint(1, 10)
       print("\nLe montre a une puissance de", force_ennemis)
       choix = input("Que voulez-vous faire? \n"
                     "1. Combattre cet adversaire \n"
                     "2. Contourner cet adversaire et aller ouvrir une autre porte \n"
                     "3. Afficher les règles du jeu \n"
                     "4. Quitter la partie \n")

       if choix == "1":
           attaque = random.randint(1, 6)
           attaque2 = random.randint(1, 6)
           attaque_totale = attaque + attaque2
           print("Votre attaque a une puissance de", attaque, "et", attaque2)
           print("Votre attaque a une puissance totale de", attaque_totale)
           print("Le montre a une puissance de", force_ennemis)

           if attaque_totale > force_ennemis:
               victoires += 1
               winstreak += 1
               vies = vies + force_ennemis
               print("Vous avez battu le montre, vous avez ganger", force_ennemis, "point(s) de vie")
               print("Vies:", vies)
               print("Victoires:", victoires)
               print("Winstreak:", winstreak)
               print("Défaites:", defaites)

           elif attaque_totale <= force_ennemis:
               vies = vies - force_ennemis
               defaites += 1
               winstreak = 0
               print("Votre attaque est trop faible, vous perdez", force_ennemis, "point(s) de vie")
               defaites = +1
               winstreak = 0
               print("Votre attaque est trop faible, vous perdez", force_ennemis, "points de vie")
               print("Vies:", vies)
               print("Victoires:", victoires)
               print("Winstreak:", winstreak)
               print("Défaites:", defaites)

       elif choix == "2":
           print("Vous échaper le monstre, vous perdez 1 point de vie \n"
                 "Il vous reste", vies, "points de vie")
           vies = vies -1
           print("Vous trouvez un autre monstre")

       elif choix == "3":
           print(regles())

       elif choix == "4":
           print("Vous avez quitté le jeu")
           sys.exit()

       else:
           print("Votre choix n'est pas bon, vieullez ressayer \n")


regles()
jeu()

