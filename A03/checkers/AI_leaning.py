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
    #GoldenRatio = imp.load_compiled("GoldenRatio", "lib/__pycache__/GoldenRatio.cpython-{}{}.pyc".format(major, minor))


# this is where the game actually starts
def AI_learn(maxplies=6, verbose=False):
    # old best values
    #_pW = 2          # pawn weight
    #_kW = 5          # king weight
    #_minDW = 0.25     # min distance to king, for one piece
    #_capSW = 1    # capture sum weight
    #_eCW = 0.25      # edge count weight

    # BEST WEIGHTS SO FAR 10/22/2020
    _pW = 2 
    _kW = 4.563486995637862 
    _minDW = -0.20805803766397996 
    _capSW = 1.363555349866284 
    _eCW = -0.18493943623434173

    # test values
    pW =_pW          # pawn weight
    kW = _kW          # king weight
    minDW = _minDW     # min distance to king, for one piece
    capSW = _capSW    # capture sum weight
    eCW = _eCW      # edge count weight
    
    # used to calculate utility of each run
    utilityValue = 0
    util_r = 0
    util_b = 0

    i=0
    while(i<50):

        # create the board
        board = checkerboard.CheckerBoard()
        #board = boardlibrary.boards["Pristine"]

        print("\n\n############iteration,", i, "#############\n")
        print("Testing the following weights")
        print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW)

        # change strategy order
        if(i%2 == 0):
            red=ai_plus.Strategy('r', board, 6)
            black=tonto.Strategy('b', board, 6)
            red.setWeights(pW, kW, minDW, capSW, eCW)
        else:
            red=tonto.Strategy('r', board, 6)
            black=ai_plus.Strategy('b', board, 6)
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
                winner = 'b'
            
            
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

            winner = board.is_terminal()[1]
        
        # calculate utility value
        #utility
        #turns
        #win, louse, None
        # ai is red
        if(i%2 == 0):
            if(winner == 'r'):
                sing = 1
            else:
                sing = -1
            
            util_r = sing * red.evaluate(board) - int(turnCount*0.05)
            print("turncount =", turnCount)
            print(board,"util_r =", util_r)

            # time elapsed
            seconds = time.time() - timeStart
            print("\nTime elapsed: %dmin %dsec" % (int(seconds/60), int(seconds%60)))

            print("winner =", winner)

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
                
                # skip thiw weight testing and start from scratch
                i+=1

        
        # ai is black
        else:

            # if ai lost
            if(winner == 'b'):
                sing = 1
            else:
                sing = -1
            util_b = sing * black.evaluate(board) - int(turnCount*0.05)
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
                print("utility of initial weights SET")
                utilityValue = util_avg

            # if better weights are found
            elif(util_avg > utilityValue and sing == 1):
                print("BETTER WEIGHTS FOUND")
                print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW)

                # save weights in to original and continue modifying
                _pW =pW          # pawn weight
                _kW = kW          # king weight
                _minDW = minDW     # min distance to king, for one piece
                _capSW = capSW    # capture sum weight
                _eCW = eCW      # edge count weight

                # modify weights
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

            
            
            # new weights are no good, return to original and modify weights
            else:
                print("BAD WEIGHTS")
                print("pW =", pW, "\nkW =", kW, "\nminDW =", minDW, "\ncapSW =", capSW, "\neCW =", eCW)

                # test values
                pW =_pW          # pawn weight
                kW = _kW          # king weight
                minDW = _minDW     # min distance to king, for one piece
                capSW = _capSW    # capture sum weight
                eCW = _eCW      # edge count weight

                # modify weights
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

        i+=1
    
    print("BEST WEIGHTS SO FAR")
    print("_pW =",_pW, "\n_kW =", _kW, "\n_minDW =", _minDW, "\n_capSW =", _capSW, "\n_eCW =", _eCW)
    print("\n***DONE***")
    file2write=open("values",'w')
    file2write.write("here goes the data\n")
    file2write.write("_pW = "+str(_pW)+"\n_kW = "+str(_kW)+"\n_minDW = "+str(_minDW)+"\n_capSW = "+str(_capSW)+"\n_eCW = "+str(_eCW)+"\n")
    file2write.close()

if __name__ == "__main__":
    AI_learn()
    
        
        
        

        
                    
            
        

    
    
