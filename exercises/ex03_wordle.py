"""Creating a Structured Wordle."""

__author__ = "730391348"


def contains_char(unlimited: str, searching_for: str) -> bool:
    """Checking if searching_for string is found in unlimited."""
    assert len(searching_for) == 1
    index: int = 0
    unlimited_letters: int = len(unlimited)
    while index < unlimited_letters:
        if searching_for == unlimited[index]:
            return True
        index = index + 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Adding in emoji boxes according to strings while using contains_char."""
    assert len(guess) == len(secret)
    result_emoji: str = ""
    i: int = 0
    while i < len(secret):
        if secret[i] == guess[i]:
            result_emoji = result_emoji + GREEN_BOX
        elif contains_char(secret, guess[i]):
            result_emoji = result_emoji + YELLOW_BOX
        else:
            result_emoji = result_emoji + WHITE_BOX
        i += 1
    return result_emoji


def input_guess(expected_length: int) -> str:
    """Asking a user for guess until it matches the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That was not {expected_length} letters! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    secret: str = "codes"
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        # function call
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        turn += 1
        if guess == secret:
            turn -= 1  
            print(f"You won in {turn} /6 turns!")
            turn = 7
    print("X/6 - Sorry, try again tomorrow!")
