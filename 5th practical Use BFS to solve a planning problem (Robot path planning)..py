from collections import deque

def bfs_path_planning(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([[start]])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        
        if (x, y) == goal:
            return path
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                new_path = list(path)
                new_path.append((nx, ny))
                queue.append(new_path)
                
    return None

# Example grid (0=free, 1=obstacle)
grid = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

path = bfs_path_planning(grid, (0, 0), (2, 3))
print("BFS Path:", path)
