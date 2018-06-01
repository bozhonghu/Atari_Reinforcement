import random
import cv2
import sys
from BrainDQN_Nature import *
import numpy as np

import time

def findThreeVsOneAndTwo():
    ones = set([ (185, 88), (185, 89), (185, 90), (185, 91),
    (186, 88), (186, 89), (186, 90), (186, 91),
    (187, 84), (187, 85), (187, 86), (187, 87), (187, 88), (187, 89), (187, 90), (187, 91),
    (188, 84), (188, 85), (188, 86), (188, 87), (188, 88), (188, 89), (188, 90), (188, 91),
    (189, 88), (189, 89), (189, 90), (189, 91),
    (190, 88), (190, 89), (190, 90), (190, 91),
    (191, 88), (191, 89), (191, 90), (191, 91),
    (192, 88), (192, 89), (192, 90), (192, 91),
    (193, 84), (193, 85), (193, 86), (193, 87), (193, 88), (193, 89), (193, 90), (193, 91), (193, 92), (193, 93), (193, 94), (193, 95),
    (194, 84), (194, 85), (194, 86), (194, 87), (194, 88), (194, 89), (194, 90), (194, 91), (194, 92), (194, 93), (194, 94), (194, 95)
    ])

    twos =set( [(185, 84), (185, 85), (185, 86), (185, 87), (185, 88), (185, 89), (185, 90), (185, 91), (185, 92), (185, 93), (185, 94), (185, 95)
    ,(186, 84), (186, 85), (186, 86), (186, 87), (186, 88), (186, 89), (186, 90), (186, 91), (186, 92), (186, 93), (186, 94), (186, 95)
    ,(187, 92), (187, 93), (187, 94), (187, 95)
    ,(188, 92), (188, 93), (188, 94), (188, 95)
    ,(189, 84), (189, 85), (189, 86), (189, 87), (189, 88), (189, 89), (189, 90), (189, 91), (189, 92), (189, 93), (189, 94), (189, 95)
    ,(190, 84), (190, 85), (190, 86), (190, 87), (190, 88), (190, 89), (190, 90), (190, 91), (190, 92), (190, 93), (190, 94), (190, 95)
    ,(191, 84), (191, 85), (191, 86), (191, 87)
    ,(192, 84), (192, 85), (192, 86), (192, 87)
    ,(193, 84), (193, 85), (193, 86), (193, 87), (193, 88), (193, 89), (193, 90), (193, 91), (193, 92), (193, 93), (193, 94), (193, 95)
    ,(194, 84), (194, 85), (194, 86), (194, 87), (194, 88), (194, 89), (194, 90), (194, 91), (194, 92), (194, 93), (194, 94), (194, 95)])

    threes = set([(185, 84), (185, 85), (185, 86), (185, 87), (185, 88), (185, 89), (185, 90), (185, 91), (185, 92), (185, 93), (185, 94), (185, 95),
    (186, 84), (186, 85), (186, 86), (186, 87), (186, 88), (186, 89), (186, 90), (186, 91), (186, 92), (186, 93), (186, 94), (186, 95),
    (187, 92), (187, 93), (187, 94), (187, 95),
    (188, 92), (188, 93), (188, 94), (188, 95),
    (189, 84), (189, 85), (189, 86), (189, 87), (189, 88), (189, 89), (189, 90), (189, 91), (189, 92), (189, 93), (189, 94), (189, 95),
    (190, 84), (190, 85), (190, 86), (190, 87), (190, 88), (190, 89), (190, 90), (190, 91), (190, 92), (190, 93), (190, 94), (190, 95),
    (191, 92), (191, 93), (191, 94), (191, 95),
    (192, 92), (192, 93), (192, 94), (192, 95),
    (193, 84), (193, 85), (193, 86), (193, 87), (193, 88), (193, 89), (193, 90), (193, 91), (193, 92), (193, 93), (193, 94), (193, 95),
    (194, 84), (194, 85), (194, 86), (194, 87), (194, 88), (194, 89), (194, 90), (194, 91), (194, 92), (194, 93), (194, 94), (194, 95)])


    couloredinthreenottow = threes-twos
    colouredinthreenotone = threes-ones

    couloredinthreeonly = couloredinthreenottow.intersection(colouredinthreenotone)

    print couloredinthreeonly # set([(191, 92), (191, 93), (192, 95), (192, 94), (191, 94), (192, 93), (191, 95), (192, 92)])

    # set([(191, 92), (191, 93), (192, 95), (192, 94), (191, 94), (192, 93), (191, 95), (192, 92)])
    # thiese are colored for three, not 2

def findNumber(observation):
    '''
    For developent


    possible row of number: 185 - 200
    possible col of number  81 - 90



    (192, 87): coul
    '''



    '''
    1:
[(185, 88), (185, 89), (185, 90), (185, 91)]
[(186, 88), (186, 89), (186, 90), (186, 91)]
[(187, 84), (187, 85), (187, 86), (187, 87), (187, 88), (187, 89), (187, 90), (187, 91)]
[(188, 84), (188, 85), (188, 86), (188, 87), (188, 88), (188, 89), (188, 90), (188, 91)]
[(189, 88), (189, 89), (189, 90), (189, 91)]
[(190, 88), (190, 89), (190, 90), (190, 91)]
[(191, 88), (191, 89), (191, 90), (191, 91)]
[(192, 88), (192, 89), (192, 90), (192, 91)]
[(193, 84), (193, 85), (193, 86), (193, 87), (193, 88), (193, 89), (193, 90), (193, 91), (193, 92), (193, 93), (193, 94), (193, 95)]
[(194, 84), (194, 85), (194, 86), (194, 87), (194, 88), (194, 89), (194, 90), (194, 91), (194, 92), (194, 93), (194, 94), (194, 95)]

    2:
[(185, 84), (185, 85), (185, 86), (185, 87), (185, 88), (185, 89), (185, 90), (185, 91), (185, 92), (185, 93), (185, 94), (185, 95)]
[(186, 84), (186, 85), (186, 86), (186, 87), (186, 88), (186, 89), (186, 90), (186, 91), (186, 92), (186, 93), (186, 94), (186, 95)]
[(187, 92), (187, 93), (187, 94), (187, 95)]
[(188, 92), (188, 93), (188, 94), (188, 95)]
[(189, 84), (189, 85), (189, 86), (189, 87), (189, 88), (189, 89), (189, 90), (189, 91), (189, 92), (189, 93), (189, 94), (189, 95)]
[(190, 84), (190, 85), (190, 86), (190, 87), (190, 88), (190, 89), (190, 90), (190, 91), (190, 92), (190, 93), (190, 94), (190, 95)]
[(191, 84), (191, 85), (191, 86), (191, 87)]
[(192, 84), (192, 85), (192, 86), (192, 87)]
[(193, 84), (193, 85), (193, 86), (193, 87), (193, 88), (193, 89), (193, 90), (193, 91), (193, 92), (193, 93), (193, 94), (193, 95)]
[(194, 84), (194, 85), (194, 86), (194, 87), (194, 88), (194, 89), (194, 90), (194, 91), (194, 92), (194, 93), (194, 94), (194, 95)]


    3:

[(185, 84), (185, 85), (185, 86), (185, 87), (185, 88), (185, 89), (185, 90), (185, 91), (185, 92), (185, 93), (185, 94), (185, 95)]
[(186, 84), (186, 85), (186, 86), (186, 87), (186, 88), (186, 89), (186, 90), (186, 91), (186, 92), (186, 93), (186, 94), (186, 95)]
[(187, 92), (187, 93), (187, 94), (187, 95)]
[(188, 92), (188, 93), (188, 94), (188, 95)]
[(189, 84), (189, 85), (189, 86), (189, 87), (189, 88), (189, 89), (189, 90), (189, 91), (189, 92), (189, 93), (189, 94), (189, 95)]
[(190, 84), (190, 85), (190, 86), (190, 87), (190, 88), (190, 89), (190, 90), (190, 91), (190, 92), (190, 93), (190, 94), (190, 95)]
[(191, 92), (191, 93), (191, 94), (191, 95)]
[(192, 92), (192, 93), (192, 94), (192, 95)]
[(193, 84), (193, 85), (193, 86), (193, 87), (193, 88), (193, 89), (193, 90), (193, 91), (193, 92), (193, 93), (193, 94), (193, 95)]
[(194, 84), (194, 85), (194, 86), (194, 87), (194, 88), (194, 89), (194, 90), (194, 91), (194, 92), (194, 93), (194, 94), (194, 95)]
    '''

    print observation[194][85]


    if observation[194][85][0] == 162 and observation[194][85][1] == 134 and observation[194][85][2] ==  56:

        for row in range(170, 210):
            colored = []
            for col in range(81, 120):
                if observation[row][col][0] == 162 and observation[row][col][1] == 134 and observation[row][col][2] ==  56:
                    colored.append((row,col))

            print colored



        print 'number on!!'
        print observation[194][85]
        print observation[194][90]



        time.sleep(.2)

def determineNumber(observation):
    '''
    (192, 94): coulered for 3 only
    194][85, couldered for all 3 numbers
    '''
    if observation[194][85][0] == 162 and observation[194][85][1] == 134 and observation[194][85][2] ==  56:
        if observation[192][94][0] == 162 and observation[192][94][1] == 134 and observation[192][94][2] ==  56:
            print '3'
        else:
            print '1 or 2'

        time.sleep(.2)

def preprocessDetermineOneOrTwo(observation):
    '''
    Given an observation, determines if the screen shows 1or2 , 3 or none

    True: 1 or 2
    False: 3 or none
    '''
    if observation[194][85][0] == 162 and observation[194][85][1] == 134 and observation[194][85][2] ==  56:
        if observation[192][94][0] == 162 and observation[192][94][1] == 134 and observation[192][94][2] ==  56:
            return False
        else:
            return True
    else:
        return False



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


    # print 'row_with_barrier', row_with_barrier
    # print 'col_with_barrier', col_with_barrier

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

# Takes the original image as input.
def is_bullet(im, side):
    left = min(np.unique(np.nonzero(np.array(np.squeeze(im))[194])[0]))
    right = left + 6
    if side == 0:
        im = im[160:190,left-5:left]
    else:
        im = im[160:190,right:right+5]
    lower_blue = np.array([120,120,120])
    upper_blue = np.array([150,150,150])
    mask = cv2.inRange(im, lower_blue, upper_blue)
    res = cv2.bitwise_and(im,im, mask = mask)
    if len(np.nonzero(res)[0]) > 0:
        return True
    else:
        return False

def preprocess(observation):
    observation = cv2.cvtColor(cv2.resize(observation, (84, 110)), cv2.COLOR_BGR2GRAY)
    observation = observation[26:110,:]
    ret, observation = cv2.threshold(observation,1,255,cv2.THRESH_BINARY)
    return np.reshape(observation,(84,84,1))
