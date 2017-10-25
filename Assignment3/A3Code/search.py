# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:00:29 2016

@author: Ajinkya
"""
import board
import numpy as np
import evalFunction
import math
import copy

def minimax(b,depth):
    # TODO
    def minimaxhelpthisworld(b, depth):        
        if depth == 0 or b.last_move_won():
            return (-1, evalFunction.evalFunction(b.board))
        moves = b.generate_moves()
        bestChild = -1
        # max player
        if b.turn:
            bestValue = -math.inf
            for child in moves:
                b.make_move(child)
                v = minimaxhelpthisworld(b, depth-1)
                if bestValue < v[1]:
                    bestChild = child
                    bestValue = v[1]
                b.unmake_last_move()
            return (bestChild, bestValue)
        # min player
        else:
            bestValue = math.inf
            for child in moves:
                b.make_move(child)
                v = minimaxhelpthisworld(b, depth-1)
                if bestValue > v[1]:
                    bestChild = child
                    bestValue = v[1]
                b.unmake_last_move()
            return (bestChild, bestValue)
    return minimaxhelpthisworld(b, depth)[0]

def minimax_root(b,depth):
    # TODO 
    cur = minimax(b, depth)
    if cur == -1:
        return (-1, None)
    temp = copy.deepcopy(b)
    temp.make_move(cur)
    if temp.last_move_won():
        return (1, None)
    return (0, cur)

def alphabeta_minimax(b,depth,a,be):
    # TODO
    def alphabeta_minimax_helper(b, depth, a, be):        
        if depth == 0 or b.last_move_won():
            return (-1, evalFunction.evalFunction(b.board))
        moves = b.generate_moves()
        bestChild = -1
        # max player
        if b.turn:
            bestValue = -math.inf
            for child in moves:
                b.make_move(child)
                v = alphabeta_minimax_helper(b, depth-1, a, be)
                if bestValue < v[1]:
                    bestChild = child
                    bestValue = v[1]
                a = max(v[1], a)
                if be <= a:
                    break
                b.unmake_last_move()
            return (bestChild, bestValue)
        # min player
        else:
            bestValue = math.inf
            for child in moves:
                b.make_move(child)
                v = alphabeta_minimax_helper(b, depth-1, a, be)
                if bestValue > v[1]:
                    bestChild = child
                    bestValue = v[1]
                be = min(be, v[1])
                if be <= a:
                    break
                b.unmake_last_move()
            return (bestChild, bestValue)
    return alphabeta_minimax_helper(b, depth, a, be)[0]

def minimax_root_alphabeta(b, depth):
    # TODO
    pass