# Secure Notes API

A RESTful Notes API built with Flask and SQLAlchemy. The project demonstrates backend fundamentals including REST API development, CRUD operations, request validation, database integration, and Docker containerization.

---

## Features

- Create, Read, Update and Delete notes (CRUD)
- RESTful API endpoints
- JSON request and response handling
- SQLite database with SQLAlchemy ORM
- Input validation and error handling
- Environment variable configuration using `.env`
- Docker container support
- API testing with Postman

---

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- Docker
- Postman
- Git & GitHub

---

## Project Structure

```text
secure-notes-api/
│
├── app.py
├── config.py
├── database.py
├── models.py
├── routes.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── .gitignore
├── README.md
├── postman/
│   └── Secure Notes API.postman_collection.json
└── screenshots/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/nehasawant99/secure-notes-api.git
cd secure-notes-api
```

Create and activate a virtual environment.

```bash
python -m venv .venv

# macOS/Linux
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///notes.db
DEBUG=True
```

Run the application.

```bash
python app.py
```

API URL

```text
http://127.0.0.1:5000
```

---

## Run with Docker

Build the Docker image.

```bash
docker build -t secure-notes-api .
```

Run the container.

```bash
docker run --env-file .env -p 5001:5000 secure-notes-api
```

Docker API URL

```text
http://localhost:5001
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health Check |
| POST | `/notes` | Create Note |
| GET | `/notes` | Get All Notes |
| GET | `/notes/<id>` | Get Note by ID |
| PUT | `/notes/<id>` | Update Note |
| DELETE | `/notes/<id>` | Delete Note |

---

## Example Request

**POST** `/notes`

```json
{
  "title": "Docker Notes",
  "description": "Learn Docker basics"
}
```

---

## Example Response

```json
{
  "message": "Note created successfully",
  "id": 1
}
```

---

## Testing

The API was tested using:

- Postman
- curl
- Docker container

The Postman collection is available in the `postman/` directory.

---

## Screenshots

Add the following screenshots inside the `screenshots/` folder.

- Docker Image Build
- Running Docker Container
- API Response (`curl`)
- Postman CRUD Testing
- Project Structure

---

## Learning Outcomes

This project helped me practice:

- REST API Development
- CRUD Operations
- SQLAlchemy ORM
- SQLite Integration
- Environment Variables
- Docker Containerization
- API Testing with Postman
- Git & GitHub Workflow

---

## License

This project is licensed under the MIT License.
