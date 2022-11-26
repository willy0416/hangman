import random
from words import words
import string

lives = 5
first_turn = True

def get_valid_word(s):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = get_valid_word(s)
    return word.upper()

def hangman():
    global first_turn, lives
    word = get_valid_word(words)
    distinct_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while distinct_letters and lives:
        print(f"Lives remaining: {lives}")
        if not first_turn:
            print(f"You have already used {' '.join(used_letters)}")
        first_turn = False
        print(f"{' '.join([letter if letter in used_letters else '_' for letter in word])}")

        guess = input("Guess a letter: ").upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in distinct_letters:
                distinct_letters.remove(guess)
            elif guess in alphabet:
                lives -= 1
        elif guess in used_letters:
            print("Don't guess a letter twice!")
        else:
            print("Invalid input.")

    if not lives:
        print(f"You ran out of lives! Better luck next time.")

    print(f"Congrats! The word was {word}.")

hangman()