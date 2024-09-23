import random

class KnapsackProblem:
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = capacity
        self.num_items = len(weights)
    
    def initial_solution(self):
        return [random.randint(0, 1) for _ in range(self.num_items)]