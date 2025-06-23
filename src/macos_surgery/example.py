"""
Example module for macos-surgery.
"""

from typing import Union


def greet(name: Union[str, None] = None) -> str:
    """
    Generates a greeting message.

    Args:
        name: The name of the person to greet. Defaults to None.

    Returns:
        A greeting string.
    """
    if name:
        return f"Hello, {name}!"
    return "Hello, world!"


def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of the two integers.
    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    return a + b
