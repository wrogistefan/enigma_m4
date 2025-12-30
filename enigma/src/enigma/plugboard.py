from __future__ import annotations

from typing import Any

TOKEN_LENGTH = 2
MAX_PAIRS = 10


class Plugboard:
    """Represents the Enigma plugboard (Steckerbrett).

    Fully historical and flexible:
    - Accepts dict: {"A": "B", "C": "D"}
    - Accepts list of pairs: [("A", "B"), ("C", "D")]
    - Accepts Kriegsmarine string: "PO ML IU KZ"
    - Accepts dash format: "A-B C-D"
    - Accepts compact format: "AB CD EF"
    """

    def __init__(self, connections: Any = None) -> None:
        self._mapping: dict[str, str] = {}

        if connections:
            normalized = self._normalize_connections(connections)
            self._initialize_connections(normalized)

    # ----------------------------------------------------------------------
    # NORMALIZATION LAYER
    # ----------------------------------------------------------------------
    def _normalize_connections(self, connections: Any) -> dict[str, str]:
        """Normalize input into a dict[str, str]."""

        # Already a dict
        if isinstance(connections, dict):
            return {a.upper(): b.upper() for a, b in connections.items()}

        # List of pairs
        if isinstance(connections, list):
            result = {}
            for a, b in connections:
                result[a.upper()] = b.upper()
            return result

        # String formats
        if isinstance(connections, str):
            text = connections.strip().upper()

            if "-" in text:
                pairs = text.split()
                result = {}
                for p in pairs:
                    a, b = p.split("-")
                    result[a] = b
                return result

            tokens = text.split()
            result = {}
            for token in tokens:
                if len(token) != TOKEN_LENGTH:
                    msg = f"Invalid plugboard token: {token!r}"
                    raise ValueError(msg)
                a, b = token[0], token[1]
                result[a] = b
            return result

        msg = "Plugboard connections must be dict, list, or string."
        raise TypeError(msg)

    # ----------------------------------------------------------------------
    # INTERNAL VALIDATION
    # ----------------------------------------------------------------------
    def _initialize_connections(self, connections: dict[str, str]) -> None:
        for a, b in connections.items():
            self._add_pair(a, b)

    def _add_pair(self, a: str, b: str) -> None:
        """Add a single plugboard pair, validating correctness."""

        # Historical limit: max 10 pairs
        if len(self._mapping) // 2 >= MAX_PAIRS:
            msg = "Plugboard cannot have more than 10 pairs."
            raise ValueError(msg)

        a = a.upper()
        b = b.upper()

        if a == b:
            msg = f"Cannot connect letter {a} to itself."
            raise ValueError(msg)

        for ch in (a, b):
            if not ch.isalpha() or len(ch) != 1:
                msg = f"Invalid plugboard character: {ch!r}"
                raise ValueError(msg)
            if ch in self._mapping:
                msg = f"Letter {ch} is already used in another pair."
                raise ValueError(msg)

        self._mapping[a] = b
        self._mapping[b] = a

    # ----------------------------------------------------------------------
    # OPERATION
    # ----------------------------------------------------------------------
    def swap(self, char: str) -> str:
        if not char.isalpha() or len(char) != 1:
            return char

        c = char.upper()
        return self._mapping.get(c, c)

    # ----------------------------------------------------------------------
    # UTILITIES
    # ----------------------------------------------------------------------
    def __repr__(self) -> str:
        return f"Plugboard({self._mapping})"

    def pairs(self) -> list[tuple[str, str]]:
        seen = set()
        result = []
        for a, b in self._mapping.items():
            if a not in seen and b not in seen:
                result.append((a, b))
                seen.add(a)
                seen.add(b)
        return result
