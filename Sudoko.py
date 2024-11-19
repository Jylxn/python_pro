def display_grid(grid):
    print("  J K L   M N O   P Q R")
    for row_idx, row in enumerate(grid):
        if row_idx % 3 == 0 and row_idx != 0:
            print("  - - - - - - - - - - -")
        print(string.ascii_uppercase[row_idx], end=" ")
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


def play_sudoku(grid):
    while True:
        display_grid(grid)
        user_input = input(
            "Enter your move (e.g., AJ 5), 'solve' to solve, or 'quit' to exit: "
        ).strip().lower()
        print()

        if user_input == "solve":
            if solve_sudoku_puzzle(grid):
                print("Sudoku puzzle solved successfully!")
            else:
                print("No solution exists for the given Sudoku puzzle.")
            display_grid(grid)
            break

        elif user_input == "quit":
            print("Goodbye!")
            break

        else:
            try:
                position, number = user_input.split()
                if len(number) != 1 or not number.isdigit():
                    raise ValueError("Number must be a single digit.")

                row_idx = ord(position[0].upper()) - ord('A')
                col_idx = ord(position[1].upper()) - ord('J')
                number = int(number)

                if row_idx < 0 or row_idx >= 9 or col_idx < 0 or col_idx >= 9:
                    raise ValueError("Row or column out of bounds.")

                if number < 1 or number > 9:
                    raise ValueError(
                        "Number out of range. Please enter a number between 1 and 9."
                    )

                if grid[row_idx][col_idx] == 0 and is_move_valid(
                        grid, row_idx, col_idx, number):
                    grid[row_idx][col_idx] = number
                else:
                    print("Invalid move! Try again.")
            except (ValueError, IndexError) as e:
                print(
                    f"Invalid input! {e}. Please enter in the format 'AJ 5', or type 'solve' or 'quit'."
                )


# Example Sudoku grid (0 represents an empty cell)
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

play_sudoku(grid)
