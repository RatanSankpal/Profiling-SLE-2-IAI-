"""
Tic-Tac-Toe: BFS vs DFS
SLE-2 Profiling Experiment
PRN: 25UAM080
Name: Ratan Ranjeet Sankpal

This version replaces Minimax/Alpha-Beta with:
1. DFS - depth-first exhaustive game-tree search with bottom-up minimax backup.
2. BFS - breadth-first exhaustive game-tree generation followed by bottom-up backup.

Profiling is done externally with py-spy (a sampling profiler) instead of
cProfile. See the "How to profile with py-spy" section at the bottom.
"""

import time
from collections import deque

WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)

def get_moves(board):
    """Return all empty cell indexes."""
    return [i for i, cell in enumerate(board) if cell == " "]

def winner(board):
    """Return X, O, or None depending on the game state."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board):
    """Return True if no empty cells remain."""
    return " " not in board

def terminal_score(board):
    """Return +1 for O win, -1 for X win, 0 for draw, else None."""
    result = winner(board)
    if result == "O":
        return 1
    if result == "X":
        return -1
    if is_full(board):
        return 0
    return None

# ---------------- DFS ----------------
dfs_nodes = 0

def dfs_value(board, maximizing):
    """Depth-first exhaustive game-tree search with minimax-style backup."""
    global dfs_nodes
    dfs_nodes += 1

    score = terminal_score(board)
    if score is not None:
        return score

    scores = []
    player = "O" if maximizing else "X"
    for move in get_moves(board):
        next_board = list(board)
        next_board[move] = player
        scores.append(dfs_value(tuple(next_board), not maximizing))

    return max(scores) if maximizing else min(scores)

def best_move_dfs(board, player="O"):
    """Return the game-theoretically best move using DFS."""
    best_score = -float("inf") if player == "O" else float("inf")
    best_move = None

    for move in get_moves(board):
        next_board = list(board)
        next_board[move] = player
        score = dfs_value(tuple(next_board), player == "X")

        if player == "O":
            if score > best_score:
                best_score, best_move = score, move
        else:
            if score < best_score:
                best_score, best_move = score, move

    return best_move

# ---------------- BFS ----------------
bfs_nodes = 0

def bfs_value(root_board, root_player="O"):
    """
    Breadth-first generation of the complete game tree.
    Values are then backed up from the deepest level to the root.
    """
    global bfs_nodes

    queue = deque()
    nodes = [(tuple(root_board), root_player, -1, None)]
    queue.append(0)

    children = {}

    while queue:
        node_id = queue.popleft()
        board, player, parent_id, move = nodes[node_id]
        bfs_nodes += 1

        if terminal_score(board) is not None:
            children[node_id] = []
            continue

        child_ids = []
        next_player = "X" if player == "O" else "O"

        for move_index in get_moves(board):
            next_board = list(board)
            next_board[move_index] = player
            child_id = len(nodes)
            nodes.append(
                (tuple(next_board), next_player, node_id, move_index)
            )
            queue.append(child_id)
            child_ids.append(child_id)

        children[node_id] = child_ids

    # Bottom-up backup after BFS has generated every level.
    values = [None] * len(nodes)

    for node_id in range(len(nodes) - 1, -1, -1):
        board, player, parent_id, move = nodes[node_id]
        score = terminal_score(board)

        if score is not None:
            values[node_id] = score
        else:
            child_values = [values[c] for c in children[node_id]]
            values[node_id] = (
                max(child_values) if player == "O" else min(child_values)
            )

    return values[0], nodes, values

def best_move_bfs(board, player="O"):
    """Return the game-theoretically best move using BFS."""
    _, nodes, values = bfs_value(board, player)

    root_children = [
        node_id for node_id, node in enumerate(nodes) if node[2] == 0
    ]

    if player == "O":
        chosen = max(root_children, key=lambda i: (values[i], -nodes[i][3]))
    else:
        chosen = min(root_children, key=lambda i: (values[i], nodes[i][3]))

    return nodes[chosen][3]

# ---------------- Experiment ----------------

def run_experiment(board):
    """Run BFS and DFS and display timing and node counts."""
    global dfs_nodes, bfs_nodes

    dfs_nodes = 0
    start = time.perf_counter()
    move_dfs = best_move_dfs(board.copy())
    time_dfs = (time.perf_counter() - start) * 1000
    nodes_dfs = dfs_nodes

    bfs_nodes = 0
    start = time.perf_counter()
    move_bfs = best_move_bfs(board.copy())
    time_bfs = (time.perf_counter() - start) * 1000
    nodes_bfs = bfs_nodes

    print("Board:", board)
    print("DFS -> Move:", move_dfs, "Time:", round(time_dfs, 4),
          "ms, Nodes:", nodes_dfs)
    print("BFS -> Move:", move_bfs, "Time:", round(time_bfs, 4),
          "ms, Nodes:", nodes_bfs)
    print()

def worst_case_workload(repeats=200):
    """
    Repeatedly solve the empty-board (worst-case) game tree with both
    DFS and BFS.

    A single empty-board solve finishes in well under a second, which is
    too fast for a sampling profiler like py-spy to catch enough stack
    samples. Looping it `repeats` times gives py-spy a long-running
    process to attach to and sample from.
    """
    for _ in range(repeats):
        board = [" "] * 9
        best_move_dfs(board.copy())
        best_move_bfs(board.copy())

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

    print("===== Tic-Tac-Toe BFS vs DFS =====\n")

    for case in test_cases:
        run_experiment(case)

    # Uncomment to run the extended workload that py-spy can sample.
    # print("Running worst-case workload for py-spy profiling...")
    # worst_case_workload(repeats=200)

"""
How to profile with py-spy
---------------------------
py-spy is a sampling profiler that runs OUTSIDE your Python process and
periodically snapshots its call stack, so nothing is imported into the
script itself.

1. Install it:
       pip install py-spy

2. Uncomment the `worst_case_workload(repeats=200)` call above (or raise
   `repeats` further) so the script runs long enough to sample. Adjust
   `repeats` until the run takes a few seconds.

3. Record a flamegraph while the script runs:
       py-spy record -o profile.svg -- python tictactoe_bfs_dfs_pyspy.py
   Open profile.svg in a browser afterward.

4. Or watch live top-like function stats while it runs:
       py-spy top -- python tictactoe_bfs_dfs_pyspy.py

5. To profile a script that's already running, find its PID and attach:
       py-spy record -o profile.svg --pid <PID>
   (On Linux this may need sudo or ptrace permissions.)

py-spy needs no code changes to the functions themselves - it samples
whatever is on the call stack of the live process, so `dfs_value`,
`best_move_dfs`, `bfs_value`, and `best_move_bfs` will all show up in
the flamegraph/top output automatically once the workload runs long
enough to be sampled.
"""
