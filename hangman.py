import random
from words import words
import string

def get_valid_word(s):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = get_valid_word(s)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    distinct_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while distinct_letters:
        print(f"You have already used {' '.join(used_letters)}")
        print(f"Current info: {' '.join([letter if letter in used_letters else '_' for letter in word])}")

        guess = input("Guess a letter: ").upper()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in distinct_letters:
                distinct_letters.remove(guess)
        elif guess in used_letters:
            print("Don't guess a letter twice!")
        else:
            print("Invalid input.")