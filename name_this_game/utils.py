import random
import sys
import cv2
from BrainDQN_Nature import *
import numpy as np
import time

def preprocess(observation):
    observation = cv2.cvtColor(cv2.resize(observation, (84, 110)), cv2.COLOR_BGR2GRAY)
    observation = observation[26:110,:]
    ret, observation = cv2.threshold(observation,1,255,cv2.THRESH_BINARY)
    return np.reshape(observation,(84,84,1))

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
    for p in range(left, right):
        if top[0][p][0] == 170 and top[1][p][0] == 170 and top[2][p][0] == 170:
            return True
    return False