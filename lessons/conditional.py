"""An example of conditional (if-else) statments."""

SECRET: int = 3

print("I am thinking of a number between 1 and 5 what is it|?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("Correct!")
else:
    print("Wrong number : ( ")

print("Game over")