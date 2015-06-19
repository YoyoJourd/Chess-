plateau = [['.']*8 for i in range(8)]
cellule = 0

def affichagePlateau(plateau, cellule):
#Piéces en haut du jeu 
     plateau[1][0]='P'
     plateau[1][1]='P'
     plateau[1][2]='P'
     plateau[1][3]='P'
     plateau[1][4]='P'
     plateau[1][5]='P'
     plateau[1][6]='P'
     plateau[1][7]='P'

     plateau[0][0]='T'
     plateau[0][7]='T'

     plateau[0][1]='C'
     plateau[0][6]='C'

     plateau[0][2]='F'
     plateau[0][5]='F'

     plateau[0][3]='D'

     plateau[0][4]='R'

#Piéce en bas du jeu                 
     plateau[6][0]='P'
     plateau[6][1]='P'
     plateau[6][2]='P'
     plateau[6][3]='P'
     plateau[6][4]='P'
     plateau[6][5]='P'
     plateau[6][6]='P'
     plateau[6][7]='P'

     plateau[7][0]='T'
     plateau[7][7]='T'

     plateau[7][1]='C'
     plateau[7][6]='C'

     plateau[7][2]='F'
     plateau[7][5]='F'

     plateau[7][3]='D'

     plateau[7][4]='R'
     
     for ligne in plateau:
         for cellule in ligne:
             print(cellule,' ', end='')
         print('\n')

affichagePlateau(plateau, cellule)    
