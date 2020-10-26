"""
Author: Carlos Gamino Reyes
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
import statistics, random
import ai_plus
import time
from lib import human, checkerboard, boardlibrary
from datetime import datetime
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
    #GoldenRatio = imp.load_compiled("GoldenRatio", "lib/__pycache__/GoldenRatio.cpython-{}{}.pyc".format(major, minor))

# Global variables
_title = None

# BEST WEIGHTS SO FAR
_pW = 0
_kW = 0
_minDW = 0
_capSW = 0
_eCW = 0

# test weights
pW = 0      # pawn weight
kW = 0      # king weight
minDW = 0   # min distance to king, for one piece
capSW = 0   # capture sum weight
eCW = 0     # edge count weight

# write new values to txt file
def write_values():
    global _title
    global pW, _pW
    global kW, _kW
    global minDW, _minDW
    global capSW, _capSW
    global eCW ,_eCW

    # append old weights to end of history file
    with open("values history.txt", "a") as txt: # you dont have to close it with this code, a is for append
        txt.write("\n")
        txt.write(_title)
        txt.write("_pW = "+str(_pW)+"\n_kW = "+str(_kW)+"\n_minDW = "+str(_minDW)+ \
                    "\n_capSW = "+str(_capSW)+"\n_eCW = "+str(_eCW)+"\n")

    # write new values to txt file
    _title = "# BEST WEIGHTS SO FAR " + datetime.now().strftime("%m/%d/%Y %H:%M:%S") + "\n"
    with open("values.txt", "w") as txt:
        txt.write(_title)
        txt.write("_pW = "+str(pW)+"\n_kW = "+str(kW)+"\n_minDW = "+str(minDW)+ \
                "\n_capSW = "+str(capSW)+"\n_eCW = "+str(eCW)+"\n")

# load values from txt file
def load_values():
    global _title
    global pW, _pW
    global kW, _kW
    global minDW, _minDW
    global capSW, _capSW
    global eCW ,_eCW

    file = open("values.txt")
    txt = file.readlines()
    if(len(txt) < 6): print("there is a problem with the values.txt file")
    _title = txt[0]
    _pW = float(txt[1].split(" = ")[1])
    _kW = float(txt[2].split(" = ")[1])
    _minDW = float(txt[3].split(" = ")[1])
    _capSW = float(txt[4].split(" = ")[1])
    _eCW = float(txt[5].split(" = ")[1])
    file.close()


# modify weights
def mod_weights():
    global pW, _pW
    global kW, _kW
    global minDW, _minDW
    global capSW, _capSW
    global eCW ,_eCW

    if(random.randint(0,1)):
        sing = 1
    else:
        sing = -1
    x = random.randint(0,4)
    ran = random.uniform(0,0.5)
    if(x == 0):pW += (sing * ran)
    elif(x == 1):kW += (sing * ran)
    elif(x == 2):minDW += (sing * ran)
    elif(x == 3):capSW += (sing * ran)
    else: eCW += (sing * ran)

# this is where the game actually starts
def AI_learn(maxplies=6, verbose=False):

    global pW, _pW
    global kW, _kW
    global minDW, _minDW
    global capSW, _capSW
    global eCW ,_eCW

    # load best values
    load_values()

    # set test values
    pW = _pW          # pawn weight
    kW = _kW          # king weight
    minDW = _minDW     # min distance to king, for one piece
    capSW = _capSW    # capture sum weight
    eCW = _eCW      # edge count weight

    # used to calculate utility of each run
    utilityValue = 0
    util_r = 0
    util_b = 0

    # needed for iteration count
    i = 0

    # run indefenitly
    while(True):

        # create the board
        board = checkerboard.CheckerBoard()

        # load specific board
        #board = boardlibrary.boards["Pristine"]

        print("\n############iteration,", i, "#############\n")
        print("Testing the following weights")
        print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW, "\n")

        # if ai_plus is first player
        if(i%2 == 0):
            red=ai_plus.Strategy('r', board, 6)
            black=tonto.Strategy('b', board, 6)
            # set weights
            red.setWeights(pW, kW, minDW, capSW, eCW)

        # else ai_plus is second player
        else:
            red=tonto.Strategy('r', board, 6)
            black=ai_plus.Strategy('b', board, 6)
            # set weights
            black.setWeights(pW, kW, minDW, capSW, eCW)

        # create players
        player_1 = red
        player_2 = black

        turnCount = 0

        if(verbose):
            print("\n****Initial Board****")
            print(board)

        # start time
        timeStart = time.time()

        winner = None

        # while the game is not finished
        while(True):
            
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
                winner = 'b'
            
            # if game has ended
            if(board.is_terminal()[0]):
                winner = board.is_terminal()[1]
                break

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
                winner = 'r'
            
            # if game has ended
            if(board.is_terminal()[0]):
                winner = board.is_terminal()[1]
                break

        # if ai is red
        if(i%2 == 0):

            # if ai won
            if(winner == 'r'): sing = 1
            # else ai lost
            else: sing = -1
            
            # calculate utility value
            util_r = sing * red.evaluate(board) - (turnCount*0.05)
            print("turncount =", turnCount)
            print(board,"util_r =", util_r)

            # time elapsed
            seconds = time.time() - timeStart
            print("\nTime elapsed: %dmin %dsec" % (int(seconds/60), int(seconds%60)))

            print("winner =", winner)

            # if weight's don't win
            if(sing == -1):
                print("BAD WEIGHTS, skipping black player test")
                print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW)

                # restore to previous values
                pW =_pW          # pawn weight
                kW = _kW          # king weight
                minDW = _minDW     # min distance to king, for one piece
                capSW = _capSW    # capture sum weight
                eCW = _eCW      # edge count weight

                # modify weights
                mod_weights()
                
                # i++ to skip this weight testing and start from scratch
                i+=1

        # else ai is black
        else:

            # if ai won
            if(winner == 'b'): sing = 1
            # else ai lost
            else: sing = -1

            # calculate utility value
            util_b = sing * black.evaluate(board) - (turnCount*0.05)
            print("turncount =", turnCount)
            print(board, "util_b =", util_b)
            
            # time elapsed
            seconds = time.time() - timeStart
            print("\nTime elapsed: %dmin %dsec" % (int(seconds/60), int(seconds%60)))
            
            print("winner =", winner)

            print("\nutil_r =", util_r)
            print("util_b =", util_b)
            util_avg = (util_r + util_b) / 2
            print("util_avg =", util_avg)

            # populate utilityValue of starting weights
            if(utilityValue == 0):
                print("\nInitial weights utility SET")
                utilityValue = util_avg

            # if better weights are found
            elif(util_avg > utilityValue and sing == 1):
                print("BETTER WEIGHTS FOUND")
                print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW)

                # write new weights in to txt file
                write_values()

                # save weights in to original and continue modifying
                _pW = pW          # pawn weight
                _kW = kW          # king weight
                _minDW = minDW     # min distance to king, for one piece
                _capSW = capSW    # capture sum weight
                _eCW = eCW      # edge count weight

                # modify weights
                mod_weights()
            
            # new weights are no good, return to original and modify weights
            else:
                print("BAD WEIGHTS")
                print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW)

                # reset test values to previous known good values
                pW =_pW          # pawn weight
                kW = _kW          # king weight
                minDW = _minDW     # min distance to king, for one piece
                capSW = _capSW    # capture sum weight
                eCW = _eCW      # edge count weight

                # modify weights
                mod_weights()

        # iteration counter
        i+=1

# defines where to start
if __name__ == "__main__":
    AI_learn()
    
        
        
        

        
                    
            
        

    
    
