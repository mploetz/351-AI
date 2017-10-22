# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:34:05 2016

@author: Ajinkya
"""
import search
import numpy as np
class Board:
    def __init__(self, orig=None, hash=None):
        # copy all
        if (orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            # try copying input board
            try:
                self.won = orig.won
                self.threats0 = orig.threats0.copy()
                self.threats1 = orig.threats1.copy()
                self.heur = orig.heur
                self.dirty = orig.dirty
            # otherwise set missing fields as defaults
            except:
                self.won = False
                self.threats0 = set()
                self.threats1 = set()
                self.heur = 0
                self.dirty = False
            return
        
    def generate_moves(self):
        # TODO
        
    def make_move(self,c):
        # TODO
            
    def unmake_last_move(self):
        # TODO
                
    def last_move_won(self):
        # TODO
    
    def __str__(self):
        return str(np.matrix(board))
    
