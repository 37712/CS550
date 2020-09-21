'''
Created on Feb 8, 2018

@author: mroch
'''
class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable"

    def __init__(self):
        "__init__() - Create an empty explored set"
        # we should use dict or list or set to store this info
        self.explored_map = dict()
        # __init__ should not return anything
        #raise NotImplemented

    def exists(self, state):
        """
        exists(state) - Has this state already been explored?
        :param state:  Hashable problem state
        :return: True if already seen, False otherwise4
        """
        # do we need to hash the state??? "hashable problem state"
        if(state in explored_map): return True
        else: return false
        #raise NotImplemented


    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        # do we hash the state? why?
        raise NotImplemented


