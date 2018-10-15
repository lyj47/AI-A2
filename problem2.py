from search import Problem
from utils import probability, argmax, weighted_sample_with_replacement
import random

#______________________________________________________________________________
#Genetic algorithms

def genetic_search(problem, fitness_fn, ngen=1000, pmut=0.1):
    """Call genetic_algorithm on the appropriate parts of a problem.
    This requires the problem to have states that can mate and mutate,
    plus a value method that scores states.
    """
    s = problem.initial
    states = [problem.result(s, a) for a in problem.actions(s)]
    random.shuffle(states)
    return genetic_algorithm(states, problem.value, ngen, pmut)
    
def genetic_algorithm(population, fitness_fn, ngen=1000, pmut=0.1):
    highest = 0
    highestEvolved = None
    for i in range(ngen):
        new_population = []
        for j in range(len(population)):
            fitnesses = map(fitness_fn, population)
            p1, p2 = weighted_sample_with_replacement(population, fitnesses, 2)
            child = p1.mate(p2)
            if random.uniform(0, 1) < pmut:
                child.mutate()
            new_population.append(child)
        population = new_population
        
        #Check and keep track of max; not necessarily pure GA
        currentEvolved = argmax(population, fitness_fn)
        currentHigh = fitness_fn(currentEvolved)
        if currentHigh > highest:    
            highest = currentHigh
            highestEvolved = currentEvolved
    return highestEvolved
    
    #Pure GA might return this instead        
    #return argmax(population, fitness_fn)
    
class GAState:
    "Abstract class for individuals in a genetic search."
    def __init__(self, genes):
        self.genes = genes

    def mate(self, other):
        "Return a new individual crossing self and other."
        c = random.randrange(len(self.genes))
        return self.__class__(self.genes[:c] + other.genes[c:])

    def mutate(self):
        "Change a few of my genes."
        abstract

    def __repr__(self):
        return "%s" % (self.genes,)
    
    #override if this is not what you want
    def __eq__(self,other):
        return isinstance(other, GAState) and self.genes == other.genes
 
#______________________________________________________________________________
#NQueenProblem and NQueenState
class NQueenState(GAState):
    '''
    special state for genetic algorithms, extends from GAState NQueen problem
    genes is the state for regular problems, wrapped in GAState child for this version
    Override the methods you are interested in.
    '''
    def __init__(self, genes):
        GAState.__init__(self, genes)

    def mutate(self):
        '''Implement this method'''
        override
        
class NQueenProblem(Problem):
    '''
    The problem of placing N queens on an NxN board with none attacking
    each other.  The problem can be initialized to some random, non-viable state.
    Recall that the states (init, etc.) are all NQueenState objects, so the genes 
    in the state are represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r. Keeps track of the number of steps too.
    '''
    def __init__(self, N, init):
        self.N = N
        self.initial = init

    def actions(self, state):
        '''
        Implement this method.
        Returns the neighbors of a given state. You must implement this so that the
        neighbors are from the "neighborhood" and are not an enormous set.
        '''
        override
    
    def result(self, state, action):
        ''' Modify this if your result state is different from your action'''
        return action

    def value(self, state):
        '''
        Implement this method.
        Assigns a value to a given state that represents the number of non-conflicts.
        The higher the better with the maximum being (n*(n-1))/2 
        Remember, you must look at state.genes
        '''
        override

    def conflict(self, row1, col1, row2, col2):    
        '''
        Utility method. You can use this in other methods.
        Would putting two queens in (row1, col1) and (row2, col2) conflict?
        '''
        return (row1 == row2 ## same row
                or col1 == col2 ## same column
                or row1-col1 == row2-col2  ## same \ diagonal
                or row1+col1 == row2+col2) ## same / diagonal

#______________________________________________________________________________
#ExampleProblem and ExampleState
class ExampleState(GAState):
    '''
    Example that does really nothing; just illustrates the process
    '''
    def __init__(self, genes):
        GAState.__init__(self, genes)

    def mutate(self):
        #flip a random bit
        c = random.randrange(len(self.genes))
        self.genes[c] = 1 - self.genes[c]

class ExampleProblem(Problem):
    '''
    An example problem with a list of bits as a list
    '''
    def __init__(self, init):
        self.initial = init

    def actions(self, state):
        '''
        Generate randomly flip one bit; do this twice to generate 2 neighbors
        Actions are just the genes
        '''
        choices=[]
        for i in range(2):
            candidate = list(state.genes)
            c = random.randrange(len(candidate))
            if probability(0.5):
                candidate[c] = 1 - candidate[c]
            choices.append(candidate)           
        return choices
    
    def result(self, state, action):
        ''' Wrap the action genes in an ExampleState and return that'''
        return ExampleState(action)

    def value(self, state):
        '''
            Simply counts number of 1's and returns 1 + that value; 
            We want to avoid  fitnesses of 0 always.
        '''
        return state.genes.count(1) + 1

         
#______________________________________________________________________________   
def main():
     
    gp = ExampleProblem(ExampleState([0,0,0,0,0,0,0,0])) 
    goal = genetic_search(gp, ExampleProblem.value, ngen=100, pmut=0.1)
    print("Goal = ",goal)    
    print()

main()