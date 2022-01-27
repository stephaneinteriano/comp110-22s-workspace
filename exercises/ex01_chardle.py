"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730391348"

word_guess: str = input("Enter a 5-character word: ")

if len(word_guess) != 5:  
    exit("Error: Word must contain 5 characters") 
else: 
    letter_guess: str = input("Enter a single character: ")
sub = letter_guess

if len(letter_guess) != 1:
    print("Error: Character must be a single character.")
    exit() 
else:
    print("Searching for " + letter_guess + " in " + word_guess)

if word_guess[0] == letter_guess:
    print(letter_guess + " found at index 0")
if word_guess[1] == letter_guess:
    print(letter_guess + " found at index 1")
if word_guess[2] == letter_guess:
    print(letter_guess + " found at index 2")
if word_guess[3] == letter_guess:
    print(letter_guess + " found at index 3")
if word_guess[4] == letter_guess:
    print(letter_guess + " found at index 4")
else:
    exit  

if word_guess.count(sub, 0, 5) == 1:
    print("1 instance of " + letter_guess + " found in " + word_guess)
if word_guess.count(sub, 0, 5) == 0:
    print("No instances of " + letter_guess + " found in " + word_guess)
if word_guess.count(sub, 0, 5) == 2:
    print("2 instances of " + letter_guess + " found in " + word_guess) 
if word_guess.count(sub, 0, 5) == 3:
    print("3 instances of " + letter_guess + " found in " + word_guess)
if word_guess.count(sub, 0, 5) == 4:
    print("4 instances of " + letter_guess + " found in " + word_guess)
if word_guess.count(sub, 0, 5) == 5:
    print("5 instances of " + letter_guess + " found in " + word_guess)
else: 
    exit 
