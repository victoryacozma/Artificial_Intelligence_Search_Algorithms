# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import pacman
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def IterativeDeepeningDepthFirstSearch(problem):
    stiva=util.Stack()
    limit=1
    from game import Directions
    while True:
        visited=[]
        startState=problem.getStartState()
        stiva.push((startState,[],0))
        
        currentState , actions ,TotalCost = stiva.pop()
        visited.append(currentState)
        while not problem.isGoalState(currentState):
            successors = problem.getSuccessors(currentState)
            for newState,newAction,newCost in successors:
                if (not newState in visited and TotalCost+newCost<=limit):
                    stiva.push((newState,actions+ [newAction],TotalCost+newCost))
                    visited.append(newState)
            if stiva.isEmpty():
                break
            currentState , actions ,TotalCost = stiva.pop()
        if problem.isGoalState(newState):
            return actions
        limit+=1

def depthLimitedSearch(problem):
    begin = problem.getStartState()
    c = problem.getStartState()
    visited = []
    # visited.append(begin)
    stiva = util.Queue()
    limit=1000
    depth=0
    stiva.push((begin , []))
    while not stiva.isEmpty() :
        if depth<=limit:
            pozitie, final = stiva.pop()
            if problem.isGoalState(pozitie):
                return final
            visited.append(pozitie)
            vecini = problem.getSuccessors(pozitie)
            for i in vecini:
                nod = i[0]
                if not nod in visited:
                    c = i[0]
                    directie = i[1]
                    stiva.push((nod, final + [directie]))
        depth+=1
    return final + [directie]
    #  util.raiseNotDefined()

def depthFirstSearch(problem):
    begin = problem.getStartState()
    c = problem.getStartState()
    visited = []
    stiva = util.Queue()
    stiva.push((begin , []))
    while not stiva.isEmpty() and not problem.isGoalState(c):
        pozitie, final = stiva.pop()
        visited.append(pozitie)
        vecini = problem.getSuccessors(pozitie)
        for i in vecini:
            nod = i[0]
            if not nod in visited:
                c = i[0]
                directie = i[1]
                stiva.push((nod, final + [directie]))
    return final + [directie]
    #  util.raiseNotDefined()

def breadthFirstSearch(problem):
    begin = problem.getStartState()
    c = problem.getStartState()
    visited = []
    # visited.append(begin)
    stiva = util.Queue()
    stiva.push((begin , []))
    while not stiva.isEmpty() and not problem.isGoalState(c):
        pozitie, final = stiva.pop()
        visited.append(pozitie)
        vecini = problem.getSuccessors(pozitie)
        for i in vecini:
            nod = i[0]
            if not nod in visited:
                c = i[0]
                directie = i[1]
                stiva.push((nod, final + [directie]))
    return final + [directie]

def uniformCostSearch(problem):
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    priorityQueue = util.PriorityQueue()
    visited = []

    priorityQueue.push((startingNode,[],0),0) # push starting point with priority num of 0

    while not priorityQueue.isEmpty():
        currentNode, direction, cost = priorityQueue.pop()

        if currentNode not in visited:
            visited.append(currentNode)

            if problem.isGoalState(currentNode):
                return direction

            for newNode, newDirection, newCost in problem.getSuccessors(currentNode):
                    actions=direction + [newDirection]
                    priority = cost + newCost
                    priorityQueue.push((newNode, actions, priority),priority)
    return direction
  

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic):
   
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    priorityQueue = util.PriorityQueue()
    #((coordinate/node , action to current node , cost to current node),priority)
    visited = []
    priorityQueue.push((startingNode, [], 0), 0)
    
    while not priorityQueue.isEmpty():
        currentNode, direction, cost = priorityQueue.pop()
        
        if currentNode not in visited:
            visited.append(currentNode)

            if problem.isGoalState(currentNode):
                return direction

            for newNode, newDirection, newCost in problem.getSuccessors(currentNode):
                actions=direction + [newDirection]
                totalCost = cost + newCost
                heuristicCost = totalCost + heuristic(newNode,problem)
                priorityQueue.push((newNode, actions, totalCost),heuristicCost)

    return direction
    util.raiseNotDefined()
def distantaEuclidiana(position, position2):
    "The Euclidean distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = position2
    return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5

def sort (v,node):
    vec=[]
    t=0
    import searchAgents
    for k in range(len(v)):
        # print v[k]
        vec.append(distantaEuclidiana(v[k],node))
        t=t+1
    min = vec[0]
    j=0
    for i in range(len(vec)):
        if vec[i]<min:
            min=vec[i]
            j=i
    return j


        
        

        
def suma (a,b):

    m,n=a
    x,y=b
    return (m+x,n+y)
def search(problem, heuristic=nullHeuristic):
   
    startingNode = problem.getStartState()
    
    priorityQueue = util.PriorityQueue()
    visited = []
    priorityQueue.push((startingNode, [], 0), 0)
    
    while not priorityQueue.isEmpty():
        currentNode, direction, cost = priorityQueue.pop()
        
        if currentNode not in visited:
            visited.append(currentNode)


            if problem.isGoalState(currentNode):

                return direction

            for newNode, newDirection, newCost  in problem.getSuccessors(currentNode):
                actions=direction + [newDirection]
                totalCost = cost + newCost
                heuristicCost = totalCost + heuristic(newNode,problem)
                priorityQueue.push((newNode, actions, totalCost),heuristicCost)

    return direction
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
dls = depthLimitedSearch
iddfs = IterativeDeepeningDepthFirstSearch
