import time
import psutil
from Simulated_Annealing.sa_solver import SimulatedAnnealing
from Simulated_Annealing.problems.knapsack_problem import KnapsackProblem
from Simulated_Annealing.problems.tsp_problem import TSPProblem

def run_simulated_annealing(problem_class, initial_temperature, cooling_rate, max_iterations, runs=10):
    total_time = 0
    total_memory = 0
    best_solutions = []
    best_costs = []

    for _ in range(runs):
        problem = problem_class()
        sa = SimulatedAnnealing(problem, initial_temperature, cooling_rate, max_iterations)

        start_time = time.time()
        process = psutil.Process()
        start_memory = process.memory_info().rss

        best_solution, best_cost = sa.run()

        end_time = time.time()
        end_memory = process.memory_info().rss

        total_time += (end_time - start_time)
        total_memory += (end_memory - start_memory)
        best_solutions.append(best_solution)
        best_costs.append(best_cost)

    avg_time = total_time / runs
    avg_memory = total_memory / runs
    avg_cost = sum(best_costs) / runs

    return avg_time, avg_memory, avg_cost, best_solutions, best_costs

def main():
    problems = {
        "1": KnapsackProblem,
        "2": TSPProblem
    }

    print("Selecione o problema para executar:")
    print("1. Problema da Mochila")
    print("2. Problema do Caixeiro Viajante")
    choice = input("Digite o número do problema: ")

    if choice not in problems:
        print("Escolha inválida.")
        return

    problem_class = problems[choice]
    initial_temperature = 1000
    cooling_rate = 0.95
    max_iterations = 1000

    avg_time, avg_memory, avg_cost, best_solutions, best_costs = run_simulated_annealing(
        problem_class, initial_temperature, cooling_rate, max_iterations
    )

    print(f"Tempo médio de execução: {avg_time:.4f} segundos")
    print(f"Uso médio de memória: {avg_memory / (1024 * 1024):.4f} MB")
    print(f"Custo médio das melhores soluções: {avg_cost:.4f}")
    print("Melhores soluções encontradas:")
    for solution, cost in zip(best_solutions, best_costs):
        print(f"  {solution} - Custo: {cost:.4f}")
    

if __name__ == "__main__":
    main()