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

<img width="812" height="552" alt="Screenshot 2026-07-30 at 3 29 55 PM" src="https://github.com/user-attachments/assets/83ee7203-6ec3-4e71-8e13-0a9e4599352e" />

---

## Testing

The API was tested using:

- Postman
- curl
- Docker container

The Postman collection is available in the `postman/` directory.

---

## Screenshots
### Architecture Diagram 

### Docker Image Build & Running Docker Container

<a href="./screenshots/running-container.png">
<img width="1076" height="392" alt="Screenshot 2026-07-30 at 4 44 07 PM" src="https://github.com/user-attachments/assets/2c996fa1-df03-45a1-b60c-d817768b3ddc" />
</a>

---

### Get Invalid Note

<a href="./screenshots/postman-create-note.png">
 <img width="799" height="438" alt="Screenshot 2026-07-30 at 4 45 00 PM" src="https://github.com/user-attachments/assets/264fdfaf-338f-4dcc-86eb-28acdbd96cd1" />
</a>

---

### Get All Notes

<a href="./screenshots/postman-get-notes.png">
  <img width="799" height="528" alt="Screenshot 2026-07-30 at 4 45 28 PM" src="https://github.com/user-attachments/assets/a24bc948-fa11-4e2b-b3ae-ed3099179eb7" />
</a>

---

### Docker Desktop

<a href="./screenshots/docker-desktop.png">
  <img width="1466" height="927" alt="Screenshot 2026-07-30 at 4 46 32 PM" src="https://github.com/user-attachments/assets/3ec7aa10-abeb-411f-b143-fa6faecb3f49" />
</a>

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
