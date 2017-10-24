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
        self.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.parent = None
        self.lastMove = None
        self.turn = True
        self.movesLeft = [5, 5, 5, 5, 5, 5, 5]
    
    # creates an empty board
    def empty_board(self):
        self.board = []
        for row in range(self.HEIGHT):
            self.board.append([])
            for col in range(self.WIDTH):
                self.board[row].append(0)

    def generate_moves(self):
        # TODO
        children = []
        index = 0
        for i in self.movesLeft:
            if i >= 0:
                children.append(index)
            index += 1
        return children


    # makes a move
    # Does not check if the move is valid
    def make_move(self,c):
        # TODO
        move = self.movesLeft[c]

        self.parent = deepcopy(self)

        self.lastMove = move

        self.movesLeft[c] -= 1

        if self.turn:
            self.board[move][c] = "R"
        else:
            self.board[move][c] = "B"

        self.turn = not self.turn

            
    def unmake_last_move(self):
        # TODO
        oldBoard = deepcopy(self.parent)

        self.board = oldBoard.board

        self.lastMove = oldBoard.lastMove

        self.turn = oldBoard.turn

        self.movesLeft = oldBoard.movesLeft

        self.parent = oldBoard.parent
                
    def last_move_won(self):
        # TODO
        total = 0
        player = None
        if self.turn:
           player = "R"
        else:
            player = "B"
        for x in range(0, self.WIDTH-3):
           for y in range(self.HEIGHT):
                if self.board[y][x] == player and self.board[y][x+1] == player and self.board[y][x+2] == player and self.board[y][x+3] == player:
                    return True
        for x in range(self.WIDTH):
            for y in range(0, self.HEIGHT - 3):
                if self.board[x][y] == player and self.board[x+1][y] == player and self.board[x+2][y] == player and self.board[x+3][y] == player:
                    return True
        for x in range(3, self.WIDTH):
            for y in range(self.HEIGHT-3):
                if self.board[x][y] == player and self.board[x+1][y-1] == player and self.board[x+2][y-2] == player and self.board[x+3][y-3] == player:
                    return True
        for x in range(self.HEIGHT-3):
            for y in range(self.WIDTH-3):
                if self.board[x][y] == player and self.board[x+1][y+1] == player and self.board[x+2][y+2] == player and self.board[x+3][y+3] == player:
                    return True

    def __str__(self):
        return str(np.matrix(self.board))