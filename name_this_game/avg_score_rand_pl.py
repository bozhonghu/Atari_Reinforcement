'''
Average score that random player gets

average score: 2329.6 out of  100 games
'''


import gym
import time

env = gym.make('NameThisGame-v0')

NUM_GAMES = 100
cur_score = 0.
sum_score = 0.


for i in range(NUM_GAMES):
    observation = env.reset() # initial observation
    for _ in range(10000):
        action = env.action_space.sample() # take random action
        observation, reward, done, info = env.step(action) # take a random action

        cur_score += reward
        sum_score += reward

        if done:
            print 'game', i, ' | score:', cur_score
            cur_score = 0
            break

print 'average score:', sum_score/float(NUM_GAMES), 'out of ', NUM_GAMES, 'games'
