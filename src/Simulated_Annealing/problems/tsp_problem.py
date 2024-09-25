import random
import time
import threading
from itertools import permutations

class TSPProblem:
    def __init__(self):
        self.distance_matrix = [
            [0, 29, 82, 46, 68, 52, 72, 42, 51, 55, 29, 74, 23, 72, 46],
            [29, 0, 55, 46, 42, 43, 43, 23, 23, 31, 41, 51, 11, 52, 21],
            [82, 55, 0, 68, 46, 55, 23, 43, 41, 29, 79, 21, 64, 31, 51],
            [46, 46, 68, 0, 82, 15, 72, 31, 62, 42, 21, 51, 51, 43, 64],
            [68, 42, 46, 82, 0, 74, 23, 52, 21, 46, 82, 58, 46, 65, 23],
            [52, 43, 55, 15, 74, 0, 61, 23, 55, 31, 33, 37, 51, 29, 59],
            [72, 43, 23, 72, 23, 61, 0, 42, 23, 31, 77, 37, 51, 46, 33],
            [42, 23, 43, 31, 52, 23, 42, 0, 33, 15, 37, 33, 33, 31, 37],
            [51, 23, 41, 62, 21, 55, 23, 33, 0, 29, 62, 46, 29, 51, 11],
            [55, 31, 29, 42, 46, 31, 31, 15, 29, 0, 51, 21, 41, 23, 37],
            [29, 41, 79, 21, 82, 33, 77, 37, 62, 51, 0, 65, 42, 59, 61],
            [74, 51, 21, 51, 58, 37, 37, 33, 46, 21, 65, 0, 61, 11, 55],
            [23, 11, 64, 51, 46, 51, 51, 33, 29, 41, 42, 61, 0, 62, 23],
            [72, 52, 31, 43, 65, 29, 46, 31, 51, 23, 59, 11, 62, 0, 59],
            [46, 21, 51, 64, 23, 59, 33, 37, 11, 37, 61, 55, 23, 59, 0]
        ]
        self.num_cities = len(self.distance_matrix)

    def initial_solution(self):
        return list(range(self.num_cities))

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
    
    # Função que calcula a solução ótima para o problema na forca bruta
    def optimal_solution(self, time_limit=60):
        def find_optimal(start_time):
            nonlocal best_solution, best_cost
            best_cost = float('inf')
            best_solution = None
            for perm in permutations(range(self.num_cities)):
                if time.time() - start_time > time_limit:
                    return
                cost = self.cost(perm)
                if cost < best_cost:
                    best_cost = cost
                    best_solution = perm

        best_solution = None
        best_cost = float('inf')
        start_time = time.time()
        thread = threading.Thread(target=find_optimal, args=(start_time,))
        thread.start()
        thread.join(timeout=time_limit)

        if thread.is_alive():
            print("Tempo limite atingido. Interrompendo a busca pela solução ótima.")
            return None, None

        return best_solution, best_cost