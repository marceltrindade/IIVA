# IIVA Configuration Management

## 1. Overview

IIVA uses a hierarchical configuration approach with multiple layers:

1. Default values (hardcoded in the application)
2. User-defined settings (`config/iiva_config.yaml`)
3. Runtime values (passed via command-line or environment variables)

## 2. Configuration File Structure

The main configuration file `config/iiva_config.yaml` contains all configurable settings:

```yaml
app:
  name: "IIVA"
  version: "0.1.0"
  debug: false
  data_dir: "~/Tyrell_Corp/IIVA/data"  # Path to student profile files

ui:
  theme: "default"  # Available themes: default, dark, light
  lesson_display_limit: 10  # Number of lessons to display initially

ai:
  provider: "openai"  # Supported: openai, anthropic, ollama
  model: "gpt-4-turbo"  # Model identifier (provider-specific)
  temperature: 0.7  # Creativity level (0.0-1.0)
  api_key: "your_api_key_here"  # API key for the service
  max_tokens: 1000  # Maximum tokens for AI responses

google:
  drive_remote: "idiomaindependente"  # rclone remote name
  calendar_id: "primary"  # Google Calendar ID to use
  classroom_integration: true  # Enable Google Classroom features
  credentials_file: "config/google_credentials.json"  # Path to credentials

paths:
  student_profiles_dir: "~/Planejamento_Aulas"  # Base directory for student files
  backup_dir: "~/Tyrell_Corp/IIVA/backups"  # Directory for backups
  temp_dir: "/tmp/iiva_temp"  # Temporary files location

workflow:
  auto_create_lesson_dirs: true  # Automatically create lesson directories
  default_lesson_duration: 60  # Default lesson duration in minutes
  auto_schedule_buffer: 15  # Minutes before lesson to send reminders
  max_lessons_per_day: 8  # Maximum lessons allowed per day

features:
  lesson_auto_generation: true  # Enable AI-assisted lesson generation
  statistical_reporting: true  # Enable statistical reporting features
  integration_sync: true  # Enable Google service synchronization
```

## 3. Environment Variables

Some settings can be overridden using environment variables:

- `IIVA_CONFIG_PATH`: Path to the configuration file
- `IIVA_DATA_DIR`: Path to the data directory
- `IIVA_DEBUG`: Enable debug mode (true/false)
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to Google service account file
- `OPENAI_API_KEY`: API key for OpenAI services

## 4. Configuration Validation

The application validates the configuration at startup to ensure:
- Required fields are present
- Values are within acceptable ranges
- File paths exist and are accessible
- API keys are properly formatted

## 5. Configuration Management Best Practices

### 5.1 Security
- Never commit API keys or credentials to version control
- Use environment variables for sensitive information
- Store the configuration file in a secure location
- Use appropriate file permissions (600 for config files with credentials)

### 5.2 Backup and Recovery
- Regularly backup the configuration file
- Version control the configuration (without sensitive information)
- Have a recovery procedure in case of configuration corruption

### 5.3 Environment-Specific Configuration
For different environments (development, testing, production), you can use:

1. Different configuration files (e.g., `config/dev.yaml`, `config/prod.yaml`)
2. Environment-specific environment variables
3. Configuration templates with environment-specific values

## 6. Default Configuration File

The application includes a default configuration that works out of the box. When the configuration file is missing, the application will:

1. Create a default configuration file at the expected location
2. Generate placeholder values for required fields
3. Provide clear instructions for customization

## 7. Configuration Updates

To update the configuration:

1. Modify the `config/iiva_config.yaml` file
2. Restart the application to apply changes
3. Some settings may require application restart to take effect
4. The application validates the configuration on each start