def initialisationPlateau():
    plateau = [['.']*8 for i in range(8)]
    cellule = 0
    for ligne in plateau:
        for cellule in ligne: 
            print('.     ',end='') 
        print('\n')

def placementPion():
    plateau = [['.']*8 for i in range(8)]
    cellule = 0
    for ligne in plateau:
        for cellule in range (1):
            cellule = 1
            print('P     ', end='')
    print('\n')
            
initialisationPlateau()
placementPion()
