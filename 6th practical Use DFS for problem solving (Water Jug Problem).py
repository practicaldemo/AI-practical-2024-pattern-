def dfs_water_jug(capacity_x, capacity_y, target):
    stack = [((0, 0), [])]
    visited = set()
    
    while stack:
        (x, y), path = stack.pop()
        
        if (x, y) in visited:
            continue
            
        visited.add((x, y))
        path = path + [(x, y)]
        
        if x == target or y == target:
            return path
            
        # Generate rules
        states = set([
            (capacity_x, y),  # Fill X
            (x, capacity_y),  # Fill Y
            (0, y),           # Empty X
            (x, 0),           # Empty Y
            (x - min(x, capacity_y - y), y + min(x, capacity_y - y)),  # Pour X to Y
            (x + min(y, capacity_x - x), y - min(y, capacity_x - x))   # Pour Y to X
        ])
        
        for state in states:
            if state not in visited:
                stack.append((state, path))
                
    return None

print("Water Jug DFS Path:", dfs_water_jug(4, 3, 2))