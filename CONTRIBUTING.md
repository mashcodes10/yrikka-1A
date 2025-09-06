# Contributing to YRIKKA Challenge Project

Thank you for contributing to the YRIKKA Challenge project! This document provides guidelines for team collaboration.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd yrikka
   ```

2. **Set up your environment**
   ```bash
   python scripts/setup_environment.py
   ```

3. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Development Workflow

### Branch Strategy
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/<feature-name>`: Individual feature development
- `hotfix/<issue>`: Critical bug fixes

### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear, documented code
   - Follow the coding standards below
   - Add tests for new functionality

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add descriptive commit message"
   ```

4. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Commit Message Convention

Use conventional commit format:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
- `feat: add image augmentation pipeline`
- `fix: resolve dataset loading issue`
- `docs: update API documentation`

## Coding Standards

### Python Code Style
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Type hints are encouraged

### File Organization
```
src/
├── models/          # Model definitions
├── data/            # Data processing utilities
├── training/        # Training scripts
├── evaluation/      # Evaluation metrics and scripts
└── utils/           # General utilities
```

### Documentation
- Document all public functions and classes
- Include usage examples in docstrings
- Update README.md for significant changes
- Add comments for complex logic

## Code Quality

### Testing
- Write unit tests for new functions
- Run tests before submitting PRs
- Aim for good test coverage

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

### Linting
```bash
# Format code
black src/

# Check style
flake8 src/

# Type checking (optional)
mypy src/
```

## Working with Datasets

### Dataset Guidelines
- Never commit large dataset files to git
- Use the provided `dataset_loader.py` utility
- Document any data preprocessing steps
- Include data validation in your scripts

### Adding New Features

When adding new functionality:

1. **Create appropriate tests**
2. **Update documentation**
3. **Follow existing patterns**
4. **Consider backwards compatibility**

## Pull Request Process

### Before Submitting
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Meaningful commit messages

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
```

### Review Process
1. At least one team member review required
2. All discussions must be resolved
3. All checks must pass
4. Squash and merge preferred

## Issue Reporting

When reporting issues:
1. Use descriptive titles
2. Provide steps to reproduce
3. Include environment information
4. Add relevant labels

## Communication

### Team Communication
- Use clear, descriptive issue titles
- Tag relevant team members in PRs
- Use discussions for design decisions
- Keep PRs focused and small

### Code Reviews
- Be constructive and respectful
- Focus on code quality and correctness
- Suggest improvements, don't just point out problems
- Approve when satisfied with changes

## Project Structure

### Key Files
- `src/dataset_loader.py`: Main data loading utility
- `notebooks/dataset_exploration.ipynb`: Data analysis
- `scripts/setup_environment.py`: Environment setup
- `requirements.txt`: Python dependencies

### Adding Dependencies
1. Add to `requirements.txt`
2. Update `setup_environment.py` if needed
3. Document in PR why dependency is needed

## Troubleshooting

### Common Issues
1. **Import errors**: Check virtual environment activation
2. **Dataset not found**: Verify BTT_Data directory structure
3. **Permission errors**: Check file permissions

### Getting Help
1. Check existing issues
2. Ask in team discussions
3. Refer to documentation
4. Contact project maintainers

## Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Best Practices](https://git-scm.com/book)

Thank you for contributing to the YRIKKA Challenge project! 🚀
