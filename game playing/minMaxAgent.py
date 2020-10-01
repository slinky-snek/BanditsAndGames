
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

class minMaxAgent:
    def __init__(self):
        self.name = "Manny the MinMaxAgent"
        self.nodes = 10000

    def minimax(self, gameState, maximizing_player):
        if self.nodes < 0 or gameState.complete():
            return gameState.heuristic_value()
        if maximizing_player:
            possible_moves = gameState.getMoves()
            best_score = -9999
            best_move = possible_moves[0]
            for move in possible_moves:
                temp_state = gameState.clone()
                temp_state.move(move)
                self.nodes -= 1
                score = self.minimax(temp_state, False)
                if score > best_score:
                    best_move = move
                    best_score = score
            return best_score
        if not maximizing_player:
            possible_moves = gameState.getMoves()
            best_score = 9999
            best_move = possible_moves[0]
            for move in possible_moves:
                temp_state = gameState.clone()
                temp_state.move(move)
                self.nodes -= 1
                score = self.minimax(temp_state, True)
                if score < best_score:
                    best_move = move
                    best_score = score
            return best_score

    def suggestMove(self, gameState):
        #Hey, your code goes here!

        self.nodes = 10000
        possible_moves = gameState.getMoves()
        best_score = -9999
        best_move = possible_moves[0]
        for move in possible_moves:
            temp_state = gameState.clone()
            temp_state.move(move)
            score = self.minimax(temp_state, True)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move
