![Python](https://img.shields.io/badge/Python-3.12-blue)
![Tests](https://img.shields.io/badge/Tests-passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

# Enigma Machine Simulator (M3 → M4)

A clean, modular, historically accurate simulation of the German Enigma M3 cipher machine, written in Python.  
The project focuses on correctness, mechanical fidelity, and modern software architecture.  
It is designed to evolve naturally into a full M4 Kriegsmarine simulator.

---

## Project Goals

- Faithfully reproduce the electrical and mechanical logic of the Enigma M3
- Preserve historical behaviour:
  - rotor stepping
  - double-stepping
  - ring settings (Ringstellung)
  - rotor positions (Grundstellung)
  - plugboard (Steckerbrett)
  - reflector involution
- Provide a clean, testable, extensible architecture
- Serve as a high-quality portfolio project demonstrating engineering skill

---

## Architecture Overview

The machine is composed of independent, testable components:

```
Plugboard
   ↓
Right Rotor → Middle Rotor → Left Rotor
   ↓             ↓              ↓
            Reflector
   ↑             ↑              ↑
Right Rotor ← Middle Rotor ← Left Rotor
   ↑
Plugboard
```

### Plugboard
- Bidirectional letter swapping  
- Full validation  
- Historical 10-pair limit  
- API: `swap(char)`

### Rotors
- Forward and backward signal path  
- Ring setting  
- Rotor position  
- Notch logic  
- `step()` rotation  
- Historical wirings included:
  - I, II, III, IV, V  
  - VI, VII, VIII (Kriegsmarine)  
  - Beta, Gamma (M4 static rotors)

### Reflectors
- Involutive mapping  
- No fixed points  
- Historical reflectors:
  - A, B, C  
  - Thin B, Thin C (M4)

### EnigmaMachine (coming next)
- Full stepping logic  
- Double-stepping  
- Complete signal path  
- M3 first, then M4 upgrade

---

## Project Structure

```
enigma/
 ├── core/
 │    ├── rotor.py
 │    ├── reflector.py
 │    ├── plugboard.py
 │    └── machine.py
 ├── data/
 │    ├── rotors.py
 │    └── reflectors.py
 ├── tests/
 │    ├── test_rotor.py
 │    ├── test_reflector.py
 │    ├── test_plugboard.py
 │    └── test_machine.py
 ├── README.md
 ├── LICENSE
 ├── CHANGELOG.md
 └── project.toml
```

---

## Testing

Run all tests:

```
pytest -q
```

---

## Roadmap

### Next (M3)
- Implement EnigmaMachine
- Implement stepping logic
- Implement double-stepping
- Implement full signal path
- Add integration tests

### After M3
- Add M4 Greek rotor (Beta/Gamma)
- Add Thin reflectors
- Add Kriegsmarine stepping logic
- Add configuration presets

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## About the Author

**Łukasz Perek** is a Python developer with a strong focus on clean architecture, cryptography, and historically inspired engineering projects.  
With over a decade of experience in technical support, telecommunications, and workflow optimization, he brings a practical, systems‑oriented mindset to software development.

Currently based in Syracuse, Sicily, Łukasz is transitioning into full‑time software engineering and AI‑driven development.  
He specializes in:

- Python (OOP, CLI tools, packaging, testing)
- Clean, modular architecture
- Cryptographic systems and historical computing
- CI/CD pipelines (GitHub Actions, linting, coverage)
- Documentation and developer experience

This Enigma simulator is part of his public portfolio — a demonstration of engineering discipline, historical accuracy, and modern Python design.

If you find this project interesting or useful, feel free to ⭐ the repository.

---

### Connect

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/wrogistefan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/lukaszperek)
