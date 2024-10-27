def build_binary_tree_and_find_nodes(S):
    # Set N to 4 to create exactly 4 nodes
    N = 4
    
    # Initialize the children array for storing left and right children
    children = [(0, 0)] * (N + 1)

    # Manually define the binary tree structure for 4 nodes
    # Node 1: (Node 2, Node 3)
    # Node 2: (Node 4, 0)
    # Node 3: (0, 0)
    # Node 4: (0, 0)
    if N >= 2:
        children[1] = (2, 3)  # Node 1 has left child 2 and right child 3
    if N >= 3:
        children[2] = (4, 0)  # Node 2 has left child 4
    if N >= 4:
        children[3] = (0, 0)  # Node 3 has no children
    if N >= 4:
        children[4] = (0, 0)  # Node 4 has no children

    # Position for starting point (A) and exit point (B)
    reachable_nodes = set()
    current_node = 1  # Start at node A

    reachable_nodes.add(current_node)

    # Move according to string S
    for move in S:
        if move == 'L':
            next_node = current_node * 2
        elif move == 'R':
            next_node = current_node * 2 + 1
        elif move == 'U':
            next_node = current_node // 2
        else:
            continue

        # Only move to a valid node
        if next_node <= N:
            current_node = next_node
            reachable_nodes.add(current_node)

    # Find a suitable exit node B that is not reachable
    for candidate_B in range(1, N + 1):
        if candidate_B not in reachable_nodes:
            A = 1  # Starting node is always node 1
            B = candidate_B
            return N, A, B, children

    return -1  # If all nodes are reachable

# Input
S = input().strip()

# Get the result
result = build_binary_tree_and_find_nodes(S)

if result == -1:
    print(-1)
else:
    N, A, B, children = result
    print(N, A, B)
    for i in range(1, N + 1):
        print(children[i][0], children[i][1])
