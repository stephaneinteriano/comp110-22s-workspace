"""Tests for the dictionary functions."""

__author__ = "730391348"

from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """This is an edge case for invert which is an empty list that should return an empty list."""
    flip: dict[str, str] = {}
    assert invert(flip) == {}


def test_invert_2_sets() -> None:
    """This is an use case for invert which has 2 set of strings and should invert both."""
    flip: dict[str, str] = {'stevie': 'nicks', 'freddie': 'mercury'}
    assert invert(flip) == {'nicks': 'stevie', 'mercury': 'freddie'}


def test_invert_3_sets() -> None:
    """This is an use case for invert which should invert the 3 sets of strings."""
    flip: dict[str, str] = {'watermelon': 'sugar', 'strawberry': 'lipstick', 'lemon': 'ice'}
    assert invert(flip) == {'sugar': 'watermelon', 'lipstick': 'strawberry', 'ice': 'lemon'}


def test_favorite_color_green_only() -> None:
    """This is an edge case for favorite color which has only one possible favorite color."""
    rainbow: dict[str, str] = {'stephanie': 'green', 'tom': 'green'}
    assert favorite_color(rainbow) == 'green'


def test_favorite_color_blue() -> None:
    """This is an use case for favorite color which has multiple colors but blue is the most popular."""
    rainbow: dict[str, str] = {'nate': 'blue', 'cassie': 'blue', 'maddy': 'purple', 'rue': 'green', 'lexi': 'red'}
    assert favorite_color(rainbow) == 'blue'


def test_favorite_color_tie() -> None:
    """This is an use case for favorite color which has a tie and the first color in the dictionary should be returned."""
    rainbow: dict[str, str] = {'stephanie': 'green', 'tom': 'green'}
    assert favorite_color(rainbow) == 'green'


def test_count_empty_inputs() -> None:
    """This is an edge case where the lists of inputs are empty and should return an empty dictionary."""
    list_numbers: list[str] = []
    assert count(list_numbers) == {}


def test_count_inputs_repeat_2() -> None:
    """This is an use case for count which has the same input that repeats twice."""
    list_numbers: list[str] = ['sleeping', 'sleeping']
    assert count(list_numbers) == {'sleeping': 2}


def test_count_inputs_repeat_3() -> None:
    """This is an use case for count which has an input that repeats twice and two others that are different."""
    list_numbers: list[str] = ['movies', 'candy', 'popcorn', 'candy']
    assert count(list_numbers) == {'movies': 1, 'candy': 2, 'popcorn': 1} 