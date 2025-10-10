# IIVA Architecture Documentation

## 1. System Overview

IIVA follows a layered architecture pattern with clearly defined responsibilities for each layer:

```
┌─────────────────────────────────────┐
│              IIVA TUI               │ <- Presentation Layer
├─────────────────────────────────────┤
│        Application Layer            │ <- Business Logic
├─────────────────────────────────────┤
│     Business Logic Services         │ <- Domain Logic
├─────────────────────────────────────┤
│      Data Access & Parsing          │ <- Data Layer
├─────────────────────────────────────┤
│     Integration & External APIs     │ <- External Services
└─────────────────────────────────────┘
```

## 2. Technology Stack

- **Language**: Python 3.10+
- **TUI Framework**: Textual
- **Data Format**: YAML frontmatter in Markdown files
- **Dependency Management**: pip with requirements.txt
- **Configuration**: YAML configuration files
- **External Integrations**: Google APIs, AI service APIs

## 3. Data Model

### 3.1 Student Profile Schema
The unified student profile follows this structure:

```yaml
# Basic Student Information
name: "Student Full Name"
contact:
  email: "student@email.com"
  phone: "+55 (11) 98765-4321"
  whatsapp: "+55 (11) 98765-4321"

# Enrollment Information
enrollment:
  start_date: "YYYY-MM-DD"
  status: "active" # active, inactive, trial, graduated
  referred_by: "How the student found you"
  trial_lesson_date: "YYYY-MM-DD" # If applicable
  conversion_date: "YYYY-MM-DD" # When they became paying student

# Contract and Scheduling
contract:
  total_lessons: 20 # Total number of lessons in contract
  remaining_lessons: 15 # Number remaining
  lessons_per_week: 2 # Frequency
  lesson_duration: 60 # Duration in minutes

schedule:
  - day: "Monday"
    time: "HH:MM-HH:MM"
    timezone: "Continent/City"
    google_calendar_event_id: "calendar_event_id" # If integrated

# Student Profile
level: "Intermediate" # beginner, elementary, pre-intermediate, intermediate, upper-intermediate, advanced
learning_goals:
  - "Goal 1"
  - "Goal 2"
  - "Goal 3"

learning_preferences:
  style: "visual" # visual, auditory, kinesthetic
  interests: ["topic1", "topic2", "topic3"]
  preferred_topics: ["topic1", "topic2"]

# Technical integrations
google_classroom:
  course_id: "classroom_course_id"
  invite_link: "https://classroom.google.com/c/..."

google_meet:
  meeting_link: "https://meet.google.com/xxx-xxxx-xxx"
  meeting_code: "xxx-xxxx-xxx"

# Statistics and Tracking
stats:
  total_lessons_completed: 5
  attendance_rate: 100.0 # Percentage
  last_lesson_date: "YYYY-MM-DD"
  next_lesson_date: "YYYY-MM-DD"
  total_absences: 0
  total_late_arrivals: 0

# Internal Notes
internal_notes: "Any internal notes about the student"
```

### 3.2 Content Structure
The Markdown portion follows this structure:

```markdown
# [Student Name] Student Profile

## Personal Information
- **Contact**: [Contact information from frontmatter]
- **Level**: [Level from frontmatter]
- **Schedule**: [Schedule from frontmatter]
- **Goals**: [Learning goals from frontmatter]

## Lesson History

### Lesson [XX]: YYYY-MM-DD [STATUS]
#### Plan
[Lesson plan content]

#### Log
[Lesson log content]

#### Backoffice
[Backoffice instructions]

#### Classroom
[Classroom content]

## Student Notes
[Additional notes, observations, and progress tracking]
```

## 4. Core Components

### 4.1 File Service
Responsible for reading, writing, and parsing student profile files:
- Validates YAML schema
- Parses structured content
- Maintains file integrity
- Handles backup and recovery

### 4.2 Student Management Service
Handles all student-related operations:
- Create, read, update student profiles
- Track student progress and statistics
- Manage student lifecycle (active, inactive, etc.)

### 4.3 Lesson Planning Service
Manages lesson content:
- Create and update lesson plans
- Track lesson status (planned, completed, etc.)
- Facilitate AI integration for content generation

### 4.4 Integration Service
Manages connections to external services:
- Google Drive/Calendar/Classroom APIs
- AI service APIs
- Third-party service connections

## 5. Implementation Patterns

### 5.1 SOLID Principles
- **Single Responsibility**: Each service has a single, well-defined purpose
- **Open/Closed**: Components are open for extension but closed for modification
- **Liskov Substitution**: Components follow expected interfaces
- **Interface Segregation**: Services define focused interfaces
- **Dependency Inversion**: High-level modules don't depend on low-level modules

### 5.2 Design Patterns
- **Repository Pattern**: For data access operations
- **Service Layer Pattern**: For business logic organization
- **Factory Pattern**: For creating complex objects
- **Observer Pattern**: For handling updates to the UI