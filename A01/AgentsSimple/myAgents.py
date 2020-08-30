"""
Pair Programming Equitable Participation & Honesty Affidavit
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.




Pair Programmer 1 (print & sign your name, then date it) Scott Sindewald 8/30/2020




Pair Programmer 2 (print & sign your name, then date it) Carlos Gamino Reyes 8/30/2020

"""


from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    # constructor
    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """
        if(ghost.isScared()): return Directions.STOP

        pacPos = pacman.getPosition()
        ghostPos = ghost.getPosition()

        # ROW
        if(pacPos[1] == ghostPos[1]):
            if(pacPos[0] - dist <= ghostPos[0] and ghostPos[0] < pacPos[0]):
                return Directions.WEST
            elif(ghostPos[0] <= pacPos[0] + dist and pacPos[0] < ghostPos[0]):
                return Directions.EAST
        # column
        if(pacPos[0] == ghostPos[0]):
            if(pacPos[1] - dist <= ghostPos[1] and ghostPos[1] < pacPos[1]):
                return Directions.SOUTH
            elif(ghostPos[1] <= pacPos[1] + dist and pacPos[1] < ghostPos[1]):
                return Directions.NORTH

        # if there is no danger return stop
        return Directions.STOP
    
    def getAction(self, state):
        """
        state - GameState
        
        Fill in appropriate documentation
        """

        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        # Get the agent's state from the game state and find agent heading
        agentState = state.getPacmanState()

        heading = agentState.getDirection()

        print(agentState)

        # are we in danger_check
        # see getPacmanState() and getGhostStates()
        ghost_list = state.getGhostStates()
        for Ghost in ghost_list:
            direction = self.inDanger(agentState, Ghost)
            print(Ghost.getPosition(), direction)
            if direction != Directions.STOP: break


        if heading == Directions.STOP:
            # Pacman is stopped, assume North (true at beginning of game)
            heading = Directions.NORTH

        # Turn left if possible
        left = Directions.LEFT[heading]  # What is left based on current heading
        if left in legal:
            action = left
        else:
            # No left turn
            if heading in legal:
                action = heading  # continue in current direction
            elif Directions.RIGHT[heading] in legal:
                action = Directions.RIGHT[heading]  # Turn right
            elif Directions.REVERSE[heading] in legal:
                action = Directions.REVERSE[heading]  # Turn around
            else:
                action = Directions.STOP  # Can't move!

        if direction != Directions.STOP: # If danger is detected.
            if Directions.REVERSE[direction] in legal: # If reversing danger direction is legal.
                action = Directions.REVERSE[direction]
            elif Directions.LEFT[direction] in legal: # If left turn from danger is legal.
                action = Directions.LEFT[direction]
            elif Directions.RIGHT[direction] in legal: # If right turn from danger is legal.
                action = Directions.RIGHT[direction]
            elif direction in legal: # Head in direction of danger
                action = direction
            else:
                action = Directions.STOP # Can't move.
        #input()
        return action

