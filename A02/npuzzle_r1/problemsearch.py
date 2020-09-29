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
      uses a priority queue for the frontier and an instance of the Explored class for
      the explored set
      """

      # list of actions to solution
      t = Timer() # starts the timer
      frontier = PriorityQueue() # we are always going to have a frontier and we always need to put in to priority queue
      explored = Explored() # explored set, NOT REALLY A SET, it is a dictionary
      frontier.append(Node(problem, problem.initial)) # add initial node to the frontier
      solution = None
      i = 0 # used for debug and verbose purposes
      while(frontier.__len__() > 0):

            current = frontier.pop() # Dequeue current node

            if(debug == True and i % 100000 == 0):
                  print("############# %d #################" % i) # display iteration number
                  print(current.state) # display current node
                  print("nodes in frontier", frontier.__len__()) # display lenght of frontier set
                  print("time elapsed %dmin %dsec" % (t.elapsed_s()/60, t.elapsed_s()%60)) # display time elapsed

            explored.add(current.state) # add current state to explored

            if problem.goal_test(current.state): # if the current state is the goal

                  if debug: # used for debugging
                        print("###goal found, i = %d ###" % i) # display the iteration number for when the goal was found
                        print(current.state) # display current node
                        print("length", len(current.path())) # display current node path length
                        print("time elapsed %dmin %dsec" % (t.elapsed_s()/60, t.elapsed_s()%60)) # display time elapsed

                  solution = current # found goal and end loop
                  break

            else:
                  child_nodes = current.expand(problem) # expand the state to find child nodes

                  for child in child_nodes:
                        if not explored.exists(child.state): # if we haven't encountered the states yet
                              frontier.append(child) # add it to the frontier
                              explored.add(child.state) # add to explored to prevent duplication in frontier

            i = i + 1 # used for debug and verbose purposes

      if solution != None and verbose == True: # if we found a solution and want more detail
            solution_path = solution.path() # create list of nodes to solution
            num_moves = len(solution_path) - 1 # number of moves to goal
            print("############# %d #################" % i)
            print("Solution in ",num_moves," moves.\n") # heading of detail
            print("Intial state")
            print(solution_path[0]) # first state printed
            print("time elapsed %dmin %dsec" % (t.elapsed_s()/60, t.elapsed_s()%60)) # display time elapsed
            for i in range(1,len(solution_path)): # print each move in order
                  print("\nMove ", i, "") # display move number
                  print(solution_path[i]) # display move

      if solution == None: # no solution found
            print("no solution found")
            path = [] # if no solution found return empty list
            return(path, len(explored.explored_set), t.elapsed_s()) # return empty path, number of nodes explored and time elapsed
      else: # solution found
            return(solution.path(), len(explored.explored_set), t.elapsed_s()) # return solution path, number of nodes expanded and time
