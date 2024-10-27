import heapq
from collections import defaultdict

def lexicographical_topological_sort(n, m, groups, dependencies):
    # Initialize adjacency list and in-degree count
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build graph from dependencies
    for a, b in dependencies:
        adj_list[a].append(b)
        in_degree[b] += 1

    # Priority queue for nodes with no dependencies (in-degree of 0)
    priority_queue = []
    
    # Add nodes with in-degree 0 to the priority queue
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(priority_queue, (groups[i-1], i))
    
    # List to hold the topologically sorted order
    topo_order = []
    
    while priority_queue:
        # Choose the project with smallest group_id and project_id
        group_id, project_id = heapq.heappop(priority_queue)
        topo_order.append(project_id)
        
        # Decrease in-degree of neighboring nodes
        for neighbor in adj_list[project_id]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add to queue with group and project ID
            if in_degree[neighbor] == 0:
                heapq.heappush(priority_queue, (groups[neighbor - 1], neighbor))
    
    # If topo_order has fewer nodes than n, there is a cycle
    if len(topo_order) < n:
        return -1  # Cycle detected, no valid ordering
    return topo_order

# Input handling as per the image format
def main():
    # Read first line: number of projects (N) and dependencies (M)
    n, m = map(int, input().strip().split())
    
    # Read second line: group IDs of each project
    groups = list(map(int, input().strip().split()))
    
    # Read next M lines: each dependency A B
    dependencies = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        dependencies.append((a, b))
    
    # Get the result
    result = lexicographical_topological_sort(n, m, groups, dependencies)
    
    # Print result
    if result == -1:
        print("-1")
    else:
        print(" ".join(map(str, result)))

# Run the main function
if __name__ == "__main__":
    main()
