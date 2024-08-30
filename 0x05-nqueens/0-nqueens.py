#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. This is a program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This is done by checking if there is a queen in the same column,
    or on the diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem and print all solutions.
    Each solution is represented as a list of lists, where each sublist
    represents the row and column of a queen on the board.
    """
    def backtrack(row, board):
        if row == N:
            # All N queens are placed successfully
            print([[i, board[i]] for i in range(N)])
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1, board)
                    # Remove the queen for backtracking

    board = [-1] * N
    backtrack(0, board)


if __name__ == "__main__":
    # Check if the correct number of arguments was provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
