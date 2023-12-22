# Importing necessary modules
from collections import deque  # For implementing a queue in the BFS solver
import copy  # For creating deep copies of the Sudoku board

# Define a class for solving Sudoku using Depth-First Search (DFS)
class SudokuSolverDFS:
    def __init__(self, board):  # Constructor method
        self.board = board  # Store the Sudoku board in the instance
        self.size = 9  # Sudoku board size (9x9)

    def is_valid(self, row, col, num):  # Check if placing 'num' in board[row][col] is valid
        # Check if 'num' already exists in the given row or column
        if num in self.board[row] or num in [self.board[i][col] for i in range(self.size)]:
            return False
        # Calculate the starting indices of the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        # Check if 'num' exists in the 3x3 subgrid
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True  # Return True if 'num' can be placed in the board[row][col]

    def find_empty(self):  # Find an empty cell in the board
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:  # 0 denotes an empty cell
                    return i, j  # Return the position of the empty cell
        return None  # Return None if there are no empty cells

    def solve(self):  # Solve the Sudoku using DFS
        empty_cell = self.find_empty()  # Find the first empty cell
        if not empty_cell:
            return True  # If there are no empty cells, the Sudoku is solved
        row, col = empty_cell
        for num in range(1, 10):  # Try numbers from 1 to 9 in the empty cell
            if self.is_valid(row, col, num):  # Check if the number is valid
                self.board[row][col] = num  # Place the number in the empty cell
                if self.solve():  # Recursively solve the rest of the board
                    return True
                self.board[row][col] = 0  # Backtrack if placing 'num' doesn't lead to a solution
        return False  # Return False if no solution is found


# Define a class for solving Sudoku using Breadth-First Search (BFS)
class SudokuSolverBFS:
    def __init__(self, board):  # Constructor method
        self.board = board  # Store the Sudoku board in the instance
        self.size = 9  # Sudoku board size (9x9)
        self.queue = deque()  # Initialize a queue for BFS algorithm

    def is_valid(self, board, row, col, num):  # Check if placing 'num' in board[row][col] is valid
        # Check if 'num' already exists in the given row, column, or 3x3 subgrid
        if num in board[row] or num in [board[i][col] for i in range(self.size)]:
            return False
        # Calculate the starting indices of the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        # Check if 'num' exists in the 3x3 subgrid
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True  # Return True if 'num' can be placed in board[row][col]

    def find_empty(self, board):  # Find an empty cell in the board
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:  # 0 denotes an empty cell
                    return i, j  # Return the position of the empty cell
        return None  # Return None if there are no empty cells

    def solve(self):  # Solve the Sudoku using BFS
        self.queue.append(copy.deepcopy(self.board))  # Add the initial board to the queue
        while self.queue:
            current_board = self.queue.popleft()  # Pop a board state from the queue
            empty_cell = self.find_empty(current_board)  # Find the first
            # Find the first empty cell in the current board state
            if not empty_cell:
                return current_board  # Return the solved board if there are no empty cells
            row, col = empty_cell
            for num in range(1, 10):  # Try numbers from 1 to 9 in the empty cell
                if self.is_valid(current_board, row, col, num):  # Check if the number is valid
                    new_board = copy.deepcopy(current_board)  # Make a copy of the current board
                    new_board[row][col] = num  # Place the number in the empty cell
                    self.queue.append(new_board)  # Add the new board state to the queue
        return None  # Return None if no solution is found

# Function to print the Sudoku board in a formatted way
def print_sudoku(board):
    for i in range(9):  # Iterate through rows
        for j in range(9):  # Iterate through columns
            print(board[i][j], end=" ")  # Print each cell value followed by a space
        print()  # Print a newline after each row

# Function to print the board (alternative formatting)
def print_board(board):
    for row in board:  # Iterate through each row of the board
        print(" ".join(map(str, row)))  # Convert each cell to string and join with spaces

# Function to get the user's choice of solving method
def user_choice():
    while True:  # Infinite loop to keep asking until a valid input is given
        choice = input("Choose the solving method (DFS/BFS): ").strip().upper()  # Get user input and convert to uppercase
        if choice in ['DFS', 'BFS']:  # Check if the choice is either 'DFS' or 'BFS'
            return choice  # Return the valid choice
        else:
            print("Invalid input. Please enter 'DFS' or 'BFS'.")  # Prompt for valid input

# Function to solve the Sudoku based on the user's choice of algorithm
def solve_sudoku_based_on_choice(board, choice):
    print("Original Sudoku:")  # Print a message
    print_sudoku(board)  # Print the original Sudoku board
    if choice == 'DFS':  # If the user chose DFS
        solver = SudokuSolverDFS(copy.deepcopy(board))  # Create a DFS solver instance with a copy of the board
        if solver.solve():  # Attempt to solve the Sudoku
            print("\nSudoku Solved with DFS:")  # Print a success message
            print_board(solver.board)  # Print the solved Sudoku board
        else:
            print("No solution exists using DFS.")  # Print a failure message
    elif choice == 'BFS':  # If the user chose BFS
        solver = SudokuSolverBFS(board)  # Create a BFS solver instance with the board
        solution = solver.solve()  # Attempt to solve the Sudoku
        if solution:
            print("\nSudoku Solved with BFS:")  # Print a success message
            print_board(solution)  # Print the solved Sudoku board
        else:
            print("No solution exists using BFS.")  # Print a failure message

# Main execution block
def main():
    while True:  # Start an infinite loop to allow multiple Sudoku puzzles to be solved
        # Ask the user to enter the difficulty level of the Sudoku
        difficulty = input("Enter difficulty (easy/medium/hard): ").lower()

        # Predefined Sudoku boards for different difficulty levels
        # Easy level Sudoku board
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

        # Medium level Sudoku board
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

        # Hard level Sudoku board
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

        # Choose the board based on the difficulty level
        if difficulty == 'easy':
            sudoku_board = easy_board
        elif difficulty == 'medium':
            sudoku_board = medium_board
        elif difficulty == 'hard':
            sudoku_board = hard_board
        else:
            print("Invalid difficulty. Defaulting to easy.")
            sudoku_board = easy_board

        # Get the user's choice of solving algorithm (DFS or BFS)
        user_input = user_choice()
        # Solve the Sudoku based on the chosen algorithm
        solve_sudoku_based_on_choice(sudoku_board, user_input)

        # Ask the user if they want to exit or solve another puzzle
        continue_choice = input("Do you want to solve another Sudoku? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the Sudoku Solver. Goodbye!")
            break  # Exit the loop if the user does not want to continue

# Check if this script is the main program and run the main function
if __name__ == "__main__":
    main()
