"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730483039"

secret_word: str = input("Enter a 5-character word: ") ##input secret word
if len(secret_word) != 5: ##prevent words with a length outside of the range
    print("Error: Word must contain 5 characters") ##print error phrase
    exit()

guess_letter: str = input("Enter a single character: ") ##input guess letter
if len(guess_letter) != 1: ##prevent characters with a length outside of the range
    print("Error: Character must be a singular character.") ##print error phrase
    exit()

times: int = 0 ##defines instances as an interger as times
print("Searching for " + guess_letter + " in "+ secret_word ) ##print search phrase

if(secret_word[0]==guess_letter): #if the letter is equal to index add 1 to instances and print index value
    times = times + 1
    print(guess_letter+ " found at index 0 ")
if(secret_word[1]==guess_letter):
    times = times + 1
    print(guess_letter+ " found at index 1 ")
if(secret_word[2]==guess_letter):
    times = times + 1
    print(guess_letter+ " found at index 2 ")
if(secret_word[3]==guess_letter):
    times = times + 1
    print(guess_letter+ " found at index 3 ")
if(secret_word[4]==guess_letter):
    times = times + 1
    print(guess_letter+ " found at index 4 ")

##print instances
if times==0:
    print("No instances of " + guess_letter + " found in  " + secret_word)
if times>1:
    print(str(times)+ " instances of " + guess_letter + " found in " + secret_word)
else:
    print(str(times)+ " instance of " + guess_letter + " found in " + secret_word)