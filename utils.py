import os
import random
import copy

def load_random_puzzle(folder="puzzles"):
    files = [f for f in os.listdir(folder) if f.endswith('.txt')]
    if not files:
        raise FileNotFoundError("No puzzle files found.")
    selected_file = random.choice(files)
    with open(os.path.join(folder, selected_file)) as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def get_solution(original_board):
    board_copy = copy.deepcopy(original_board)
    if solve_puzzle(board_copy):
        return board_copy
    return None  # no solution found

def solve_puzzle(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):  # Numbers 1–9
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_puzzle(board):
                return True

            board[row][col] = 0  # Backtrack

    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, row, col):
    # Check row
    if any(board[row][x] == num for x in range(9)):
        return False
    # Check column
    if any(board[x][col] == num for x in range(9)):
        return False
    # Check 3x3 box
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def available_space(board, row, col, num):
    return (
        not row_checking(board, row, num) and
        not column_checking(board, col, num) and
        not box_checking(board, row - row % 3, col - col % 3, num)
    )

def row_checking(board, row, num):
    return num in board[row]

def column_checking(board, col, num):
    return any(board[i][col] == num for i in range(9))

def box_checking(board, start_row, start_col, num):
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return True
    return False
