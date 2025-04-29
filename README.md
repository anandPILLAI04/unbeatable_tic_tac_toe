# Unbeatable Tic Tac Toe

This project is a command-line implementation of the classic Tic Tac Toe game with an **unbeatable AI** opponent using the **Minimax algorithm**. The AI evaluates all possible game states to ensure it never loses — it will always win or draw.

## Table of Contents

- [Overview](#overview)
- [How the AI Works](#how-the-ai-works)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Running the Game](#running-the-game)
- [Example Gameplay](#example-gameplay)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Author](#author)

---

## Overview

This project demonstrates how artificial intelligence can be applied to classic games using game theory. The goal is to show how an optimal decision-making algorithm like **Minimax** ensures a flawless game from the computer's side. It's an educational and fun project that also serves as a solid introduction to game AI.

## How the AI Works

The **Minimax algorithm** is used to simulate all possible moves of both the player and the computer:
- Each move is scored: `+1` for a win, `-1` for a loss, and `0` for a draw.
- The computer assumes that the opponent (player) plays optimally.
- It recursively explores all game states and always selects the move with the highest score.

This guarantees that:
- The AI never loses.
- The AI always chooses the optimal path — win if possible, otherwise draw.

---

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/anandPILLAI04/unbeatable_tic_tac_toe.git
cd unbeatable_tic_tac_toe
