# Enigma-M4

A modern, fully tested, and extensible Enigma machine simulator written in Python.  
This project aims to recreate the historical Enigma M3/M4 cipher machine with clean architecture, full test coverage, and optional GUI for educational purposes.

## Features (current and planned)

- 🔌 **Plugboard (Steckerbrett)** — fully validated letter‑pair swapping  
- ⚙️ **Rotors** — historically accurate wiring, stepping, ring settings  
- 🔄 **Reflectors** — including Thin B and Thin C for M4  
- 🧠 **EnigmaMachine** — complete signal path implementation  
- 🧪 **Full test suite** — unit tests and integration tests  
- 🖥️ **CLI interface** — encrypt/decrypt from the command line  
- 🎨 **GUI (planned)** — interactive interface showing rotor movement and lampboard  
- 📜 **Historical test vectors** — including real Kriegsmarine messages

## Project Goals

- Provide a clean, readable, and well‑structured implementation suitable for learning and teaching.
- Recreate the behavior of the historical Enigma machine as accurately as possible.
- Offer both a command‑line interface and a graphical interface.
- Include real historical ciphertexts and plaintexts as integration tests.

## Repository Structure

enigma/
core/          # Core cryptographic components
data/          # Rotor and reflector definitions
cli/           # Command-line interface
gui/           # Graphical interface (planned)
tests/             # Unit and integration tests


## Installation

```bash
pip install -e .

Historical Test Case
This project includes a real Kriegsmarine M4 ciphertext from 25 November 1942
("WETTERVORHERSAGE BISKAYA") as a golden integration test.

License
MIT License

