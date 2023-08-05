#!/usr/bin/python3
"""
N Queens Problem Solver

Usage: nqueens N

This program solves the N Queens problem by placing N non-attacking queens on an N×N chessboard.

Arguments:
    N (int): The size of the chessboard and the number of queens.

Example:
    To solve the 4 Queens problem:
    $ ./nqueens.py 4

    To solve the 6 Queens problem:
    $ ./nqueens.py 6
"""

import sys


def is_safe(board, row, col):
    '''Check if it's safe to place a queen at board[x][y]'''
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def nqueens(board, row):
    '''Use backtracking to find all solutions'''
    if row == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            nqueens(board, row + 1)
            board[row][col] = 0


def solve_nqueens(N):
    '''Solve the N Queens problem'''
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    nqueens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
