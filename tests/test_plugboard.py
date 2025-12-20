from enigma.core.plugboard import Plugboard


def test_plugboard_swaps_configured_pairs():
    pb = Plugboard({"A": "V", "B": "S"})
    assert pb.swap("A") == "V"
    assert pb.swap("V") == "A"
    assert pb.swap("B") == "S"
    assert pb.swap("S") == "B"


def test_plugboard_leaves_unconnected_letters_unchanged():
    pb = Plugboard({"A": "V"})
    assert pb.swap("C") == "C"
    assert pb.swap("Z") == "Z"


def test_plugboard_is_case_insensitive():
    pb = Plugboard({"a": "v"})
    assert pb.swap("a") == "V"
    assert pb.swap("A") == "V"
    assert pb.swap("v") == "A"
    assert pb.swap("V") == "A"


def test_plugboard_rejects_self_connection():
    try:
        Plugboard({"A": "A"})
    except ValueError as exc:
        assert "Cannot connect letter" in str(exc)
    else:
        assert False, "Expected ValueError for A->A connection"


def test_plugboard_rejects_duplicate_usage_of_letter():
    try:
        Plugboard({"A": "V", "B": "V"})
    except ValueError as exc:
        assert "already used" in str(exc)
    else:
        assert False, "Expected ValueError for duplicate letter usage"
