from __future__ import annotations


class Plugboard:
    """Represents the Enigma plugboard (Steckerbrett).

    The plugboard swaps pairs of letters before and after the rotor encoding.
    Only uppercase A–Z letters are considered. If a letter is not part of any
    configured pair, it passes through unchanged.

    Historically, the plugboard allowed up to 10 cables (10 pairs).
    """

    def __init__(self, connections: dict[str, str] | None = None) -> None:
        """
        Initialize the plugboard with optional letter-pair connections.

        Parameters
        ----------
        connections : dict[str, str] | None
            A dictionary mapping letters to letters, e.g. {"A": "V"}.
            If only one direction is provided, the reverse mapping is added
            automatically. All letters must be unique across all pairs.
        """
        self._mapping: dict[str, str] = {}
        if connections:
            self._initialize_connections(connections)

    def _initialize_connections(self, connections: dict[str, str]) -> None:
        """Validate and register all plugboard connections."""
        for a, b in connections.items():
            self._add_pair(a, b)

    def _add_pair(self, a: str, b: str) -> None:
        """Add a single plugboard pair, validating correctness."""

        # 🔥 HISTORYCZNY LIMIT: maksymalnie 10 par (20 liter)
        if len(self._mapping) // 2 >= 10:
            raise ValueError("Plugboard cannot have more than 10 pairs.")

        a = a.upper()
        b = b.upper()

        if a == b:
            raise ValueError(f"Cannot connect letter {a} to itself.")

        for ch in (a, b):
            if not ch.isalpha() or len(ch) != 1:
                raise ValueError(f"Invalid plugboard character: {ch!r}")
            if ch in self._mapping:
                raise ValueError(f"Letter {ch} is already used in another pair.")

        self._mapping[a] = b
        self._mapping[b] = a

    def swap(self, char: str) -> str:
        """Return the letter after passing through the plugboard.

        Parameters
        ----------
        char : str
            A single alphabetic character.

        Returns
        -------
        str
            The swapped character if connected, otherwise the original.
        """
        if not char.isalpha() or len(char) != 1:
            return char

        c = char.upper()
        return self._mapping.get(c, c)

    def __repr__(self) -> str:
        return f"Plugboard({self._mapping})"

    def pairs(self) -> list[tuple[str, str]]:
        """Return the list of plugboard pairs (unique, no duplicates)."""
        seen = set()
        result = []
        for a, b in self._mapping.items():
            if a not in seen and b not in seen:
                result.append((a, b))
                seen.add(a)
                seen.add(b)
        return result
