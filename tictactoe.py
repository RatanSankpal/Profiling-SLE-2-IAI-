"""
Tic-Tac-Toe: Minimax vs Alpha-Beta Pruning
SLE-2 Profiling Experiment
PRN: 25UAM080
Name: Ratan Ranjeet Sankpal
"""

import time
import cProfile
import pstats
import io


def get_moves(board):
    """Return all empty cell indexes."""
    return [i for i, cell in enumerate(board) if cell == " "]


def winner(board):
    """Return X, O, or None depending on the game state."""
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def is_full(board):
    """Return True if no empty cells remain."""
    return " " not in board


def minimax(board, maximizing):
    """Plain Minimax search."""
    global minimax_nodes
    minimax_nodes += 1

    result = winner(board)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if is_full(board):
        return 0

    moves = get_moves(board)

    if maximizing:
        best = -float("inf")

        for move in moves:
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best = max(best, score)

        return best

    best = float("inf")

    for move in moves:
        board[move] = "X"
        score = minimax(board, True)
        board[move] = " "
        best = min(best, score)

    return best


def minimax_ab(board, maximizing, alpha, beta):
    """Minimax search with Alpha-Beta pruning."""
    global alphabeta_nodes
    alphabeta_nodes += 1

    result = winner(board)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if is_full(board):
        return 0

    moves = get_moves(board)

    if maximizing:
        best = -float("inf")

        for move in moves:
            board[move] = "O"
            score = minimax_ab(board, False, alpha, beta)
            board[move] = " "
            best = max(best, score)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    best = float("inf")

    for move in moves:
        board[move] = "X"
        score = minimax_ab(board, True, alpha, beta)
        board[move] = " "
        best = min(best, score)
        beta = min(beta, best)

        if beta <= alpha:
            break

    return best


def best_move_minimax(board, player="O"):
    """Return the best move using plain Minimax."""
    best_score = -float("inf")
    best_move = None

    for move in get_moves(board):
        board[move] = player
        score = minimax(board, False)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def best_move_alphabeta(board, player="O"):
    """Return the best move using Alpha-Beta pruning."""
    best_score = -float("inf")
    best_move = None

    for move in get_moves(board):
        board[move] = player
        score = minimax_ab(board, False, -float("inf"), float("inf"))
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def run_experiment(board):
    """Run both algorithms and display timing and node counts."""
    global minimax_nodes, alphabeta_nodes

    minimax_nodes = 0
    start = time.perf_counter()
    move_a = best_move_minimax(board.copy())
    time_a = (time.perf_counter() - start) * 1000
    nodes_a = minimax_nodes

    alphabeta_nodes = 0
    start = time.perf_counter()
    move_b = best_move_alphabeta(board.copy())
    time_b = (time.perf_counter() - start) * 1000
    nodes_b = alphabeta_nodes

    print("Board:", board)
    print("Minimax     -> Move:", move_a, "Time:", round(time_a, 4),
          "ms, Nodes:", nodes_a)
    print("Alpha-Beta  -> Move:", move_b, "Time:", round(time_b, 4),
          "ms, Nodes:", nodes_b)
    print()


def profile_worst_case():
    """Profile the empty-board workload using cProfile."""
    board = [" "] * 9

    profiler = cProfile.Profile()
    profiler.enable()

    best_move_minimax(board.copy())
    best_move_alphabeta(board.copy())

    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(20)

    print("\n===== cProfile Output =====")
    print(stream.getvalue())


if __name__ == "__main__":
    test_cases = [
        ["X", "O", "X",
         "O", "O", "X",
         " ", "X", " "],   # 3 empty cells

        ["X", "O", " ",
         " ", "X", " ",
         "O", " ", " "],   # 5 empty cells

        [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]    # empty board
    ]

    print("===== Tic-Tac-Toe Minimax vs Alpha-Beta =====\n")

    for case in test_cases:
        run_experiment(case)

    # Uncomment to generate cProfile output for the worst-case workload.
    # profile_worst_case()
