
import heapq

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Heuristic function: Manhattan Distance
def h(s):
    d = 0

    for i in range(9):
        if s[i] != 0:
            j = goal.index(s[i])

            d += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)

    return d


# A* Search Algorithm
def astar(start):

    # Priority queue: (f, g, state, path)
    q = [(h(start), 0, start, [])]

    # Set of visited states
    seen = set()

    while q:

        # Get state with minimum f value
        f, g, s, path = heapq.heappop(q)

        # Skip if already visited
        if s in seen:
            continue

        # Mark state as visited
        seen.add(s)

        # Check whether goal is reached
        if s == goal:
            return path + [s]

        # Find position of blank (0)
        z = s.index(0)

        # Convert position into row and column
        r, c = divmod(z, 3)

        # Possible moves: Down, Up, Right, Left
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            nr, nc = r + dr, c + dc

            # Check whether the move is valid
            if 0 <= nr < 3 and 0 <= nc < 3:

                # Find new position
                x = nr * 3 + nc

                # Create new state
                t = list(s)

                # Swap blank with adjacent tile
                t[z], t[x] = t[x], t[z]

                # Convert list back to tuple
                t = tuple(t)

                # Calculate f = g + h and add to queue
                heapq.heappush(
                    q,
                    (g + 1 + h(t), g + 1, t, path + [s])
                )


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


# Find solution
solution = astar(start)


# Display solution
print("Solution:")
print()

for s in solution:

    print(s[0:3])
    print(s[3:6])
    print(s[6:9])
    print()
