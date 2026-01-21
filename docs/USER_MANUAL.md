# Enigma Machine Simulator User Manual

## What is the Enigma Machine?

The Enigma machine was a cipher device used by Nazi Germany during World War II for secure communication. It implemented a polyalphabetic substitution cipher with rotor-based encryption, making it extremely difficult to break without the correct settings.

This simulator faithfully recreates the Enigma M3 (Heer/Luftwaffe) and M4 (Kriegsmarine) machines, including all historical mechanics like rotor stepping, ring settings, plugboard connections, and reflectors.

## Installation

Install from PyPI:

```bash
pip install enigma-m4
```

Or install from source:

```bash
git clone https://github.com/wrogistefan/enigma_m4.git
cd enigma_m4
pip install -e .
```

## Quick Start

Here's a basic example to encrypt a message:

```python
from enigma.core.machine import EnigmaMachine
from enigma.core.rotor import Rotor
from enigma.core.reflector import Reflector
from enigma.core.plugboard import Plugboard
from enigma.data.rotors import ROTOR_I, ROTOR_II, ROTOR_III
from enigma.data.reflectors import REFLECTOR_B

# Create components
rotor_right = Rotor(*ROTOR_I, ring_setting=0, position="A")
rotor_middle = Rotor(*ROTOR_II, ring_setting=0, position="A")
rotor_left = Rotor(*ROTOR_III, ring_setting=0, position="A")
reflector = Reflector(REFLECTOR_B)
plugboard = Plugboard({"A": "B", "C": "D"})  # Simple plugboard

# Create machine
machine = EnigmaMachine([rotor_right, rotor_middle, rotor_left], reflector, plugboard)

# Encrypt a message
plaintext = "HELLO"
ciphertext = ""
for char in plaintext:
    ciphertext += machine.encode_letter(char)

print(f"Encrypted: {ciphertext}")
```

## Configuring Rotors

### Basic Rotor Setup

Each rotor has:
- **Wiring**: The internal letter substitution mapping
- **Notch**: Position that triggers the next rotor to step
- **Ring setting**: Offset for the internal wiring (0-25)
- **Position**: Current rotor position (A-Z)

```python
from enigma.data.rotors import ROTOR_I

# Create rotor with default settings
rotor = Rotor(*ROTOR_I)  # ring_setting=0, position="A"

# Or specify settings
rotor = Rotor(*ROTOR_I, ring_setting=5, position="B")
```

### Available Rotors

#### M3 Rotors (I-V)
- `ROTOR_I`: Wehrmacht/Luftwaffe rotor I
- `ROTOR_II`: Wehrmacht/Luftwaffe rotor II
- `ROTOR_III`: Wehrmacht/Luftwaffe rotor III
- `ROTOR_IV`: Wehrmacht/Luftwaffe rotor IV
- `ROTOR_V`: Wehrmacht/Luftwaffe rotor V

#### Kriegsmarine Rotors (VI-VIII)
- `ROTOR_VI`: Kriegsmarine rotor VI
- `ROTOR_VII`: Kriegsmarine rotor VII
- `ROTOR_VIII`: Kriegsmarine rotor VIII

#### M4 Greek Rotors
- `ROTOR_BETA`: Greek rotor Beta (static, doesn't rotate)
- `ROTOR_GAMMA`: Greek rotor Gamma (static, doesn't rotate)

## Configuring Reflectors

Reflectors provide the "reflection" that makes Enigma self-reciprocal (encrypting twice returns the original text).

```python
from enigma.data.reflectors import REFLECTOR_B

reflector = Reflector(REFLECTOR_B)
```

### Available Reflectors

#### M3 Reflectors
- `REFLECTOR_A`: Reflector A
- `REFLECTOR_B`: Reflector B
- `REFLECTOR_C`: Reflector C

#### M4 Thin Reflectors
- `REFLECTOR_B_THIN`: Thin reflector B
- `REFLECTOR_C_THIN`: Thin reflector C

## Configuring Ring Settings

Ring settings offset the rotor's internal wiring:

```python
# Ring setting of 1 rotates the wiring by one position
rotor = Rotor(*ROTOR_I, ring_setting=1, position="A")
```

Ring settings range from 0-25 (0 = no offset, 25 = 25 positions offset).

## Configuring Rotor Positions

Rotor positions determine the initial alignment:

```python
# Start with rotor at position "B"
rotor = Rotor(*ROTOR_I, position="B")
```

Positions are letters A-Z.

## Configuring the Plugboard

The plugboard swaps letters before and after rotor encryption:

```python
# Dictionary format
plugboard = Plugboard({"A": "B", "C": "D"})

# List of pairs
plugboard = Plugboard([("A", "B"), ("C", "D")])

# Kriegsmarine string format
plugboard = Plugboard("PO ML IU KZ")

# Dash format
plugboard = Plugboard("A-B C-D")

# Compact format
plugboard = Plugboard("AB CD EF")
```

**Historical limit**: Maximum 10 pairs.

## Using Enigma M3

The M3 uses 3 rotors in the order: Right → Middle → Left.

```python
from enigma.core.machine import EnigmaMachine
from enigma.core.rotor import Rotor
from enigma.core.reflector import Reflector
from enigma.core.plugboard import Plugboard
from enigma.data.rotors import ROTOR_I, ROTOR_II, ROTOR_III
from enigma.data.reflectors import REFLECTOR_B

# Create 3 rotors
rotors = [
    Rotor(*ROTOR_I, position="A"),    # Right
    Rotor(*ROTOR_II, position="A"),   # Middle
    Rotor(*ROTOR_III, position="A"),  # Left
]

reflector = Reflector(REFLECTOR_B)
plugboard = Plugboard([])  # No connections

machine = EnigmaMachine(rotors, reflector, plugboard)
```

## Using Enigma M4

The M4 adds a 4th Greek rotor that doesn't rotate, placed between the left rotor and reflector.

```python
from enigma.data.rotors import ROTOR_BETA
from enigma.data.reflectors import REFLECTOR_B_THIN

# Create 4 rotors: Right, Middle, Left, Greek
rotors = [
    Rotor(*ROTOR_I, position="A"),      # Right
    Rotor(*ROTOR_II, position="A"),     # Middle
    Rotor(*ROTOR_III, position="A"),    # Left
    Rotor(*ROTOR_BETA, position="A"),   # Greek (static)
]

reflector = Reflector(REFLECTOR_B_THIN)
plugboard = Plugboard([])

machine = EnigmaMachine(rotors, reflector, plugboard)
```

## Encryption/Decryption Flows

### Single Letter Encryption

```python
# Each call to encode_letter advances the rotors
encrypted = machine.encode_letter("H")
```

### Full Message Encryption

```python
def encrypt_message(machine, message):
    ciphertext = ""
    for char in message.upper():
        if char.isalpha():
            ciphertext += machine.encode_letter(char)
        else:
            ciphertext += char  # Preserve non-letters
    return ciphertext

plaintext = "HELLO WORLD"
ciphertext = encrypt_message(machine, plaintext)
```

### Decryption

Since Enigma is reciprocal, decryption uses the same settings:

```python
# Use the same machine configuration
decrypted = encrypt_message(machine, ciphertext)
assert decrypted == plaintext
```

## Historical Accuracy

This simulator implements:

- **Authentic rotor stepping**: Right rotor steps every keypress, middle steps at turnover, double-stepping when middle is at its notch
- **Correct signal path**: Plugboard → Rotors (forward) → Reflector → Rotors (backward) → Plugboard
- **Historical rotor wirings**: Exact reproductions of real Enigma rotors
- **Plugboard constraints**: Maximum 10 pairs, no self-connections
- **M4 mechanics**: Greek rotor doesn't rotate, thin reflectors

## Limitations and Expected Behavior

### Case Handling
- Input is automatically converted to uppercase
- Non-alphabetic characters pass through unchanged
- Output is always uppercase letters

### Rotor Stepping
- Only the right 3 rotors step (Greek rotor in M4 is static)
- Stepping happens **before** each letter encryption
- Double-stepping occurs when middle rotor reaches its notch

### Validation
- Rotor wiring must be exactly 26 characters
- Reflectors must be involutions (paired mappings)
- Plugboard limited to 10 pairs maximum
- All positions must be A-Z

### Performance
- Each `encode_letter()` call processes one character
- No batch processing optimization
- Suitable for educational use, not high-volume encryption

## Troubleshooting

### Common Issues

**"Rotor wiring must be 26 characters long"**
- Check that you're unpacking rotor tuples correctly: `Rotor(*ROTOR_I, ...)`

**"Reflector wiring must be an involution"**
- Ensure reflector wiring is properly paired (each letter maps to exactly one other)

**"Plugboard cannot have more than 10 pairs"**
- Historical Enigma limit; reduce connections

**Unexpected output**
- Verify rotor order: `[right, middle, left]` for M3, `[right, middle, left, greek]` for M4
- Check that rotors are created with correct positions and ring settings