import random
import cv2
import sys
from BrainDQN_Nature import *
import numpy as np 

import gym
from utils import *

lefts = [1, 4]
rights = [2, 5]
shoots = [3, 4, 5]

if __name__ == '__main__':

    # Initialize game
    env = gym.make('SpaceInvaders-v0')
    env.reset()
    actions = env.action_space.n
    brain = BrainDQN(actions)

    action0 = 0  # do nothing
    observation0, reward0, terminal, info = env.step(action0)

    observation0 = preprocess(observation0)
    brain.setInitState(observation0)
    brain.currentState = np.squeeze(brain.currentState)

    while True:
        action = brain.getAction()
        actionmax = np.argmax(np.array(action))

        env.render()
        nextObservation,reward,terminal, info = env.step(actionmax)
        
        if terminal:
            nextObservation = env.reset()

        # Create restricted array.    
        restricted = [1] * 6
        if (is_bullet(nextObservation, 0)):
            for i in lefts:
                restricted[i] = 0
        if (is_bullet(nextObservation, 1)):
            for i in rights:
                restricted[i] = 0
        if (canHitBarrier(nextObservation)):
            for i in shoots:
                restricted[i] = 0  

        nextObservation = preprocess(nextObservation)
        brain.setPerception(nextObservation,action,reward,terminal, restricted)