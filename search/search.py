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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # We initialize the stack for the dfs algorithm
    stack = util.Stack()

    # The list of directions we will return
    ret = []

    """
    We create a list with the states that have been already expanded, so that we don´t repeat
    them in the algorithm. We add the first state which corresponds to the pacman position.
    """
    expanded = []
    state = problem.getStartState()
    expanded.append(state)

    """
    We create two dictionaries that store the parent state and the direction we came from
    for any state we use as a key. In this way, we can traceback our route once we reached the
    goal.
    """
    parent = {}
    direction = {}
    parent[state] = state
    direction[state] = None

    # We run the algorithm until we reach the goal
    while not problem.isGoalState(state):
        # We get all the successors that were not visited yet
        for successor in problem.getSuccessors(state):

            # We get the coordenates of the state to see if we have already expanded it
            childState = successor[0]
            if childState not in expanded:
                parent[childState] = state
                direction[childState] = successor[1]
                stack.push(childState)

        # We expand one succesor (only if it was never expanded before) to discover new states
        while state in expanded:
            # We check if the stack is empty. If it is, the goal was not found
            if stack.isEmpty():
                return None
            state = stack.pop()
        expanded.append(state)

    # We store in the list the direction of the path we took
    while parent[state] != state:
        ret.insert(0, direction[state])
        state = parent[state]

    return ret

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # We initialize the queue for the bfs algorithm
    queue = util.Queue()

    # The list of directions we will return
    ret = []

    """
    We create a list with the states that have been already expanded, so that we don´t repeat
    them in the algorithm. We add the first state which corresponds to the pacman position.
    """
    expanded = []
    state = problem.getStartState()
    expanded.append(state)

    """
    We create two dictionaries that store the parent state and the direction we came from
    for any state we use as a key. In this way, we can traceback our route once we reached the
    goal.
    """
    parent = {}
    direction = {}
    parent[state] = state
    direction[state] = None

    # We run the algorithm until we reach the goal
    while not problem.isGoalState(state):
        # We get all the successors that were not visited yet
        for successor in problem.getSuccessors(state):

            # We get the coordenates of the state to see if we have already expanded it
            childState = successor[0]
            if childState not in expanded:
                # If the child state has already a parent/direction, we don't overwrite them
                if childState not in parent.keys():
                    parent[childState] = state
                    direction[childState] = successor[1]
                queue.push(childState)

        # We expand one succesor (only if it was never expanded before) to discover new states
        while state in expanded:
            # We check if the queue is empty. If it is, the goal was not found
            if queue.isEmpty():
                return None
            state = queue.pop()
        expanded.append(state)

    # We store in the list the direction of the path we took
    while parent[state] != state:
        ret.insert(0, direction[state])
        state = parent[state]

    return ret

def uniformCostSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # We initialize the priority queue for the ucs algorithm
    queue = util.PriorityQueue()

    # The list of directions we will return
    ret = []

    """
    We create a list with the states that have been already expanded, so that we don´t repeat
    them in the algorithm. We add the first state which corresponds to the pacman position.
    """
    expanded = []
    state = problem.getStartState()
    expanded.append(state)

    """
    We create two dictionaries that store the parent state and the direction we came from
    for any state we use as a key. In this way, we can traceback our route once we reached the
    goal.
    """
    parent = {}
    accumulatedCost = {}
    direction = {}
    parent[state] = state
    accumulatedCost[state] = 0
    direction[state] = None

    # We run the algorithm until we reach the goal
    while not problem.isGoalState(state):
        # We get all the successors that were not visited yet
        for successor in problem.getSuccessors(state):

            # We get the coordenates of the state to see if we have already expanded it
            childState = successor[0]
            if childState not in expanded:
                # If the child state has already a parent/direction, we don't overwrite them
                if childState not in parent.keys():
                    accumulatedCost[childState] = accumulatedCost[state] + 1
                    parent[childState] = state
                    direction[childState] = successor[1]
                queue.push(childState, accumulatedCost[childState])

        # We expand one succesor (only if it was never expanded before) to discover new states
        while state in expanded:
            # We check if the queue is empty. If it is, the goal was not found
            if queue.isEmpty():
                return None
            state = queue.pop()
        expanded.append(state)

    # We store in the list the direction of the path we took
    while parent[state] != state:
        ret.insert(0, direction[state])
        state = parent[state]

    return ret

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
