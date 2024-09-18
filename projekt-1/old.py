"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Provázek
email: provazek@24s.cz
discord: provazek24s.cz_84357
"""
# import seznam registrovaných uživatelů a kontrolované texty
import re
from collections import defaultdict
from users import registered_users  # Importujeme seznam uživatelů
from task_template import TEXTS  # Importujeme texty

# Získání uživatelského jména a hesla
username = input("username: ")
password = input("password: ")

# Ověření uživatele
if username in registered_users and registered_users[username] == password:
    print(f"Welcome to the app, {username}")
    
    # Výběr textu
    print("We have 3 texts to be analyzed.")
    try:
        text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
        if text_choice < 1 or text_choice > 3:
            print("Invalid choice, terminating the program..")
        else:
            selected_text = TEXTS[text_choice - 1]
            
            # Rozdělení textu na slova
            words = selected_text.split()

            # Počítáme statistiky
            word_count = len(words)
            titlecase_count = len([word for word in words if word.istitle()])
            uppercase_count = len([word for word in words if word.isupper()])
            lowercase_count = len([word for word in words if word.islower()])
            numeric_strings = [word for word in words if word.isdigit()]
            numeric_count = len(numeric_strings)
            numeric_sum = sum(map(int, numeric_strings))

            # Zobrazíme výsledky
            print("----------------------------------------")
            print(f"There are {word_count} words in the selected text.")
            print(f"There are {titlecase_count} titlecase words.")
            print(f"There are {uppercase_count} uppercase words.")
            print(f"There are {lowercase_count} lowercase words.")
            print(f"There are {numeric_count} numeric strings.")
            print(f"The sum of all the numbers is {numeric_sum}.")
            print("----------------------------------------")
            
            # Vytvoření slovníku pro četnost délek slov
            word_lengths = defaultdict(int)
            for word in words:
                word_lengths[len(word)] += 1

            # Zobrazení grafu
            print("LEN|  OCCURENCES  |NR.")
            print("----------------------------------------")
            for length, count in sorted(word_lengths.items()):
                print(f"{length:3}| {'*' * count:<13} |{count}")
            
    except ValueError:
        print("Invalid input, terminating the program..")
else:
    print("unregistered user, terminating the program..")
