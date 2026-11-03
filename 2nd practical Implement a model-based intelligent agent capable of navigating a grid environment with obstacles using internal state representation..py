class ModelBasedAgent:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.internal_state = set()  # Stores visited locations

    def perceive_and_act(self, current_pos, obstacles, goal):
        self.internal_state.add(current_pos)
        if current_pos == goal:
            return "Goal Reached"
        x, y = current_pos
        possible_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        valid_moves = [
            m for m in possible_moves 
            if 0 <= m[0] < self.grid_size and 0 <= m[1] < self.grid_size 
            and m not in obstacles and m not in self.internal_state
        ]
        if valid_moves:
            return valid_moves[0]  # Move to the first valid unvisited state
        return "Stuck"

# Example usage
agent = ModelBasedAgent(grid_size=4)
obstacles = {(1, 1), (2, 2)}
pos = (0, 0)
goal = (3, 3)

for step in range(10):
    print(f"Step {step}: Current Position {pos}")
    action = agent.perceive_and_act(pos, obstacles, goal)
    if action == "Goal Reached" or action == "Stuck":
        print(action)
        break
    pos = action
    