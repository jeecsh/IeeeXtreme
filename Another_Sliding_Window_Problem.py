def optimal_cost(subarray):
    k = len(subarray)
    if k == 0:
        return 0

    pair_sums = []
    for i in range(k // 2):
        pair_sums.append(subarray[i] + subarray[k - 1 - i])
    
    if k % 2 == 1:
        pair_sums.append(subarray[k // 2])

    return max(pair_sums)

def calculate_sums(N, A, Q, queries):
    results = []
    optimal_costs = []
    
    for l in range(N):
        for r in range(l, N):
            cost = optimal_cost(A[l:r + 1])
            diff = A[r] - A[l]
            optimal_costs.append((cost, diff))
    
    optimal_costs.sort()

    for x in queries:
        total_sum = 0
        for cost, diff in optimal_costs:
            if cost <= x:
                total_sum += diff
            else:
                break
        results.append(total_sum)

    return results

import sys

input_data = sys.stdin.read().strip().splitlines()

N, Q = map(int, input_data[0].split())
A = list(map(int, input_data[1].split()))
queries = [int(input_data[i + 2]) for i in range(Q)]

results = calculate_sums(N, A, Q, queries)

for res in results:
    print(res)
