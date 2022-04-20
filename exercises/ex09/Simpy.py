"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730391348"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, x: list[float]):
        """Constructor for simpy."""
        self.values = x

    def __str__(self) -> str:
        """Function that returns a string."""
        return f"Simpy({self.values})"

    def fill(self, value: float, number: int) -> None:
        """Function that fills a Simpy's values with a sepcific number of repeating values."""
        self.values = []
        i: int = 0
        while i < number: 
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> list[float]:
        """Function that fills values with range of values.""" 
        assert step != 0.0
        self.values = []
        i: int = 0
        while start < stop or start > stop:
            self.values.append(start)
            start += step
            i += 1
        return self.values

    def sum(self) -> float:
        """Function that sums up the values."""
        total = 0.0
        for numbers in self.values:
            total += numbers
        return total

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Function that when the right side ixs SImpy it adds both values and whne it is a float each value is added to rhs."""
        i: int = 0
        result = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in self.values:
                self.values.append(item += rhs.values)
                result.append(self.values)
                i += 1
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        return Simpy(result)

