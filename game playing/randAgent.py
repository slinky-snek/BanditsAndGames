
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
class randomAgent: 
	def __init__(self):
		#self.currentState.print_board()
		self.name = "Randy the RandomAgent"
	
	def suggestMove(self, gameState):
		possibleMoves = gameState.getMoves()
		return random.choice(possibleMoves)
