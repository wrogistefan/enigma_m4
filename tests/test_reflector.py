from enigma.core.reflector import Reflector


def test_reflector_basic_mapping():
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    assert reflector.reflect("A") == "Y"
    assert reflector.reflect("Y") == "A"
    assert reflector.reflect("B") == "R"
    assert reflector.reflect("R") == "B"


def test_reflector_involution_validation():
    # This wiring is NOT an involution, should raise error
    invalid = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        Reflector(invalid)
        assert False, "Expected ValueError for non-involutive reflector"
    except ValueError:
        pass
