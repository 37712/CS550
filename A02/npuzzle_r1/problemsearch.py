'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
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
      explored = Explored() # explored set, NOT REALLY A SET
      # need to dequeue and add child nodes to queue
      root = Node(problem, problem.initial)
      frontier.append(root)
      done = False
      optimal = None
      path = []
      i = 0
      length = 0
      while(done == False):

            current = frontier.pop() # Dequeue current node
            #print(current)

            if(debug == True and i % 100000 == 0):
                  print("############# %d #################" % i)
                  print(current.state)
                  print("length", frontier.__len__())
            
            explored.add(current.state) # add current state to explored

            if problem.goal_test(current.state): # if the current state is the goal

                  if optimal == None: # no solution found yet
                        optimal = current # the only solution so far is the most optimal
                  elif len(current.path()) < len(optimal.path()): # if the path length is shorter than that of the optimal one
                        optimal = current # the current solution is the optimal one so far

                  if debug: # used for debugging
                        print("###goal found, i = %d ###" % i)
                        print(current.state) # display current node
                        print("length", len(current.path()))
                  
                  if verbose:
                        print("############# %d #################" % i)
                        for node in current.path():
                              print(node)
                        input()
                                    
            else:
                  child_nodes = current.expand(problem) # expand the state to find child nodes

                  for child in child_nodes:
                        if not explored.exists(child.state): # if we haven't encountered the states yet
                              frontier.append(child) # add them to the frontier
            
            done = frontier.__len__() == 0 # If all out of states to explore, end loop
            i = i + 1
            if(frontier.__len__() > length): length = frontier.__len__()

      if debug == True: # used for debugging
            print(optimal) # display current node
            print("length", len(optimal.path()))
            print("iterations =",i)

      if optimal != None and verbose == True: # if we found a solution and want more detail
            solution_path = optimal.path() # create list of nodes to solution
            num_moves = len(solution_path) # number of moves to goal
            print("Solution in ",num_moves," moves.\n") # heading of detail
            print("Intial state\n")
            print(solution_path[0],"\n") # first state printed
            for i in range(1,len(solution_path)): # print each move in order
                  print("Move ", i, "\n")
                  print(solution_path[i])
      if optimal == None: # no solution found
            return(path, len(explored.explored_set), t.elapsed_s()) # return empty path, number of nodes explored and time elapsed
      else: # solution found
            return(optimal.path(), len(explored.explored_set), t.elapsed_s()) # return solution path, number of nodes expanded and time
