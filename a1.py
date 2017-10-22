# Author Matthew Ploetz
# Partner: Tim Jones
import random

# A state is represented by a List [1,2,3] 
# A Board is a ListOf States Ex: [[1,2,3],[4,5,6][7,8,0]]
# the blank spot is represented by a 0

# genRandomBoard:
# returns a randomly shuffled Board
def genRandomBoard():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    random.shuffle(board)
    temp = []
    newBoard = []
    j = 0
    while (j < len(board)):
        i = 0
        while (i < 3):
            temp.append(board[j])
            i += 1
            j += 1
        newBoard.append(temp)
        temp = []
    return newBoard

# makeState
# params Board
# returns the each State of the current Board
def makeState(board):
    for x in board:
        print(x)

# General Search Procedure
def makeNode(state, parent, depth, pathCost):
    return [state, parent, depth, pathCost]


def generalSearch(queue, limit, numRuns):
    if queue == []:
        return False
    elif testProcedure(queue[0]):
        outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print("Limit reached")
    else:
        limit -= 1
        numRuns += 1
        generalSearch(expandProcedure(
            queue[0], queue[1:len(queue)]), limit, numRuns)

# Testing #
board = genRandomBoard()
print("Printing Randomly Shuffled Board:")
print(board)
print("\n")
print("Printing the state of the Board:")
makeState(board)