
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
class epsGreedyAgent: 
    def __init__(self):
        #self.currentState.print_board()
        self.name = "Eric the Epsilon Greedy Agent"
        self.epsilon = 0.2  # This guy likes to explore
        self.arm_rewards = np.zeros(10)
        self.avg_payout = np.zeros(10)
        self.num_pulled = np.zeros(10)

    def recommendArm(self, bandit, history):
        #Hey, your code goes here!
        # Update payouts
        if len(history):
            arm, reward = history[-1]
            self.arm_rewards[arm] += reward
            self.num_pulled[arm] += 1
            self.avg_payout[arm] = self.arm_rewards[arm]/self.num_pulled[arm]
        # Decay epsilon
        if divmod(len(history), 100) == 0:
            self.epsilon -= .00005
        # Select arm
        if random.random() < self.epsilon:
            return random.choice(range(bandit.getNumArms()))
        else:
            return np.argmax(self.avg_payout)
