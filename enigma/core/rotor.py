from __future__ import annotations
from string import ascii_uppercase


class Rotor:
    """Represents a single Enigma rotor.

    A rotor performs a forward and backward substitution based on its internal wiring,
    ring setting, and current rotational position. It also defines a notch position
    that determines when the next rotor should step.
    """

    def __init__(
        self,
        wiring: str,
        notch: str,
        ring_setting: int = 0,
        position: str = "A",
    ) -> None:
        """
        Parameters
        ----------
        wiring : str
            A 26-character string defining the rotor's internal substitution.
        notch : str
            The letter at which this rotor triggers the next rotor to step.
        ring_setting : int
            The ring setting (Ringstellung), 0–25.
        position : str
            The current rotational position of the rotor (A–Z).
        """
        if len(wiring) != 26:
            raise ValueError("Rotor wiring must be 26 characters long.")

        self.wiring = wiring.upper()
        self.notch = notch.upper()
        self.ring_setting = ring_setting
        self.position = position.upper()

    @staticmethod
    def _char_to_index(char: str) -> int:
        """Convert an uppercase letter A–Z to an index 0–25."""
        return ord(char) - ord("A")

    @staticmethod
    def _index_to_char(index: int) -> str:
        """Convert an index 0–25 back to an uppercase letter A–Z."""
        return chr(ord("A") + index)

    def encode_forward(self, char: str) -> str:
        """Encode a character from right to left through the rotor.

        Includes rotor position and ring setting.
        """
        c = char.upper()
        if c < "A" or c > "Z":
            return c

        i = self._char_to_index(c)
        pos = self._char_to_index(self.position)
        ring = self.ring_setting

        # Apply position and ring setting
        shifted_in = (i + pos - ring) % 26

        # Pass through wiring
        wired_char = self.wiring[shifted_in]
        j = self._char_to_index(wired_char)

        # Undo position and ring setting
        shifted_out = (j - pos + ring) % 26

        return self._index_to_char(shifted_out)

    def encode_backward(self, char: str) -> str:
        """Encode a character from left to right through the rotor.

        This is the inverse mapping of encode_forward, including rotor
        position and ring setting.
        """
        c = char.upper()
        if c < "A" or c > "Z":
            return c

        i = self._char_to_index(c)
        pos = self._char_to_index(self.position)
        ring = self.ring_setting

        # Apply position and ring setting
        shifted_in = (i + pos - ring) % 26

        # Find which wiring index produces this output
        wired_index = self.wiring.index(self._index_to_char(shifted_in))

        # Undo position and ring setting
        shifted_out = (wired_index - pos + ring) % 26

        return self._index_to_char(shifted_out)


    def step(self) -> bool:
        """Advance the rotor by one position.

        Returns
        -------
        bool
            True if the rotor is now at its notch position and should
            trigger the next rotor to step.
        """
        # Convert current position to index
        pos = self._char_to_index(self.position)

        # Advance by one
        pos = (pos + 1) % 26

        # Update position
        self.position = self._index_to_char(pos)

        # Check if we hit the notch
        return self.position == self.notch
