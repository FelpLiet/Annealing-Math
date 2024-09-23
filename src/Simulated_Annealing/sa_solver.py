import math
import random

class SimulatedAnnealing:
    def __init__(self, problem, initial_temperature, cooling_rate, max_iterations):
        self.problem = problem
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.max_iterations = max_iterations

    def acceptance_probability(self, old_cost, new_cost, temperature):
        if new_cost < old_cost:
            return 1.0
        return math.exp((old_cost - new_cost) / temperature)

    def run(self):
        current_solution = self.problem.initial_solution()
        current_cost = self.problem.cost(current_solution)
        best_solution = current_solution
        best_cost = current_cost

        for i in range(self.max_iterations):
            new_solution = self.problem.neighbor(current_solution)
            new_cost = self.problem.cost(new_solution)

            if random.random() < self.acceptance_probability(current_cost, new_cost, self.temperature):
                current_solution = new_solution
                current_cost = new_cost

            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost

            # Resfriamento
            self.temperature *= self.cooling_rate

        return best_solution, best_cost