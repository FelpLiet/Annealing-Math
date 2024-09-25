from Simulated_Annealing import knapsack_dynamic
from Simulated_Annealing.problems.knapsack_problem import KnapsackProblem
from Simulated_Annealing.problems.tsp_problem import TSPProblem
from Simulated_Annealing.sa_solver import SimulatedAnnealing
import time
import psutil

def calculate_weight(solution, weights):
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
    return total_weight

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

    print("\n==================== Resultados ====================")
    print(f"Tempo médio de execução: {avg_time:.4f} segundos")
    print(f"Uso médio de memória: {avg_memory / (1024 * 1024):.4f} MB")
    print(f"Custo médio das melhores soluções: {-avg_cost:.4f}")
    print("\nMelhores soluções encontradas:")
    for solution, cost in zip(best_solutions, best_costs):
        print(f"  {solution} - Custo: {cost}") 

    if choice == "1":
        problem = KnapsackProblem()
        optimal_cost = knapsack_dynamic(problem.weights, problem.values, problem.capacity)
        print("\n==================== Comparação com Solução Ótima ====================")
        print(f"Solução ótima para o problema da mochila: {optimal_cost}")
        print(f"Melhor custo encontrado pelo Simulated Annealing: {-min(best_costs)}")  # Negativo porque a função usa -total_value
        best_solution = best_solutions[best_costs.index(min(best_costs))]
        best_weight = calculate_weight(best_solution, problem.weights)
        print(f"Peso total da melhor solução: {best_weight}")
    elif choice == "2":
        problem = TSPProblem()
        optimal_solution, optimal_cost = problem.optimal_solution(time_limit=10)
        print("\n==================== Comparação com Solução Ótima ====================")
        if optimal_solution is None:
            print("Tempo limite atingido para a solução ótima.")
            print(f"Melhor custo para P01 com 15 cidades do Caixeiro Viajante segundo https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html: 291")
        else:
            print(f"Solução ótima para o problema do Caixeiro Viajante: {optimal_solution} - Custo: {optimal_cost}")
        print(f"Melhor custo encontrado pelo Simulated Annealing: {min(best_costs)}")
          
if __name__ == "__main__":
    main()
