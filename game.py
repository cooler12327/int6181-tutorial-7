def is_win(game):
    win = False
    # rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win


def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]
    markers = ('X', 'O')
    player = 0
    moves = 0

    print("X = Player 1")
    print("O = Player 2")

    while moves < 9:
        print(f"Player {player + 1}: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ", end="")
        try:
            i, j = map(int, input().split())
        except ValueError:
            print("Enter exactly two integers separated by whitespace.")
            continue

        if not (1 <= i <= 3 and 1 <= j <= 3):
            print("Coordinates must be between 1 and 3.")
            continue

        row, column = i - 1, j - 1
        if game[row][column] != ' ':
            print("That cell is already occupied. Choose another cell.")
            continue

        game[row][column] = markers[player]
        moves += 1

        if is_win(game):
            print("Win!")
            break
        if moves == 9:
            print("Tie!")
            break

        player = 1 - player

    for row in game:
        print(' '.join(row))


if __name__ == "__main__":
    main()
