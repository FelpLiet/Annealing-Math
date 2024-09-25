import random

class KnapsackProblem:
    def __init__(self):
        # Gerar 20 itens com pesos entre 1 e 50 e valores entre 1 e 100
        self.weights = [random.randint(1, 50) for _ in range(20)]
        self.values = [random.randint(1, 100) for _ in range(20)]
        self.capacity = 500
        self.num_items = len(self.weights)
    
    def initial_solution(self):
        # Solução inicial aleatória
        return [random.randint(0, 1) for _ in range(self.num_items)]

    def cost(self, solution):
        total_value = 0
        total_weight = 0
        for i in range(self.num_items):
            if solution[i] == 1:
                total_weight += self.weights[i]
                total_value += self.values[i]
        
        if total_weight > self.capacity:
            return float('inf')  # Penalizar soluções que excedem a capacidade
        return -total_value  # Maximizar o valor, então usar o negativo

    def neighbor(self, solution):
        neighbor = solution[:]
        i = random.randint(0, self.num_items - 1)
        neighbor[i] = 1 - neighbor[i]  # Troca o estado do item i (de 0 para 1 ou de 1 para 0)
        return neighbor
