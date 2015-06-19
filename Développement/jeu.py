plateau = [['0']*8 for i in range(8)]
cellule = 0

def initialisationPlateau(plateau, cellule):
    for ligne in plateau:
        for cellule in ligne:
            print('0   ', end='')
        print('\n')
    return plateau        

def placementPion(plateau, cellule):
     plateau[1][0]=1
     plateau[1][1]=1
     plateau[1][2]=1
     plateau[1][3]=1
     plateau[1][4]=1
     plateau[1][5]=1
     plateau[1][6]=1
     plateau[1][7]=1
                 
     plateau[6][0]=1
     plateau[6][1]=1
     plateau[6][2]=1
     plateau[6][3]=1
     plateau[6][4]=1
     plateau[6][5]=1
     plateau[6][6]=1
     plateau[6][7]=1
        
     for ligne in plateau:
         for cellule in ligne:
             print(cellule,' ', end='')
         print('\n')
        
initialisationPlateau(plateau, cellule)
placementPion(plateau, cellule)
