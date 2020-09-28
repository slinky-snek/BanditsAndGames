
import numpy as np
import math
import sys
import copy
import time
import random
import argparse
######################################################

#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
class UCBAgent:
    def __init__(self):
        #self.currentState.print_board()
        self.name = "Uma the UCB Agent"
        self.arm_rewards = np.zeros(10)
        self.avg_payout = np.zeros(10)
        self.num_pulls = np.zeros(10)
        self.total_pulls = 0
    
    def recommendArm(self, bandit, history):
        #Hey, your code goes here!
        # Update payouts
        if len(history):
            arm, reward = history[-1]
            self.arm_rewards[arm] += reward
            self.num_pulls[arm] += 1
            self.total_pulls += 1
            self.avg_payout[arm] = self.arm_rewards[arm] / self.num_pulls[arm]
        # Pull every arm at least once
        if self.total_pulls < 10:
            return self.total_pulls
        # Select arm
        max_payout = 0
        maximum = 0
        for i in range(len(self.avg_payout)):
            ucb = self.avg_payout[i] + math.sqrt(2*math.log(self.total_pulls)/self.num_pulls[i])
            possible_payout = self.avg_payout[i] + ucb
            if possible_payout > max_payout:
                max_payout = possible_payout
                maximum = i
        return maximum
