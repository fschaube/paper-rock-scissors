import game_logic

print(
    "Welcome to Paper-Rock-Scissors Game! Against which Player do you wanna play?"
)


def logic():
    player_options = {
        "randomplayer": game_logic.RandomPlayer(),
        "humanplayer": game_logic.HumanPlayer(),
        "reflectplayer": game_logic.ReflectPlayer(),
        "cycleplayer": game_logic.CyclePlayer()
    }

    player1 = input("Choose Player 1:\n").lower()
    player2 = input("Choose Player 2:\n").lower()

    while player1 not in player_options or player2 not in player_options:
        print("Please repeat submissions!\n")
        player1 = input("Choose Player 1:\n").lower()
        player2 = input("Choose Player 2:\n").lower()

    game = game_logic.Game(player_options[player1],
                            player_options[player2])
    game.play_game()


def choice():
    choice = input("Do you wanna play again? Type 'yes' or 'no'\n")
    if choice in "yes":
        logic()
    elif choice in "no":
        print("Goodbye")
    else:
        print("I don't understand you. Please repeat the entry!")
        choice()

if __name__ == '__main__':
    print("""Welcome to Paper-Rock-Scissors Game! 
    Against which Player do you wanna play?""")

logic()
choice()
