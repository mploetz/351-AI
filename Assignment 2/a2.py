from math import sqrt
from copy import deepcopy
import math

class Node(object):
    # constructor for Node objects
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    # method to print Node objects -- feel free to modify!
    def str(self):
        return "Name: " + self.name + " Cost: " + str(self.f)

# AI City Graph representation
AI_nodeA = Node('A', -6, -2)
AI_nodeB = Node('B', -3, 2)
AI_nodeC = Node('C', -4, -3)
AI_nodeD = Node('D', 2, 4)
AI_nodeE = Node('E', 1, 0)
AI_nodeF = Node('F', 6, 5)

# node list
AI_CITY_NODE_LIST = [AI_nodeA, AI_nodeB, AI_nodeC, AI_nodeD, AI_nodeE, AI_nodeF]

# adjacency list
AI_CITY_ADJ_LIST = [[AI_nodeA, AI_nodeB, 5],
          [AI_nodeA, AI_nodeC, 4],
          [AI_nodeA, AI_nodeD, 11],
          [AI_nodeB, AI_nodeC, 6],
          [AI_nodeB, AI_nodeD, 5],
          [AI_nodeB, AI_nodeE, 5],
          [AI_nodeC, AI_nodeD, 10],
          [AI_nodeC, AI_nodeE, 5],
          [AI_nodeD, AI_nodeE, 5],
          [AI_nodeD, AI_nodeF, 5],
          [AI_nodeE, AI_nodeD, 5],
          [AI_nodeC, AI_nodeF, 16]]

# Heuristic function -- takes two nodes, returns a number: the Euclidean distance 
# between aNode and bNode
def euclideanDistance(aNode, bNode):
    #TODO
    points = (bNode.x - aNode.x)**2 + (bNode.y - aNode.y)**2
    return sqrt(points)

# find_node_to_explore -- takes a list of nodes, returns a node:
# the lowest-cost node in the frontier
def find_node_to_explore(frontier):
    #TODO
    cheapest = frontier[0]
    for node in frontier:
        if cheapest.f > node.f:
            cheapest = node
    return cheapest

# expand_frontier -- takes a node, a list of nodes, the adjacency matrix, and a node
# returns the updated frontier, as described in assignment description
def expand_frontier(to_explore, frontier, adjacencyMatrix, goal_state):
    #TODO     
    for child in adjacencyMatrix:
        # add the explored nodes successors to the frontier
        if (child[0].name == to_explore.name):
            ref = deepcopy(child[1])
            ref.g = to_explore.g + child[2]
            ref.h = euclideanDistance(ref, goal_state)
            ref.f = ref.h + ref.g
            inOr = True
            for node in frontier:
                if (ref.name is node.name):
                    inOr = False
                    if ref.f < node.f:
                        frontier.remove(node)
                        frontier.append(ref)
                        break
                    elif ref.g < node.g and ref.f == node.f:
                        frontier.remove(node)
                        frontier.append(ref)
                        break
            if inOr:
                frontier.append(ref)
    # remove explored node from the frontier
    frontier.remove(to_explore)
    return frontier

# aStar -- full A* function: takes a list of nodes, an adjacency matrix, a start node, and a goal node
# feel free to turn debugging (printing) on/off as you wish
def aStar(nodeList, adjacencyMatrix, startNode, goalNode, debug=True):
    #Our hint to you -- getting started
    startNode.h = euclideanDistance(startNode, goalNode)
    startNode.g = 0
    startNode.f = startNode.g + startNode.h
    frontier = [startNode]
    explored = []
    
    while(frontier != []):
        #printing procedure to see your progress
        if (debug):
            print("frontier:")
            for node in frontier:
                print(node.str())
            print("explored:")
            for node in explored:
                print(node.str())
        #TODO       
        current = find_node_to_explore(frontier)
        if current.name == goalNode.name:
            goalNode.g = current.g
            explored.append(current)
            found = True
            break
        else:
            isExplored = None
            found = False
            for node in explored:
                if node.name == current.name:
                    isExplored = node
                    found = True
                    break
            if not found or (isExplored != None and isExplored.g > current.g): 
                frontier = expand_frontier(current, frontier, adjacencyMatrix, goalNode)               
                explored.append(current)
                for node in frontier:
                    for expNode in explored:
                        if node.name == expNode.name:
                            frontier.remove(node)    
        
    # Once search is finished, show results
    if found:
        print("frontier:")
        for node in frontier:
            print(node.str())
        print("explored:")
        for node in explored:
            print(node.str())
        print("We found the goal!")
    else: print("Goal not found :(")
    return (explored, goalNode.g)

# Main method. Add more tests!
def main():
    #Test for AI City Graph, starting at A with goal node F
    result = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST, AI_nodeA, AI_nodeF)
    for i in result[0]:
        print(i.name)
        print ("Total Path Cost: %d" % result[1])
    #add your own tests below!
    print('\n')
    # Cant go backwards
    res = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST,AI_nodeF, AI_nodeA)
    for n in res[0]:
        print(n.name)
        print ("Total Path Cost: %d" % res[1])
    # Check to make sure doesnt get stuck on a loop
    print('\n')
    S = Node('S', 0, 1) 
    A = Node('A', 5, 1)
    B = Node('B', 11, 6)
    C = Node('C', -1, 5)
    D = Node('D', -11, 12)
    G = Node('G', 7, 3)
    nodeList = [S, A, B, C, D, G]
    nodeAdjList = [[S, A, 9], [S, B, 8], [A, D, 20], [B, B, 20], [B, C, 1], [C, D, 4], [C, G, 15], [D, G, 9]]
    res2 = aStar(nodeList, nodeAdjList, S, G)
    for node in res2[0]:
        print(node.name)
        print("Total Path Cost: %d" % res2[1])
    print('\n')
    # Big graph, should find the goal with cost of 55
    F = Node('F', 6, 7)
    H = Node('H', 0, -1)
    J = Node('J', -2, -3)
    K = Node('K', 3, 2)
    L = Node('L', 1, 1)
    M = Node('M', 2, 1)
    N = Node('N', 100, 300)
    nodeList2 = [S, A, B, C, D, G, F, H, J, K, L, M, N]
    nodeAdjList2 = [[S, A, 9], [S, B, 8], [A, D, 20], [B, B, 20], [B, C, 1], [C, D, 4], [C, G, 15], [D, G, 9], [G, H, 3], [G, F, 7], [H, F, 4], [H, J, 2], [F, L, 15], [F, H, 21], [L, M, 9], [L, N, 11], [M, N, 2]]
    res3 = aStar(nodeList2, nodeAdjList2, S, N)
    for node in res3[0]:
        print(node.name)
        print("Total Path Cost: %d" % res3[1])
    # AI city dif start and end goals
    # should be cost of 15 C->F
    res4 = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST, AI_nodeC, AI_nodeF)
    print('\n')
    for node in res4[0]:
        print(node.name)
        print("Total Path Cost: %d" % res4[1])
if __name__ == "__main__": main()


    
