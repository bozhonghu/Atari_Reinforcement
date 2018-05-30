'''
Started straining on mon may 28, 9pm
'''


import random
import cv2
import sys
from BrainDQN_Nature import *
import numpy as np
import time

import gym
from utils import *

# import pickle

TWO_DAY_TO_SEC = 172800
FIVE_HRS_TO_SEC = 18000
FIVE_MIN_TO_SEC = 300

TIME_TO_TRAIN = TWO_DAY_TO_SEC

lefts = [1, 4]
rights = [2, 5]
shoots = [3, 4, 5]

if __name__ == '__main__':

    # Initialize game
    env = gym.make('SpaceInvaders-v0')
    env.reset()
    actions = env.action_space.n

    print 'actions:' , actions

    brain = BrainDQN(actions)

    action0 = 0  # do nothing
    observation0, reward0, terminal, info = env.step(action0)

    observation0 = preprocess(observation0)
    brain.setInitState(observation0)
    brain.currentState = np.squeeze(brain.currentState)

    iters = 0 # number of games played
    start_time = time.clock()

    while time.clock() - start_time < TIME_TO_TRAIN:

        # print 'trained for ' + str(time.clock() - start_time) + ' sexs'

        action = brain.getAction()
        actionmax = np.argmax(np.array(action))

        # env.render()
        nextObservation,reward,terminal, info = env.step(actionmax)

        if terminal:
            iters += 1
            nextObservation = env.reset()

        # Create restricted array.
        restricted = [1] * 6
        # if (is_bullet(nextObservation, 0)):
        #     for i in lefts:
        #         restricted[i] = 0
        # if (is_bullet(nextObservation, 1)):
        #     for i in rights:
        #         restricted[i] = 0
        if (canHitBarrier(nextObservation)):
            for i in shoots:
                restricted[i] = 0

        nextObservation = preprocess(nextObservation)
        brain.setPerception(nextObservation,action,reward,terminal, restricted)



    print 'trained for ' + str(TIME_TO_TRAIN) + 'secs, ' + str(iters) + ' iters (games played)..'

    # Now, play the game with the trained network and see how it performs
    brain.epsilon = 0.2 #  Must do this or else brain might keep performing random actions

    env.reset()
    games = 0
    sum_score = 0.
    NUM_GAMES = 100

    while True:
        action = brain.getAction()
        actionmax = np.argmax(np.array(action))

        # env.render()
        nextObservation,reward,terminal, info = env.step(actionmax)

        sum_score += reward

        if terminal:
            nextObservation = env.reset()
            games += 1
            print 'test games: ' + str(games)

        if games == NUM_GAMES:
            break

        nextObservation = preprocess(nextObservation)
        brain.setPerception(nextObservation,action,reward,terminal, restricted)


    print 'Restricted avg score: ' + str(sum_score / float(games))
    print 'out of ' + str(NUM_GAMES) + ' games '
