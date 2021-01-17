#Program solve sudoku 9x9

sudoku=[[9,0,0,1,0,0,0,0,5],
        [0,0,5,0,9,0,2,0,1],
        [8,0,0,0,4,0,0,0,0],
        [0,0,0,0,8,0,0,0,0],
        [0,0,0,7,0,0,0,0,0],
        [0,0,0,0,2,6,0,0,9],
        [2,0,0,3,0,0,0,0,6],
        [0,0,0,2,0,0,9,0,0],
        [0,0,1,9,0,4,5,7,0]]
#Define a grid contain a sudoku exemple

#Create a function who he verifies if a number in line and colunm of sudoku

def test_number_in_line_colunm(sudoku,chiffre_tester,line,colunm):
    test=False
    for l in range(9):
        if sudoku[line][l]==chiffre_tester:
            test=True
            break
        if sudoku[l][colunm]==chiffre_tester:
            test=True
            break
    return(test)

#Create a function who he verifies if a number in line of sudoku

def number_in_line(sudoku,line,chiffre_tester):
    test=False
    for j in range(9):
        if sudoku[line][j]==chiffre_tester:
            test=True
            break
    return(test)

#Create a function who he verifies if a number in colunm of sudoku 

def number_in_colunm(sudoku,colunm,chiffre_tester):
    test=False
    for i in range(9):
        if sudoku[i][colunm]==chiffre_tester:
            test=True
            break
    return(test)

#Create a function who he verifies if a number in case 3x3 of sudoku

def number_case_3(sudoku,line,colunm,chiffre_tester):
    test=False
    i=line
    j=colunm
    iTop,jTop=3*(i//3), 3*(j//3)
    for k in range(iTop,iTop+3):
        for l in range(jTop,jTop+3):
            if sudoku[k][l]==chiffre_tester:
                test=True
                break
    return(test)

#Function show the possibilities in the same case for different number
def liste_possibilities(sudoku,line,colunm):
    liste_nb=[]
    test=False
    for k in range(1,10):
        test=test_number_in_line_colunm(sudoku,k,line,colunm)
        if test==False:
            test=number_case_3(sudoku,line,colunm,k)
            if test==False:
                liste_nb.append(k)
    return(liste_nb)

#Create a function who he solves sudoku

def solver(sudoku):
    """Function solver sudoku and return sudoku result as board  """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                possibility=liste_possibilities(sudoku,i,j)
                for k in possibility:
                    sudoku[i][j]==k
                    solver(sudoku)
                    sudoku[i][j]=0
                    return
    print()
    for ligne in sudoku:
        print(ligne)
    solver(sudoku)
print(solver(sudoku))
