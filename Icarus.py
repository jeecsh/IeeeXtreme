def trap_icarus(S):
  
    
    N = 3  
    A = 1 
    B = 2 
    

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    
  
    left[1] = 2  
    right[1] = 3 
    left[2] = 0
    right[2] = 0
    left[3] = 0
    right[3] = 0
    

    print(N, A, B)
    for i in range(1, N + 1):
        print(left[i], right[i])


S = input().strip()
trap_icarus(S)
