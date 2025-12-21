# Changelog

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
