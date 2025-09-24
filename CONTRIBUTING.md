# Contributing to Deep Research

Thank you for your interest in contributing to Deep Research! This document provides guidelines for contributing to this project.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- OpenAI API key (for testing)

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/deep_research.git
   cd deep_research
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use type hints where applicable
- Write descriptive docstrings for functions and classes
- Keep functions focused and single-purpose

### Project Structure
```
deep_research/
├── src/deep_research/     # Main source code
├── examples/              # Usage examples
├── docs/                  # Documentation
├── tests/                 # Test files
├── app.py                 # Main entry point
└── README.md
```

### Adding New Features

1. **Create an Issue**: Describe the feature you want to add
2. **Branch**: Create a feature branch from main
3. **Implement**: Write the code following our guidelines
4. **Test**: Add tests for your new functionality
5. **Document**: Update relevant documentation
6. **Submit**: Create a pull request

### Agent Development

When creating new agents:

1. **Follow the Agent Pattern**:
   ```python
   from agents import Agent

   agent = Agent(
       name="YourAgent",
       instructions="Clear instructions for the agent",
       model="gpt-4o-mini",
       output_type=YourOutputModel,  # Optional Pydantic model
   )
   ```

2. **Define Clear Interfaces**:
   - Use Pydantic models for structured output
   - Document input expectations
   - Handle errors gracefully

3. **Test Thoroughly**:
   - Unit tests for agent logic
   - Integration tests with other agents
   - Error handling tests

### Testing

Run tests with:
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_research_manager.py

# Run with coverage
python -m pytest --cov=src tests/
```

### Documentation

- Update README.md for user-facing changes
- Update ARCHITECTURE.md for design changes
- Add docstrings to new functions and classes
- Include examples for complex features

## Pull Request Process

1. **Update Version**: Bump version in `pyproject.toml` if needed
2. **Update Changelog**: Add your changes to CHANGELOG.md
3. **Test**: Ensure all tests pass
4. **Review**: Request review from maintainers
5. **Merge**: Maintainers will merge after approval

### Pull Request Template

Please include:
- [ ] Description of changes
- [ ] Type of change (bug fix, feature, docs, etc.)
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Breaking changes noted

## Issue Guidelines

### Bug Reports
Include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/stack traces

### Feature Requests
Include:
- Problem description
- Proposed solution
- Alternative solutions considered
- Impact on existing functionality

## Code of Conduct

### Our Standards
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Respect different viewpoints

### Enforcement
Maintainers will address any behavior that violates our standards. Serious violations may result in temporary or permanent exclusion from the project.

## Questions?

- Create an issue for bug reports or feature requests
- Check existing documentation first
- Be patient - maintainers are volunteers

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special recognition for outstanding contributions

Thank you for helping improve Deep Research! 🎉