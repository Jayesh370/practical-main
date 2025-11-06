# n-Queens problem with backtracking
# First queen is already placed

def print_board(board):
    n = len(board)
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += " Q "
            else:
                row += " . "
        print(row)
    print("\n")

# Function to check if placing a queen is safe
def is_safe(board, row, col):
    for i in range(row):
        # Check column conflict
        if board[i] == col:
            return False
        # Check diagonal conflicts
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

# Backtracking function to solve n-Queens
def solve_n_queens(board, row):
    n = len(board)
    if row == n:
        print("Solution found:")
        print_board(board)
        return True  # Change to False to find all solutions

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            if solve_n_queens(board, row + 1):
                return True  # Stop after first solution
            board[row] = -1   # Backtrack
    return False

# ----------------- MAIN -----------------
n = int(input("Enter size of board (n): "))

board = [-1] * n  # Initialize board with -1 (no queen)
first_row = int(input("Enter row for first queen (0-based index): "))
first_col = int(input("Enter column for first queen (0-based index): "))

board[first_row] = first_col  # Place the first queen

# Start solving from next row if first queen is in row 0, else from row 0
start_row = 0 if first_row != 0 else 1

if not solve_n_queens(board, start_row):
    print("No solution exists.")

