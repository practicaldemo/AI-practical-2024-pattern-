
N = 8
board = [-1] * N


def is_safe(row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        # Same column
        if previous_col == col:
            return False

        # Same diagonal
        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True


def solve(row):
    # All queens are placed
    if row == N:
        return True

    # Try every column
    for col in range(N):
        if is_safe(row, col):
            board[row] = col

            # Place queen in next row
            if solve(row + 1):
                return True

            # Backtrack
            board[row] = -1

    return False


# Solve the problem
if solve(0):
    print("Solution found:")

    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution found")
