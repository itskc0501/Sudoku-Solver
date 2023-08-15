'''

This Project Aims to create a Sudoku Solver using the Back Tracking Algorithm.
I have used the tkinter library to obtain the GUI of the program.

'''

import tkinter as tk

class SudokuSolver:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        block = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i] |= (1 << num)
                    cols[j] |= (1 << num)
                    p = self.blockcheck(i, j)
                    block[p] |= (1 << num)

        self.backtrack(board, 0, 0, rows, cols, block)

    def backtrack(self, board, i, j, rows, cols, block):
        if j == 9:
            i += 1
            j = 0
        if i == 9:
            return True

        if board[i][j] != '.':
            return self.backtrack(board, i, j + 1, rows, cols, block)
        else:
            for s in range(1, 10):
                p = self.blockcheck(i, j)
                if (rows[i] & (1 << s)) or (cols[j] & (1 << s)) or (block[p] & (1 << s)):
                    continue
                else:
                    rows[i] |= (1 << s)
                    cols[j] |= (1 << s)
                    block[p] |= (1 << s)
                    board[i][j] = str(s)
                    if self.backtrack(board, i, j + 1, rows, cols, block):
                        return True
                    else:
                        rows[i] &= ~(1 << s)
                        cols[j] &= ~(1 << s)
                        block[p] &= ~(1 << s)
                        board[i][j] = '.'
            return False

    def blockcheck(self, i, j):
        if i >= 0 and i < 3:
            if j >= 0 and j < 3:
                return 0
            elif j >= 3 and j < 6:
                return 1
            else:
                return 2
        elif i >= 3 and i < 6:
            if j >= 0 and j < 3:
                return 3
            elif j >= 3 and j < 6:
                return 4
            else:
                return 5
        else:
            if j >= 0 and j < 3:
                return 6
            elif j >= 3 and j < 6:
                return 7
            else:
                return 8

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry('330x370')
        self.create_widgets()

    def create_widgets(self):
        self.filledBoard = [[tk.StringVar(self.root) for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 20))
                entry.grid(row=row, column=col)
                self.filledBoard[row][col] = entry

        solve_button = tk.Button(self.root, text='Solve', command=self.solve_sudoku)
        solve_button.grid(column=3, row=20)

    def solve_sudoku(self):
        # Get input puzzle from GUI
        puzzle = []
        for row in range(9):
            row_data = []
            for col in range(9):
                value = self.filledBoard[row][col].get()
                if value == "":
                    value = "."
                row_data.append(value)
            puzzle.append(row_data)

        # Create SudokuSolver object and solve the puzzle
        solver = SudokuSolver()
        solver.solveSudoku(puzzle)

        # Update GUI with solved puzzle
        for row in range(9):
            for col in range(9):
                self.filledBoard[row][col].delete(0, tk.END)
                self.filledBoard[row][col].insert(0, puzzle[row][col])

#The Main Implementation of the program is given below. 
#Fill the boxes with some input (correct input) and click 'Solve' to get the final output.

if __name__ == '__main__':
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
