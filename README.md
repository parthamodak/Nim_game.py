# Nim Game

A simple command-line implementation of the classic Nim game written in Python.

## Overview

This is a single-player Nim game where the player takes stones from a pile. The objective is to remove all stones from the pile by taking 1, 2, or 3 stones per turn.

## How to Play

1. Run the program:
   ```bash
   python Practice.py
   ```

2. Enter the initial number of stones when prompted

3. On each turn:
   - The program displays the number of stones remaining
   - Enter how many stones you want to take (1, 2, or 3)
   - The program validates your input and updates the pile

4. The game continues until all stones are removed

## Features

- **Input Validation**: Only accepts valid numbers (1-3 stones)
- **Error Handling**: Handles invalid input gracefully with try-except
- **Game Loop**: Continues until all stones are taken
- **Clear Feedback**: Shows remaining stones and invalid move messages

## Requirements

- Python 3.x

## Files

- `Practice.py` - Main Nim game implementation

## Example Gameplay

```
Enter the number of stones in the pile: 10
There are 10 stones in the pile.

Your turn.
Stones left: 10
you can take 1, 2, or 3 stones: 2
Stones left: 8
...
```

## Code Structure

- Uses `try-except` for input validation
- `while` loop to continue game until stones are gone
- Input validation to ensure only 1-3 stones can be taken
- Decrements stone count after each valid move
