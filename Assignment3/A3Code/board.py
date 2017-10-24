# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:34:05 2016

@author: Ajinkya
"""
import search
import numpy as np
class Board:
    WIDTH = 7
    HEIGHT = 6
    def __init__(self):
        self.board = self.empty_board()
        self.won = False
        self.parent = self.empty_board()
        self.lastMove = None
        self.numMoves = 0
        self.turn = 0
    
    # creates an empty board
    def empty_board(self):
        self.board = []
        for row in range(self.HEIGHT):
            self.board.append([])
            for col in range(self.WIDTH):
                self.board[row].append('_')

    def generate_moves(self):
        # TODO
        children = []
        for i in range(self.WIDTH):
            if len(self.board[i]) < self.HEIGHT:
                child = self.board.deepcopy()
                child.make_move(i)
                children.append(i)
        return children

    # makes a move
    # Does not check if the move is valid
    def make_move(self,c):
        # TODO
        # whos turn moving
        piece = self.numMoves % 2
        # keep track of that move
        self.lastMove = (piece, c)
        # update moves
        self.numMoves += 1
        # keep track of all moves
        self.moves.append(self.lastMove)
        # put the piece on the board at given move(c)
        self.board[c].append(piece)
            
    def unmake_last_move(self):
        # TODO
        pass
                
    def last_move_won(self):
        # TODO
        horscore = 0
        verscore = 0
        rightdiag = 0
        leftdiag = 0
        phor = 0
        pver = 0
        pleft = 0
        pright = 0
        for row in range(self.HEIGHT):
            horscore = 0
            for col in range(self.WIDTH):
                verscore = 0
                if self.board[row][col] == self.turn:
                    horscore += 1
                else:
                    horscore = 0
                for row2 in range(self.HEIGHT):
                    if self.board[row2][col] == self.turn:
                        verscore += 1
                    else:
                        verscore = 0
        # checks \
        for i in range(3):
            for j in range(4):
                prev = self.board[i][j]
                for k in range(1, 4):
                    if self.board[i+k][j+k] != 0 and self.board[i+k][j+k] == prev:
                        rightDiag += 1
                    if (rightDiag == 4):
                        return True
                    else:
                        break
                    rightDiag = 1
                    prev = 0
        return False
        
        for row in range(3, 6):
            for col in range(4):
                prev = self.board[row][col]
            for k in range(1,4):
                if self.board[row-k][col+k] != 0 and self.board[row-k][col+k] == prev:
                    leftdiag += 1
                if leftdiag == 4:
                    return self.board[row-k][col+k]
            else:
                break
            leftdiag = 1
            prev = 0

    def __str__(self):
        return str(np.matrix(self.board))   
