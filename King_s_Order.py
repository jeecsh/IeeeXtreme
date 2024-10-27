import heapq
from collections import defaultdict

def topo_sort(n, m, groups, dependencies):
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for a, b in dependencies:
        adj_list[a].append(b)
        in_degree[b] += 1

    que = []
    
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(que, (groups[i-1], i))
    
    order = []
    
    while que:
        group_id, project_id = heapq.heappop(que)
        order.append(project_id)
        
        for neighbor in adj_list[project_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(que, (groups[neighbor - 1], neighbor))
    
    if len(order) < n:
        return -1
    return order

def main():
    n, m = map(int, input().strip().split())
    groups = list(map(int, input().strip().split()))
    dependencies = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        dependencies.append((a, b))
    
    result = topo_sort(n, m, groups, dependencies)
    
    if result == -1:
        print("-1")
    else:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
