"""
Pair Programming Equitable Participation & Honesty Affidavit
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.



Pair Programmer 1 (print & sign your name, then date it)    Scott Sindewald 9/28/2020


Pair Programmer 2 (print & sign your name, then date it)    Carlos Gamino Reyes 9/28/2020

"""

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
verbose = False

def driver() :
    lengthOfPath = dict() # number of steps to solution for each search type
    numOfNodes = dict() # number of nodes expanded, we can put lists inside of the dict indexes
    timeElapsedSec = dict() # time elapsed for each of the seach methods for each of the puzzles
    t = Timer() # time of entire run

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

    print("#####SUMMARY PRINT OUT#####\n")

    # print path length summary
    print("\t\tBreadthFirst\n"
            "path length\tmean %.2f, std %.2f\n"
            % (mean(lengthOfPath[BreadthFirst]), stdev(lengthOfPath[BreadthFirst]))+
            "num of nodes\tmean %.2f, std %.2f\n"
            % (mean(numOfNodes[BreadthFirst]), stdev(numOfNodes[BreadthFirst]))+
            "time elapsed\tmean %.2f, std %.2f\n"
            % (mean(timeElapsedSec[BreadthFirst]), stdev(timeElapsedSec[BreadthFirst])))
    
    print("\t\tDepthFirst\n"
            "path length\tmean %.2f, std %.2f\n"
            % (mean(lengthOfPath[DepthFirst]), stdev(lengthOfPath[DepthFirst]))+
            "num of nodes\tmean %.2f, std %.2f\n"
            % (mean(numOfNodes[DepthFirst]), stdev(numOfNodes[DepthFirst]))+
            "time elapsed\tmean %.2f, std %.2f\n"
            % (mean(timeElapsedSec[DepthFirst]), stdev(timeElapsedSec[DepthFirst])))
    
    print("\t\tA* - Manhattan\n"
            "path length\tmean %.2f, std %.2f\n"
            % (mean(lengthOfPath[Manhattan]), stdev(lengthOfPath[Manhattan]))+
            "num of nodes\tmean %.2f, std %.2f\n"
            % (mean(numOfNodes[Manhattan]), stdev(numOfNodes[Manhattan]))+
            "time elapsed\tmean %.2f, std %.2f\n"
            % (mean(timeElapsedSec[Manhattan]), stdev(timeElapsedSec[Manhattan])))
    
    print("\ntime elapsed to solve all puzzles %dmin %dsec" % (t.elapsed_s()/60, t.elapsed_s()%60))

driver()
