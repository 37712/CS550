from lib import abstractstrategy, boardlibrary
import math
#import time

class AlphaBetaSearch:

    def __init__(self, strategy, maxplayer, minplayer, maxplies=6,
                 verbose=False):
        """"alphabeta_search - Initialize a class capable of alphabeta search
        problem - problem representation
        maxplayer - name of player that will maximize the utility function
        minplayer - name of player that will minimize the uitlity function
        maxplies- Maximum ply depth to search
        verbose - Output debugging information
        """
        self.strategy = strategy
        self.maxplayer = maxplayer
        self.minplayer = minplayer
        self.maxplies = maxplies # max depth of search strategy
        self.verbose = verbose

    # the state is a checkerboard state node
    def alphabeta(self, state):
        """
        Conduct an alpha beta pruning search from state
        :param state: Instance of the game representation
        :return: best action for maxplayer
        """

        # we use maxvalue and cutoff to get best action
        # [1] is the best action return value
        value, maxaction = self.maxvalue(state, -math.inf, math.inf, 0)

        return maxaction

    # this is used by both min and max values
    def cutoff(self, state, ply):
        """
        cutoff_test - Should the search stop?
        :param state: current game state
        :param ply: current ply (depth) in search tree
        :return: True if search is to be stopped (terminal state or cutoff
           condition reached)
        """
        # cut off condition
        if(self.maxplies == ply): return True
        # terminal state
        if(state.is_terminal()[0]): return True
        # continue search
        return False

    def maxvalue(self, state, alpha, beta, ply):
        """
        maxvalue - - alpha/beta search from a maximum node
        Find the best possible move knowing that the next move will try to
        minimize utility.
        :param state: current state
        :param alpha: lower bound of best move max player can make
        :param beta: upper bound of best move max player can make
        :param ply: current search depth
        :return: (value, maxaction)
        """
        value = -math.inf
        #print("here", value)
        #input()
        maxaction = None

        #if cut off
        if(self.cutoff(state, ply)):
            value = self.strategy.evaluate(state)

        else:
            for action in state.get_actions(self.maxplayer):

                # get temporary min value, [0] is the return value
                tmpValue = self.minvalue(state.move(action), alpha, beta, ply + 1)[0]

                # if better value
                if(tmpValue > value):
                    value = tmpValue
                    maxaction = action

                # if value is greater or equal to upper bound, prune
                if(value >= beta): break # skip the rest of the posible actions

                else: alpha = max(alpha, value) # new max value

        return value, maxaction

    def minvalue(self, state, alpha, beta, ply):
        """
        minvalue - alpha/beta search from a minimum node
        :param state: current state
        :param alpha:  lower bound on best move for min player
        :param beta:  upper bound on best move for max player
        :param ply: current depth
        :return: (v, minaction)  Value of min action and the action that
           produced it.
        """
        value = math.inf
        minaction = None

        #if cut off
        if(self.cutoff(state, ply)):
            value = self.strategy.evaluate(state)

        else:
            for action in state.get_actions(self.minplayer):
                # get temporary max value, [0] is the return value
                tmpValue = self.maxvalue(state.move(action), alpha, beta, ply + 1)[0]

                # if better value
                if(tmpValue < value):
                    value = tmpValue
                    minaction = action

                # if value is less or equal to lower bound, prune
                if(value <= alpha): break # skip the rest of the posible actions

                else: beta = max(beta, value) # new max value

        return value, minaction

class Strategy(abstractstrategy.Strategy):
    """Your strategy, maybe you can beat Tamara Tansykkuzhina,
       2019 World Women's Champion
    """

    def __init__(self, *args):
        """
        Strategy - Concrete implementation of abstractstrategy.Strategy
        See abstractstrategy.Strategy for parameters
        """

        super(Strategy, self).__init__(*args)

        self.search = \
            AlphaBetaSearch(self, self.maxplayer, self.minplayer,
                                   maxplies=self.maxplies, verbose=False)

    def play(self, board):
        """
        play(board) - Find best move on current board for the maxplayer
        Returns (newboard, action)
        """

        print(self.maxplayer,"thinking using ai.py strategy...")
        # use alpha beta search to find optimal move
        action = self.search.alphabeta(board)

        # if action is None then no action is possible
        # therefore you lose
        if(action == None): return board, None

        # create new board by applying the action
        newboard = board.move(action)

        return newboard, action

    # what is the utility of a state/checkerboard
    def evaluate(self, state, verbose = False):
        """
        evaluate - Determine utility of terminal state or estimated
        utility of a non-terminal state
        :param state: Game state
        :param turn: Optional turn (None to omit)
        :return:  utility or utility estimate based on strength of board
                  (bigger numbers for max player, smaller numbers for
                   min player)
        """

        utilityEstimate = 0
        # Pawns and Kings for each player
        if(self.maxplayer == 'r'):
            playerPawnCount = state.get_pawnsN()[0]
            opponentPawnCount = state.get_pawnsN()[1]
            playerKingCount = state.get_kingsN()[0]
            opponentKingCount =  state.get_kingsN()[1]
        else:
            playerPawnCount = state.get_pawnsN()[1]
            opponentPawnCount = state.get_pawnsN()[0]
            playerKingCount = state.get_kingsN()[1]
            opponentKingCount =  state.get_kingsN()[0]

        # create lists for both players containing the distance to king for each piece
        playerDistList = []
        opponentDistList = []
        playerEdgeCount = 0
        opponentEdgeCount = 0

        # iterate through each piece and identify pawns for turn player
        # or opponent. Then determine the distance to king for the piece and
        # append its distance to the appropriate list
        for row, col, piece in state:

            #print("player token {} at row={}, col={}".format(piece,row,col))
            piecePlayer, isKing = state.identifypiece(piece)
            #print("piece {}, king {}".format(piecePlayer,isKing))

            # if piece belongs to player (maxplayer)
            if(piecePlayer == state.playeridx(self.maxplayer)):

                # if piece is on the edge, and not a king
                if((col==0 or col==7) and not isKing):
                    playerEdgeCount += 1
                # if pawn
                if (not isKing):
                    playerDistList.append(state.disttoking(self.maxplayer, row))

            # if piece belongs to opponent (minplayer)
            else:
                # if piece is on the edge, and not a king
                if((col==0 or col==7) and not isKing):
                    opponentEdgeCount += 1
                # if pawn
                if(not isKing):
                    opponentDistList.append(state.disttoking(self.minplayer, row))

        # Min distance of all of the pawns to be king
        playerDistMin=0
        opponentDistMin=0
        if(len(playerDistList)>0):
            playerDistMin = min(playerDistList)
        if(len(opponentDistList)>0):
            opponentDistMin = min(opponentDistList)

        # Number of possible captures per action per player
        playerCaptureSum = 0
        opponentCaptureSum = 0
        # the length of the each move in move list will always be 1 value longer
        # than the total number of captures.
        # The standard length for the tuple at the second index in move is 2. When there is a possible
        # capture, the length of the tuple at the second index will be greater.
        for action in state.get_actions(self.maxplayer):
            # if element [1] length is greater than 2 then there is a capture
            if(len(action[1])>2):
                playerCaptureSum += len(action)-1 # -1 so that we only count captured pawns in that move

        for action in state.get_actions(self.minplayer):
            # if element [1] length is greater than 2 then there is a capture
            if(len(action[1])>2):
                opponentCaptureSum += len(action)-1 # -1 so that we only count captured pawns in that move



        '''
        #golden ratio, wins on regular board, decent weights
        pW = 2          # pawn weight
        kW = 5          # king weight
        minDW = 0.25    # min distance to king, for one piece
        capSW = 1       # capture sum wight
        eCW = 0.25      # edge count weight
        '''

        #golden ratio, wins almost always
        pW = 2          # pawn weight
        kW = 5          # king weight
        minDW = 0.25     # min distance to king, for one piece
        capSW = 1    # capture sum weight
        eCW = 0.25      # edge count weight

        # pawnCount, kingCount, min disttoking, captureSum, edgeCount
        playerEvaluation = playerPawnCount*pW + playerKingCount*kW - playerDistMin*minDW + \
                            playerCaptureSum*capSW + playerEdgeCount*eCW

        opponentEvaluation = opponentPawnCount*pW + opponentKingCount*kW - opponentDistMin*minDW + \
                            opponentCaptureSum*capSW + opponentEdgeCount*eCW


        if(verbose):
            print("playerEvaluation =", playerEvaluation, self.maxplayer)
            print(playerPawnCount*pW, playerKingCount*kW, -playerDistMin*minDW, playerCaptureSum*capSW, playerEdgeCount*eCW)

            print("opponentEvaluation =", opponentEvaluation, self.maxplayer)
            print(opponentPawnCount*pW, opponentKingCount*kW, -opponentDistMin*minDW, opponentCaptureSum*capSW, opponentEdgeCount*eCW)


        # positive if good for player, negative if bad for the player
        utilityEstimate = playerEvaluation - opponentEvaluation

        return utilityEstimate


# Run test cases if invoked as main module
if __name__ == "__main__":

    board = boardlibrary.boards["Pristine"]
    print(board)

    Player_1 = Strategy('r', board, 3)
    Player_2 = Strategy('b', board, 3)
    print("Player_1, red")
    Player_1.evaluate(board, True)
    print("\n\nPlayer_2, black")
    Player_2.evaluate(board, True)


    '''
    Player_1 = Strategy('r', board, 3)
    Player_2 = Strategy('b', board, 3)

    print(board)
    while(not board.is_terminal()[0]):

        print("RED TURN****************")
        Player_1 = Strategy('r', board, 3)
        (board, action) = Player_1.play(board)
        print("Red action", action)
        print(board)

        input()

        if(board.is_terminal()[0]): break

        print("BLACK TURN**************")
        Player_2 = Strategy('b', board, 3)
        (board, action) = Player_2.play(board)
        print("Black action", action)
        print(board)

        input()
    '''
    print("\nDONE")
