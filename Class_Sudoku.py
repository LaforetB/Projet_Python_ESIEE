import numpy as np                      # module numpy pour les tableaux
from random import randint, shuffle     # Shuffle permet de mettre dans l'odre les entiers d'une liste, randint pour générer des entiers

class Sudoku:

    def __init__(self,line,colunm):
        """Create a vacum sudoku """
        self.line=line
        self.colunm=colunm
        self.grille=np.zeros((line,colunm),dtype=int)
    
    def copy_sudoku_in_grille(self,sudok_import):
        """Créer une copie du sudoku """
        for i in range(sudok_import.line):              # Parcours les lignes du sudoku
            for j in range(sudok_import.colunm):        # Parcours les colonnes du sudoku
                self.grille[i][j]=sudok_import.grille[i][j]    # Enregistre chaque élément dans self de sudok_import
    
    def chiffre_in_line(self,chiffre,number_line):
        """Test si le chiffre est déjà dans la ligne du sudoku """
        test=False                                          # Initialise le test à False
        for j in range(self.colunm):                        # Parcours la ligne
            if self.grille[number_line][j]==chiffre:        # Si le chiffre est dans la ligne alors
                test=True                                   # test passe à vrai
                break
        return(test)                                        # Retourne le test 
     
    def chiffre_in_colunm(self,chiffre,number_colunm):
        """Test si le chiffre est dèjà dans la colonne """
        test=False                                          # Initialise le test à False
        for i in range(self.line):                          # Parcours la colonne 
            if self.grille[i][number_colunm]==chiffre:      # Si le chiffre est dans la colonne alors
                test=True                                   # test passe à vrai
                break
        return(test)                                        # Retourne le test
    
    def chiffre_in_case(self,chiffre,number_colunm,number_line):
        """Test si le chiffre est dans la case """
        test=False                                          # Initialise le test à False
        i=number_line
        j=number_colunm
        iTop,jTop=3*(i//3), 3*(j//3)                        # Permet de connaître le i et j max du carré
        for k in range(iTop,iTop+3):                        # Parcours le carré suivant les lignes
            for l in range(jTop,jTop+3):                    # Parcours le carré suivant les lignes
                if self.grille[k][l]==chiffre:              # Si la grille contient le chiffre alors
                    test=True                               # test passe à vrai
                    break
        return(test)                                        # Retourne le test
    
    def liste_possibilities(self,number_line,number_colunm):
        """Donner la liste des chiffres possibles pour une place dans la grille donnée """
        liste_nb=[]                                                         # Création liste des possibilités
        test1=False                                                         # Valeur par défaut de test1
        test2=False                                                         # Valeur par défaut de test2
        for k in range(1,10):                                               # Parcours les valeurs possibles pour cette place
            test1=self.chiffre_in_line(k,number_line)                       # test1 regarde le chifffre suivant la ligne
            test2=self.chiffre_in_colunm(k,number_colunm)                   # test2 regarde le chifffre suivant la colonne
            if test1==False and test2==False:                               # Si test1 et test2 sont faux alors
                test1=self.chiffre_in_case(k,number_colunm,number_line)     # test1 regarde les carrés correspondant
                if test1==False:                                            # Si test1 est faux alors
                    liste_nb.append(k)                                      # la liste des possibilités prend le chiffre k
        return(liste_nb)                                                    # Retourne la liste des possibilités

    def replace(self,chiffre,number_line,number_colunm):
        """Remplacer un chiffre dans une case du sudoku """
        self.grille[number_line][number_colunm]=chiffre
    
    def supr(self,number_line,number_colunm):
        """Supprimer un chiffre dans une case du sudoku"""
        self.grille[number_line][number_colunm]=0
    
    def supr_number_case(self,number):
        """Supprimer les cases sans bloquer le jeu"""
        n=0
        while n<number:
            ir=randint(0,8)
            jr=randint(0,8)
            if self.grille[ir][jr]!=0:
                self.grille[ir][jr]=0
                n+=1
    
    def random_completer(self,sudoku_autre):
        "Remplie une case non remplie de manière aléatoire"
        var=False
        while var==False :
            i=randint(0,8)
            j=randint(0,8)
            if self.grille[i][j]==0:
                self.grille[i][j]=sudoku_autre.grille[i][j]
                print(self.grille[i][j],"ligne:",i+1,"colonne:",j+1)
                var=True

    def add_case(self,number,sudok):
        """Rajouter les cases si le sudoku étaient déjà rempli en difficultées"""
        n=0                                                 # Initialisation de n
        while n<number:                                     # Tant que n<number=nb de case à rajouter
            ir=randint(0,8)                                # i random
            jr=randint(0,8)                                # j random
            if self.grille[ir][jr]==0:                      # si la case est vide alors
                n+=1                                        # n=n+1
                self.grille[ir][jr]=sudok.grille[ir][jr]    # la grille self prend la valeur de la grille pleine et résolue sudok
            if self.check_grid()==True:
                n=number

    def appear_case_none(self,sudoku,line,colunm,sudoku_resolve):
        list_case_none=[ [(i,j) for j in colunm if sudoku[i][j]==None] for i in line]
        index_random=randint(0,len(list_case_none))
        (i_case,j_case)=list_case_none[index_random]
        sudoku[i_case][j_case]=sudoku_resolve[i_case][j_case]


    def check_grid(self):
        """Regarder si la grille est pleine """
        for i in range(self.line):          # On parcours les lignes
            for j in range(self.colunm):    # On parcours les colonnes
                if (self.grille[i][j]==0):  # On regarde si il y a un 0 dans la case
                    test=False
                    return test
        return True

"""Après de multiple tentative il y a un problème qui est non résolu (je laisse le programme ici, avec les commentaires et une version ou j'ai essayé d'intégrer les méthodes)
n'ayant pas eu plus de temps pour m'occuper de ce problème, nous avons réalisé le sudoku autrement.
    def solver_and_generator(self):
        #Résoudre et générer un sudoku
        # la fonction regarde la suite du programme pour savoir si la valeur ne bloquera pas le sudoku plus tard d'où le bactraking + récursivité de fullgrid
        numberList=[1,2,3,4,5,6,7,8,9]
        #shuffle(numberList)
        def fillGrid(self,grl):
            global counter                                                  # Décalaration d'une fonction globale
            for i in range((self.line*self.colunm)):                        # Parcours les 81 cases du sudoku (si ligne=9 et colonne=9)
                row=i//self.line                                            # Calcul pour avoir les ligne
                col=i%self.colunm                                           # Calcul pour avoir les colonnes
                if grl[row][col]==0:                                # Si dans la case, il y a 0 alors
                    shuffle(numberList)                                     # On remet les valeurs dans l'ordre dans numberlist
                    for value in numberList:                                # Pour les valeurs de numberlist
                        if not(value in grl[row]):        # Si tu respectes la condition sur les lignes
                            if not value in (grl[0][col],grl[1][col],grl[2][col],grl[3][col],grl[4][col],grl[5][col],grl[6][col],grl[7][col],grl[8][col]):  # Si tu respectes la condition sur les colonnes
                                square=[]
                                if row<3:                                    # Condition pour remplir square suivant le carré 3x3 concerné
                                    if col<3:
                                        square=[grl[i][0:3] for i in range(0,3)]     # comprehension liste in ordre to create square 3x3 correspondant
                                    elif col<6:
                                        square=[grl[i][3:6] for i in range(0,3)]
                                    else:  
                                        square=[grl[i][6:9] for i in range(0,3)]
                                elif row<6:
                                    if col<3:
                                        square=[grl[i][0:3] for i in range(3,6)]
                                    elif col<6:
                                        square=[grl[i][3:6] for i in range(3,6)]
                                    else:  
                                        square=[grl[i][6:9] for i in range(3,6)]
                                else:
                                    if col<3:
                                        square=[grl[i][0:3] for i in range(6,9)]
                                    elif col<6:
                                        square=[grl[i][3:6] for i in range(6,9)]
                                    else:  
                                        square=[grl[i][6:9] for i in range(6,9)]
                                    #Check that this value has not already be used on this 3x3 square
                                if not value in (square[0] + square[1] + square[2]):     # Si value n'est pas dans le carré 3x3 alors
                                        grl[row][col]=value                      # Completer la grille avec la value car il respecte les règles du sudoku
                                        if checkGrid(grl):                              # La grille est-elle complète ?
                                            return True                   
                                        else:
                                            if fillGrid(self,grl):                          # Sinon on utilise la récursivité
                                                return True
                    break
            self.grille[row][col]=0          # Affecter un 0 à la case
                    
        def checkGrid(grle):
            for row in range(0,9):              #i=row, on parcours les lignes
                for col in range(0,9):          #j=col, on parcours les colonnes
                    if (grle[row][col]==0):      # Si la grille contient un zéro alors c'est faux, grille n'est pas pleine
                        return False

            #We have a complete grid!  
            return True
        
        grille = []
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        grille.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        fillGrid(self,grille)
        self.grille=np.copy(np.array(grille))
        # Fin de solve and generator
  
# Tentative de simplification avec des méthodes existantes 

    def solver_and_generator_2_0(self):
        "Résoudre et générer un sudoku"
        def fill_grid(self):
            for i in range((self.line*self.colunm)):        # Parcours les 81 cases du sudoku (si ligne=9 et colonne=9)
                    row=i//self.line                        # Calcul pour avoir les ligne
                    col=i%self.colunm                       # Calcul pour avoir les colonnes
                    if (self.grille[row][col]==0):
                        numberList=self.liste_possibilities(row,col) # Permet de connaître les nombres possibles en respectant les trois règles
                        for k in numberList:
                            self.grille[row][col]=k
                            if self.check_grid():
                                return True
                            else:
                                if fill_grid(self):
                                    return True
                    break
            self.grille[row][col]=0 

        fill_grid(self)
"""
