from sys import stdin, stdout
from math import gcd
from array import array
from typing import List, Tuple

class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.data = array('q', data)  # Using array for better memory efficiency
        self.tree = array('q', [0] * (4 * self.n))
        self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.data[start]
            return
            
        mid = (start + end) >> 1  # Faster integer division
        left_child = (node << 1) + 1  # Faster multiplication
        right_child = (node << 1) + 2
        
        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update_range(self, l: int, r: int, val: int) -> None:
        self._update(l, r, val, 0, 0, self.n - 1)
        
    def _update(self, l: int, r: int, val: int, node: int, start: int, end: int) -> None:
        if start > r or end < l:
            return
            
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            return
            
        mid = (start + end) >> 1
        left_child = (node << 1) + 1
        right_child = (node << 1) + 2
        
        self._update(l, r, val, left_child, start, mid)
        self._update(l, r, val, right_child, mid + 1, end)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query_range(self, l: int, r: int) -> int:
        return self._query(l, r, 0, 0, self.n - 1)
    
    def _query(self, l: int, r: int, node: int, start: int, end: int) -> int:
        if start > r or end < l:
            return 0
            
        if start >= l and end <= r:
            return self.tree[node]
            
        mid = (start + end) >> 1
        left_child = (node << 1) + 1
        right_child = (node << 1) + 2
        
        return (self._query(l, r, left_child, start, mid) + 
                self._query(l, r, right_child, mid + 1, end))

def format_fraction(P: int, Q: int) -> str:
    """Format fraction after reducing by GCD."""
    d = gcd(P, Q)
    return f"{P // d}/{Q // d}"

def process_events(N: int, Q: int, salaries: List[int], events: List[Tuple]) -> List[str]:
    salary_tree = SegmentTree(salaries)
    happiness = array('q', [0] * N)  # Using array for better memory efficiency
    result = []
    
    for event_type, l, r, *args in events:
        if event_type == 0:  # Set salary
            c = args[0]
            for i in range(l, r + 1):
                old_salary = salaries[i]
                if old_salary != c:
                    happiness[i] += 1 if old_salary < c else -1
                salaries[i] = c
            
        elif event_type == 1:  # Modify salary
            c = args[0]
            for i in range(l, r + 1):
                happiness[i] += 1 if c > 0 else -1
                salaries[i] += c
            
        elif event_type == 2:  # Query average salary
            total = sum(salaries[l:r + 1])
            result.append(format_fraction(total, r - l + 1))
            
        elif event_type == 3:  # Query average happiness
            total = sum(happiness[l:r + 1])
            result.append(format_fraction(total, r - l + 1))
            
    return result

def main():
    # Read all input at once for better performance
    data = stdin.read().split()
    pos = 0
    
    # Parse input
    N = int(data[pos])
    Q = int(data[pos + 1])
    pos += 2
    
    salaries = list(map(int, data[pos:pos + N]))
    pos += N
    
    # Parse events
    events = []
    for _ in range(Q):
        event_type = int(data[pos])
        l = int(data[pos + 1]) - 1
        r = int(data[pos + 2]) - 1
        pos += 3
        
        if event_type in (0, 1):
            c = int(data[pos])
            pos += 1
            events.append((event_type, l, r, c))
        else:
            events.append((event_type, l, r))
    
    # Process events and write output
    result = process_events(N, Q, salaries, events)
    stdout.write('\n'.join(result) + '\n')

if __name__ == "__main__":
    main()