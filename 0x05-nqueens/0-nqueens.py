#!/usr/bin/python3
"""
0-nqueens.py
"""
import sys


def is_safe(board, row, col):
    """
    is_safe
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False

    return True


def solve_n_queens_util(board, row, n, solutions):
    """
    solve_n_queens_util
    """
    if row == n:
        solutions.append(board[:])

        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)


def solve_n_queens(n):
    """
    solve_n_queens
    """
    board = [-1] * n
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except (ValueError):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_n_queens(n)

    for solution in solutions:
        print([[i, col] for i, col in enumerate(solution)])
