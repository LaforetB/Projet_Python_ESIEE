# Importation des fichiers obligatoires

#from Class_Sudoku import *
#from pile_enregistrement import *
import Class_Sudoku as C_S
from random import randint, shuffle
import numpy as np
import pile_enregistrement as p_l
# Fin des importations fichiers et modules


# Initialisation

print("Le jeu va se lancer, merci de votre patience")
sudok_resolut= C_S.Sudoku(9,9)

# Fonction trouvable sur Internet (essai ensuite pour refaire une fonction similaire mais sans plagier, nous avons eu beaucoup de problème ainsi pour être sur que ça marche nous avons mis celle-ci dans le programme)
# Fonction pour résoudre et générer le sudoku qui devait être intégrer au fichier class mais suite à de nombreux problèmes j'ai du la mettre ici
# Les commentaires de cette fonction sont dans le fichier Class Sudoku
# Ce que l'on a besoin pour la fonction suivante
# La grille sous forme de liste
grille = [[0 for j in range(9)] for i in range(9)]
# La liste des chiffres possibles
numberList=[1,2,3,4,5,6,7,8,9]
def checkGrid(grid):
    for row in range(0,9):  #i=row
        for col in range(0,9):  #j=col
            if grid[row][col]==0:
                return False  
    return True 
# Fin  Fonction préliminaire
# Début de la fonction

def fill_su_Grid(grid):
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            shuffle(numberList)      
            for value in numberList:
                if not(value in grid[row]):
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col]=value
                            if checkGrid(grid):
                                return True
                            else:
                                if fill_su_Grid(grid):
                                    return True
            break
    grid[row][col]=0            
fill_su_Grid(grille)
# Fin de la fonction

sudok_resolut.grille=np.copy(np.array(grille))      # On affecte la nouvelle grille à sudok_resolut

# Grille générer

sudok_joueur= C_S.Sudoku(9,9)
sudok_non_modif= C_S.Sudoku(9,9)
choix_coup='None'
choix_partie='None'
liste_lettre=['A','B','C','D','E','F','G','H','I']
liste_chiffre=['1','2','3','4','5','6','7','8','9']
score=2000
var=0
pile_score=[]
pile_sudok=[]
print("Bonne chance et amusez-vous")

# Fin initialisation


# Début du programme principal du jeu
while (choix_partie=='None'):

    sudok_joueur.copy_sudoku_in_grille(sudok_resolut)
    # Choix du joueur entre commencer une partie ou reprendre une déjà enregistrer
    print('Choisir entre commencer une partie ou une partie enregistrer: commencer ou enregistrer')
    choix_partie=input()
    if choix_partie=='commencer':
        # Choix de la difficulté + enlever les cases pour commmencer a jouer
        choix='None'
        while choix=='None':        # Boucle qui permet le choix de la difficulté avec une demande continue si le joueur rentre des bêtises
            print('Choisir la difficulté du sudoku en écrivant: facile ou moyen ou hard ou extreme')
            choix=input()
            if choix=='facile':
                sudok_joueur.supr_number_case(14)
                break
            if choix=='moyen':
                sudok_joueur.supr_number_case(28)
                break
            if choix=='hard':
                sudok_joueur.supr_number_case(42)
                break
            if choix=='extreme':
                sudok_joueur.supr_number_case(56)
                break
            else :
                print("Veuillez suivre les indications s'il vous plaît")
                choix='None'
    elif choix_partie=='enregistrer':
        sudok_joueur=p_l.lire_sudoku('Enregistrement_sudoku.txt')       # Récupération du sudoku joueur
        score=p_l.lire_score("Enregistrement_score.txt")                # Récupération du score
        sudok_resolut=p_l.lire_sudoku("Enregistrement_solution.txt")    # Récupération de la solution
    elif choix_partie!='commencer' or choix_partie!='enregistrer' :
        print("Veuillez suivre les indications s'il vous plaît")
        choix_partie='None'
sudok_non_modif.copy_sudoku_in_grille(sudok_joueur)      # Création du sudoku non modifiable pour connaître les chiffres non modiafiables
pile_sudok.append(np.copy(sudok_joueur.grille))
pile_score.append(score)

# Boucle de jeu

while(sudok_joueur.check_grid()==False):
    grille_presentable=list(sudok_joueur.grille)
    # Création de la grille à afficher
    grille_presentable.insert(0,['#','A','B','C','D','E','F','G','H','I'])  # Insertion des lettres pour les coordonées
    for i in range(1,10):       # Boucle pour insérer les chiffres en coordonnées en colonne
        if i!=9:
            liste_change=grille_presentable[i]
            grille_presentable.pop(i)
            liste_change=np.insert(liste_change,0,i)
            grille_presentable.insert(i,list(liste_change))
        else:
            liste_change=grille_presentable[i]
            grille_presentable.pop(i) 
            liste_change=np.insert(liste_change,0,i)
            grille_presentable.insert(i,list(liste_change))
    print(np.array(grille_presentable))
    # Fin de création et l'affichage de la grille à afficher
    print("Que voulez-vous faire ?")
    print("Pour enregistrer la partie ecrivez: enregistrer ;Pour ajouter ou remplacer un chiffre dans la grille ecrivez: ajouter")
    print("Pour supprimer un chiffre: supprimer ; Pour auto-résoudre le sudoku ecrivez: auto; Pour avoir de l'aide en vous donnant un chiffre ecrivez: aide")
    print("Pour revenir en arrière ecrivez: retour")
    choix_coup=input()
    if choix_coup=="enregistrer" and choix_coup=="aide" and choix_coup=="ajouter" and choix_coup=="supprimer":  # Enregistrement de la grille pour revenir en arrière
        pile_sudok.append(np.copy(sudok_joueur.grille)) # Utilisation de np.copy() pour éviter de modifier ce que l'on vient d'enregistrer

    # Enregistrement de la partie

    if choix_coup=="enregistrer":   # Condition pour enregistrer la partie
        p_l.enregistre_score("Enregistrement_score.txt",score)              # Enregistrer le score du joueur
        p_l.enregistre_sudoku("Enregistrement_score.txt",sudok_joueur)      # Enregistrer la grille de sudoku du joueur
        p_l.enregistre_sudoku("Enregistrement_solution.txt",sudok_resolut)  # Enregistrer la solution de la partie
        break
    # Fin enregistrement

    # Ajouter ou remplacer un chiffre dans le sudoku

    elif choix_coup=="ajouter":                           # Condition pour ajouter ou remplacer un chiffre dans le sudoku
        print(np.array(grille_presentable))
        print("Rentrer la lettre correspondant à la colonne du chiffre")
        Lettre=input()                                  # Demande de la case à changer grâce au système de coordonnées
        print("Rentrer le chiffre correspondant à la ligne du chiffre")
        position=input()
        print(np.array(grille_presentable))
        print("Rentrer le chiffre souhaité")
        chiffre_voulue=input()                          # Demande du chiffre à insérer dans la case
        if Lettre in liste_lettre:                      # Test si Lettre contient bien l'information demandée
            if position in liste_chiffre:               # Test si position contient bien un chiffre entre 1 et 9
                if chiffre_voulue in liste_chiffre:     # Test si chiffre_voulue contient bien un chiffre entre 1 et 9
                    ip=0    #Initialisation pour trouver colonne et ligne
                    jl=0    #Initialisation pour trouver colonne et ligne
                    line_voulue=0   #Initialisation pour trouver colonne et ligne
                    colonne_voulue=0    #Initialisation pour trouver colonne et ligne
                    while line_voulue==0 and colonne_voulue==0 and ip<9 and jl<9: # Boucle pour trouver la colonne et la ligne voulue
                        if Lettre==liste_lettre[jl] and colonne_voulue==0:
                            colonne_voulue=jl
                        if position==liste_chiffre[ip] and line_voulue==0:
                            line_voulue=ip
                        ip+=1
                        jl+=1
                    if sudok_non_modif.grille[line_voulue][colonne_voulue]==0:          # Vérification si le chiffre est modifiable
                        sudok_joueur.replace(chiffre_voulue,line_voulue,colonne_voulue) # Modification du chiffre à l'endroit souhaité
                        if sudok_resolut.grille[line_voulue][colonne_voulue]==chiffre_voulue:
                            score-=5
                            p_l.pile_add(pile_score,score)                                  # Ajout du nouveau score modifié au retour en arrière
                        else:
                            score-=15
                            p_l.pile_add(pile_score,score)                                  # Ajout du nouveau score modifié au retour en arrière
                    else :
                        print("Choisir un chiffre modifiable")
                else:
                    print("Choisir un chiffre entre 1 et 9")    # Message d'erreur
            else:
                print("Choisir une coordonnée correcte pour la colonne (celle des chiffres)")   # Message d'erreur
        else:
            print("Respectez le système de coordonnées s'il vous plaît !")  # Message d'erreur
    # Fin coup ajouter

    # Supprimer un élément

    elif choix_coup=="supprimer":
        print(np.array(grille_presentable))
        print("Rentrer la lettre correspondant à la colonne du chiffre")
        Lettre=input()                                  # Demande de la case à changer grâce au système de coordonnées
        print("Rentrer le chiffre correspondant à la ligne du chiffre")
        position=input()
        if Lettre in liste_lettre:                      # Test si Lettre contient bien l'information demandée
            if position in liste_chiffre:               # Test si position contient bien un chiffre entre 1 et 9
                ip=0    #Initialisation pour trouver colonne et ligne
                jl=0    #Initialisation pour trouver colonne et ligne
                line_voulue=0   #Initialisation pour trouver colonne et ligne
                colonne_voulue=0    #Initialisation pour trouver colonne et ligne
                while line_voulue==0 and colonne_voulue==0 and ip<=9 and jl<=9: # Boucle pour trouver la colonne et la ligne voulue
                    if Lettre==liste_lettre[jl] and colonne_voulue==0:
                        colonne_voulue=jl
                    if position==liste_chiffre[ip] and line_voulue==0:
                        line_voulue=ip
                    ip+=1
                    jl+=1
                if sudok_non_modif.grille[line_voulue][colonne_voulue]==0: # Vérification si le chiffre est modifiable 
                    sudok_joueur.supr(line_voulue,colonne_voulue) # Suppression du chiffre à l'endroit souhaité
                    score-=10
                    p_l.pile_add(pile_score,score)  # Ajout du nouveau score modifié au retour en arrière
                else:
                    print("Choisir un chiffre modifiable") 
            else:
                print("Choisir une coordonnée correcte pour la colonne (celle des chiffres)")   # Message d'erreur
        else:
            print("Respectez le système de coordonnées s'il vous plaît !")  # Message d'erreur
    # Fin coup supprimer

    # Auto_résolution

    elif choix_coup=="auto":
        print("Voici la grille qu'il fallait trouver:")
        print(sudok_resolut.grille)     # Afficher la grille résolut
        score=0
        print("Voici votre score:", score)
        var=1
        break
    # Fin coup auto_résolution

    # Aide

    elif choix_coup=="aide":
        print("Nous allons vous aider !")
        score-=50
        p_l.pile_add(pile_score,score)  # Ajout du nouveau score modifié au retour en arrière
        sudok_joueur.random_completer(sudok_resolut)
    # Fin de l'aide

    # Retour en arriere

    elif choix_coup=="retour":
        if  len(pile_sudok)>1:    # Test si les piles ne sont pas vides
            sudok_joueur.grille=pile_sudok[-1]
            pile_sudok[-1]=2   # Supprime le dernier élément car pop ne fonctionne pas sur les éléments de Sudoku
            pile_sudok.pop()
            score=p_l.pile_sub_return_element(pile_score)-50
        elif len(pile_sudok)==1:        # Test si les piles ont une taille égales à 1
            sudok_joueur.grille=pile_sudok[-1]
            score=pile_score[-1]
            print("Vous ne pouvez pas revenir plus en arrière")
        else:
            print("Vous ne pouvez pas revenir en arrière")
    # Fin du retour en arrière

    else: 
        print("Choisir une action avec la bonne écriture")
# Fin de la boucle de jeu

# Programme de fin

if var==0:      # Si on est pas passé par l'auto-résolution alors
    Test=True   # La grille joueur est-elle conforme avec la grille résolut ?
    for i in range(0,9):
        for j in range(0,9):
            if sudok_joueur.grille[i][j]!=sudok_resolut.grille[i][j]:
                Test=False  # Non conforme
                break
    if Test==True :
        print("Voici la solution que vous avez trouvée:", sudok_resolut.grille)
        print("Voici votre score et bonne chance pour la prochaine fois:", score)
    if Test==False:
        score=0
        print("Votre grille n'était pas juste, voici la solution:", sudok_resolut.grille)
        print("Voici votre score et courage vous y arriverez la prochaine fois:", score)
# Message de fin
print("Merci d'avoir jouer à notre jeu")

# Fin du programme de fin


# Fin du jeu 
