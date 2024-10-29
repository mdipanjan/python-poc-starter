# Python Project Template

A full-stack Python project template using FastAPI, SQLAlchemy, and PostgreSQL.

## Features
- FastAPI web framework
- SQLAlchemy ORM
- PostgreSQL database
- Pydantic data validation
- Jinja2 templating
- Docker support
- Pre-commit hooks
- Code formatting (Black, isort)
- Testing with pytest
- Development tools (flake8, black, isort)

## Setup

### Local Development
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   # or
   .\env\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   make install-dev
   ```
4. Copy .env.example to .env and update values
5. Run the development server:
   ```bash
   make run
   ```

### Docker Setup
1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Project Structure
```
.
├