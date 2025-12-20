from enigma.core.rotor import Rotor


def test_rotor_initialization():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", ring_setting=0, position="A")
    assert rotor.position == "A"
    assert rotor.ring_setting == 0
    assert rotor.notch == "Q"
    assert len(rotor.wiring) == 26
