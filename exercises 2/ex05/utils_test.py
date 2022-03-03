"""Tests for the utils functions."""

__author__ = "730391348"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Edge case for only_evens which is an empty list that should return an empty list."""
    digits: list[int] = []
    assert only_evens(digits) == []


def test_only_evens_all_odd() -> None:
    """Use case for only odds in only_evens function which should return an empty list."""
    digits: list[int] = [1, 5, 3]
    assert only_evens(digits) == []


def test_only_evens_mixed_items() -> None:
    """This is a normal use case of mixed values being even and odd should have only the even values."""
    digits: list[int] = [2, 7, 8, 10, 3] 
    assert only_evens(digits) == [2, 8, 10]


def test_sub_empty() -> None:
    """Edge case for sub which is an empty list that should return an empty list."""
    red: list[int] = []
    first: int = 0
    last: int = 3
    assert sub(red, first, last) == []


def test_sub_first_negative_last_out_of_range() -> None:
    """This checks that the first value being negative, should change to use index 0 and the last value being out of range should be the last value of red."""
    red: list[int] = [10, 20, 30, 40]
    first: int = -1
    last: int = 7
    assert sub(red, first, last) == [10, 20, 30, 40]


def test_sub_first_too_large() -> None:
    """This tests for when first is too large for the lists length and should be empty."""
    red: list[int] = [10, 20, 30, 40]
    first: int = 7
    last: int = 3
    assert sub(red, first, last) == []


def test_sub_last_negative() -> None:
    """This tests for when the last value is negative and it should be empty."""
    red: list[int] = [10, 20, 30, 40]
    first: int = 2
    last: int = -3
    assert sub(red, first, last) == []


def test_sub_normal_scenario() -> None:
    """This case is for when the list fits with the first and last values."""
    red: list[int] = [10, 20, 30, 40, 50, 60]
    first: int = 0
    last: int = 3
    assert sub(red, first, last) == [10, 20, 30]


def test_concat_both_empty() -> None:
    """This edge case is for when both of the lists are empty and should return an empty list."""
    thing_1: list[int] = []
    thing_2: list[int] = []
    assert concat(thing_1, thing_2) == []


def test_concat_2nd_list_empty() -> None:
    """This use case is for when the first list has integers but the 2nd list does not."""
    thing_1: list[int] = [15, 20]
    thing_2: list[int] = []
    assert concat(thing_1, thing_2) == [15, 20]


def test_concat_both_diff() -> None:
    """This use case is for when both lists have values within."""
    thing_1: list[int] = [12, 13, 4, 8]
    thing_2: list[int] = [25, 2022]
    assert concat(thing_1, thing_2) == [12, 13, 4, 8, 25, 2022]
