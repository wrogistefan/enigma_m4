"""Tests for the Rotor class."""


from enigma.rotor import Rotor


def test_forward_encoding():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "A")
    assert rotor.encode_forward("A") == "E"
    assert rotor.encode_forward("B") == "K"


def test_backward_encoding():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "A")
    assert rotor.encode_backward("E") == "A"
    assert rotor.encode_backward("K") == "B"


def test_ring_setting():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 1, "A")
    assert rotor.encode_forward("A") == "K"


def test_stepping():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "A")
    rotor.step()
    assert rotor.position == "B"


def test_notch_detection():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "P")
    assert rotor.at_notch() is False
    rotor.step()
    assert rotor.at_notch() is True
