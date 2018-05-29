# Python3

import gym
import time
import numpy as np

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
                return True
    return False

if __name__ == '__main__':
    env = gym.make('NameThisGame-v0')
    env.reset()

    # Plays game 10 times
    for _ in range(10):
        observation = env.reset() # initial observation
        for _ in range(10000):
            time.sleep(0.05)

            env.render()
            action = env.action_space.sample() # take random action
            observation, reward, done, info = env.step(action) # take a random action

            if is_refilling(observation):
                time.sleep(5)

            if done:
                time.sleep(2)
                break

'''
Reward not cumulative:
- hit tentacle
- hit shark






'''
