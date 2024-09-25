def knapsack_dynamic(weights, values, capacity):
    num_items = len(weights)
    # Cria uma tabela de (num_items+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    # Preenchendo a tabela de forma bottom-up
    for i in range(1, num_items + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[num_items][capacity]  # Valor ótimo
