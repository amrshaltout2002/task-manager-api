# Task Manager API

## Overview

The `task-manager-api` is a Python-based RESTful API designed to provide a robust backend for managing tasks. It includes built-in user authentication and a JWT token system to ensure secure access to task data. Each user can only access their own tasks. The project is equipped with a full suite of automated tests and is ready for containerized deployment using Docker.

---

## Features

- **User Authentication:** Secure registration and login using JWT tokens with bcrypt password hashing.
- **Task Management:** Full CRUD operations — create, read, update, and delete tasks tied to authenticated users.
- **Ownership Protection:** Users can only view and modify their own tasks.
- **Database Migrations:** Managed through Alembic to ensure consistent database schema updates.
- **Containerization:** Full support for Docker and Docker Compose for easy environment setup.
- **Automated Testing:** Comprehensive test suite for authentication and task endpoints using Pytest.
- **Input Validation:** Strict request validation using Pydantic schemas.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core language |
| FastAPI | Web framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM for database interaction |
| Alembic | Database migrations |
| Pydantic | Data validation and schemas |
| JWT (python-jose) | Authentication tokens |
| Passlib + bcrypt | Password hashing |
| Pytest | Automated testing |
| Docker + Docker Compose | Containerization |

---

## Project Structure

```
task-manager-api/
├── app/
│   ├── core/           # Security, config, and dependencies
│   ├── db/             # Database connection and session management
│   ├── models/         # SQLAlchemy database models
│   ├── routers/        # API route handlers
│   ├── schemas/        # Pydantic request and response schemas
│   └── main.py         # Application entry point
├── alembic/            # Database migration scripts
├── tests/              # Pytest test suite
├── Dockerfile          # Docker image configuration
├── docker-compose.yml  # Multi-container Docker setup
├── requirements.txt    # Python dependencies
└── .env                # Environment variables (not committed)
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/amrshaltout2002/task-manager-api.git
cd task-manager-api
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the project root with the following variables:
```
DATABASE_URL=postgresql://user:password@localhost:5432/taskmanager
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. **Run database migrations**
```bash
alembic upgrade head
```

6. **Start the server**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`
Auto-generated docs available at `http://localhost:8000/docs`

---

## Running with Docker

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

---

## Running Tests

```bash
pytest tests/ -v
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | /auth/register | Register a new user | No |
| POST | /auth/login | Login and receive JWT token | No |

### Users

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | /users/me | Get current logged in user | Yes |

### Tasks

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | /tasks | Create a new task | Yes |
| GET | /tasks | Get all tasks for current user | Yes |
| GET | /tasks/{id} | Get a single task by ID | Yes |
| PUT | /tasks/{id} | Update a task | Yes |
| DELETE | /tasks/{id} | Delete a task | Yes |

---

## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key for JWT signing |
| `ALGORITHM` | JWT algorithm (HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry duration in minutes |
