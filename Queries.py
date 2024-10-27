class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def queris_prog(N, Q, P, queries):
    fenwick_tree = FenwickTree(N)
    output = []

    for query in queries:
        if query[0] == 0:
            _, l, r, c = query
            fenwick_tree.update(l, c)
            fenwick_tree.update(r + 1, -c)
        elif query[0] == 1:
            _, l, r, c = query
            for i in range(l, r + 1):
                fenwick_tree.update(P[i - 1], c)
        elif query[0] == 2:
            _, l, r = query
            total_sum = fenwick_tree.range_query(l, r)
            output.append(total_sum)
        elif query[0] == 3:
            _, l, r = query
            total_sum = sum(fenwick_tree.query(P[i - 1]) for i in range(l, r + 1))
            output.append(total_sum)

    return output

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    P = list(map(int, data[idx:idx + N]))
    idx += N
    queries = []
    for _ in range(Q):
        query = list(map(int, data[idx:idx + 4]))
        queries.append(query)
        idx += len(query)

    results = queris_prog(N, Q, P, queries)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')