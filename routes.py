from flask import request, jsonify

from database import db
from models import Note


def register_routes(app):

    # Create Note
    @app.route("/notes", methods=["POST"])
    def create_note():

        data = request.get_json(silent=True)

        if data is None:
            return jsonify({
                "error": "Request body must be valid JSON"
            }), 400

        title = data.get("title", "").strip()
        description = data.get("description", "").strip()

        if not title or not description:
            return jsonify({
                "error": "Title and description are required"
            }), 400

        note = Note(
            title=title,
            description=description
        )

        db.session.add(note)
        db.session.commit()

        return jsonify({
            "message": "Note created successfully",
            "id": note.id
        }), 201


    # Get All Notes
    @app.route("/notes", methods=["GET"])
    def get_notes():

        notes = Note.query.order_by(Note.created_at.desc()).all()

        result = []

        for note in notes:
            result.append({
                "id": note.id,
                "title": note.title,
                "description": note.description,
                "created_at": note.created_at.isoformat()
            })

        return jsonify(result), 200


    # Get One Note
    @app.route("/notes/<int:id>", methods=["GET"])
    def get_note(id):

        note = db.session.get(Note, id)

        if note is None:
            return jsonify({
                "error": "Note not found"
            }), 404

        return jsonify({
            "id": note.id,
            "title": note.title,
            "description": note.description,
            "created_at": note.created_at.isoformat()
        }), 200


    # Update Note
    @app.route("/notes/<int:id>", methods=["PUT"])
    def update_note(id):

        note = db.session.get(Note, id)

        if note is None:
            return jsonify({
                "error": "Note not found"
            }), 404

        data = request.get_json(silent=True)

        if data is None:
            return jsonify({
                "error": "Request body must be valid JSON"
            }), 400

        title = data.get("title", "").strip()
        description = data.get("description", "").strip()

        if not title or not description:
            return jsonify({
                "error": "Title and description are required"
            }), 400

        note.title = title
        note.description = description

        db.session.commit()

        return jsonify({
            "message": "Note updated successfully"
        }), 200


    # Delete Note
    @app.route("/notes/<int:id>", methods=["DELETE"])
    def delete_note(id):

        note = db.session.get(Note, id)

        if note is None:
            return jsonify({
                "error": "Note not found"
            }), 404

        db.session.delete(note)
        db.session.commit()

        return jsonify({
            "message": "Note deleted successfully"
        }), 200