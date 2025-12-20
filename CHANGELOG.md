# Changelog
All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog  
and this project adheres to Semantic Versioning.

---

## [0.2.0] – 2025‑12‑20
### Added
- Full Plugboard implementation with validation and historical 10‑pair limit.
- Complete Rotor class:
  - forward/backward signal path
  - ring setting (Ringstellung)
  - rotor position (Grundstellung)
  - notch logic
  - step() rotation
- Added all historical rotor wirings (I–VIII, Beta, Gamma).
- Implemented Reflector class with involution and fixed‑point validation.
- Added all historical reflectors (A, B, C, Thin B, Thin C).
- Added unit tests for plugboard, rotors, and reflectors.

### Next
- Implement EnigmaMachine stepping (including double‑stepping).
- Implement full signal path through the machine.
- Add integration tests for M3.
- Prepare for M4 upgrade (Greek rotor + Thin reflectors).

---

## [0.1.0] – Initial
### Added
- Project structure
- Basic test suite
