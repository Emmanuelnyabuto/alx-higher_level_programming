#!/usr/bin/python3
"""Defines quare-printing function."""


def print_square(size):
    """Print square with the # character.

    Args:
        size (int): The height/width the square.
    Raises:
        TypeError: If size is not integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
