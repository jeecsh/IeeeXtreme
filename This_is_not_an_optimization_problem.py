def dfs(node, parent):
    # Initialize the subtree size and total contribution of the current node
    subtree_size[node] = 1
    contribution = weights[node]  # Start with the node's own weight
    
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        
        child_weight, child_size = dfs(neighbor, node)
        
        contribution += child_weight
        subtree_size[node] += child_size
        
        # Update weights_sum for all combinations including this child
        for k in range(1, child_size + 1):
            weights_sum[k + 1] += (child_weight * binomial[subtree_size[node] - 1][k - 1]) % MOD
            weights_sum[k + 1] %= MOD
            
    # For size 1, add the weight of the current node
    weights_sum[1] += weights[node]
    weights_sum[1] %= MOD
    
    return contribution, subtree_size[node]

def preprocess_binomial_coefficients(n):
    for i in range(n + 1):
        binomial[i][0] = 1
        for j in range(1, i + 1):
            binomial[i][j] = (binomial[i - 1][j - 1] + binomial[i - 1][j]) % MOD

# Read input
N = int(input())
weights = [0] + list(map(int, input().split()))  # Indexing from 1 to N
MOD = 10**9 + 99999

# Initialize graph with N + 1 to accommodate 1-based index
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# Initialize arrays for storing subtree sizes and results
subtree_size = [0] * (N + 1)
weights_sum = [0] * (N + 1)

# Prepare binomial coefficients for counting
binomial = [[0] * (N + 1) for _ in range(N + 1)]
preprocess_binomial_coefficients(N)

# Perform DFS from node 1 (or any node since it's a connected tree)
dfs(1, -1)

# Output the results for each size k from 1 to N
for k in range(1, N + 1):
    print(weights_sum[k] % MOD)
