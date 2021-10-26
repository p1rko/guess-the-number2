from functions import play_game, get_top_scores

while True:
    selection = input("Would you like to play a new game (write A), see the best scores (write B), or quit (write C)? ")

    if selection.upper() == "A":
        mode = input("What mode do you want (hard or easy)? ")
        if mode.lower() == "hard":
            play_game("hard")
        elif mode.lower() == "easy":
            play_game("easy")
    elif selection.upper() == "B":
        number = int(input("How many top scores would you like to see? "))
        get_top_scores(number)
    elif selection.upper() == "C":
        break