import random
import cv
import sys
from BrainDQN_Nature import *
import numpy as np 

import gym

env = gym.make('SpaceInvaders-v0')
env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample() # take a random action
    observation, reward, done, info = env.step(action)
    print(reward)