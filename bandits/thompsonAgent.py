
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

class thompsonAgent: 
    def __init__(self):
        self.name = "Terry the Thompson Sampling Agent"
        self.arm_rewards = np.zeros(10)
        self.avg_payout = np.zeros(10)
        self.posterior = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
                          [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
        self.posterior = np.asarray(self.posterior)
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
            if reward == 1:
                self.posterior[arm, 0] += 1
            else:
                self.posterior[arm, 1] += 1
        # Select arm
        max_mu = 0
        max = 0
        for i in range(len(self.posterior)):
            alpha = self.posterior[i, 0]
            beta = self.posterior[i, 1]
            mu = np.random.beta(alpha, beta)
            if mu > max_mu:
                max_mu = mu
                max = i
        return max
