
explored_set = dict()

def exists(x):
    """
    exists(state) - Has this state already been explored?
    :param state:  Hashable problem state
    :return: True if already seen, False otherwise4
    """ 
    return hash(x) in explored_set

def add(state):
    """
    add(state) - Add a given state to the explored set
    :param state:  A problem state that is hashable, e.g. a tuple
    :return: None
    """
    # do we hash the state? why?
    if(not exists(state)):
        explored_set[hash(state)] = state

# this is our main
#print(hash("hello") in explored_set)

def foo():
    return "hello", 123, "world"

def doo(x = False):
    return x

def eoo(**kwargs):
    return kwargs['q']

"""
#######################################TEST#########################
"""

def driver():
    print(exists("hello"))
    add("hello")
    print(exists("hello"))

    x,y,z =foo()
    print(x,y,z)

    print(doo())
    print(doo(100))

    print(eoo(a ="adsfasdf", o = 3245342, q = "hello master", z = 12431234))

driver()