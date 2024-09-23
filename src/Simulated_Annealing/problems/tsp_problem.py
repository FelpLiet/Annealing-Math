import random

class TSPProblem:
    def __init__(self):
        distance_matrix = [
            [0, 29, 20, 21],
            [29, 0, 15, 18],
            [20, 15, 0, 26],
            [21, 18, 26, 0]
        ]
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def initial_solution(self):
        solution = list(range(self.num_cities))
        random.shuffle(solution)
        return solution

    def cost(self, solution):
        total_distance = 0
        for i in range(len(solution)):
            city_a = solution[i]
            city_b = solution[(i + 1) % self.num_cities]  
            total_distance += self.distance_matrix[city_a][city_b]
        return total_distance

    def neighbor(self, solution):
        neighbor = solution[:]
        i, j = random.sample(range(self.num_cities), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        return neighbor