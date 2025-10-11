# Qwen AI Assistant Guidelines for IIVA Project

## Project Context

IIVA (Idioma Independente Virtual Assistant) is an intelligent assistant designed to streamline the entire student management and lesson planning workflow for English teachers. The project consolidates student information, automates lesson planning, and integrates with external services to reduce administrative overhead.

## Current Project Status

- The project is in the documentation and planning phase
- Core architecture and structure have been defined
- Docker containerization capabilities have been added
- The system uses a unified student profile format with YAML frontmatter
- Terminal User Interface (TUI) built with Textual is planned

## Your Role

As the Qwen AI Assistant for this project, you are responsible for:

1. Maintaining consistency with the documented architecture and development guidelines
2. Following the Git Flow branching model for version control
3. Implementing features that align with the core principles of consolidation, automation, integration, AI assistance, and scalability
4. Ensuring Docker containerization compatibility for all components
5. Respecting the unified student profile format with YAML frontmatter
6. Preserving the existing workflow processes while improving automation

## Working Guidelines

### Before Implementing Changes:
- Always check the existing codebase and documentation first
- Verify that your implementation aligns with the architectural guidelines
- Consider how changes will affect the Docker containerization
- Follow the coding standards and naming conventions documented in DEVELOPMENT.md
- Use appropriate Git commit messages following the documented format

### During Implementation:
- Focus on modularity to ensure components work well in containerized environments
- Maintain backward compatibility with existing student profile files
- Follow security best practices, especially in Docker implementation
- Prioritize data integrity and file format consistency
- Implement proper error handling as per the guidelines

### File Management:
- Student profiles follow the unified format with YAML frontmatter
- New files should follow the naming conventions documented in DEVELOPMENT.md
- Maintain compatibility with the existing file structure
- Ensure proper backup and recovery mechanisms for student data

### Docker Best Practices:
- Use multi-stage builds to reduce image size
- Run applications as non-root users
- Securely handle sensitive information (API keys, credentials)
- Leverage Docker layer caching appropriately

## Communication Guidelines

- When making changes, explain the reasoning behind the implementation
- Propose solutions that align with the project's core principles
- Always verify how the changes will impact the Docker containerization
- Use appropriate Git commit messages following the format: `<type>(<scope>): <description>`

## Memory and Context

This project is focused on creating an efficient virtual assistant for English teachers. Your actions should always support this goal while maintaining the technical standards established in the documentation. Remember that the system will be containerized for easy deployment across environments.

## Safety and Security

- Handle sensitive student information securely
- Validate all inputs appropriately
- Follow security best practices for containerization
- Never commit sensitive information to version control
- Respect data privacy and protection regulations