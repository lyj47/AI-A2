
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search
from search import UndirectedGraph,GraphProblem,Graph
from search import InstrumentedProblem,compare_searchers
from search import uniform_cost_search,greedy_best_first_graph_search,astar_search
from utils import Dict,euclidean

#______________________________________________________________________________
#Define the Romania problem by simply creating the graph data structure directly

#edge or g costs based on actual travel distances
romania = UndirectedGraph(Dict(
    A=Dict(Z=75, S=140, T=118),
    B=Dict(U=85, P=101, G=90, F=211),
    C=Dict(D=120, R=146, P=138),
    D=Dict(M=75),
    E=Dict(H=86),
    F=Dict(S=99),
    H=Dict(U=98),
    I=Dict(V=92, N=87),
    L=Dict(T=111, M=70),
    O=Dict(Z=71, S=151),
    P=Dict(R=97),
    R=Dict(S=80),
    U=Dict(V=142)))

#heuristic or h costs based on straight-line distance
romania.locations = Dict(
    A=( 91, 492),    B=(400, 327),    C=(253, 288),   D=(165, 299),
    E=(562, 293),    F=(305, 449),    G=(375, 270),   H=(534, 350),
    I=(473, 506),    L=(165, 379),    M=(168, 339),   N=(406, 537),
    O=(131, 571),    P=(320, 368),    R=(233, 410),   S=(207, 457),
    T=( 94, 410),    U=(456, 350),    V=(509, 444),   Z=(108, 531))

#______________________________________________________________________________
def simpleGraphCreation():
    '''
    UUUU
    US U
    U  U
    U GU
    UUUU
    '''
    g = Graph({
            (1,1): {(1,2): 1, (2,1): 1},
            (1,2): {(2,2): 1},
            (2,1): {(2,2): 1, (3,1): 1},
            (2,2): {(3,2): 1},
            (3,1): {(3,2): 1},
          }, directed=False)
    
    print(g.get((2,2)))
    print(g.nodes())
    g.locations = Dict()
    for i in g.nodes():
        g.locations.update({i: i}) 
    print (euclidean(g.locations[(1,1)], g.locations[(3,2)]))
    
 #______________________________________________________________________________   
def main():
    '''
    #Explicitly create an instrumented problem
    ab = InstrumentedProblem(GraphProblem('A','B',romania))  
    goal = uniform_cost_search(ab)
    print("Path = ",goal.path())
    print("Cost = ",goal.path_cost)
    print("Expanded/Goal Tests/Generated/Cost/Goal Found")
    ab.final_cost = goal.path_cost
    print(ab)
    '''
    
    #To change h dynamically, provide a selection parameter in the constructor of your 
    #derived class, then use that parameter to choose the version of h in your
    #overriden version of h in the derived class
    #You might need to create multiple versions of the problem, one for each value of the parameter   
    
    compare_searchers(problems=[GraphProblem('A', 'B', romania),GraphProblem('A', 'N', romania)],
                header=['Algorithm', 'Romania(A, B)','Romania(A, N)'], 
            searchers=[uniform_cost_search, greedy_best_first_graph_search, astar_search])  
    
    print()
    	
main()













