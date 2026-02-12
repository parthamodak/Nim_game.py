# Nim Game

A command-line implementation of the classic Nim game with an AI opponent written in Python.

## Overview

This is an interactive Nim game where the player competes against the computer. Both players take turns removing 1, 2, or 3 stones from a shared pile. The player who is forced to take the last stone loses the game.

## How to Play

1. Run the program:
   ```bash
   python nim_game.py
   ```

2. Enter the initial number of stones when prompted

3. On each turn:
   - The program displays the number of stones remaining
   - Enter how many stones you want to take (1, 2, or 3)
   - The computer automatically makes its move based on an optimal strategy
   - The game continues until all stones are removed

4. Win/Lose Conditions:
   - **You Win**: If the computer takes the last stone
   - **Computer Wins**: If you take the last stone

## Game Strategy

The computer uses a simple mathematical strategy based on modulo 4 arithmetic:
- If remaining stones % 4 == 0, the computer takes 1 stone
- Otherwise, the computer takes (remaining stones % 4) stones

This strategy aims to leave a multiple of 4 stones after each computer move, which gives the computer an advantage.

## Features

- **Input Validation**: Only accepts valid numbers (1-3 stones, and not more than available)
- **Error Handling**: Handles invalid input gracefully with try-except
- **AI Opponent**: Computer makes strategic moves
- **Real-time Feedback**: Shows remaining stones after each move
- **Interactive Gameplay**: Turn-based game loop

## Requirements

- Python 3.x

## Files

- `nim_game.py` - Main Nim game implementation with AI opponent

## Example Gameplay

```
Enter the number of stones in the pile: 12
There are 12 stones in the pile.

Your turn.
Stones left: 12
you can take 1, 2, or 3 stones: 3

Computer takes: 1
Stones left: 8

Your turn.
Stones left: 8
you can take 1, 2, or 3 stones: 2

Computer takes: 2
Stones left: 4

Your turn.
Stones left: 4
you can take 1, 2, or 3 stones: 1

Computer took the last stone. Computer wins!
```

## Code Structure

- Uses `try-except` for input validation
- `while` loop to continue game until stones are gone
- Input validation to ensure only 1-3 stones can be taken
- Decrements stone count after each valid move
