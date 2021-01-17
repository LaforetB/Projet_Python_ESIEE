import pickle
# Système de pile pour l'enregistrement des coups et scores + fichier pour enregistrer les parties

pile_score=[]
pile_coup=[]

def pile_add(pile,element):
    return(pile.append(element))

def pile_sub_return_element(pile):
    return(pile.pop())

def pile_sub(pile,element):
    return(pile.remove(element))

def remise_zero(pile):
    return([])

def register_file(sudoku,pile_score):       #attention ceci efface totalement l'ancien fichier
    file=open("Enregistrement.txt","w")
    file.write(sudoku,"\n")
    file.write(pile_score,"\n")
    file.close

def read_file():                            #attention ceci lis sans effacer l'ancien fichier
    file=open("Enregistrement.txt","r")
    str_recup=str(file)
    file.close
    liste_recup=str_recup.split("\n")
    sudoku=liste_recup[0]
    pile_score=liste_recup[1]
    return(sudoku,pile_score)

#Fonction avec Pickle

def enregistre_sudoku(mon_fichier,truc):
    """Enregistre le sudoku dans le fichier voulu en binaire """
    with open(mon_fichier,'wb') as fichier:
        record=pickle.Pickler(fichier)                              # Affecter à une variable la possibilité de mettre des éléments dans un fichier
        record.dump(truc)                                           # Enregistrer dans le fichier le truc grâce à record et pickler 

def enregistre_score(mon_fichier,truc):
    """Enregistre le score dans le fichier voulu en binaire """
    with open(mon_fichier,'wb') as fichier:
        record=pickle.Pickler(fichier)
        record.dump(truc)

def lire_sudoku(mon_fichier):
    """Donne le sudoku depuis le fichier """
    with open(mon_fichier,'rb') as fichier:
        get_record=pickle.Unpickler(fichier)
        return(get_record.load())

def lire_score(mon_fichier):
    """Donne le score depuis le fichier """
    with open(mon_fichier,'rb') as fichier:
        get_record=pickle.Unpickler(fichier)
        return(get_record.load())