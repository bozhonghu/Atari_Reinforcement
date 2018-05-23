def preprocessBarrierFindPossibleRowsCols(observation):
    '''
    Given the START observation, returns which rows/cols have barriers. 
    
    Color of barrier: 181  83  40
    observation[row][col][color]
    
    Rows that can have barrier:
        set([160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 157, 158, 159])
    
    '''
    row_with_barrier = set() # rows with barrier
    col_with_barrier = set() 
    
    for row in range(len(observation)):
        for col in range(len(observation[row])):
            if observation[row][col][0] == 181 and observation[row][col][1] == 83 and observation[row][col][2] == 40:
                row_with_barrier.add(row)
                col_with_barrier.add(col)
                
                
    print 'row_with_barrier', row_with_barrier
    print 'col_with_barrier', col_with_barrier
    
def preprocessBarrierCols(observation):
    '''
    Takes observation (state) as input and returns which columns in the 210x160 pixel image 
    contain a barrier
    '''
    
    # Taken from result of preprocessBarrierFindPossibleRowsCols()
    possible_row_with_barrier = [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 157, 158, 159]
    possible_col_with_barrier = [42, 43, 44, 45, 46, 47, 48, 49, 74, 75, 76, 77, 78, 79, 80, 81, 106, 107, 108, 109, 110, 111, 112, 113]

    col_with_barrier = set()
        
    for col in possible_col_with_barrier:
        for row in possible_row_with_barrier:
            if observation[row][col][0] == 181 and observation[row][col][1] == 83 and observation[row][col][2] == 40:
                col_with_barrier.add(col)
                break
    
    return col_with_barrier

def findShipTip(observation):
    '''
    Finds the column where the tip of the shipp is
    (presumably the bullets com out of the tip)
    
    ship color: 50 132  50
    row of the top of the ship: 185
    '''
    for col in range(len(observation[0])):
        if observation[185][col][0] == 50 and observation[185][col][1] == 132 and observation[185][col][2] == 50:
            return col
    
    return -1 # some error occured

def canHitBarrier(observation):
    '''
    returns true if the ship will hit a barrier if it shoots.
    '''
    cols = preprocessBarrierCols(observation)
    tip = findShipTip(observation)
    
    return tip in cols

    