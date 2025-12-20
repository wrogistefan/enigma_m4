from __future__ import annotations


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
        self.wiring = wiring
        self.notch = notch
        self.ring_setting = ring_setting
        self.position = position.upper()

    def encode_forward(self, char: str) -> str:
        """Encode a character from right to left through the rotor."""
        raise NotImplementedError

    def encode_backward(self, char: str) -> str:
        """Encode a character from left to right through the rotor."""
        raise NotImplementedError

    def step(self) -> bool:
        """Advance the rotor by one position.

        Returns
        -------
        bool
            True if this rotor reaches its notch and should trigger the next rotor.
        """
        raise NotImplementedError
