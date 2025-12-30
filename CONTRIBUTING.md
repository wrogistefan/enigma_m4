# Contributing to Enigma M4 Simulator

Thank you for your interest in contributing to the Enigma M4 Simulator project!

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. By participating, you agree to:
- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Show empathy towards other contributors

## How to Contribute

### Reporting Bugs
- Use the issue tracker to report bugs
- Include detailed steps to reproduce
- Provide system information and Python version
- Include error messages and stack traces

### Suggesting Features
- Use the issue tracker for feature requests
- Clearly describe the proposed feature
- Explain why it would be beneficial
- Consider alternative approaches

### Pull Requests
1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Ensure tests pass: `pytest`
5. Run linting: `ruff check src/`
6. Run type checking: `mypy src/`
7. Update documentation if needed
8. Submit a pull request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/wrogistefan/enigma_m4.git
cd enigma_m4

# Install in development mode
pip install -e .

# Install development dependencies
pip install ruff mypy pytest pytest-cov safety

# Run tests
pytest

# Run linting
ruff check src/

# Run type checking
mypy src/
```

## Code Standards

- **Type Hints**: All functions and methods must have type hints
- **Linting**: Code must pass `ruff` checks
- **Testing**: Maintain high test coverage
- **Documentation**: Update docstrings and README for significant changes
- **Style**: Follow PEP 8 with 88 character line length

## Commit Messages

Use clear, descriptive commit messages:
- Start with a verb (Add, Fix, Update, etc.)
- Keep the first line under 50 characters
- Provide detailed description in the body if needed

## License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.