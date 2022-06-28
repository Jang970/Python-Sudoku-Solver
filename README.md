# Python-Sudoku-Solver
Implementing a sudoku solver in python using backtracking and recursion

Here I implemented a sudoku solver which will check and place a number from 1 to 9 in an empty slot from a given sudoku puzzle.
It will first check if the current guess is valid and if it is valid, then recursively solve the puzzle
If the guess is invalid however, it will reset that slot and make another guess.
If all guesses have been used and is still invalid, then the puzzle must be unsolvable.
