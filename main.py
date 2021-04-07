import random


def show_board(gameboard_square):
    top_row = [gameboard_square[n] for n in range(1, 4)]
    middle_row = [gameboard_square[n] for n in range(4, 7)]
    bottom_row = [gameboard_square[n] for n in range(7, 10)]
    print("\n")
    print("|".join(top_row))
    print("-+-+-")
    print("|".join(middle_row))
    print("-+-+-")
    print("|".join(bottom_row))
    print("\n")


def choose_opponent():
    valid = False
    players = {}
    while not valid:
        opponent = input("Play vs 'user' or 'cpu': ").title()
        if opponent not in ['User', 'Cpu']:
            print("Enter a valid choice: 'user' or 'cpu'.")
        else:
            valid = True
            if opponent == 'User':
                players = {'User 1': "", 'User 2': ""}
            else:
                players = {'User 1': "", 'Cpu': ""}
    return players

def choose_symbol(players):
    picked = False
    while not picked:
        choice = str(input(f"User 1 will choose symbol: 'X' or 'O'  ")).upper()
        if choice not in 'XO':
            print("Choose only between 'X' or 'O'.")
        else:
            if choice == 'X':
                choice_2 = '0'
            else:
                choice_2 = 'X'
            players["User 1"] = choice
            if "User 2" in players:
                players["User 2"] = choice_2
            else:
                players["Cpu"] = choice_2
            print(players)
            return players


def is_winner(gameboard_square):
    if " " in gameboard_square.values():
        winner_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for line in winner_grid:
            if gameboard_square[int(line[0])] == gameboard_square[int(line[1])] == gameboard_square[int(line[2])] != " ":
                return "Winner"
        return "Continue"
    else:
        return "Draw"


def choose_square(gameboard_square, turn):
    picked = False
    player = turn[0]
    symbol = turn[1]
    while not picked:
        try:
            if player == "Cpu":
                square = random.randint(1, 9)
            else:
                square = int(input(f"{player} place your {symbol}"
                                   " in a square, e.g. 1 = top left, 5 = center, 9 = bottom right: "))
            if gameboard_square[square] == " ":
                gameboard_square[square] = symbol
                picked = True
            else:
                print("Sorry, that square is taken!")
        except ValueError:
            print("Please enter number between 1 and 9.")
        except KeyError:
            print("Please enter number between 1 and 9.")
        else:
            show_board(gameboard_square)

    return gameboard_square


def play_game(players):
    gameboard_square = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    players = choose_symbol(players)
    print("\nLet's play!")
    # print(f"User: {players['User']}, CPU: {players['CPU']}\n")
    print(f"{100 * '_'}\n")
    show_board(gameboard_square)
    end_game = False
    while not end_game:
        for player in players.items():
            print(f"{player[0]} is up!")
            gameboard_square = choose_square(gameboard_square, player)
            status = is_winner(gameboard_square)
            if status == "Winner":
                print(f"{player[0]} is the winner!")
                end_game = True
                break
            elif status == "Draw":
                print("Sorry, this game has ended in a draw!")
                end_game = True
                break


if __name__ == "__main__":
    play = True
    while play:
        players = choose_opponent()
        play_game(players)
        repeat = input("Press 'q' to quit or any key to play again.")
        if repeat == 'q':
            play = False
