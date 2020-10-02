
import numpy as np
import sys
import copy
import time
import random
import argparse
import math
######################################################
global total_nodes

#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
class Node:
    def __init__(self):
        self.children = []
        self.parent = ''
        self.state = ''
        self.score = 0
        self.visits = 0
        self.incoming_action = ''
        self.untried_actions = []

class MCTSAgent:
    def __init__(self):
        #self.currentState.print_board()
        self.name = "Mallory the MCTSAgent"

    def suggestMove(self, gameState):
        #Hey, your code goes here!
        global total_nodes
        total_nodes = 0
        return UCTSearch(gameState)

def UCTSearch(gameState):
    global total_nodes
    root = Node()
    root.state = gameState
    root.untried_actions = gameState.getMoves()
    while total_nodes != 10000:
        node = TreePolicy(root)
        score = DefaultPolicy(node.state)
        Backup(node, score)
    return BestChild(root, 1).incoming_action

def TreePolicy(node):
    while not node.state.complete():
        if len(node.untried_actions) != 0:
            return Expand(node)
        else:
            node = BestChild(node, 1)
    return node

def Expand(node):
    global total_nodes
    if len(node.untried_actions) != 0:
        total_nodes += 1
        move = node.untried_actions[0]
        node.untried_actions.remove(move)
        child = Node()
        child.parent = node
        temp_state = node.state.clone()
        temp_state.move(move)
        child.state = temp_state
        child.incoming_action = move
        child.untried_actions = temp_state.getMoves()
        node.children.append(child)
        return child

def BestChild(node, selection_policy):
    best_child = None
    best_score = 0
    for child in node.children:
        ucb = (child.score/child.visits) + selection_policy * (math.sqrt(2 * math.log(node.visits)/child.visits))
        if ucb > best_score:
            best_score = ucb
            best_child = child
    return best_child

def DefaultPolicy(gameState):
    temp_state = gameState.clone()
    while not temp_state.complete():
        move = random.choice(temp_state.getMoves())
        temp_state.move(move)
    return temp_state.heuristic_value()

def Backup(node, score):
    while node:
        node.visits += 1
        node.score = node.state.heuristic_value()  ## add reward of parent?? (what goes here)
        node = node.parent
