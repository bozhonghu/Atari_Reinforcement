import random
import cv2
import sys
from BrainDQN_Nature import *
import numpy as np
import time

import gym
from utils import *


if __name__ == '__main__':

    env = gym.make('SpaceInvaders-v0')
    env.reset()

    games = 0
    sum_score = 0.
    NUM_GAMES = 100

    while True:
        action = env.action_space.sample() # take a random action
        observation, reward, done, info = env.step(action)

        sum_score += reward

        if done:
            env.reset()
            games += 1
            print 'test games: ' + str(games)

        if games == NUM_GAMES:
            break

    print 'Random avg score: ' + str(sum_score / float(games))
    print 'out of ' + str(NUM_GAMES) + ' games '