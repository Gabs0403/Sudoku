from tkinter import *
import utils as utils

entries = []

def initiate_gui():
    main_window = Tk()
    main_window.title("Sudoku")
    main_window.geometry("800x800")
    main_window.configure(bg="grey")
    main_window.resizable(False, False)

    grid_frame = Frame(main_window)
    grid_frame.place(relx=0.5, rely=0.5, anchor='center')

    generate_grid(grid_frame)

    button = Button(main_window, text="New Game", width=10, command=lambda: generate_grid(grid_frame))
    button.place(relx=0.35, rely=0.8, anchor="center")
    button = Button(main_window, text="Check", width=10)
    button.place(relx=0.65, rely=0.8, anchor="center", command= check_puzzle)


    main_window.mainloop()

def generate_grid(frame):
    global entries

    # Clear previous widgets if they exist
    for row in entries:
        for entry in row:
            entry.destroy()
    entries.clear()

    try:
        sudoku = utils.load_random_puzzle("puzzles")
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

            if sudoku[i][j] != 0:
                entry.insert(0, sudoku[i][j])
                entry.config(state='disabled', disabledforeground='black')
            # Add the Entry widget to the row
            row.append(entry)

            # After finishing the row, append the row to the main list
        entries.append(row)

def check_puzzle():
    global entries
