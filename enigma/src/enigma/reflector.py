class Reflector:
    """Represents an Enigma reflector (Umkehrwalze)."""

    ALPHABET_SIZE = 26

    def __init__(self, wiring: str, *, involution: bool = True) -> None:
        if len(wiring) != self.ALPHABET_SIZE:
            msg = "Reflector wiring must be 26 characters long."
            raise ValueError(msg)

        self.wiring = wiring.upper()
        self.involution = involution

        if self.involution:
            # Validate involution AND no fixed points
            for i, c in enumerate(self.wiring):
                j = ord(c) - ord("A")

                # 1. No letter may map to itself
                if i == j:
                    msg = "Reflector cannot map a letter to itself."
                    raise ValueError(msg)

                # 2. Must be symmetric: wiring[wiring[i]] == i
                if self.wiring[j] != chr(ord("A") + i):
                    msg = "Reflector wiring must be an involution."
                    raise ValueError(msg)

    @staticmethod
    def _char_to_index(c: str) -> int:
        return ord(c) - ord("A")

    @staticmethod
    def _index_to_char(i: int) -> str:
        return chr(ord("A") + i)

    def reflect(self, char: str) -> str:
        """Reflect a character through the reflector."""
        c = char.upper()
        if c < "A" or c > "Z":
            return c

        i = self._char_to_index(c)
        return self.wiring[i]
