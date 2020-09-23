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
        return hash(state) in explored_set

    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        # do we hash the state? why?
        if(not exists(state)):
            explored_set[hash(state)] = state
