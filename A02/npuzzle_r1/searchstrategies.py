"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."

        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the center, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state.
"""

import math
from basicsearch_lib02.searchrep import *
from basicsearch_lib02.tileboard import *

class BreadthFirst:
    "BreadthFirst - breadth first search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        # maybe we need get_g and get_h from seachrep/node
        #g = childnode.get_g()
        #g = len(childnode.path())
        g = childnode.depth
        return g

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        h = 0
        return h

class DepthFirst:
    "DepthFirst - depth first search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        g = 0
        return g

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        #h = -childnode.get_h()
        #h = -len(childnode.path())
        h = -searchnode.depth
        return h

class Manhattan:
    "Manhattan distance"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """
        123
        456
        78
        """
        return childnode.depth

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        """
        goal_state = [1,2,3,4,5,6,7,8,None]
        flattened_state = state.state_tuple()
        #for value in goal_state:
        # Need to implement: find distance each value is from goal position and add up the distances
        """

# To complete:
# Write two more classes, DepthFirst and Manhattan
# that support appropriate g/h with the same signatures for the class functions