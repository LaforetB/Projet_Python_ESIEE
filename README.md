# Projet_Python_ESIEE

###### Bonjour, 
###### Nous vous rendons le projet concernant le Sudoku.
###### Après avoir récupéré l'ensemble des fichiers:
###### Les trois fichiers textes permettent la sauvegarde des parties, ils sont donc indispensables.
###### Pour faire fonctionner le jeu vous avez besoin des 3 fichiers textes, Class_Sudoku, pile_enregistrement, Prog_principale dans un même répertoire.
###### Puis dans visual studio code, vous allez lancer le Prog_principale.py pour pouvoir jouer directement dans le terminal.

##### Attention petit message:

###### Le but du programme étant de seulement résoudre ce qui possible avec les différentes méthodes et programmes d'essai, nous avons tout de même essayer de générer la grille avec notre algorithme. 
###### Notre algorithme possédant une erreur dans la génération de la grille, il ne vérifiait pas l'une des trois conditions. Puisque le but était de résoudre la grille et non de la générer nous avons emprûnter une partie de code générant cette grille à la littérature.
###### if grid[row][col]==0:
######            shuffle(numberList)      
######            for value in numberList:
######                if not(value in grid[row]):
######                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
######                        square=[]
######                        if row<3:
######                           if col<3:
######                               square=[grid[i][0:3] for i in range(0,3)]
######                            elif col<6:
######                                square=[grid[i][3:6] for i in range(0,3)]
######                            else:  
######                                square=[grid[i][6:9] for i in range(0,3)]
######                        elif row<6:
######                            if col<3:
######                                square=[grid[i][0:3] for i in range(3,6)]
######                            elif col<6:
######                                square=[grid[i][3:6] for i in range(3,6)]
######                            else:  
######                                square=[grid[i][6:9] for i in range(3,6)]
######                        else:
######                            if col<3:
######                                square=[grid[i][0:3] for i in range(6,9)]
######                            elif col<6:
######                                square=[grid[i][3:6] for i in range(6,9)]
######                            else:  
######                                square=[grid[i][6:9] for i in range(6,9)]
######                        if not value in (square[0] + square[1] + square[2]):
######                            grid[row][col]=value
######                            if checkGrid(grid):
######                                return True
######                            else:
######                                if fill_su_Grid(grid):
######                                    return True
######            break
######    grid[row][col]=0 

###### Nous avions réussi à résoudre mais on voulait générer un sudoku et nous voulions modifier la fonction pour utiliser nos méthodes de classe.
###### Malheureusement, nous avons trop de problème et donc nous avons inclus un commentaire de ces lignes de codes.
###### A part ceci tout le reste vient de nous!
###### Si vous souhaitez en savoir plus n'hésitez pas à nous contacter.
