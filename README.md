![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tests](https://img.shields.io/badge/Tests-passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
[![codecov](https://codecov.io/gh/wrogistefan/enigma_m4/branch/main/graph/badge.svg)](https://codecov.io/gh/wrogistefan/enigma_m4)

# 🔐 Enigma Machine Simulator (M3 → M4)

A clean, modular, historically accurate simulation of the German **Enigma M3** and **Kriegsmarine M4** cipher machines — implemented in modern Python, with full test coverage and historically faithful mechanics.

This project emphasizes:

- correctness  
- mechanical fidelity  
- clean architecture  
- testability  
- extensibility  

It is both a **learning tool** and a **professional portfolio project** demonstrating engineering discipline and historical accuracy.

---

# ✨ Features

### 🧠 Core Capabilities
- Full **M3** support (rotors I–VIII, reflectors A/B/C)
- Full **M4** support (III–II–I + Greek rotor)
- Greek rotors: **Beta**, **Gamma**
- Thin reflectors: **Thin B**, **Thin C**
- Historically accurate **stepping** and **double‑stepping**
- Ring settings (Ringstellung)
- Rotor positions (Grundstellung)
- Plugboard (Steckerbrett) with validation
- Full reversibility (Enigma property)

### 🔌 Historical Plugboard
Supports all historically used formats:

```python
{"A": "B"}                     # dict
[("A", "B"), ("C", "D")]       # list of pairs
"PO ML IU KZ"                  # Kriegsmarine format
"A-B C-D"                      # dash format
```

Up to **10 pairs**, matching real Enigma constraints.

---

# 🧩 Architecture Overview

The machine is composed of independent, testable components:

```
Plugboard
   ↓
Right Rotor → Middle Rotor → Left Rotor → Greek Rotor (M4)
   ↓             ↓              ↓             ↓
                     Reflector
   ↑             ↑              ↑             ↑
Right Rotor ← Middle Rotor ← Left Rotor ← Greek Rotor
   ↑
Plugboard
```

### 🔧 Components

#### 🔌 Plugboard
- Bidirectional letter swapping  
- Full validation  
- Historical 10‑pair limit  
- API: `swap(char)`

#### ⚙ Rotors
- Forward & backward signal path  
- Ring setting  
- Rotor position  
- Notch logic  
- `step()` rotation  
- Includes:
  - I, II, III, IV, V  
  - VI, VII, VIII (Kriegsmarine)  
  - Beta, Gamma (M4 static rotors)

#### 🪞 Reflectors
- Involutive mapping  
- No fixed points  
- Includes:
  - A, B, C  
  - Thin B, Thin C (M4)

#### 🖥 EnigmaMachine
- Correct stepping logic (M3 + M4)
- Double‑stepping implemented
- Full signal path implemented
- Plugboard integration
- Reversible encryption

---

# 📁 Project Structure

```
enigma_m4/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── enigma/
│       ├── __init__.py
│       ├── core/
│       │   ├── rotor.py
│       │   ├── reflector.py
│       │   ├── plugboard.py
│       │   └── machine.py
│       ├── data/
│       │   ├── rotors.py
│       │   └── reflectors.py
│       └── utils/
│           ├── cli/
│           │   ├── __init__.py
│           │   └── main.py
│           └── gui/
│               ├── __init__.py
│               └── app.py
└── tests/
    ├── test_rotor.py
    ├── test_reflector.py
    ├── test_plugboard.py
    ├── test_machine.py
    ├── test_rotors.py
    ├── test_reflectors.py
    ├── test_integration.py
    ├── test_integration_m4.py
    ├── test_intergation_m4_historical.py
    └── __init__.py
```

---

# 🧪 Testing

Run all tests:

```
pytest -q
```

The test suite includes:

- unit tests for rotors, reflectors, plugboard  
- M3 integration tests  
- M4 integration tests  
- historical canonical tests:
  - Beta + Thin B → A → **B**
  - Gamma + Thin C → A → **P**
- reversibility tests  
- ring setting tests  
- plugboard tests  
- Kriegsmarine‑style configuration tests  

---

# 🗺 Roadmap

### ✅ Completed (v0.4.0)
- Full M3 implementation  
- Full M4 implementation  
- Greek rotors (Beta/Gamma)  
- Thin reflectors (Thin B/C)  
- Historical plugboard formats  
- Full stepping logic  
- Comprehensive test suite  

### 🔜 Next
- Add historical daily key sheets  
- Add real U‑boat message examples  
- Add CLI interface  
- Add web demo  
- Add visualization of rotor stepping  

---

# 📜 License

This project is licensed under the [MIT License](LICENSE).

---

# 👤 About the Author

**Łukasz Perek** — Python developer focused on clean architecture, cryptography, and historically inspired engineering.

Based in **Syracuse, Sicily**, transitioning into full‑time software engineering and AI‑driven development.

Specializes in:

- Python (OOP, CLI tools, packaging, testing)
- Clean, modular architecture
- Cryptographic systems & historical computing
- CI/CD (GitHub Actions, linting, coverage)
- Documentation & developer experience

This Enigma simulator is part of his public portfolio — a demonstration of engineering discipline, historical accuracy, and modern Python design.

If you find this project interesting or useful, feel free to ⭐ the repository.

---

# 🔗 Connect

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/wrogistefan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/lukaszperek)
