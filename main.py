import math


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board():
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner():

    
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

   
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None


def is_draw():
    for row in board:
        if ' ' in row:
            return False
    return True


def minimax(depth, is_maximizing):

    winner = check_winner()

    if winner == 'O':
        return 1

    if winner == 'X':
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j] == ' ':

                    board[i][j] = 'O'

                    score = minimax(depth + 1, False)

                    board[i][j] = ' '

                    best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(3):
            for j in range(3):

                if board[i][j] == ' ':

                    board[i][j] = 'X'

                    score = minimax(depth + 1, True)

                    board[i][j] = ' '

                    best_score = min(score, best_score)

        return best_score


def ai_move():

    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):

            if board[i][j] == ' ':

                board[i][j] = 'O'

                score = minimax(0, False)

                board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        board[move[0]][move[1]] = 'O'


def player_move():

    while True:

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid position!")
                continue

            if board[row][col] != ' ':
                print("Cell already occupied!")
                continue

            board[row][col] = 'X'
            break

        except ValueError:
            print("Enter numbers only!")


def main():

    print("=== TIC TAC TOE AI ===")
    print("You = X")
    print("AI = O")

    while True:

        print_board()

        player_move()

        winner = check_winner()

        if winner:
            print_board()
            print("You Win!")
            break

        if is_draw():
            print_board()
            print(" Draw!")
            break

        print("AI is thinking...")

        ai_move()

        winner = check_winner()

        if winner:
            print_board()
            print(" AI Wins!")
            break

        if is_draw():
            print_board()
            print("Draw!")
            break


if __name__ == "__main__":
    main()