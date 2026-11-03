import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def manhattan_distance(board, goal):
    dist = 0
    for i in range(1, 9):
        xi, yi = divmod(board.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        dist += abs(xi - xg) + abs(yi - yg)
    return dist

def a_star_8_puzzle(start, goal):
    pq = []
    visited = set()
    start_state = PuzzleState(start, None, "", 0, manhattan_distance(start, goal))
    heapq.heappush(pq, start_state)
    
    while pq:
        current = heapq.heappop(pq)
        
        if current.board == goal:
            return current.depth
            
        visited.add(tuple(current.board))
        
        zero_idx = current.board.index(0)
        x, y = divmod(zero_idx, 3)
        moves = {'U': (x-1, y), 'D': (x+1, y), 'L': (x, y-1), 'R': (x, y+1)}
        
        for move, (nx, ny) in moves.items():
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_idx = nx * 3 + ny
                new_board = list(current.board)
                new_board[zero_idx], new_board[new_idx] = new_board[new_idx], new_board[zero_idx]
                
                if tuple(new_board) not in visited:
                    depth = current.depth + 1
                    cost = depth + manhattan_distance(new_board, goal)
                    heapq.heappush(pq, PuzzleState(new_board, current, move, depth, cost))
                    
    return -1

# Example usage
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print("Moves to solve:", a_star_8_puzzle(start_state, goal_state))