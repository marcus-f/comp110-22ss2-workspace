"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730483039"

secret_word: str = input("Enter a 5-character word: ") 
if len(secret_word) != 5: 
    print("Error: Word must contain 5 characters")  
    exit()

guess_letter: str = input("Enter a single character: ")
if len(guess_letter) != 1:  
    print("Error: Character must be a singular character.") 
    exit()

times: int = 0  
print("Searching for " + guess_letter + " in "+ secret_word ) 

if(secret_word[0]==guess_letter): 
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


if times == 0:
    print("No instances of " + guess_letter + " found in  " + secret_word)
else:
    if times == 1:
        print(str(times)+ " instances of " + guess_letter + " found in " + secret_word)
    else:
        print(str(times)+ " instance of " + guess_letter + " found in " + secret_word)