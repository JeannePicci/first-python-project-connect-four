# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:53:31 2023

@author: 33782
"""



import tkinter         # import de tkinter

# je fais une liste plateau
 
plateau = [['L', 'L', 'L', 'L', 'L', 'L', 'L'],
           ['L', 'L', 'L', 'L', 'L', 'L', 'L'],
           ['L', 'L', 'L', 'L', 'L', 'L', 'L'],
           ['L', 'L', 'L', 'L', 'L', 'L', 'L'],
           ['L', 'L', 'L', 'L', 'L', 'L', 'L'],
           ['L', 'L', 'L', 'L', 'L', 'L', 'L']]


# définition des joueurs
joueurs = ["red", "yellow"]

# fonction pour afficher le plateau de jeu
def fIniPlat():
    for ligne in plateau: #je parcours chaque grande liste (les six) et je met une barre par liste
        print('|', end=' ')
        for colonne in ligne: #je parcours mes petites listes (à l'interieur des  grandes) et à chaque élément 
            print("-", end=' | ')# je met un espace puis une barre
        print()
#en gros mes 6 premières barres en colonnes c'est la première boucle et je la multiplie 7 fois
#print(fIniPlat()) #voir la matrice avec les tuples vides dedans


# objectif: placer un jeton dans une colonne du plateau
def fPlacer_jeton(colonne, jeton):
    global reussi,couleurs
    for ligne in range(5, -1, -1): # commencer à partir de la dernière rangée puis on remonte les lignes du plateau (5,4,3,2,1,0)
        if plateau[ligne][colonne] == 'L' and not victoire(jeton) : # si la case est vide
            plateau[ligne][colonne] = jeton
            ca.create_oval(2+colonne*100,2+ligne*100,colonne*100+98,98+ligne*100, fill = jeton, width = 2)
            reussi = True              
            return reussi  

        
    reussi = False
    return "Tu ne peux pas mettre ton jeton là c'est pleins !"

#print(Placer_jeton(3,"rouge"))

# fonction pour vérifier si le joueur a gagné lorsqu'il  place un jeton dans une certaine position
def victoire(jeton):
    # 1 : 4 jetons sont alignés horizontalement
    for ligne in range(6):
        for colonne in range(4):
            if (plateau[ligne][colonne] == jeton  
                and plateau[ligne][colonne+1] == jeton 
                and plateau[ligne][colonne+2] == jeton 
                and plateau[ligne][colonne+3] == jeton):
                zone_texte = tkinter.Label (text = "PUISSANCE QUATRE HORIZONTAL !",font=("broadway",23), fg="black")
                zone_texte.pack()
                zone_texte.place(x=350,y=650)
                return True
                

    # 2: 4 jetons sont alignés verticalement
    for ligne in range(3):
        for colonne in range(7):
            if (plateau[ligne][colonne] == jeton 
            and plateau[ligne+1][colonne] == jeton 
            and plateau[ligne+2][colonne] == jeton 
            and plateau[ligne+3][colonne] == jeton):
                zone_texte = tkinter.Label (text = "PUISSANCE QUATRE VERTICAL !",font=("broadway",23), fg="black")
                zone_texte.pack()
                zone_texte.place(x=350,y=650)
                return True

    # 3: 4 jetons sont alignés en diagonal
    for ligne in range(3):
       for colonne in range(4):
           #vérifie toute les diagonales de la partie supérieure droite par rapport à la grande diagonale du plateau
           if plateau[ligne][colonne] == jeton and plateau[ligne+1][colonne+1] == jeton and plateau[ligne+2][colonne+2] == jeton and plateau[ligne+3][colonne+3] == jeton:
               zone_texte = tkinter.Label (text = "PUISSANCE QUATRE DIAGONAL !",font=("broadway",23), fg="black")
               zone_texte.pack()
               zone_texte.place(x=350,y=650)
               return True
           #vérifie toutes les diagonales de la partie inférieur gauche par rapport à la grande diagonale du plateau
           if plateau[ligne+3][colonne] == jeton and plateau[ligne+2][colonne+1] == jeton and plateau[ligne+1][colonne+2] == jeton and plateau[ligne][colonne+3] == jeton:
               zone_texte = tkinter.Label (text = "PUISSANCE QUATRE DIAGONAL !",font=("broadway",23), fg="black")
               zone_texte.pack()
               zone_texte.place(x=350,y=650)
               return True   
            
    # 3 : 4 jetons sont alignés diagonalement*


# programme PRINCIPAL pour jouer une partie complète de Puissance quatre
tour=0
partie_terminee = False # j'initiale ce qui va me permettre de terminer la partie
    
###########################################################################################

root = tkinter.Tk ()
root.configure(bg='gray') 
   # création de la fenêtre principale
ca = tkinter.Canvas ()#création d'un caneva 
root.attributes('-fullscreen',True)

#dimensions du canevas:
# width <--> largeur en pixels
# height <--> hauteur en pixels
ca.config (width = 700 , height = 600,bg = "black")
ca.pack()
#création du cadrillage:
for i in range (6):
    ca.create_line (0,i*100,700,i*100, fill = "white", width = 2) #les lignes
for j in range(7):
    ca.create_line (j*100,0,j*100,600, fill = "white", width = 2) #les colonnes

def Transformateur (event):#fonction qui va permettre d'assigner à un clique un choix de colonne
    global tour
    coordX=event.x
    if coordX >= 700:
        coordX = 600
    coordX=str(coordX+100)
    coordX=coordX[0]
    coordX=int(coordX)-1
    print (coordX)
    joueur = joueurs[tour % 2] #permet d'alterner les joueurs
    H=fPlacer_jeton(coordX, joueur)
    print(H)
    if victoire(joueur):
        print("Le joueur " + str(joueur)+" a gagné !")
    else:
        tour=tour+1
    print(plateau)


ca.bind("<Button-1>", Transformateur)

# bouton pour quitter le jeu
bouton_quitter = tkinter.Button(
    root,
    text="X Quitter",
    command=root.destroy,
    font=("Arial", 12),
    bg="red",
    fg="white"
)

bouton_quitter.pack()
bouton_quitter.place(x=720, y=10)

root.mainloop ()  # on affiche enfin la fenêtre principale
