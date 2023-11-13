import random
import sys
from termcolor import colored

def main():
    # Get a random word.
    answer = getRandomWord()

    # Start by asking the user for their initial guess
    attempts = 0
    guess = ""

    while attempts < 5 and guess != answer:
        guess = input("Enter a five-letter guess: ")
        attempts += 1 

        printGuessColors(guess, answer)

    if attempts == 5 and guess != answer:
        print(f"You lose! The answer is {answer}")
    elif guess == answer and attempts % 2 == 0:
        print(f"Congratulations, you won! It took {attempts} guesses")
    elif guess == answer and attempts % 2 == 1:
        print(f"Congratulations, you won! It took {attempts} guess")

    
# A helper method that prints the guess with the
# correct colors to the console.
def printGuessColors(guess, answer):
        for index in range(len(guess)):
            result = letterColor(index, guess, answer)
            print(result)


# A helper method that determines the color
# of the letter in the guess. 
def letterColor(index, guess, answer):
    if guess[index] in answer:
        if guess[index] == answer[index]:
            colored(f"{guess[index]}","green")
        else:
            return colored(f"{guess[index]}","yellow")
    else:
        return colored(f"{guess[index]}","red")

# A method that gets a random word from a file.
def getRandomWord():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)

main()
