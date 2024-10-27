def cnt_permutations(N, C, R, B):
    MOD = 998244353
    totaln = set(range(1, 2 * N + 1))
    used_numbers = set(x for x in C if x != -1)
    ava_numb = list(totaln - used_numbers)
    ava_numb.sort()

    from itertools import permutations
    
    valid_count = 0
    
    for perm in permutations(ava_numb):
        A = C[:]
        j = 0  
        
        for i in range(2 * N):
            if A[i] == -1:
                A[i] = perm[j]
                j += 1
        
        is_valid = True
        for i in range(N):
            if R[i] == 0:
                if B[i] != min(A[2 * i], A[2 * i + 1]):
                    is_valid = False
                    break
            else:
                if B[i] != max(A[2 * i], A[2 * i + 1]):
                    is_valid = False
                    break
        
        if is_valid:
            valid_count += 1
    
    return valid_count % MOD

N = int(input())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
B = list(map(int, input().split()))

result = cnt_permutations(N, C, R, B)
print(result)
