def is_target_format(perm):
    mid = (len(perm) + 1) // 2
    if any(perm[i] > perm[i + 1] for i in range(mid - 1)):
        return False
    if any(perm[i] < perm[i + 1] for i in range(mid - 1, len(perm) - 1)):
        return False
    return True

def min_swaps_to_target(perm):
    n = len(perm)
    swaps = 0
    temp_perm = perm[:]

    for i in range(n):
        while temp_perm[i] != i + 1:
            target_index = temp_perm[i] - 1
            temp_perm[i], temp_perm[target_index] = temp_perm[target_index], temp_perm[i]
            swaps += 1

    return swaps if not is_target_format(perm) else 0

def generate_permutations(n, current_perm, used, total_swaps, m):
    if len(current_perm) == n:
        swaps = min_swaps_to_target(current_perm)
        total_swaps[0] = (total_swaps[0] + swaps) % m
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            current_perm.append(i)
            generate_permutations(n, current_perm, used, total_swaps, m)
            current_perm.pop()
            used[i] = False

def solve(n, m):
    total_swaps = [0]
    current_perm = []
    used = [False] * (n + 1)
    generate_permutations(n, current_perm, used, total_swaps, m)
    return total_swaps[0]

n, m = map(int, input().split())
result = solve(n, m)
print(result)
