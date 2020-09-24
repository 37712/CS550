'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from explored.py import *

from explored import Explored


def graph_search(problem, verbose=False, debug=False):
      """graph_search(problem, verbose, debug) - Given a problem representation
      (instance of basicsearch_lib02.representation.Problem or derived class),
      attempt to solve the problem.

      If debug is True, debugging information will be displayed.

      if verbose is True, the following information will be displayed:

      Number of moves to solution
      List of moves and resulting puzzle states
      Example:

            Solution in 25 moves
            Initial state
                  0        1        2
            0     4        8        7
            1     5        .        2
            2     3        6        1
            Move 1 -  [0, -1]
                  0        1        2
            0     4        8        7
            1     .        5        2
            2     3        6        1
            Move 2 -  [1, 0]
                  0        1        2
            0     4        8        7
            1     3        5        2
            2     .        6        1

            ... more moves ...

                  0        1        2
            0     1        3        5
            1     4        2        .
            2     6        7        8
            Move 22 -  [-1, 0]
                  0        1        2
            0     1        3        .
            1     4        2        5
            2     6        7        8
            Move 23 -  [0, -1]
                  0        1        2
            0     1        .        3
            1     4        2        5
            2     6        7        8
            Move 24 -  [1, 0]
                  0        1        2
            0     1        2        3
            1     4        .        5
            2     6        7        8

      If no solution were found (not possible with the puzzles we
      are using), we would display:

      No solution found

      Returns a tuple (path, nodes_explored, elapsed_s) where:
      path - list of actions to solve the problem or None if no solution was found
      nodes_explored - Number of nodes explored (dequeued from frontier)
      elapsed_s is the elapsed wall clock time performing the search
      """
      """
      need to print each state,
      need to provide debugging information
      use search information and priority queue to solve problem
      """
      # list of actions to solution
      t = Timer() # starts the timer
      frontier = PriorityQueue() # we are always going to have a frontier and we always need to put in to priority queue
      explored = Explored() # explored set
      # need to dequeue and add child nodes to queue
      frontier.append(problem.initial)
      while(frontier.__len__()!=0):
          current = frontier.pop()
          explored.add(current) # add initial state to explored
          if problem.goal_test(current): # if the initial state is the goal
            return(current.path(), explored.len(), t) # return path size 0, explored size 1, and time elapsed
          actions = current.get_actions()

      path = [] # no solution found
      return(path, explored.len(), t) # return empty path, number of nodes explored and time elapsed


      #frontier.append(problem.initial) # add the first state to the queue

      # we need to return 3 things path, nodes_explored, elapsed_s
      #return ???
