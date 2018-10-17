from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean
from array import *
import re
import math

class Problem1:

    # graph
    graph_file = ''
    graph = ''

    # heuristics
    manhattan_distances = Dict()

    # start/end coords
    start_coordinates = ''
    end_coordinates = ''

    def __init__(self, graph_file):
        self.graph_file = graph_file

    def create_graph(self, graph_file=None):
        map = ''

        if graph_file == None:
            map = open(self.graph_file, 'r')
        else:
            map = open(graph_file, 'r')

        # index of the row for graph_arr
        index = 0
        # temp array to hold the row of numbers
        arr = []
        # temp array to hold the 2D array of numbers
        graph_arr = []
        # dictionary to hold the vertices and paths
        dict = Dict()

        start_coord = map.readlines()[0:1]
        map.seek(0)
        goal_coord = map.readlines()[1:2]
        map.seek(0)

        # set the coordinates
        start_coord = re.sub('[^0-9,.]', '', str(start_coord)).split(",")
        self.start_coordinates = (int(start_coord[0]), int(start_coord[1]))
        goal_coord = re.sub('[^0-9,.]', '', str(goal_coord)).split(",")
        self.end_coordinates = (int(goal_coord[0]), int(goal_coord[1]))

        for line in map.readlines()[2:]:
            for i in range(0, len(line)):
                if line[i] != '\n': # avoid new line characters
                    arr.append(int(line[i]))
            index = index + 1
            graph_arr.insert(index, arr)
            arr = []

        self.graph_arr = graph_arr
        for row in range(0, len(graph_arr)-1):
            for col in range(0, len(graph_arr[row])):
                if graph_arr[row][col] == 0:
                    continue
                else:
                    # if both right and bottom are free and not = 0, make a path.
                    if col+1 < len(graph_arr[row]) and row+1 < len(graph_arr) and graph_arr[row][col+1] != 0 and graph_arr[row+1][col] != 0:
                        dict.update({(row, col):
                                        {
                                            (row, col+1): int(graph_arr[row][col+1]),
                                            (row+1, col): int(graph_arr[row+1][col])
                                        }
                                    })
                    # if the bottom is free, but not the right and the bottom isn't = 0, make a path.
                    elif graph_arr[row][col+1] == 0 and graph_arr[row+1][col] != 0 and row+1 < len(graph_arr):
                        dict.update({(row, col): {
                                            (row, col): int(graph_arr[row+1][col])
                                           }})
                    # if the right is free, but not the bottom and the right isn't = 0, make a path.
                    elif graph_arr[row+1][col] == 0 and graph_arr[row][col+1] != 0 and col+1 < len(graph_arr[row]):
                        dict.update({(row, col): {
                                            (row, col): int(graph_arr[row][col+1])
                                           }})
                # self.manhattan_distances.update({(row, col): (row, col)}) # self.get_manhattan_distance((row, col))
        # graph created
        self.graph = Graph(dict, directed=False)
        # self.graph.locations = self.manhattan_distances
        self.graph.locations = Dict()
        for i in self.graph.nodes():
            self.graph.locations.update({i: i})

        map.close()

    def set_graph_file(self, graph_file):
        if graph_file == None:
            print('you must specify a file in the set_graph_file function')
        else:
            self.graph_file = graph_file

    def get_manhattan_distance(self, coordinates):
        return (math.fabs(self.end_coordinates[0] - coordinates[0]) +
                    math.fabs(self.end_coordinates[1] - coordinates[1]))

def main():

    problem = Problem1('L3.txt')

    problem.create_graph()

    problem = InstrumentedProblem(GraphProblem(problem.start_coordinates, problem.end_coordinates, problem.graph))
    goal = uniform_cost_search(problem)
    print("Path = ",goal.path())
    print("Cost = ",goal.path_cost)
    print("Expanded/Goal Tests/Generated/Cost/Goal Found")
    problem.final_cost = goal.path_cost
    print(problem)

main()
