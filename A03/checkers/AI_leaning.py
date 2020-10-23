"""
Pair Programming Equitable Participation & Honesty Affidavit
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.


Pair Programmer 1 (print & sign your name, then date it)    Scott Sindewald 10/18/2020


Pair Programmer 2 (print & sign your name, then date it)    Carlos Gamino Reyes 10/18/2020
"""

# Game representation and mechanics

# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.7 and 3.8 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.
import statistics
import ai
import time, datetime
from lib import human, checkerboard, boardlibrary 
#from lib import tonto

# Python can load compiled modules using the imp module (deprecated)
# We'll format the path to the tonto module based on the
# release of Python.  Note that we provided tonto compilations for Python 3.7
# and 3.8.  If you're not using one of these, it won't work.
if True:
    import imp
    import sys
    major = sys.version_info[0]
    minor = sys.version_info[1]
    modpath = "lib/__pycache__/tonto.cpython-{}{}.pyc".format(major, minor)
    tonto = imp.load_compiled("tonto", modpath)
    GoldenRatio = imp.load_compiled("GoldenRatio", "lib/__pycache__/GoldenRatio.cpython-{}{}.pyc".format(major, minor))


# this is where the game actually starts
def Game(
         maxplies=6, init=None, verbose=True, firstmove=0):
    """Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 

    Returns winning player 'r' or 'b'
    """
    for(i=0; i<40; i+=1)

        red=ai.Strategy, black=tonto.Strategy, verbose=False))
        red=tonto.Strategy, black=ai.Strategy, verbose=False))

        # create the board
        board = checkerboard.CheckerBoard()
        #board = boardlibrary.boards["Pristine"]

        # create players
        player_1 = red('r', board, maxplies, False)
        player_2 = black('b', board, maxplies, False)

        turnCount = 0

        if(verbose):
            print("\n****Initial Board****")
            print(board)

        # Note start time
        timeStart = time.time()

        # while the game is not finished
        while(not board.is_terminal()[0]):
            
            ##### first player's turn #####
            turnCount += 1
            if(verbose):print("\n****player_1, turn",turnCount,"****")
            # get new board and best move/action
            board, action = player_1.play(board)
            if(verbose):
                print(board, action)
                print("player 1 evaluate =", player_1.evaluate(board))
                print("player 2 evaluate =", player_2.evaluate(board))
            if(action == None):
                if verbose: print("Player_1 is Forfeit")
                return 'b'
            
            if(board.is_terminal()[0]):break

            ##### second player's turn #####
            turnCount += 1
            if(verbose):print("\n****player_2, turn",turnCount,"****")
            # get new board and best move/action
            board, action = player_2.play(board)
            if(verbose):
                print(board, action)
                print("player 1 evaluate =", player_1.evaluate(board))
                print("player 2 evaluate =", player_2.evaluate(board))
            if(action == None):
                if verbose: print("Player_2 is Forfeit")
                return 'r'

        ''' not working yet
        if(verbose):
            seconds = datetime.timedelta(seconds=(time.time()-timeStart)).total_seconds
            print("\ntime elapsed to solve all puzzles %dmin %dsec" % (seconds/60, seconds%60))
        '''
    print(board, turnCount)
    return  board.is_terminal()[1] # returns winner

if __name__ == "__main__":

    # my test
    #print(Game(red=ai.Strategy, black=tonto.Strategy, verbose=False))
    #print(Game(red=tonto.Strategy, black=ai.Strategy, verbose=False))
    #print(Game(red=ai.Strategy, black=ai.Strategy, maxplies=6))
    #print(Game(red=tonto.Strategy, black=tonto.Strategy, maxplies=6))
    #print(Game(red=human.Strategy, black=ai.Strategy, maxplies=6))
    #print(Game(red=ai.Strategy, black=human.Strategy, maxplies=6))
    #print(Game(red=GoldenRatio.Strategy, black=tonto.Strategy, maxplies=6))

    #Play with default strategies...
    Game()
        
        
        

        
                    
            
        

    
    
