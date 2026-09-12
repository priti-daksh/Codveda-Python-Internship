def print_board(board):
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1),
                    range(col - 1, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1),
                    range(col + 1, n)):
        if board[i][j] == "Q":
            return False

    return True


def solve_n_queens(board, row, n):

    # All queens placed
    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = "Q"

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = "."

    return False


def main():

    try:
        n = int(input("Enter number of queens: "))

        if n < 1:
            print("Please enter a positive number!")
            return

        board = [["." for _ in range(n)] for _ in range(n)]

        if solve_n_queens(board, 0, n):

            print("\n===== N-QUEENS SOLUTION =====\n")
            print_board(board)

        else:
            print("\nNo solution exists!")

    except ValueError:
        print("Please enter a valid number!")


main()