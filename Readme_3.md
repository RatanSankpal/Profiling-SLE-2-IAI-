Tic Tac Toe AI – BFS and DFS

1. Project Description

Tic Tac Toe AI is a Python-based game where a human player plays Tic Tac Toe against an AI agent on a 3 × 3 board.

The AI uses two state-space search techniques:

- BFS (Breadth-First Search) – explores the game tree level by level.
- DFS (Depth-First Search) – follows one path deeply and backtracks.

The system finds winning moves without using a heuristic.

---

2. C4 Model

Level 1 – System Context Diagram

System

Tic Tac Toe AI System

User

Player

Description

The Player enters a move using a cell number from 1–9. The Tic Tac Toe system processes the move, updates the board and provides the game result.

The system displays the board and result through a console or GUI.

Interaction

+---------+          +-------------------------+
| Player  | -------->| Tic Tac Toe AI System  |
+---------+  Move    +-------------------------+
     ^                         |
     |                         |
     +------ Board/Result -----+

No external services are required.

---

Level 2 – Container Diagram

The Tic Tac Toe AI System is divided into five main containers:

1. Input Module

- Reads the player's move.
- Validates cell numbers from 1–9.

2. Game Controller

- Controls the game turn loop.
- Applies game rules.
- Checks for win or draw.

3. AI Agent

- Selects the computer's move.
- Uses BFS or DFS to search game states.

4. Game Board

- Stores the 3 × 3 board.
- Handles legal moves.
- Supports "make_move()" and "undo_move()".

5. Output Module

- Displays the board.
- Shows moves played.
- Displays the final result.

Container Structure

                    +----------------+
                    |    Player      |
                    +-------+--------+
                            |
                            v
                    +---------------+
                    | Input Module  |
                    +-------+-------+
                            |
                            v
                    +-------------------+
                    | Game Controller   |
                    +----+----------+---+
                         |          |
                         v          v
                +------------+   +-----------+
                | Game Board |   | AI Agent  |
                +------------+   +-----+-----+
                                      |
                                +-----+-----+
                                | BFS / DFS |
                                +-----------+
                         |
                         v
                  +--------------+
                  | Output Module|
                  +--------------+

---

Level 3 – Component Diagram

The AI Agent is divided into smaller components.

1. Successor Generator

- Finds empty cells.
- Generates possible next board states.

2. Frontier

Stores the board states waiting to be checked.

- BFS: uses a Queue.
- DFS: uses a Stack or recursion.

3. Goal Test

- Checks whether the current board is an AI winning state.
- A player win or draw is treated as a dead end.

4. Move Selector

- Finds a winning path.
- Returns the first move of that path.

Component Structure

                    +----------------+
                    |    AI Agent    |
                    +-------+--------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
     +---------------+ +-----------+ +-----------+
     |   Successor   | | Frontier  | | Goal Test |
     |   Generator   | | Queue/Stack| +-----------+
     +---------------+ +-----------+
             |              |
             +------+-------+
                    v
             +-------------+
             | Move        |
             | Selector    |
             +-------------+

---

Level 4 – Code Diagram / Code Level

The main classes and functions used in the system are:

Class / Function| Responsibility
"Board"| Stores the 3 × 3 grid and manages moves
"bfs(board, player)"| Performs Breadth-First Search
"dfs(board, player)"| Performs Depth-First Search
"is_goal(board)"| Checks whether the AI has won
"best_move(board, method)"| Selects the AI's best available move
"play_game()"| Controls the complete game loop
"print_board(board)"| Displays the current board

Code-Level Flow

play_game()
     |
     +----> Board
     |
     +----> Player Move
     |
     +----> best_move()
               |
          +----+----+
          |         |
         BFS       DFS
          |         |
       Queue      Stack/
                  Recursion
          |         |
          +----+----+
               |
          is_goal()
               |
          Move Selected
               |
          Board Updated
               |
          print_board()

---

3. BFS and DFS Comparison

BFS| DFS
Uses a queue| Uses a stack/recursion
Searches level by level| Searches deeply
Finds the shortest winning path| Finds the first winning line
Requires more memory| Generally uses less memory

---

4. Project Structure

Tic-Tac-Toe-AI/
│
├── tic_tac_toe.py
├── README.md
├── contribution_log.md
└── requirements.txt

---

5. How to Run

1. Clone or download the repository.
2. Open the project in VS Code or Python.
3. Run the main Python file.
4. Enter a cell number from 1 to 9.
5. Play against the AI.

---

6. AI Contribution

AI assistance was used for drafting diagram layouts, C4 model descriptions and documentation wording.

The implementation, testing and understanding of the Tic Tac Toe AI system were done by the project contributor.

---

7. Conclusion

The C4 model represents the Tic Tac Toe AI system at four levels:

1. Context – shows the Player and the complete system.
2. Container – shows the major modules of the system.
3. Component – shows the internal components of the AI Agent.
4. Code – shows the classes and functions implementing the system.

This structure makes the BFS/DFS-based Tic Tac Toe system easier to understand, test and extend.
