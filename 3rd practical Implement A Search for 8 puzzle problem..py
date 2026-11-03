
def winner(board):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def terminal(board):
    return winner(board) is not None or " " not in board


def utility(board):
    w = winner(board)

    if w == "X":
        return 1
    if w == "O":
        return -1

    return 0


def alphabeta(board, maximizing, alpha, beta):
    if terminal(board):
        return utility(board)

    if maximizing:
        value = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                value = max(
                    value,
                    alphabeta(board, False, alpha, beta)
                )

                board[i] = " "

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

        return value

    else:
        value = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                value = min(
                    value,
                    alphabeta(board, True, alpha, beta)
                )

                board[i] = " "

                beta = min(beta, value)

                if alpha >= beta:
                    break

        return value


def best_move(board):
    best = None
    best_val = -float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            val = alphabeta(
                board,
                False,
                -float("inf"),
                float("inf")
            )

            board[i] = " "

            if val > best_val:
                best = i
                best_val = val

    return best, best_val


# Current Tic-Tac-Toe board
board = [
    "X", "O", "X",
    " ", "O", " ",
    " ", " ", " "
]

move, value = best_move(board)

print("Best move index:", move)
print("Minimax value:", value)
