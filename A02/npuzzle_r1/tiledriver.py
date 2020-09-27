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

numPuzzles = 3 #31 # number of puzzles
puzzleSize = 8 # size of puzzel, 8 will give us a 3x3 grid puzzle
searchType = [BreadthFirst, DepthFirst, Manhattan] # list of search methods


#used for configuration purposes
debug = False
vervose = False

def driver() :
    lengthOfPath = dict() # number of steps to solution for each search type
    numOfNodes = dict() # number of nodes expanded, we can put lists inside of the dict indexes
    timeElapsedSec = dict() # time elapsed for each of the seach methods for each of the puzzles

    # initialize dictionaries with list for every seach method
    for search in searchType:
        lengthOfPath[search] = list()
        numOfNodes[search] = list()
        timeElapsedSec[search] = list()

    # PROCESSING SOLUTIONS FOR PUZZLES
    for i in range(1,numPuzzles+1):

        print("puzzle number",i)

        for search in searchType:

            # prints out the name of the search trategy used to solve the puzzle
            print("solving with", search.__name__)

            # create the puzzle
            npuzzle = NPuzzle(puzzleSize, g = search.g, h = search.h)

            # solving the npuzzle
            # graph_search will return 3 values, the path, nodes explored, and elapsed time in seconds
            path, nodes_explored, elapsedtime = graph_search(npuzzle, debug=False, verbose=False)

            print("puzzle solved in %dmin %dsec"
                % (int(elapsedtime/60), elapsedtime%60))

            # appending the lenth of the path to the list
            lengthOfPath[search].append(len(path))

            # appending number of nodes explored
            numOfNodes[search].append(nodes_explored)

            # appending the time it took to solve
            timeElapsedSec[search].append(elapsedtime)

    # SUMMARY PRINT OUT SECTION
    
    print("#####SUMMARY PRINT OUT#####")
    print("\t\tBreadthFirst\t\t\tDepthFirst\t\t\tManhattan")
    
    # print path length summary
    print("path length\tmean %.2f, std %.2f\tmean %.2f, std %.2f\tmean %.2f, std %.2f\t" % (
        mean(lengthOfPath[BreadthFirst]), stdev(lengthOfPath[BreadthFirst]),
        mean(lengthOfPath[DepthFirst]), stdev(lengthOfPath[DepthFirst]),
        mean(lengthOfPath[Manhattan]), stdev(lengthOfPath[Manhattan])))

    # print number of nodes summary
    print("num of nodes\tmean %.2f, std %.2f\tmean %.2f, std %.2f\tmean %.2f, std %.2f\t" % (
        mean(numOfNodes[BreadthFirst]), stdev(numOfNodes[BreadthFirst]),
        mean(numOfNodes[DepthFirst]), stdev(numOfNodes[DepthFirst]),
        mean(numOfNodes[Manhattan]), stdev(numOfNodes[Manhattan])))

    # print time elapsed summary
    print("time elapsed\tmean %.2f, std %.2f\tmean %.2f, std %.2f\tmean %.2f, std %.2f\t" % (
        mean(timeElapsedSec[BreadthFirst]), stdev(timeElapsedSec[BreadthFirst]),
        mean(timeElapsedSec[DepthFirst]), stdev(timeElapsedSec[DepthFirst]),
        mean(timeElapsedSec[Manhattan]), stdev(timeElapsedSec[Manhattan])))

driver()
