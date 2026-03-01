# Contributing to Flask Debugger

Thank you for your interest in contributing to Flask Debugger! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## Development Setup

```bash
# Repo klonen
git clone https://github.com/marzaun/debugger.git
cd debugger

# Virtuele Umgebung erstellen
python -m venv venv
source venv/bin/activate

# Abhängigkeiten erstellen
pip install -r requirements.txt

# Umgebungstamplate kopieren
cp .env.example .env

# Applikation laufen lassen n
python app.py
```

## Code Style

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

## Testing

Before submitting a pull request:

1. Ensure all existing tests pass
2. Add tests for new functionality
3. Test in both development and production modes
4. Check for security vulnerabilities

## Commit Messages

Write clear, concise commit messages:

- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Add detailed description if needed

Good examples:
- `Add user authentication endpoint`
- `Fix memory leak in debug mode`
- `Update documentation for Docker deployment`

## Pull Request Process

1. Update README.md with details of changes if needed
2. Update the documentation with any new features
3. Ensure all tests pass
4. Request review from maintainers
5. Address any feedback from reviewers

## Security

If you discover a security vulnerability:

1. **DO NOT** open a public issue
2. Email security concerns to: security@example.com
3. Include detailed information about the vulnerability
4. Allow time for the issue to be fixed before disclosure
