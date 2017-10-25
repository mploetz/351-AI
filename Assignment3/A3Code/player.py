# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 19:21:51 2016

@author: Ajinkya
"""
import board
import search
class Player:
    def __init__(self, board):
        # TODO
        self.b = board
        self.name = "Connect4 Legend"

    def make_move(self,c):
        # TODO
        self.b.make_move(c)

    def get_move(self):
        # TODO
        return search.minimax_root(self.b, 5)
    def __str__(self):
        # TODO
        return self.b.__str__()