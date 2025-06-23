"""
Tests for the example module.
"""

import pytest

from macos_surgery.example import add_numbers, greet


def test_greet_no_name() -> None:
    """Test greet function with no name."""
    assert greet() == "Hello, world!"


def test_greet_with_name() -> None:
    """Test greet function with a name."""
    assert greet("Alice") == "Hello, Alice!"


def test_add_numbers() -> None:
    """Test add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_add_numbers_type_error() -> None:
    """Test add_numbers with incorrect types (runtime check; Mypy should also catch)."""
    with pytest.raises(TypeError):
        # This test is more about runtime safety if type hints are ignored or bypassed.
        # Mypy should catch this statically.
        add_numbers("a", "b")  # type: ignore

    with pytest.raises(TypeError):
        add_numbers(1, "b")  # type: ignore
