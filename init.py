import game_logic

def logic():
    player_options = {
        "1": game_logic.RandomPlayer(),
        "2": game_logic.HumanPlayer(),
        "3": game_logic.ReflectPlayer(),
        "4": game_logic.CyclePlayer()
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
        print("Goodbye :-)")
        exit();
    else:
        print("I don't understand you. Please repeat the entry!")
        choice()

if __name__ == '__main__':
    print("Welcome to Paper-Rock-Scissors Game! Against which Player do you wanna play?\n")
    print( "- randomplayer: 1\n" )
    print( "- humanplayer: 2\n" )
    print( "- reflectplayer: 3\n" )
    print( "- cycleplayer: 4\n" )
    logic()
    choice()
