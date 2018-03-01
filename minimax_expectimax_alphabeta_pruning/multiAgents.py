# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    food_distance = 1000
    avg_ghost_distance = 0
    g_position = successorGameState.getGhostPositions()
    c_position = successorGameState.getCapsules()
    
    if newPos in g_position:
        return -99999999999
    elif newPos in c_position:
        return 99999999999

    newfoodlist = newFood.asList()

    for food in newfoodlist:
        food_distance = min(food_distance, util.manhattanDistance(food, newPos) + 1)
    
    for g in g_position:
        avg_ghost_distance=avg_ghost_distance+manhattanDistance(newPos, g)
    
    newscore = successorGameState.getScore() + avg_ghost_distance / food_distance
    return newscore 
    #return successorGameState.getScore()
    
def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    mv = Directions.STOP
    val = -999999

    for action in gameState.getLegalActions():
        val1 = self.minimum_Value(gameState.generateSuccessor(0, action), 1, 1)
        if val1>val:
            val = val1
            mv = action
    return mv

  def minimum_Value(self, state, depth, ghost):
      if depth == self.depth or state.isWin() or state.isLose() :
          return self.evaluationFunction(state)
      val = 999999

      for action in state.getLegalActions(ghost):
          if ghost < state.getNumAgents() - 1:
              val = min(val, self.minimum_Value(state.generateSuccessor(ghost, action), depth, ghost +1))
          else:
              val = min(val, self.maximum_Value(state.generateSuccessor(ghost, action), depth + 1))
      return val

  def maximum_Value(self, state, depth):
      if state.isLose() or depth == self.depth or state.isWin():
          return self.evaluationFunction(state)
      val = -999999

      for action in state.getLegalActions(0):
          val= max(val, self.minimum_Value(state.generateSuccessor(0, action), depth+1, 1))
      return val

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    mv = Directions.STOP
    val = -999999
    alpha = -999999
    beta = 999999
    for action in gameState.getLegalActions():
        val1 = self.minimum_Value(gameState.generateSuccessor(0, action), alpha,beta, 1, 1)
        if val1>val:
            val = val1
            mv = action
    return mv

  def maximum_Value(self, state, alpha, beta, depth):
      if state.isLose() or depth == self.depth or state.isWin():
          return self.evaluationFunction(state)
      val = -999999

      for action in state.getLegalActions(0):
          val= max(val, self.minimum_Value(state.generateSuccessor(0, action),alpha,beta, depth+1, 1))
          if beta <= val:
              return val
          alpha = max(alpha,val)
      return val

  def minimum_Value(self, state, alpha, beta, depth, ghost):
      if depth == self.depth or state.isWin() or state.isLose() :
          return self.evaluationFunction(state)
      val = 999999

      for action in state.getLegalActions(ghost):
          if ghost < state.getNumAgents() - 1:
              val = min(val, self.minimum_Value(state.generateSuccessor(ghost, action),alpha,beta,depth,ghost+1))
          else:
              val = min(val, self.maximum_Value(state.generateSuccessor(ghost, action),alpha,beta,depth+1))
          if alpha >= val:
              return val
          beta = min(beta,val)
      return val



class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
#    util.raiseNotDefined()
    mv = Directions.STOP
    val = -999999

    for action in gameState.getLegalActions():
        val1 = self.expectimax_Value(gameState.generateSuccessor(0, action), 1, 1)
        if val1>val:
            val = val1
            mv = action
    return mv

  def maximum_Value(self, state, depth):
      if state.isLose() or depth == self.depth or state.isWin():
          return self.evaluationFunction(state)
      val = -999999

      for action in state.getLegalActions(0):
          val= max(val, self.expectimax_Value(state.generateSuccessor(0, action), depth+1, 1))
      return val

  def expectimax_Value(self,state,depth,ghost):
      if depth == self.depth or state.isWin() or state.isLose():
          return self.evaluationFunction(state)
      val = -1
      for  action in state.getLegalActions(ghost):
          if state.getNumAgents()-1 >ghost:
              val = val + self.expectimax_Value(state.generateSuccessor(ghost,action), depth, 1 + ghost) 
          else:
              val = val + self.maximum_Value(state.generateSuccessor(ghost,action), 1 + depth)
      len_ghost = len(state.getLegalActions(ghost))
      mod_val = val/len_ghost
      return mod_val

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """
  "*** YOUR CODE HERE ***"
  #util.raiseNotDefined()

  position = currentGameState.getPacmanPosition()
  capule_position = currentGameState.getCapsules()
  ghost_states = currentGameState.getGhostStates()
  list_food = currentGameState.getFood().asList()
  ghost_position = currentGameState.getGhostPositions()

  score = 0
  food_distance = 10
  ghost_distance = 10
  avg_ghost_distance = 0
    
  if position in ghost_position:
      score = -999999
      return score

  for food in list_food:
      food_distance = min(food_distance, util.manhattanDistance(food,position)+1)
    
  for ghost in ghost_states:
      score = score+ ghost.scaredTimer
   
  for ghost in ghost_position:
      ghost_distance = min(ghost_distance, util.manhattanDistance(position,ghost))
      avg_ghost_distance += util.manhattanDistance(position,ghost) 
  avg_ghost_distance = avg_ghost_distance/len(ghost_position)            
    
  score = score + currentGameState.getScore() + avg_ghost_distance / food_distance - ghost_distance + len(list_food)
  return score
# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

