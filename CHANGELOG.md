# Changelog

## [0.4.0] — 2025-12-21
### Added
- Full support for the Kriegsmarine Enigma M4 machine.
- Greek rotors (Beta, Gamma) with correct non-rotating behavior.
- Thin reflectors (Thin B, Thin C) with historically accurate wiring.
- Complete M4 stepping logic (right/middle/left rotors only).
- Historical, flexible plugboard supporting:
  - dict format: {"A": "B"}
  - list of pairs: [("A", "B")]
  - Kriegsmarine format: "PO ML IU KZ"
  - dash format: "A-B C-D"
- Comprehensive M4 integration test suite:
  - Beta + Thin B canonical test
  - Gamma + Thin C canonical test
  - reversibility tests
  - ring-setting tests
  - plugboard tests
  - Kriegsmarine-style configuration test

### Improved
- Rotor stepping logic unified for M3 and M4.
- Code clarity and historical accuracy across core modules.
- Test suite stability and coverage.

### Fixed
- Import issues and indentation errors in rotor and plugboard modules.
- Incorrect assumptions in earlier M4 tests.


## v0.3.0-alpha — Stepping Logic Implemented
**Release date:** 2025-01-21

### Added
- Fully implemented rotor stepping logic for the Enigma M3
- Historically accurate double-stepping behaviour
- Unit tests verifying:
  - right rotor always steps
  - turnover (right rotor notch → middle rotor steps)
  - double-step (middle rotor notch → middle + left rotor step)
  - forced double-step scenario
- Updated README with version information and stepping milestone

### Notes
This release marks the first milestone where the mechanical heart of the Enigma is fully functional.  
Next step: implement the full electrical signal path (forward → reflector → backward).

---

## v0.2.0-alpha — Rotor, Reflector, Plugboard Core
**Release date:** 2025-01-15

### Added
- Rotor class with forward/backward mapping, ring settings, and notch logic
- Reflector class with involutive mapping and historical wirings
- Plugboard with validation and bidirectional swapping
- Initial unit tests for all core components

---

## v0.1.0-alpha — Project Initialization
**Release date:** 2025-01-10

### Added
- Project structure and repository setup
- Basic documentation
- CI configuration and coverage reporting
