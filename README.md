# Secure Notes API

A RESTful Notes API built with Flask and SQLAlchemy that supports creating, reading, updating, and deleting notes. The project demonstrates backend fundamentals including REST APIs, database operations, request validation, and CRUD functionality.

## Features

- Create a note
- Get all notes
- Get a note by ID
- Update a note
- Delete a note
- JSON request and response handling
- SQLite database using SQLAlchemy ORM
- Input validation and error handling

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- Postman
- Git & GitHub

## Project Structure

```text
secure-notes-api/
│
├── app.py
├── config.py
├── database.py
├── models.py
├── routes.py
├── requirements.txt
├── .gitignore
├── README.md
├── postman/
│   └── Secure Notes API.postman_collection.json
└── screenshots/
```

## Installation

Clone the repository.

```bash
git clone https://github.com/nehasawant99/secure-notes-api.git
```

Move into the project.

```bash
cd secure-notes-api
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

macOS/Linux

```bash
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
```

Run the application.

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health check |
| POST | `/notes` | Create a note |
| GET | `/notes` | Get all notes |
| GET | `/notes/<id>` | Get a note by ID |
| PUT | `/notes/<id>` | Update a note |
| DELETE | `/notes/<id>` | Delete a note |

## Example Request

**POST** `/notes`

```json
{
    "title": "Docker Notes",
    "description": "Learn Docker basics"
}
```

## Example Response

```json
{
    "id": 1,
    "message": "Note created successfully"
}
```

<img width="812" height="552" alt="image" src="https://github.com/user-attachments/assets/1dea30c1-d1cb-4249-a147-1a8b5ad66dcc" />


## Testing

The API was tested using Postman.

The exported Postman collection is available in the `postman/` directory.

## License

This project is licensed under the MIT License.
