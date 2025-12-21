class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def step(self):
        r, m, l = self.rotors

        right_at_notch = r.at_notch()
        middle_at_notch = m.at_notch()

        # Double-step: middle steps if it is at its own notch
        if middle_at_notch:
            m.step()
            l.step()

        # Normal turnover: middle steps if right is at its notch
        if right_at_notch:
            m.step()

        # Right rotor always steps
        r.step()

        


    def encode_letter(self, char):
        # najpierw stepping
        self.step()

        # na razie zwracamy literę bez zmian
        return char
