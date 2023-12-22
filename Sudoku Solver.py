from collections import deque
import copy

class SudokuSolverDFS:
    def __init__(self, board):
        self.board = board
        self.size = 9

    def is_valid(self, row, col, num):
        if num in self.board[row] or num in [self.board[i][col] for i in range(self.size)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False


class SudokuSolverBFS:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.queue = deque()

    def is_valid(self, board, row, col, num):
        # Check if the number is already in the row, column, or 3x3 box
        if num in board[row] or num in [board[i][col] for i in range(self.size)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def find_empty(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    return i, j
        return None

    def solve(self):
        self.queue.append(copy.deepcopy(self.board))
        while self.queue:
            current_board = self.queue.popleft()
            empty_cell = self.find_empty(current_board)
            if not empty_cell:
                return current_board
            row, col = empty_cell
            for num in range(1, 10):
                if self.is_valid(current_board, row, col, num):
                    new_board = copy.deepcopy(current_board)
                    new_board[row][col] = num
                    self.queue.append(new_board)
        return None


def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def user_choice():
    while True:
        choice = input("Choose the solving method (DFS/BFS): ").strip().upper()
        if choice in ['DFS', 'BFS']:
            return choice
        else:
            print("Invalid input. Please enter 'DFS' or 'BFS'.")


def solve_sudoku_based_on_choice(board, choice):
    print("Original Sudoku:")
    print_sudoku(board)
    if choice == 'DFS':
        solver = SudokuSolverDFS(copy.deepcopy(board)) # Use a copy to preserve the original board
        if solver.solve():
            print("\nSudoku Solved with DFS:")
            print_board(solver.board) # Ensure this call matches the function definition
        else:
            print("No solution exists using DFS.")
    elif choice == 'BFS':
        solver = SudokuSolverBFS(board)
        solution = solver.solve()
        if solution:
            print("\nSudoku Solved with BFS:")
            print_board(solution) # And this one
        else:
            print("No solution exists using BFS.")

if __name__ == "__main__":
    difficulty = input("Enter difficulty (easy/medium/hard): ").lower()

    easy_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    medium_board = [
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [9, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 5, 0, 6, 1, 0],
        [6, 0, 0, 0, 0, 4, 0, 0, 0]
    ]

    hard_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]

    if difficulty == 'easy':
        sudoku_board = easy_board
    elif difficulty == 'medium':
        sudoku_board = medium_board
    elif difficulty == 'hard':
        sudoku_board = hard_board
    else:
        print("Invalid difficulty. Defaulting to easy.")
        sudoku_board = easy_board

    user_input = user_choice()
    solve_sudoku_based_on_choice(sudoku_board, user_input)
