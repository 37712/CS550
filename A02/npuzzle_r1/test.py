from basicsearch_lib02.timer import Timer
import time
from statistics import (mean, stdev)  # used for printing summary

class myClass(object):
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
        return hash(state) in self.explored_set

    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        # we use the hash as the index to save the state
        if(not self.exists(state)):
            self.explored_set[hash(state)] = state

def foo():
    return "hello", 123, "world"

def doo(x = False):
    return x

def eoo(**kwargs): # basically a dictionary
    return kwargs['q']

def goo(a,b,c):
    print(a)
    print(b)
    print(c)

"""
#######################################TEST#######################################
"""

def driver():
    """
    x,y,z =foo()
    print(x,y,z)

    print(doo())
    print(doo(100))

    print(eoo(a ="adsfasdf", o = 3245342, q = "hello master", z = 12431234))

    goo(c = 111, a = 222, b = 333)
        
    x = myClass()
    x.add("hello")
    x.exists("hello")
    
    t = Timer()
    while(True):
        print("%dmin %dsec" % (int(t.elapsed_s()/60), t.elapsed_s()%60))
        time.sleep(1)
    
    path = None
    assert path is not None
    """

    x = list()
    x.append(8)
    x.append(6)
    x.append(4)
    x.append(1)
    x.append(7)
    print(x)
    print(mean(x))
    print(stdev(x))

driver()