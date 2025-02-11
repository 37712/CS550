

from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem

class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, force_state = None, **kwargs):
        """"__init__(n, force_state, **kwargs)

        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.

        The parent's class constructor is then called with the TileBoard
        instance any any remaining arguments captured in **kwargs.

        """

        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments
        # into a dictionary.  The dictionary can be accessed like any other
        # dictionary, e.g. kwargs[“keyname”], or passed to another function
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).
        # calls Problem constructor and passes instance of Tileboard as the initial state
        super().__init__(TileBoard(n, force_state = force_state),
                         **kwargs)

    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        # check legal actions
        return state.get_actions()

    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        # to apply an action you need the move() function from tyle board, I think
        return state.move(action)

    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        # is state solved for the entire tileboard
        return state.solved()
