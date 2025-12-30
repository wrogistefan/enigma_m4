"""Tests for the EnigmaMachine class."""


from enigma.machine import EnigmaMachine
from enigma.plugboard import Plugboard
from enigma.reflector import Reflector
from enigma.rotor import Rotor


def test_correct_stepping():
    rotors = [
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "A"),  # I
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", 0, "A"),  # II
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", 0, "A"),  # III
    ]
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = Plugboard([])
    machine = EnigmaMachine(rotors, reflector, plugboard)

    # Initial positions
    assert rotors[0].position == "A"
    assert rotors[1].position == "A"
    assert rotors[2].position == "A"

    machine.step()
    assert rotors[0].position == "B"
    assert rotors[1].position == "A"
    assert rotors[2].position == "A"


def test_double_step():
    rotors = [
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "Q"),  # I at notch
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", 0, "E"),  # II at notch
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", 0, "A"),  # III
    ]
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = Plugboard([])
    machine = EnigmaMachine(rotors, reflector, plugboard)

    machine.step()
    # Double step: middle and left should step
    assert rotors[0].position == "R"
    assert rotors[1].position == "G"
    assert rotors[2].position == "B"


def test_full_encode_cycle():
    rotors = [
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "A"),
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", 0, "A"),
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", 0, "A"),
    ]
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = Plugboard([])
    machine = EnigmaMachine(rotors, reflector, plugboard)

    result = machine.encode_letter("A")
    assert result.isalpha()
    assert len(result) == 1


def test_m4_behavior():
    rotors = [
        Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0, "A"),  # I
        Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", 0, "A"),  # II
        Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", 0, "A"),  # III
        Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "Z", 0, "A"),  # Beta (greek)
    ]
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = Plugboard([])
    machine = EnigmaMachine(rotors, reflector, plugboard)

    machine.step()
    # Greek rotor should not rotate
    assert rotors[3].position == "A"
