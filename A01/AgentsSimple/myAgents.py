"""
Pair Programming Equitable Participation & Honesty Affidavit
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.



Pair Programmer 1 (print & sign your name, then date it)    Scott Sindewald 8/30/2020


Pair Programmer 2 (print & sign your name, then date it)    Carlos Gamino Reyes 8/30/2020

"""


from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    Two functions: inDanger and getAction
    """

    # constructor
    def __init__(self):
        super().__init__()  # Call parent constructor

    def inDanger(self, pacman, ghost, dist=3):
        """
        inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger, we return the direction to the ghost.
        If ghost is scared, we return Directions.STOP
        """

        if ghost.isScared(): return Directions.STOP # If ghosts are scared, agent is not in danger

        pacPos = pacman.getPosition() # Get (x,y) position of pacman
        ghostPos = ghost.getPosition() # Get (x,y) position of ghost

        # row
        if(pacPos[1] == ghostPos[1]): # If ghost and pacman are in the same row
            if(pacPos[0] - dist <= ghostPos[0] and ghostPos[0] < pacPos[0]): # If ghost is within 3 units to left
                return Directions.WEST
            elif(ghostPos[0] <= pacPos[0] + dist and pacPos[0] < ghostPos[0]): # If ghost is within 3 units to right
                return Directions.EAST
        # column
        if(pacPos[0] == ghostPos[0]): # If ghost and pacman are in the same column
            if(pacPos[1] - dist <= ghostPos[1] and ghostPos[1] < pacPos[1]): # If ghost is within 3 units below
                return Directions.SOUTH
            elif(ghostPos[1] <= pacPos[1] + dist and pacPos[1] < ghostPos[1]): # If ghost is within 3 units above
                return Directions.NORTH

        # if there is no danger return stop
        return Directions.STOP

    def getAction(self, state):
        """
        state - GameState
        Checks if pacman is in danger for each ghost. Once the first instance of danger is detected, pacman chooses
        a different direction based on the priority: reverse, left and right of danger. If none are available, pacman
        heads in the direction of danger or stops if unable. If no danger is detected, pacman functions like the
        LeftTurnAgent.
        """

        # List of directions the agent can choose from
        legal = state.getLegalPacmanActions()

        # Get the agent's state and heading from the game state
        agentState = state.getPacmanState()
        heading = agentState.getDirection()

        # in case there are no ghosts
        direction = Directions.STOP

        # if there are ghosts
        if state.getNumAgents() > 1:
            # are we in danger_check
            ghost_list = state.getGhostStates()
            for ghost in ghost_list:
                direction = self.inDanger(agentState, ghost)
                if direction != Directions.STOP: break

        if heading == Directions.STOP:
            # Pacman is stopped (true at beginning of game), assume North
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

        # If danger is detected
        if direction != Directions.STOP:
            if Directions.REVERSE[direction] in legal: # If reversing danger direction is legal
                action = Directions.REVERSE[direction]
            elif Directions.LEFT[direction] in legal: # If left turn from danger is legal
                action = Directions.LEFT[direction]
            elif Directions.RIGHT[direction] in legal: # If right turn from danger is legal
                action = Directions.RIGHT[direction]
            elif direction in legal: # If direction of danger is legal
                action = direction
            else:
                action = Directions.STOP # Can't move!
        return action
