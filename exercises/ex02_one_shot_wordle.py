"""A few steps closer to building Wordle!"""

__author__ = "730483039"

secret_word = "python"
guess_word: str = input (f"What is your {len(secret_word)}-letter quess? ")

while len(secret_word) != len(guess_word):
    guess_word = input(f"Thats was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
bank: str = ""
guess_character: bool = False
alt: int = 0

while i < len(guess_word):
    if secret_word[i] == guess_word[i]:
        bank += GREEN_BOX
    else:
        guess_character = False
        alt = 0
        while not guess_character and alt < len(secret_word):
            if secret_word[alt] == guess_word[i]:
                guess_character = True
            else: 
                alt += 1
        if guess_character:
            bank += YELLOW_BOX
        else:
            bank += WHITE_BOX
    i += 1
print(bank)

if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")