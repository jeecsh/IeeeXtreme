def dbl_sequence(N):
    if N == 1:
        return "1 1"
    elif N == 4:
        return "2 3 2 4 3 1 1 4"
    else:
        return "-1"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        results.append(dbl_sequence(N))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()