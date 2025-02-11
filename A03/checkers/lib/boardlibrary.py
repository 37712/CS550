'''
Created on Mar 1, 2015

@author: mroch
'''
import copy
from lib import checkerboard
#import checkerboard

boards = dict()

def init_boards():
    """Set up a library of board positions for test purposes
    WARNING:  Some components of the checkers program rely on this library
    for testing.  Changing board configurations will result in breakage of
    tests if the tests are not updated.  Adding new tests is fine.
    """


    # Initial board
    boards["Pristine"] = checkerboard.CheckerBoard()

    # Set up for two red single hops
    #           0  1  2  3  4  5  6  7
    #        0  .  b  .  b  .  b  .  b
    #        1  b  .  b  .  b  .  b  .
    #        2  .  b  .  .  .  .  .  b
    #        3  .  .  .  .  .  .  b  .
    #        4  .  .  .  b  .  .  .  r
    #        5  r  .  r  .  r  .  .  .
    #        6  .  r  .  r  .  r  .  r
    #        7  r  .  r  .  r  .  r  .
    b = checkerboard.CheckerBoard()
    b.place(2, 3, None)
    b.place(2, 5, None)
    b.place(3, 6, 'b')
    b.place(4, 3, 'b')
    b.place(5, 6, None)
    b.place(4, 7, 'r')
    b.recount_pieces()  # Update pawn/king counts

    boards["SingleHopsRed"] = b

    # Set up for black single hops
    #     0  1  2  3  4  5  6  7
    #  0  .  b  .  b  .  b  .  b
    #  1  b  .  b  .  b  .  b  .
    #  2  .  b  .  .  .  .  .  b
    #  3  .  .  .  .  .  .  r  .
    #  4  .  .  .  b  .  .  .  r
    #  5  r  .  r  .  r  .  .  .
    #  6  .  .  .  r  .  r  .  r
    #  7  r  .  r  .  r  .  r  .
    b = copy.deepcopy(b)
    b.place(6, 1, None)
    b.place(3, 6, 'r')
    b.recount_pieces()  # Update pawn/king counts
    boards["SingleHopsBlack"] = b

    # multihop
    #     0  1  2  3  4  5  6  7
    #  0  .  b  .  b  .  b  .  b
    #  1  b  .  r  .  b  .  .  .
    #  2  .  r  .  .  .  b  .  b
    #  3  .  .  .  .  .  .  .  .
    #  4  .  .  .  r  .  b  .  .
    #  5  .  .  .  .  .  .  r  .
    #  6  .  r  .  r  .  r  .  r
    #  7  r  .  .  .  r  .  .  .
    b = checkerboard.CheckerBoard()
    b.place(7, 2, None)
    b.place(7, 6, None)
    b.place(5, 0, None)
    b.place(5, 2, None)
    b.place(5, 4, None)
    b.place(4, 3, 'r')
    b.place(4, 5, 'b')
    b.place(2, 1, 'r')
    b.place(2, 3, None)
    b.place(1, 2, 'r')
    b.place(1, 6, None)
    b.recount_pieces()  # Update pawn/king counts
    boards["multihop"] = b


    # KingBlack
    # Black can move to become a King but should
    # not be able to move after being kinged
    #    0  1  2  3  4  5  6  7
    #    0  .  .  .  .  .  .  .  .
    #    1  .  .  .  .  .  .  .  .
    #    2  .  .  .  .  .  .  .  .
    #    3  .  .  .  .  b  .  .  .
    #    4  .  .  .  r  .  r  .  .
    #    5  .  .  .  .  .  .  .  .
    #    6  .  .  .  r  .  r  .  .
    #    7  .  .  .  .  .  .  .  .
    b  = checkerboard.CheckerBoard()
    b.clearboard()
    # Set up for tour by black
    b.place(3, 4, 'b')  # pawn that will be making partial tour
    b.place(4, 3, 'r')
    b.place(6, 3, 'r')  # king black after this jump
    b.place(6, 5, 'r')  # or this one depending on path
    b.place(6, 5, 'r')
    b.place(4, 5, 'r')
    b.recount_pieces()  # Update pawn/king counts
    boards["KingBlack"] = b

    # BlackKingTour
    #    0  1  2  3  4  5  6  7
    #    0  .  .  .  .  .  .  .  .
    #    1  .  .  .  .  .  .  .  .
    #    2  .  .  .  .  .  .  .  .
    #    3  .  .  .  .  B  .  .  .
    #    4  .  .  .  r  .  r  .  .
    #    5  .  .  .  .  .  .  .  .
    #    6  .  .  .  r  .  r  .  .
    #    7  .  .  .  .  .  .  .  .
    b = copy.deepcopy(b)
    b.place(3, 4, 'B')  # king that will make tour
    b.recount_pieces()
    boards["BlackKingTour"] = b

    # RedKingTour
    # Probably don't need to test this one as rules similar, but...
    #    0  1  2  3  4  5  6  7
    #    0  .  .  .  .  .  .  .  .
    #    1  .  .  .  .  .  .  .  .
    #    2  .  .  .  .  .  .  .  .
    #    3  .  .  .  .  R  .  .  .
    #    4  .  .  .  b  .  b  .  .
    #    5  .  .  .  .  .  .  .  .
    #    6  .  .  .  b  .  b  .  .
    #    7  .  .  .  .  .  .  .  .
    b = copy.deepcopy(b)
    b.place(3, 4, 'R')  # pawn that will be making partial tour
    b.place(4, 3, 'b')
    b.place(6, 3, 'b')  # king red after this jump
    b.place(6, 5, 'b')  # or this one depending on path
    b.place(6, 5, 'b')
    b.place(4, 5, 'b')
    b.recount_pieces()
    boards["RedKingTour"] = b

    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(0, 1, 'b')
    b.place(0, 7, 'b')
    b.place(1, 6, 'r')
    b.place(2, 1, 'r')
    b.place(2, 3, 'b')
    b.place(2, 5, 'b')
    b.place(4, 3, 'r')
    b.place(5, 4, 'r')
    b.place(6, 1, 'b')
    b.place(6, 3, 'r')
    b.recount_pieces()
    boards["StrategyTest1"] = b

    # EndGame 1 - Red can easily win
    #       0  1  2  3  4  5  6  7
    #    0     .     .     R     b
    #    1  .     .     .     .
    #    2     .     .     .     .
    #    3  .     .     .     .
    #    4     .     .     .     .
    #    5  .     .     .     .
    #    6     .     .     .     R
    #    7  .     .     .     .
    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(6,7, 'R')
    b.place(0,5, 'R')
    b.place(0,7, 'b')
    b.recount_pieces()
    boards["EndGame1"] = b

    # Endgame 2 - Black can easily win

    #    0  1  2  3  4  5  6  7
    # 0     .     .     .     b
    # 1  .     .     .     .
    # 2     .     .     .     .
    # 3  .     .     .     .
    # 4     .     .     .     .
    # 5  .     B     .     .
    # 6     .     .     .     .
    # 7  .     r     .     .

    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(7,2, 'r')
    b.place(5,2, 'B')
    b.place(0,7, 'b')
    b.recount_pieces()
    boards["EndGame2"] = b

    # Red has won

    #    0  1  2  3  4  5  6  7
    # 0     .     .     .     .
    # 1  .     .     .     .
    # 2     r     .     .     .
    # 3  .     .     .     .
    # 4     .     .     .     R
    # 5  .     r     .     .
    # 6     .     .     .     .
    # 7  .     .     .     .
    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(5,2, 'r')
    b.place(2,1, 'r')
    b.place(4,7, 'R')
    boards['RedWins'] = b

    # Black has won
    #    0  1  2  3  4  5  6  7
    # 0     b     .     b     .
    # 1  .     .     .     .
    # 2     .     .     .     .
    # 3  .     .     .     .
    # 4     .     .     .     .
    # 5  .     .     B     B
    # 6     .     .     .     .
    # 7  .     .     .     .
    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(0,1, 'b')
    b.place(0,5, 'b')
    b.place(5,6, 'B')
    b.place(5,4, 'B')
    boards['BlackWins'] = b

    # Test 1

    #    0  1  2  3  4  5  6  7
    # 0     .     .     .     .
    # 1  .     .     .     .
    # 2     .     .     .     .
    # 3  b     .     .     .
    # 4     .     .     .     .
    # 5  .     .     .     .
    # 6     .     .     .     .
    # 7  R     R     .     .

    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(3,0,'b')
    b.place(7,0,'R')
    b.place(7,2,'R')
    b.recount_pieces()
    boards["Test1"] = b

    # Test 2

    #    0  1  2  3  4  5  6  7
    # 0     .     .     .     .
    # 1  .     .     .     .
    # 2     .     .     .     .
    # 3  .     .     .     .
    # 4     .     .     .     .
    # 5  .     .     .     .
    # 6     .     b     .     .
    # 7  .     r     r     .

    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(7,4,'r')
    b.place(7,2,'r')
    b.place(6,3,'b')
    b.recount_pieces()
    boards["Test2"] = b

    # Test 3

    #    0  1  2  3  4  5  6  7
    # 0     b     b     b     b
    # 1  r     r     r     r
    # 2     .     r     r     r
    # 3  r     .     .     .
    # 4     .     .     .     .
    # 5  .     .     .     .
    # 6     .     .     .     .
    # 7  .     .     .     .

    b = checkerboard.CheckerBoard()
    b.clearboard()
    b.place(0,1,'b')
    b.place(0,3,'b')
    b.place(0,5,'b')
    b.place(0,7,'b')
    b.place(1,0,'r')
    b.place(1,2,'r')
    b.place(1,4,'r')
    b.place(1,6,'r')
    b.place(3,0,'r')
    b.place(2,3,'r')
    b.place(2,5,'r')
    b.place(2,7,'r')
    b.recount_pieces()
    boards["Test3"] = b


    # Draw
    # Black is in a good position, but there have been too many moves
    # since the last capture.
    b = boards['KingBlack']
    b = copy.deepcopy(b)
    # advance the move past the draw threshold, no captures will have been
    # reported as we advanced this artificially
    b.movecount += b.drawthreshN + 1
    boards['Draw'] = b


init_boards()
