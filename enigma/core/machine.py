class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def step(self):
        # minimalny krok: obraca się tylko prawy rotor
        self.rotors[0].step()

    def encode_letter(self, char):
        # najpierw stepping
        self.step()

        # na razie zwracamy literę bez zmian
        return char
