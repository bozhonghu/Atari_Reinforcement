# Python3

import gym
import time

env = gym.make('NameThisGame-v0')

# Plays game 10 times
for _ in range(10):
    observation = env.reset() # initial observation
    for _ in range(10000):
        time.sleep(0.05)

        env.render()
        action = env.action_space.sample() # take random action
        observation, reward, done, info = env.step(action) # take a random action

        print 'reward:' , reward
        if reward != 0.:
            time.sleep(5)

        if done:
            time.sleep(2)
            break



'''
Reward not cumulative:
- hit tentacle
- hit shark






'''
