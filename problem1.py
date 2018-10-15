from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean
from array import *

class Problem1:

    graphFile = ''
    graphArr = []
    startPosition = ''
    endPosition = ''

    def __init__(self, graphFile):
        self.graphFile = graphFile

    def create_graph(self):
        # the map of the maze
        map = open(self.graphFile, 'r')
        # index of the row for graphArr
        index = 0
        # a temp arr to hold the row of numbers
        arr = []

        for line in map.readlines()[2:]:
            for i in range(0, len(line)):
                if line[i] != '\n': # avoid new line characters
                    arr.append(int(line[i]))
            index = index + 1
            self.graphArr.insert(index, arr)
            arr = []

    def set_graph_file(self, newGraph):
        self.graphFile = newGraph

def main():

    problem = Problem1('L1.txt')

    problem.create_graph()

    print(problem.graphArr)

main()
