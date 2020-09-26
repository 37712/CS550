'''
Created on Feb 8, 2018

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        # we should use dict or list or set to store this info
        self.explored_set = dict()

    def exists(self, state):
        """
        exists(state) - Has this state already been explored?
        :param state:  Hashable problem state
        :return: True if already seen, False otherwise4
        """
        return state.__hash__() in self.explored_set

    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        # we use the hash as the index to save the state
        if(not self.exists(state)):
            self.explored_set[state.__hash__()] = state