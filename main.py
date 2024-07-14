import os
from logic import make_archiv, game, adds_players_in_ranking, show_ranking, show_words, show_credits

# Creates the "players", "ranking", "words" folders in the same directory as the main.py file.
while True:
    if os.path.exists("./players") and os.path.exists("./ranking") and os.path.exists("./words"):
        break
    else:
        os.mkdir("./players")
        os.mkdir("./ranking")
        os.mkdir("./words")
        break


name = input("Enter you name: ").title()

# Creates the file path with the player name.
file_path = f"./players/{name}.json"
make_archiv(name, file_path)

# Path of archiv for put the words of game.
file_path_words = "./words/words.txt" 

while True:
    
    option = input("Choice the option - 'Play' | 'Ranking' | 'Words' | 'Credits' | 'Quit': ").lower().replace(" ", "")

    if option == "play":
        game(name, file_path, file_path_words)
    elif option == "ranking":
        adds_players_in_ranking("./players","./ranking/ranking.json")
        show_ranking("./ranking/ranking.json")
    elif option == "words":
        show_words(file_path_words)
    elif option == "credits":
        show_credits()
    elif option == "quit":
        quit()
    else:
        print("Option invalid!")
