from itertools import product

def count_assig(N, M, constraints):
    mod = 998244353
    if M == 0:
        return "infinity"

    count = 0
    max_value = 100

    for values in product(range(max_value + 1), repeat=N):
        valid = True
        for (low, high, K, indices) in constraints:
            total = sum(values[i] for i in indices)
            if not (low <= total <= high):
                valid = False
                break
        if valid:
            count = (count + 1) % mod
            
    return count





N, M = map(int, input().split())

if M == 0:
    print("infinity")
else:
    constraints = []
    for _ in range(M):
        line = list(map(int, input().split()))
        low, high, K = line[0], line[1], line[2]
        indices = [x - 1 for x in line[3:]]
        constraints.append((low, high, K, indices))

    result = count_assig(N, M, constraints)
    print(result)
