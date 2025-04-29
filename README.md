# Unbeatable Tic Tac Toe

An interactive Tic Tac Toe game in Python featuring an **unbeatable AI** opponent powered by the Minimax algorithm. Play against the computer in your terminal or with a simple GUI and experience a flawless, optimal AI that will never lose.

---

## Table of Contents

1. [Demo](#demo)  
2. [Features](#features)  
3. [Game Rules](#game-rules)  
4. [How the AI Works](#how-the-ai-works)  
5. [Prerequisites](#prerequisites)  
6. [License](#license)  
7. [Acknowledgments](#acknowledgments)  

---

## Demo

![Gameplay Demo](assets/demo.gif)

*Play a round and watch the AI never make a mistake!*  

---

## Features

- **Unbeatable AI**: Implements the Minimax algorithm to guarantee a win or draw.  
- **Dual Interfaces**: Choose between a terminal-based CLI or a minimal GUI for interactive play.  
- **AI Explanation Mode**: Step through the AI’s decision process to learn how Minimax evaluates moves.  
- **Configurable Difficulty**: Optionally limit search depth for adjustable challenge.  

---

## Game Rules

1. The board is a 3×3 grid.  
2. Two players alternate placing their symbol (X or O) in empty squares.  
3. The first player to align three of their symbols horizontally, vertically, or diagonally wins.  
4. If all squares are filled without a winning line, the game ends in a draw.  

---

## How the AI Works

The computer uses the **Minimax algorithm**, a decision rule for minimizing the possible loss in a worst-case scenario:

1. **Recursive Simulation**: The algorithm recursively simulates every possible move from the current board state.  
2. **Scoring**:  
   - Win for AI → +1  
   - Draw → 0  
   - Loss for AI → -1  
3. **Optimal Opponent Assumption**: Assumes the human player also plays optimally.  
4. **Move Selection**: Chooses the move with the highest minimax score (maximizes AI’s outcome).

This exhaustive search ensures the AI cannot be beaten; at best you can force a draw.

---

## Prerequisites

- Python 3.7 or higher  
- `tkinter` (for GUI mode; usually bundled with Python)  

---

## License

This project is released under the **MIT License**.  
See the [LICENSE](LICENSE) file for full terms and conditions.

---

## Acknowledgments

- Original Tic Tac Toe AI tutorials and algorithm write-ups on Minimax.  
- The Python open-source ecosystem for easy access to `tkinter` and rapid prototyping.  
- Community contributions and feedback that shaped the dual-interface design.  
