import os
import json
import platform


list_ranking = []
list_words = []
player_data_list = []

def update_json(file_path, list_data):
    with open(file_path, "w") as file_object:
            json.dump(list_data, file_object)

def make_archiv(name, file_path):
    """Makes a archiv with informations of player."""
    if os.path.exists(file_path):
        print(f"Welcome back {name}!")
    else:
        list_ranking.append({"name": name, "pontuation": 0})
        update_json(file_path, list_ranking)


def show_words(file_path_words):
    """Shows all words used in the game."""
    with open(file_path_words) as file_obj:
        contents = file_obj.read()

        if len(contents) == 0:
            print("\nThere are no words here for now ;) \n")
        else:
            print(f"\nHere are the words that were used in the game: \n{contents}")


def show_credits():
        print("Creator: \nWilliam")


def adds_players_in_ranking(home_folder, final_file_path):
    """Takes information from each player and adds it to a single file (ranking.json).
    """
    archivs = os.listdir(home_folder)

    for archiv in archivs:
        with open(f"{home_folder}/{archiv}") as file_object:
            user_data = json.load(file_object)

        for dic in user_data:
            player_data_list.append(dic)
            update_json(final_file_path, player_data_list)


def show_ranking(file_path):
    """Shows informations of a each player like a ranking."""
    with open(file_path) as file_object:
        file_with_user_data = json.load(file_object)

    def show(list_players):
        print()
        for item in list_players:
            for key, value in item.items():
                print(f"{key} - {value}")
            print()

    # Lambda function to sort information based on player scores.
    l1 = sorted(file_with_user_data, key=lambda item: item['pontuation'], reverse=True)
    show(l1)


def game(name, file_path, file_path_words):
    """Controls how the game works."""
    invalid_and_valid_letters = []

    # Valids the word.
    while True:
        secret_word = input("Enter the secret word: ").lower().replace(" ", "")
        if len(secret_word) < 3 or secret_word == secret_word[0] * len(secret_word):
            print("Enter a valid word: ")
        else:
            break
  
    # Adds the word in a archiv.
    with open(file_path_words, 'a') as f_obj:
        f_obj.write(f"- {secret_word} \n")

            
    theme = input("Enter the theme: ")
    
    # Cleans the terminal
    system_ =  platform.system()
    if system_ == "Windows":
        os.system("cls") or None
    else:
        os.system("clear") or None

    word_size = len(secret_word)
    hidden_word = ['-'] * word_size
    hidden_word_two = '-' * word_size
    number_chances = 4

    while True:
        print(f"Theme - {theme} | Number of chances: {number_chances}\n")
        print(hidden_word_two, "\n")

        if hidden_word_two == secret_word:
            print(f"Congratulations {name}, you found the word!")
            # Add the point for the player.
            with open(file_path) as file_object_player:
                list_players_json = json.load(file_object_player)

                for player in list_players_json:
                    if player["name"] == name:
                        player["pontuation"] += 1
                        update_json(file_path, list_players_json)
            break
        
        # Valids the letter or word.
        while True:
            typed_letter = input("Enter one letter: ").lower().replace(" ", "")

            if len(typed_letter) == len(secret_word):
                break
            elif len(typed_letter) != 1:
                print("Enter only one letter or enter the word complete!")
            elif typed_letter in invalid_and_valid_letters:
                print("Letter already typed")
            else:
                break
        
        # Checks whether the word entered is correct or not.
        if len(typed_letter) == len(secret_word):
            if typed_letter == secret_word:
                print("\n. \n. \n. \n")
                print(f"Congratulations {name}, you found the word! \nThe word is {secret_word}")
                # Adds the point for the player.
                with open(file_path) as file_object_player:
                    list_players_json = json.load(file_object_player)

                    for player in list_players_json:
                        if player["name"] == name:
                            player["pontuation"] += 1
                            update_json(file_path, list_players_json)
                break
            else:
                print("\n. \n. \n. \n")
                print(f"{typed_letter} not is the word!")
                print(f"\nNumber of chances is: 0 \n{name}, unfortunately, you didn't discover the word! \n")
                break


        position_letter = secret_word.find(typed_letter)

        # Puts the letters in the word.
        if position_letter != -1:
            for index in range(len(secret_word)):
                if typed_letter == secret_word[index]:
                    hidden_word[index] = secret_word[index] 
                    hidden_word_one = ", ".join(hidden_word).replace(", ", "")
                    hidden_word_two = hidden_word_one
            invalid_and_valid_letters.append(typed_letter)
        else:
            print(f"{typed_letter} does not exist in the word")
            number_chances -= 1
            print(f"Current number of attempts: {number_chances}")
            invalid_and_valid_letters.append(typed_letter)

            if number_chances == 0:
                print(f"\n{name}, unfortunately, you didn't discover the word")
                break
