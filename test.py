import random
import cv2
import sys
from BrainDQN_Nature import *
import numpy as np 

import gym

# Takes the original image as input.
def is_bullet(im, side):
    left = min(np.unique(np.nonzero(np.array(np.squeeze(im))[194])[0]))
    right = left + 6
    if side == 0:
        im = im[160:180,left-5:left]
    else:
        im = im[160:180,right:right+5]
    lower_blue = np.array([120,120,120])
    upper_blue = np.array([150,150,150])
    mask = cv2.inRange(im, lower_blue, upper_blue)
    res = cv2.bitwise_and(im,im, mask = mask)
    if len(np.nonzero(res)[0]) > 0:
        return True
    else:
        return False

env = gym.make('SpaceInvaders-v0')
env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample() # take a random action
    observation, reward, done, info = env.step(action)
    if (is_bullet(observation, 0)):
        print("left")