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
        g = childnode.depth # cost for g is the depth of the search
        return g

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        h = 0 # cost for h is a constant. we chose 0
        return h

class DepthFirst:
    "DepthFirst - depth first search"

    @classmethod
    def g(cls, parentnode, action, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        g = 0 # cost for g is a constant. we chose 0
        return g

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        h = -searchnode.depth # cost for h is the negative depth of the search
        return h

class Manhattan:
    "Manhattan distance"
    # f is equal the total cost encountered (g) + the manhattan distance heuristic (h)
    @classmethod
    def g(cls, parentnode, action, childnode):
        "g - depth of the search with a transition cost of 2 applied at each transition"
        return childnode.depth * 2

    @classmethod
    def h(cls, searchnode):
        "h - heuristic value"
        goal_state = [1,2,3,4,5,6,7,8,None] # flattened state tuple of the goal state
        current_state = searchnode.state.state_tuple() # take the current node's flattened state tuple
        h=0 # initialize the distance to 0
        for goal_index, goal_value in enumerate(goal_state): # for every item in the goal_state
            for current_index, current_value in enumerate(current_state): # for every item in the current_state
                if goal_value == current_value: # if their values are the same
                    goal_col = int(goal_index%3) # the column number (range is 0 to 2) of the goal_index
                    goal_row = int((goal_index)/3) # the row number (range is 0 to 2) of the goal_index
                    current_col = int(current_index%3) # the column number (range is 0 to 2) of the current_index
                    current_row = int((current_index)/3) # the row number (range is 0 to 2) of the current_index
                    h += (abs(goal_col-current_col) + abs(goal_row-current_row)) # add the absolute vertical and horizontal distances
        return h # sum of the manhattan distances for each value in the node
