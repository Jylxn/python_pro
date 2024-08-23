def display_grid(grid):
    print("  A B C   D E F   G H I")
    for row_idx, row in enumerate(grid):
        if row_idx % 3 == 0 and row_idx != 0:
            print("  - - - - - - - - - - -")
        print(row_idx + 1, end=" ")
        for col_idx, value in enumerate(row):
            if col_idx % 3 == 0 and col_idx != 0:
                print("|", end=" ")
            print(value if value != 0 else ".", end=" ")
        print()

def is_move_valid(grid, row_idx, col_idx, number):
    for i in range(9):
        if grid[row_idx][i] == number or grid[i][col_idx] == number:
            return False

    start_row, start_col = 3 * (row_idx // 3), 3 * (col_idx // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == number:
                return False

    return True

def find_empty_cell(grid):
    for row_idx in range(9):
        for col_idx in range(9):
            if grid[row_idx][col_idx] == 0:
                return (row_idx, col_idx)
    return None

def solve_sudoku_puzzle(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True
    else:
        row_idx, col_idx = empty_cell

    for number in range(1, 10):
        if is_move_valid(grid, row_idx, col_idx, number):
            grid[row_idx][col_idx] = number

            if solve_sudoku_puzzle(grid):
                return True

            grid[row_idx][col_idx] = 0

    return False

def get_hint(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return None
    else:
        row_idx, col_idx = empty_cell

    for number in range(1, 10):
        if is_move_valid(grid, row_idx, col_idx, number):
            return (row_idx, col_idx, number)
    return None

def play_sudoku(grid):
    move_history = []
    while True:
        display_grid(grid)
        user_input = input("Enter your move (e.g., A1 5), 'solve' to solve, 'hint' for a suggestion, 'undo' to undo last move, or 'quit' to exit: ").strip().lower()

        if user_input == "solve":
            if solve_sudoku_puzzle(grid):
                print("Sudoku puzzle solved successfully!")
            else:
                print("No solution exists for the given Sudoku puzzle.")
            display_grid(grid)
            break

        elif user_input == "hint":
            hint = get_hint(grid)
            if hint:
                print(f"Hint: Try placing {hint[2]} at {chr(hint[1] + ord('A'))}{hint[0] + 1}.")
            else:
                print("No hints available. The puzzle might be already solved or unsolvable.")

        elif user_input == "undo":
            if move_history:
                last_move = move_history.pop()
                grid[last_move[0]][last_move[1]] = 0
                print(f"Move undone: Removed {last_move[2]} from {chr(last_move[1] + ord('A'))}{last_move[0] + 1}.")
            else:
                print("No moves to undo.")

        elif user_input == "quit":
            print("Goodbye!")
            break

        else:
            try:
                position, number = user_input.split()
                col_idx = ord(position[0].upper()) - ord('A')
                row_idx = int(position[1]) - 1
                number = int(number)

                if grid[row_idx][col_idx] == 0 and is_move_valid(grid, row_idx, col_idx, number):
                    grid[row_idx][col_idx] = number
                    move_history.append((row_idx, col_idx, number))
                else:
                    print("Invalid move! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter in the format 'A1 5', or type 'solve', 'hint', 'undo', or 'quit'.")


grid = [
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

play_sudoku(grid)