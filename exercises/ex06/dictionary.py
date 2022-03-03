"""Creating different functions w/ dictionaries."""

__author__ = "730391348"


def invert(flip: dict[str, str]) -> dict[str, str]: 
    """Inverting the strings."""
    inverted_dict: dict[str, str] = {}
    for key in flip:
        value: str = flip[key]
        if value in inverted_dict:
            raise KeyError("There was a key error.")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(rainbow: dict[str, str]) -> str:
    """Finding out which is the most popular color."""
    paint: dict[str, int] = {}
    for key in rainbow: 
        color: str = rainbow[key]
        if color in paint:
            paint[color] += 1
        else:
            paint[color] = 1
    limit: int = 0 
    most_popular: str = ""
    for color in paint:
        if paint[color] > limit:
            limit = paint[color]
            most_popular = color
    return most_popular


def count(list_numbers: list[str]) -> dict[str, int]: 
    """Finding the frequency of a value in a list."""
    empty: dict[str, int] = {}
    for key in list_numbers: 
        value: str = key
        if value in empty:
            empty[value] += 1
        else:
            empty[value] = 1 
    return empty 