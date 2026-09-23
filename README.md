# Tic-Tac-Toe: Minimax vs Alpha-Beta Pruning

## SLE-2 Profiling Project

**Course:** 02AML204 — Introduction to Artificial Intelligence  
**Student:** Ratan Ranjeet Sankpal  
**PRN:** 25UAM080  
**Date:** 22 September 2026

## Project Overview

This project compares two game-tree search algorithms for **optimal move selection in 3×3 Tic-Tac-Toe**:

1. **Minimax** — plain full game-tree search.
2. **Minimax with Alpha-Beta Pruning** — Minimax optimized by pruning branches that cannot affect the final decision.

The uploaded SLE-2 report describes the same experiment and uses Python's `cProfile`, `time.perf_counter()`, and manual recursive-call/node counting for profiling. fileciteturn0file0L8-L20

## Files

- `tictactoe_minimax_alphabeta.py` — Python implementation of both algorithms and the experiment driver.
- `README.md` — project description and usage instructions.
- `contribution_log.md` — record of AI and student contributions.

## Algorithms

### 1. Minimax

Minimax explores the possible game states recursively and selects the move that gives the best game-theoretic result.

### 2. Alpha-Beta Pruning

Alpha-Beta pruning uses the same Minimax evaluation but skips branches that cannot improve the current result. The report notes that it preserves the same optimal move while reducing the number of explored nodes. fileciteturn0file0L77-L93

## How to Run

Make sure Python 3 is installed.

```bash
python tictactoe_minimax_alphabeta.py
```

The program tests three board states:

- 3 empty cells — best/near-end case
- 5 empty cells — average/mid-game case
- 9 empty cells — worst/empty-board case

The experiment design and number of runs are documented in the report. fileciteturn0file0L21-L36

## Profiling

The program uses:

- `time.perf_counter()` for execution-time measurement.
- Manual node counters for recursive calls.
- Python's built-in `cProfile` for call-graph profiling.

The report used cProfile because the py-spy binary could not be installed in the offline sandbox, and it provides the exact py-spy command for reproducing the flame graph on a normal machine. fileciteturn0file0L13-L20

To enable the cProfile output in this code, uncomment:

```python
profile_worst_case()
```

at the bottom of the Python file.

## Reported Results

The SLE-2 report recorded the following measurements:

| Test Case | Algorithm | Avg. Time (ms) | Nodes Expanded | Move |
|---|---|---:|---:|---|
| 3 empty cells | Minimax | 0.0165 | 10 | Cell 6 |
| 3 empty cells | Alpha-Beta | 0.0154 | 8 | Cell 6 |
| 5 empty cells | Minimax | 0.1763 | 149 | Cell 8 |
| 5 empty cells | Alpha-Beta | 0.0816 | 58 | Cell 8 |
| 9 empty cells | Minimax | 609.0264 | 549,945 | Cell 0 |
| 9 empty cells | Alpha-Beta | 24.9258 | 20,865 | Cell 0 |

These values are taken directly from the uploaded SLE-2 report. fileciteturn0file0L55-L62

The report states that both algorithms selected the same move in all three cases, while Alpha-Beta expanded substantially fewer nodes. fileciteturn0file0L81-L93

## Complexity

### Minimax

Worst-case time complexity:

**O(b^d)**

where:

- `b` = branching factor
- `d` = search depth

### Alpha-Beta

Worst-case complexity remains:

**O(b^d)**

With good move ordering, the effective search can approach:

**O(b^(d/2))**

as discussed in the report. fileciteturn0file0L89-L103

## Conclusion

For this Tic-Tac-Toe experiment, Alpha-Beta pruning reduced the number of recursive states explored while maintaining the same game-theoretic result as plain Minimax. The difference became much larger on the empty board. fileciteturn0file0L116-L128

## AI Contribution

The original report states that Claude (Anthropic) helped with the code structure, profiling/driver scripts, chart and flame-graph scripts, and report layout. It also states that the student selected the test cases, ran the experiments, checked the results, and wrote the justification and conclusion based on the measured results. fileciteturn0file0L105-L115
