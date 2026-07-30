from flask import Flask

from config import Config
from database import db

# Import models so SQLAlchemy knows about them
from models import Note


app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Connect SQLAlchemy to Flask
db.init_app(app)


@app.route("/")
def home():
    return {
        "message": "Secure Notes API is running!"
    }


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run()