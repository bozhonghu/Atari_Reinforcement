import random
import sys
from BrainDQN_Nature import *
import numpy as np
import time

def is_refilling(im):
    left = 0
    scan = np.array(im)[148]
    for i in range(len(scan)):
        if scan[i][0] == 92:
            left = i
            break
    right = 0
    for i in range(len(scan)-1, 0, -1):
        if scan[i][0] == 92:
            right = i
            break
    top = np.array(im)[135:138,]
    print((left,right))
    for p in range(left, right):
            if top[0][p][0] == 170 and top[1][p][0] == 170 and top[2][p][0] == 170: