def calculate_regions(L, N, M, laser_A_beams, laser_B_beams):
    # Parse beams into lists for U and R (laser A) and U and L (laser B)
    laser_A_up, laser_A_right = [], []
    laser_B_up, laser_B_left = [], []
    
    # Separate beams based on direction for each laser
    for beam in laser_A_beams:
        direction, C = beam
        if direction == 'U':
            laser_A_up.append(C)
        elif direction == 'R':
            laser_A_right.append(C)
    
    for beam in laser_B_beams:
        direction, C = beam
        if direction == 'U':
            laser_B_up.append(C)
        elif direction == 'L':
            laser_B_left.append(C)

    # Sort coordinates for easier intersection counting
    laser_A_up.sort()
    laser_A_right.sort()
    laser_B_up.sort()
    laser_B_left.sort()

    # Calculate intersections based on sorted beams.
    intersections = set()
    
    # For each beam in laser A's up direction, find intersections with laser B's left beams
    for x in laser_A_up:
        for y in laser_B_left:
            intersections.add((x, y))

    # For each beam in laser A's right direction, find intersections with laser B's up beams
    for y in laser_A_right:
        for x in laser_B_up:
            intersections.add((x, y))

    # Number of regions formula
    num_regions = len(intersections) + 1
    
    return num_regions

# Example usage:
L = 30
N = 3
M = 2
laser_A_beams = [('U', 10), ('U', 25), ('R', 10)]
laser_B_beams = [('L', 15), ('U', 20)]
result = calculate_regions(L, N, M, laser_A_beams, laser_B_beams)
print(result)  # Expected output: 11
