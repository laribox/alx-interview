#!/usr/bin/python3
import sys

def print_solution(board):
    """Prints a solution in the required format."""
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)

def is_safe(board, row, col):
    """Checks if a queen can be placed on board at (row, col)."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, n):
    """Uses backtracking to find all solutions for the N-Queens problem."""
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)

def main():
    """Main function to parse arguments and run the N-Queens solution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n  # Initialize the board
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    main()

