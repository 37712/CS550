'''
driver for graph search problem

'''

from statistics import (mean, stdev)  # used for printing summary

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections

numPuzzles = 1 #31 # number of puzzles
puzzleSize = 8 # size of puzzel, 8 will give us a 3x3 grid puzzle, 3 will give us a 2x2 puzzle
searchType = [BreadthFirst, DepthFirst, Manhattan] # list of search methods


#used for configuration purposes
debug = True
vervose = True

def driver() :

    lengthOfPath = list()
    numOfNodes = list()
    timeElapsedSec = list()

    # PROCESSING 
    search = Manhattan

    # create the puzzle
    npuzzle = NPuzzle(puzzleSize, g = search.g, h = search.h)

    # solving the npuzzle
    # graph_search will return 3 values, the path, nodes explored, and elapsed time in seconds
    path, explored, elapsedtime = graph_search(npuzzle, debug=debug, verbose=vervose)

    print("puzzle solved in %dmin %dsec" % (elapsedtime/60, elapsedtime%60))

    # appending the lenth of the path to the list
    lengthOfPath.append(len(path))

    # appending number of nodes explored
    numOfNodes.append(explored)

    # appending the time it took to solve
    timeElapsedSec.append(elapsedtime)

driver()