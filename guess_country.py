"""
This is a simple game where the user has to guess the country based on clues.
"""
import json
import random

with open("countries.json", "r", encoding="utf-8") as file:
    countries = json.load(file)

PLAY_AGAIN = "Y"
while PLAY_AGAIN == "Y":
    country = random.choice(countries)

    print("\nI'm thinking of a country. Can you guess what it is?")
    print("Here are some clues:\n")
    print(f"The capital of this country is {country['capital']}")
    print(f"The language spoken in this country is {country['language']}\n")

    guess = input("What is your guess?: ").title()

    if guess == country["name"]:
        print("Congratulations! You guessed correctly.\n")
    else:
        print(f"Sorry, that's not correct. The answer is {country['name']}.\n")

    PLAY_AGAIN = input("Do you want to play again? (Y/N): ").upper()
