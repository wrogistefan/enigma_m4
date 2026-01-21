# Enigma Machine Simulator API Reference

This document provides a complete reference for the public API of the Enigma machine simulator.

## Core Classes

### EnigmaMachine

The main entry point for using the Enigma simulator.

#### Constructor

```python
EnigmaMachine(rotors: list[Rotor], reflector: Reflector, plugboard: Plugboard)
```

**Parameters:**
- `rotors` (list[Rotor]): List of rotors in order from right to left. For M3: [right, middle, left]. For M4: [right, middle, left, greek]
- `reflector` (Reflector): The reflector to use
- `plugboard` (Plugboard): The plugboard configuration

#### Methods

##### encode_letter(char: str) -> str

Encrypts a single letter, advancing the rotors before encryption.

**Parameters:**
- `char` (str): Single character to encrypt (case-insensitive)

**Returns:**
- `str`: Encrypted character (uppercase), or original character if not A-Z

**Example:**
```python
machine = EnigmaMachine([rotor_r, rotor_m, rotor_l], reflector, plugboard)
result = machine.encode_letter("A")  # Returns encrypted letter
```

##### step()

Advances the rotors according to Enigma stepping rules. Called automatically by `encode_letter()`.

**Behavior:**
- Right rotor always steps
- Middle rotor steps if right rotor is at its notch
- Middle rotor also steps if it is at its own notch (double-stepping)
- Left rotor steps only when middle rotor is at its notch
- Greek rotor (M4) never steps

### Rotor

Represents a single Enigma rotor with its wiring, notch, ring setting, and position.

#### Constructor

```python
Rotor(wiring: str, notch: str, ring_setting: int = 0, position: str = "A")
```

**Parameters:**
- `wiring` (str): 26-character string representing the rotor's internal wiring
- `notch` (str): Letter position that triggers the next rotor to step (None for Greek rotors)
- `ring_setting` (int): Ring offset (0-25), default 0
- `position` (str): Initial rotor position (A-Z), default "A"

**Raises:**
- `ValueError`: If wiring is not exactly 26 characters

#### Methods

##### encode_forward(char: str) -> str

Encodes a character from right to left through the rotor.

**Parameters:**
- `char` (str): Character to encode

**Returns:**
- `str`: Encoded character

##### encode_backward(char: str) -> str

Encodes a character from left to right through the rotor (reverse direction).

**Parameters:**
- `char` (str): Character to encode

**Returns:**
- `str`: Encoded character

##### step() -> bool

Advances the rotor by one position.

**Returns:**
- `bool`: True if the rotor is now at its notch position

##### at_notch() -> bool

Checks if the rotor is currently at its notch position.

**Returns:**
- `bool`: True if at notch

#### Properties

##### position: str

Current rotor position (A-Z). Can be modified directly.

##### ring_setting: int

Current ring setting (0-25). Can be modified directly.

### Reflector

Represents an Enigma reflector (Umkehrwalze).

#### Constructor

```python
Reflector(wiring: str, involution: bool = True)
```

**Parameters:**
- `wiring` (str): 26-character string representing the reflector's wiring
- `involution` (bool): Whether to validate as an involution (default True)

**Raises:**
- `ValueError`: If wiring is not 26 characters or not a valid involution

**Validation:**
- Must be exactly 26 characters
- Must be an involution (paired mappings, no fixed points)
- Each letter maps to exactly one other letter

#### Methods

##### reflect(char: str) -> str

Reflects a character through the reflector.

**Parameters:**
- `char` (str): Character to reflect

**Returns:**
- `str`: Reflected character

### Plugboard

Represents the Enigma plugboard (Steckerbrett).

#### Constructor

```python
Plugboard(connections=None)
```

**Parameters:**
- `connections` (dict | list | str | None): Plugboard connections in various formats

**Supported Formats:**

1. **Dictionary:**
   ```python
   {"A": "B", "C": "D"}
   ```

2. **List of pairs:**
   ```python
   [("A", "B"), ("C", "D")]
   ```

3. **Kriegsmarine string:**
   ```python
   "PO ML IU KZ"
   ```

4. **Dash format:**
   ```python
   "A-B C-D"
   ```

5. **Compact format:**
   ```python
   "AB CD EF"
   ```

**Raises:**
- `ValueError`: If more than 10 pairs, self-connections, or invalid characters

#### Methods

##### swap(char: str) -> str

Swaps a character through the plugboard.

**Parameters:**
- `char` (str): Character to swap

**Returns:**
- `str`: Swapped character, or original if no connection

##### pairs() -> list[tuple[str, str]]

Returns list of current plugboard pairs.

**Returns:**
- `list[tuple[str, str]]`: List of (letter1, letter2) pairs

## Data Constants

### Rotors

All rotor constants are tuples of `(wiring: str, notch: str)`.

#### M3 Rotors
```python
ROTOR_I = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
ROTOR_II = ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
ROTOR_III = ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
ROTOR_IV = ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
ROTOR_V = ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
```

#### Kriegsmarine Rotors
```python
ROTOR_VI = ("JPGVOUMFYQBENHZRDKASXLICTW", "Z")
ROTOR_VII = ("NZJHGRCXMYSWBOUFAIVLPEKQDT", "Z")
ROTOR_VIII = ("FKQHTLXOCBJSPDZRAMEWNIUYGV", "Z")
```

#### M4 Greek Rotors
```python
ROTOR_BETA = ("LEYJVCNIXWPBQMDRTAKZGFUHOS", None)    # No notch
ROTOR_GAMMA = ("FSOKANUERHMBTIYCWLQPZXVGJD", None)  # No notch
```

### Reflectors

All reflector constants are strings of 26 characters.

#### M3 Reflectors
```python
REFLECTOR_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
REFLECTOR_C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
```

#### M4 Thin Reflectors
```python
REFLECTOR_B_THIN = "ENKQAUYWJICOPBLMDXZVFTHRGS"
REFLECTOR_C_THIN = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
```

## Usage Examples

### Basic M3 Setup

```python
from enigma.core.machine import EnigmaMachine
from enigma.core.rotor import Rotor
from enigma.core.reflector import Reflector
from enigma.core.plugboard import Plugboard
from enigma.data.rotors import ROTOR_I, ROTOR_II, ROTOR_III
from enigma.data.reflectors import REFLECTOR_B

# Create components
rotors = [
    Rotor(*ROTOR_I, position="A"),
    Rotor(*ROTOR_II, position="A"),
    Rotor(*ROTOR_III, position="A")
]
reflector = Reflector(REFLECTOR_B)
plugboard = Plugboard()

# Create machine
machine = EnigmaMachine(rotors, reflector, plugboard)

# Encrypt
result = machine.encode_letter("H")
```

### M4 Setup with Greek Rotor

```python
from enigma.data.rotors import ROTOR_BETA
from enigma.data.reflectors import REFLECTOR_B_THIN

# Add Greek rotor
greek_rotor = Rotor(*ROTOR_BETA, position="A")
rotors = [
    Rotor(*ROTOR_I, position="A"),
    Rotor(*ROTOR_II, position="A"),
    Rotor(*ROTOR_III, position="A"),
    greek_rotor
]
reflector = Reflector(REFLECTOR_B_THIN)
machine = EnigmaMachine(rotors, reflector, plugboard)
```

### Advanced Configuration

```python
# Custom ring settings and positions
rotors = [
    Rotor(*ROTOR_I, ring_setting=5, position="B"),
    Rotor(*ROTOR_II, ring_setting=10, position="C"),
    Rotor(*ROTOR_III, ring_setting=15, position="D")
]

# Complex plugboard
plugboard = Plugboard({
    "A": "Z", "B": "Y", "C": "X", "D": "W",
    "E": "V", "F": "U", "G": "T", "H": "S",
    "I": "R", "J": "Q"
})
```

## Error Handling

The API provides clear error messages for common configuration mistakes:

- **Rotor wiring length**: "Rotor wiring must be 26 characters long."
- **Reflector validation**: "Reflector wiring must be an involution."
- **Plugboard limits**: "Plugboard cannot have more than 10 pairs."
- **Invalid characters**: "Invalid plugboard character: {char!r}"

All validation happens at object creation time, so configuration errors are caught early.