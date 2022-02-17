"""EX02 - One Shot Wordle Game."""

__author__ = "730391348"


secret_word: str = "python"
word_letters: int = len(secret_word) 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
result_emoji: str = ""
banana: bool = False 
rest_of_indices: int = 0 
guess: str = (input(f"What is your {word_letters}-letter guess? "))

while len(guess) != word_letters:
    guess = str = (input(f"That was not {word_letters} letters! Try again: "))
while index < word_letters:
    if secret_word[index] == guess[index]:
        result_emoji = result_emoji + GREEN_BOX
    else:
        while rest_of_indices < word_letters and not banana:
            if secret_word[rest_of_indices] == guess[index]:
                result_emoji = result_emoji + YELLOW_BOX
                banana = True
            else:
                rest_of_indices = rest_of_indices + 1
        if not banana:
            result_emoji = result_emoji + WHITE_BOX
    index = index + 1
    banana = False
    rest_of_indices = 0 
print(result_emoji)
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
