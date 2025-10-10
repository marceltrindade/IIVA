# IIVA Development Guidelines

## 1. Coding Standards

### 1.1 Python Style Guide
- Follow PEP 8 for Python code style
- Use 4 spaces for indentation (no tabs)
- Maximum line length of 88 characters (compatible with Black formatter)
- Use descriptive variable and function names
- Include documentation strings for all public functions
- Write clean, readable code with appropriate comments

### 1.2 Naming Conventions
- Use `snake_case` for functions, variables, and file names
- Use `PascalCase` for class names
- Use `UPPER_SNAKE_CASE` for constants
- Prefix private methods and attributes with a single underscore

### 1.3 Code Organization
- Group related functions and classes together
- Use meaningful module names
- Organize imports in the following order:
  1. Standard library imports
  2. Third-party library imports
  3. Local application imports
- Separate import groups with blank lines

## 2. File Structure

```
IIVA/
├── README.md
├── ARCHITECTURE.md
├── DEVELOPMENT.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── application.py
│   │   └── screens/
│   ├── services/
│   │   ├── __init__.py
│   │   ├── file_service.py
│   │   ├── student_service.py
│   │   ├── lesson_service.py
│   │   └── integration_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_file_service.py
│   └── test_student_service.py
└── docs/
    ├── ...
    └── ...
```

## 3. Version Control

### 3.1 Git Workflow
- Use Git Flow branching model:
  - `main` branch: Production-ready code
  - `develop` branch: Next release development
  - `feature/*` branches: Feature development
  - `release/*` branches: Release preparation
  - `hotfix/*` branches: Critical bug fixes
- Write descriptive commit messages in the imperative mood
- Keep commits focused on a single concept
- Use semantic versioning (MAJOR.MINOR.PATCH)

### 3.2 Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

Types include:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code restructuring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

Example:
```
feat(student-service): add method to calculate attendance rate

The new calculate_attendance_rate method computes the student's
attendance percentage based on completed and missed lessons.

Closes #123
```

## 4. Testing Strategy

### 4.1 Unit Testing
- Test individual functions and methods
- Mock external dependencies
- Achieve high code coverage (>80%)
- Use pytest framework
- Name test files as `test_<module_name>.py`
- Name test functions as `test_<functionality>`

### 4.2 Integration Testing
- Test interactions between components
- Validate file I/O operations
- Test external service integrations
- Use dedicated test configurations

### 4.3 Test Structure
```python
def test_function_name():
    # Arrange: Set up test conditions
    # Act: Execute the function under test
    # Assert: Verify the expected outcome
    # Clean up if necessary
```

## 5. Documentation Standards

### 5.1 Code Documentation
- Document all public functions, classes, and modules
- Use Google-style docstrings
- Include type hints where appropriate
- Document parameters, return values, and exceptions

Example:
```python
def create_student_profile(name: str, email: str) -> Student:
    """Creates a new student profile with the given information.
    
    Args:
        name: The full name of the student
        email: The student's email address
        
    Returns:
        Student: The newly created student profile
        
    Raises:
        ValueError: If email format is invalid
        DuplicateStudentError: If student with same email exists
    """
    # Implementation here
```

### 5.2 External Documentation
- Keep documentation synchronized with code changes
- Document all public APIs
- Include examples for complex functionality
- Maintain an up-to-date changelog
- Provide clear installation and usage instructions

## 6. Error Handling

- Use specific exception types (create custom exceptions where appropriate)
- Handle errors gracefully with appropriate fallbacks
- Log errors with sufficient context for debugging
- Never catch exceptions without handling them appropriately
- Fail fast when appropriate

## 7. Security Considerations

- Validate all user inputs
- Sanitize data before processing or storing
- Store sensitive information securely (API keys, etc.)
- Follow the principle of least privilege
- Regularly update dependencies to address security vulnerabilities