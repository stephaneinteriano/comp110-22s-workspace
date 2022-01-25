"""EX01 - Chardle  - A cute step toward Wordle."""
__author__ = 730391348

request: str = "Enter a 5-character word: "
word_guess: str = "hello"
request_again: str = "Enter a single character: "
letter_guess: str = "h"

if len(word_guess) != 5:
    print(request + word_guess)
    print("Error: Word must contain 5 characters")
else: 
    print(request + word_guess)
    print(request_again + letter_guess)
    if len(letter_guess) != 1:
        print("Error: Character must be a single character")
    else:
        if letter_guess == " ":
            print("Error: Character must be a single character")
        else: 
            if len(letter_guess) == 1:
                print("Searching for " + letter_guess + " in " + word_guess)

if letter_guess == word_guess[1]:
    print(letter_guess + " is found at index 1") 
else: 
    if letter_guess == word_guess[0]:
        print(letter_guess + " is found at index 0") 
    else:
        if letter_guess == word_guess[2]:
            print(letter_guess + " is found at index 2")
        else:
            if letter_guess == word_guess[3]:
                print(letter_guess + " is found at index 3")
            else:
                if letter_guess == word_guess[4]:
                    print(letter_guess + " is found at index 4") 

sub = letter_guess
if word_guess.count(sub, 0, 5) == 1:
    print("1 instance of " + sub + " is found in " + word_guess)
else:
    if word_guess.count(sub, 0, 5) == 0:
        print("No instances of " + sub + " found in " + word_guess)
    else: 
        if word_guess.count(sub, 0, 5) == 2:
            print("2 instance of " + sub + " is found in " + word_guess) 
        else: 
            if word_guess.count(sub, 0, 5) == 3:
                print("3 instance of " + sub + " is found in " + word_guess)
            else: 
                if word_guess.count(sub, 0, 5) == 4:
                    print("4 instance of " + sub + " is found in " + word_guess)
                else:
                    if word_guess.count(sub, 0, 5) == 5:
                        print("5 instance of " + sub + " is found in " + word_guess)
