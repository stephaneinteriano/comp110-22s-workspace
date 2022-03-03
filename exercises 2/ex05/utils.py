"""Creating utils functions."""

__author__ = "730391348"


def only_evens(digits: list[int]) -> list[int]:
    """Create a list with only even values."""
    lol: list[int] = list()
    for x in digits:
        if x % 2 == 0:
            lol.append(x)
    return lol


def sub(red: list[int], first: int, last: int) -> list[int]:
    """Creating a sub list from the indices."""
    new: list[int] = list()
    empty: list[int] = list()
    if len(red) == 0 or first > len(red) or last <= 0:
        return empty
    if first < 0:
        first = 0 
    if last > len(red): 
        last = len(red)
    while first < last:
        new.append(red[first])
        first += 1
    return new


def concat(thing_1: list[int], thing_2: list[int]) -> list[int]:
    """A new list with all the values."""
    for x in thing_2:
        thing_1.append(x)
    return thing_1