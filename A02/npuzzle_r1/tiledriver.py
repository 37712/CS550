'''
driver for graph search problem

'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections

numPuzzles = 31 # number of puzzles
puzzleSize = 8 # size of puzzel, 8 will give us a 3x3 grid puzzle
searchType = [BreadthFirst, DepthFirst, Manhattan] # list of search methods


#used for configuration purposes
debug = False
vervose = False

def driver() :
    numOfNodes = dict() # number of nodes expanded, we can put lists inside of the dict indexes
    timeElapsedMin = dict() # time elapsed for each of the seach methods for each of the puzzles
    timeElapsedSec = dict() # time elapsed for each of the seach methods for each of the puzzles

    # initialize dictionaries with list for every seach method
    for method in searchType:
        numOfNodes[method] = list()
        timeElapsedMin[method] = list()
        timeElapsedSec[method] = list()

    for i in range(numPuzzles):

        print("puzzle number",i)

        for search in searchType:

            # prints out the name of the search trategy used to solve the puzzle
            print("solving with", search.__name__)

            #create the puzzle
            npuzzle = NPuzzle(puzzleSize, search.g, search.h)

            #path, nodes_explored, timeElapsedSec[search] = graph_search(npuzzle, debug=False, verbose=False)

            

            



driver()
