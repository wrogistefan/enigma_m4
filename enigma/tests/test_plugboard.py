"""Tests for the Plugboard class."""

import pytest

from enigma.plugboard import Plugboard


def test_dict_format():
    pb = Plugboard({"A": "B", "C": "D"})
    assert pb.swap("A") == "B"
    assert pb.swap("B") == "A"


def test_list_format():
    pb = Plugboard([("A", "B"), ("C", "D")])
    assert pb.swap("A") == "B"


def test_string_dash_format():
    pb = Plugboard("A-B C-D")
    assert pb.swap("A") == "B"


def test_string_compact_format():
    pb = Plugboard("AB CD")
    assert pb.swap("A") == "B"


def test_10_pair_limit():
    pairs = [
        ("A", "B"),
        ("C", "D"),
        ("E", "F"),
        ("G", "H"),
        ("I", "J"),
        ("K", "L"),
        ("M", "N"),
        ("O", "P"),
        ("Q", "R"),
        ("S", "T"),
    ]
    Plugboard(pairs)
    with pytest.raises(ValueError, match=r"Plugboard cannot have more than 10 pairs."):
        Plugboard([*pairs, ("U", "V")])


def test_swap_behavior():
    pb = Plugboard([("A", "B")])
    assert pb.swap("A") == "B"
    assert pb.swap("B") == "A"
    assert pb.swap("C") == "C"
