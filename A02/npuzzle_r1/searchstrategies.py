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

class BreadthFirst:
    "BreadthFirst - breadth first search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
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
        h = -searchnode.depth
        return h

class Manhattan:
    "Manhattan distance"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """
        123
        456
        78.

        567
        328
        .41
        """
        return childnode.depth * 2

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        goal_state = [1,2,3,4,5,6,7,8,None]
        current_state = searchnode.state.state_tuple()
        h=0
        for goal_index, goal_value in enumerate(goal_state):
            for current_index, current_value in enumerate(current_state):
                if goal_value == current_value:
                    goal_col = int(goal_index%3)
                    goal_row = int((goal_index)/3)
                    current_col = int(current_index%3)
                    current_row = int((current_index)/3)
                    h += (abs(goal_col-current_col) + abs(goal_row-current_row))
        return h
        # Need to implement: find distance each value is from goal position and add up the distances
