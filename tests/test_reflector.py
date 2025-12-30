"""Tests for the Reflector class."""

import pytest

from enigma.reflector import Reflector


def test_involution_validation():
    # Valid reflector
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    assert reflector.wiring == "YRUHQSLDPXNGOKMIEBFZCWVJAT"


def test_no_fixed_points():
    with pytest.raises(ValueError):
        Reflector("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # A maps to A


def test_correct_reflection():
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    assert reflector.reflect("A") == "Y"
    assert reflector.reflect("Y") == "A"
