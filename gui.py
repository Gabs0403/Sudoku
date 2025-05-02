from tkinter import *
import utils as utils


entries = []
sudoku_puzzle = []
solved_puzzle = []

def initiate_gui():
    main_window = Tk()
    main_window.title("Sudoku")
    main_window.geometry("800x800")
    main_window.configure(bg="grey")
    main_window.resizable(False, False)

    grid_frame = Frame(main_window)
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    generate_grid(grid_frame)

    button = Button(main_window, text="New Game", width=10, command=lambda: load_new_game())
    button.place(relx=0.4, rely=0.8, anchor="center")
    button = Button(main_window, text="Check", width=10)
    button.place(relx=0.6, rely=0.8, anchor="center")
    button.configure(command=check_puzzle)

    main_window.mainloop()

def generate_grid(frame):
    global entries, sudoku_puzzle, solved_puzzle

    try:
        sudoku_puzzle = utils.load_random_puzzle("puzzles")
        solved_puzzle = utils.get_solution(sudoku_puzzle)
        print(solved_puzzle)
    except Exception as e:
        print("Failed to load puzzle:", e)
        return

    for i in range(9):
        row = []
        for j in range(9):
            entry = Entry(
                frame,
                width=2,
                font=("Courier", 24),
                justify="center",
                relief="solid",  # gives a solid border
                bd=1  # thin internal border
            )
            # Add extra padding between 3x3 blocks
            padx = 4 if j % 3 == 0 and j != 0 else 0
            pady = 4 if i % 3 == 0 and i != 0 else 0

            entry.grid(row=i, column=j, padx=(padx, 0), pady=(pady, 0))

            if sudoku_puzzle[i][j] != 0:
                entry.insert(0, sudoku_puzzle[i][j])
                entry.config(state='disabled', disabledforeground='black')
            # Add the Entry widget to the row
            row.append(entry)

            # After finishing the row, append the row to the main list
        entries.append(row)

def load_new_game():
    global entries, sudoku_puzzle, solved_puzzle

    try:
        sudoku_puzzle = utils.load_random_puzzle("puzzles")
        solved_puzzle = utils.get_solution(sudoku_puzzle)
        print(solved_puzzle)
    except Exception as e:
        print("Failed to load puzzle:", e)
        return None, None

    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            entry.config(state='normal')
            entry.delete(0, END)

            if sudoku_puzzle[i][j] != 0:
                entry.insert(0, sudoku_puzzle[i][j])
                entry.config(state='disabled', disabledforeground='black')
            else:
                entry.config(bg='white')  # Reset background
    return sudoku_puzzle, solved_puzzle

def check_puzzle():
    board = get_user_board(entries)  # user's answers
    correct = True

    for i in range(9):
        for j in range(9):
            entry_val = board[i][j]
            correct_val = solved_puzzle[i][j]

            if entry_val == correct_val:
                entries[i][j].configure(bg='lightgreen')
            else:
                if entries[i][j]['state'] != 'disabled':  # don't color original clues
                    entries[i][j].configure(bg='lightcoral')
                correct = False

    return correct

def is_valid_group(group):
    return sorted(group) == list(range(1, 10))

def get_user_board(entries):
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            try:
                num = int(value)
            except ValueError:
                num = 0
            row.append(num)
        board.append(row)
    return board


