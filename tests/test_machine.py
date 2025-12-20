from enigma.core.rotor import Rotor
from enigma.core.reflector import Reflector
from enigma.core.plugboard import Plugboard
from enigma.core.machine import EnigmaMachine
from enigma.data.rotors import ROTOR_I, ROTOR_II, ROTOR_III
from enigma.data.reflectors import REFLECTOR_B

def test_single_letter_encoding():
    plugboard = Plugboard([])

    rotor_r = Rotor(*ROTOR_I, ring_setting=0, position="A")
    rotor_m = Rotor(*ROTOR_II, ring_setting=0, position="A")
    rotor_l = Rotor(*ROTOR_III, ring_setting=0, position="A")

    reflector = Reflector(REFLECTOR_B)

    machine = EnigmaMachine([rotor_r, rotor_m, rotor_l], reflector, plugboard)
    result = machine.encode_letter("A")

    assert isinstance(result, str)
    assert len(result) == 1


def test_right_rotor_steps_on_each_keypress():
    plugboard = Plugboard([])
    rotor_r = Rotor(*ROTOR_I, ring_setting=0, position="A")
    rotor_m = Rotor(*ROTOR_II, ring_setting=0, position="A")
    rotor_l = Rotor(*ROTOR_III, ring_setting=0, position="A")
    reflector = Reflector(REFLECTOR_B)

    machine = EnigmaMachine([rotor_r, rotor_m, rotor_l], reflector, plugboard)

    machine.encode_letter("A")
    assert rotor_r.position == "B"
