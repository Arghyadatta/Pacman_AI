# Pacman AI

Based on Washington University's CSE 511: Introduction to Artificial Intelligence course.

## Usage
### ghostbusters
```
python busters.py
python busters.py -k 1
python busters.py -s -k 1
python busters.py -s -k 1 -g StationaryGhost
python busters.py -s -g StationaryGhost
python busters.py -s -k 1 -g DirectionalGhost
python busters.py -s -k 1
python busters.py -l bigHunt
python busters.py -p GreedyBustersAgent -l smallHunt
python busters.py -k 1 -s -a inference=ParticleFilter
python busters.py -s -a inference=MarginalInference -g DispersingGhost
python busters.py -s -k 3 -a inference=MarginalInference -g DispersingGhost
python busters.py -s -k 3 -a inference=MarginalInference -g DispersingGhost -p GreedyBustersAgent -l oneHunt
```
### reinforcement_learning_MDP
```
python gridworld.py -m
python gridworld.py -h
python gridworld.py -g MazeGrid
python gridworld.py -a value -i 100 -k 10
python gridworld.py -a value -i 5
python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.2 --livingReward 0.0
python gridworld.py -a q -k 5 -m
python gridworld.py -a q -k 100 
python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1
python crawler.py
python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid 
python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid 
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid 
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic 
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 150 -l mediumGrid -q -f
```
### minimax_expectimax_alphabeta_pruning
```
python pacman.py
python pacman.py -p ReflexAgent
python pacman.py -p ReflexAgent -l testClassic
python pacman.py -p ReflexAgent -l testClassic
python pacman.py --frameTime 0 -p ReflexAgent -k 1
python pacman.py --frameTime 0 -p ReflexAgent -k 2
python pacman.py -p ReflexAgent -l openClassic -n 10 -q
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
python pacman.py -l smallClassic -p ExpectimaxAgent -a evalFn=better -q -n 10
python pacman.py -l contestClassic -p ContestAgent -g DirectionalGhost -q -n 10
```
### search_algorithms
```
python pacman.py
python pacman.py --layout testMaze --pacman GoWestAgent
python pacman.py --layout tinyMaze --pacman GoWestAgent
python pacman.py -h
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
python eightpuzzle.py
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l trickySearch -p AStarFoodSearchAgent
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
python pacman.py -l bigSearch -p ApproximateSearchAgent -z .5 -q 
```
