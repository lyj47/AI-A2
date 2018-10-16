from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean
from array import *

class Problem1:

    graphFile = ''
    graph = ''
    startPosition = ''
    endPosition = ''

    def __init__(self, graphFile):
        self.graphFile = graphFile

    def create_graph(self, graphFile=None):
        map = ''

        if graphFile == None:
            map = open(self.graphFile, 'r')
        else:
            map = open(graphFile, 'r')

        # index of the row for graphArr
        index = 0
        # temp array to hold the row of numbers
        arr = []
        # temp array to hold the 2D array of numbers
        graphArr = []
        # dictionary to hold the vertices and paths
        dict = {}

        for line in map.readlines()[2:]:
            for i in range(0, len(line)):
                if line[i] != '\n': # avoid new line characters
                    arr.append(int(line[i]))
            index = index + 1
            graphArr.insert(index, arr)
            arr = []

        self.graphArr = graphArr
        for row in range(0, len(graphArr)-1):
            for col in range(0, len(graphArr[row])):
                if graphArr[row][col] == 0:
                    continue
                else:
                    # if both right and bottom are free and not = 0, make a path.
                    if col+1 < len(graphArr[row]) and row+1 < len(graphArr) and graphArr[row][col+1] != 0 and graphArr[row+1][col] != 0:
                        print("BOTH")
                        dict[(row, col)] = {
                                            (row, col+1): int(graphArr[row][col+1]),
                                            (row+1, col): int(graphArr[row+1][col])
                                           }
                    # if the bottom is free, but not the right and the bottom isn't = 0, make a path.
                    elif graphArr[row][col+1] == 0 and graphArr[row+1][col] != 0 and row+1 < len(graphArr):
                        print("BOTTOM")
                        dict[(row, col)] = {
                                            (row, col): int(graphArr[row+1][col])
                                           }
                    # if the right is free, but not the bottom and the right isn't = 0, make a path.
                    elif graphArr[row+1][col] == 0 and graphArr[row][col+1] != 0 and col+1 < len(graphArr[row]):
                        print("RIGHT")
                        dict[(row, col)] = {
                                            (row, col): int(graphArr[row][col+1])
                                           }
        # graph created
        self.graph = Graph(dict, directed=False)

    def set_graph_file(self, graphFile):
        if graphFile == None:
            print('you must specify a file in the set_graph_file function')
        else:
            self.graphFile = graphFile

def main():

    problem = Problem1('L1.txt')

    problem.create_graph()

    print(problem.graph)

main()
