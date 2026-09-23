# Tic-Tac-Toe: BFS vs DFS

## SLE-2 Profiling Project

**Course:** 02AML204 — Introduction to Artificial Intelligence  
**Student:** Ratan Ranjeet Sankpal  
**PRN:** 25UAM080  
**Date:** 23 September 2026

## Project Overview

This project compares two uninformed game-tree search algorithms for **optimal move selection in 3×3 Tic-Tac-Toe**:

1. **DFS (Depth-First Search)** — recursively explores a complete game-tree branch before moving to the next branch, with values backed up from terminal states.
2. **BFS (Breadth-First Search)** — generates the game tree level by level and then performs bottom-up value backup to determine the game-theoretic value of the root and its legal moves.

The earlier version of the project used plain Minimax and Minimax with Alpha-Beta pruning. This version removes Alpha-Beta pruning and changes the algorithms throughout the project to BFS and DFS.

## Files

- `tictactoe_bfs_dfs.py` — Python implementation and experiment driver.
- `README.md` — project description and usage instructions.
- `contribution_log.md` — record of AI and student contributions.
- `SLE2_25UAM080_TicTacToe_BFS_DFS.pdf` — updated profiling report.

## Algorithms

### DFS

DFS visits one branch of the game tree as deeply as possible before backtracking. For this project, every reachable continuation is evaluated, and the values are backed up using MAX for O and MIN for X.

### BFS

BFS visits the game tree level by level. Because a queue alone does not directly provide a game-theoretic move, this implementation first generates the complete tree with BFS and then backs up values from the deepest nodes to the root.

This keeps the comparison focused on **search order** rather than introducing pruning or heuristic cut-offs.

## Profiling

The experiment uses:

- `time.perf_counter()` for execution-time measurement.
- Manual node counters for the number of game-tree states visited/generated.
- Python's built-in `cProfile` for call-graph profiling.

To reproduce the profiler output, uncomment `profile_worst_case()` at the bottom of the Python file and run:

```bash
python tictactoe_bfs_dfs.py
```

For py-spy on a normal machine:

```bash
py-spy record -o flamegraph.svg --rate 100 -- python tictactoe_bfs_dfs.py
```

## Test Cases

- 3 empty cells — near-end / small search space
- 5 empty cells — mid-game search space
- 9 empty cells — empty-board / largest search space

Five runs were used for each algorithm and test case; the table below reports the average execution time.

## Measured Results

| Test Case | Algorithm | Avg. Time (ms) | Nodes Expanded | Move |
|---|---|---:|---:|---:|
| Best case (3 empty cells) | DFS | 0.0083 | 4 | Cell 8 |
| Best case (3 empty cells) | BFS | 0.0217 | 5 | Cell 8 |
| Average case (5 empty cells) | DFS | 0.2060 | 209 | Cell 8 |
| Average case (5 empty cells) | BFS | 0.3730 | 210 | Cell 8 |
| Worst case (9 empty cells) | DFS | 458.5446 | 549,945 | Cell 0 |
| Worst case (9 empty cells) | BFS | 1750.5920 | 549,946 | Cell 0 |

### Notes

- Node counts are deterministic for the implemented search procedures.
- Execution time can vary between computers and Python versions, so the reported timings are the measurements from this run.
- Both algorithms use exhaustive search and therefore return the same game-theoretic move for each tested board state.
- BFS uses substantially more memory than recursive DFS because it retains the generated tree until value backup is complete.
