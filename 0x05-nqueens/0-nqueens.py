#!/usr/bin/python3
"""Solution to the N-Queens puzzle"""
import sys

def print_board(board, n):
    """Prints allocated positions to the queen"""
    b = []
    for i in range(n):
        b.append([i, board[i]])
    print(b)

def safe_position(board, row, col):
    """Determines whether the position is safe for the queen"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def determine_positions(board, row, n):
    """Recursively finds all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)
    else:
        for col in range(n):
            if safe_position(board, row, col):
                board[row] = col
                determine_positions(board, row + 1, n)

def create_board(size):
    """Generates the board"""
    return [-1] * size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = create_board(n)
    determine_positions(board, 0, n)
