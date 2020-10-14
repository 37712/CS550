from lib import abstractstrategy, boardlibrary
import math


class AlphaBetaSearch:
    
    def __init__(self, strategy, maxplayer, minplayer, maxplies=3, 
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
        return self.maxvalue(state, -math.inf, math.inf, 0)[1]
    
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
        if(state.is_terminal()): return True
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
        if(self.cutoff(state, ply)): value = self.strategy.evaluate(state)

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
        action = self.search.alphabeta(board)

        # if action is None then
        if(action == None): return board, None

        newboard = board.move(action)
        return newboard, action
    
    # what is the utility of the state/checkerboard
    def evaluate(self, state, turn = None):
        """
        evaluate - Determine utility of terminal state or estimated
        utility of a non-terminal state
        :param state: Game state
        :param turn: Optional turn (None to omit)
        :return:  utility or utility estimate based on strengh of board
                  (bigger numbers for max player, smaller numbers for
                   min player)
        """

        # I AM LOST ?????? how do ?????

        raise NotImplemented
        

# Run test cases if invoked as main module
if __name__ == "__main__":
    b = boardlibrary.boards["StrategyTest1"]
    redstrat = Strategy('r', b, 6)
    blackstrat = Strategy('b', b, 6)
    
    print(b)
    (nb, action) = redsttrat.play(b)
    print("Red would select ", action)
    print(nb)
    
    
    (nb, action) = blacstrat.play(b)
    print("Black would select ", action)
    print(nb)
    
 

