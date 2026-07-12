import os

from flask import Flask, redirect, render_template, request  # type: ignore[import]
from flask_sqlalchemy import SQLAlchemy  # type: ignore[import]

app = Flask(__name__)

# -----------------------
# Database Configuration
# -----------------------
os.makedirs(app.instance_path, exist_ok=True)

database_path = os.path.join(app.instance_path, "notes.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# -----------------------
# Database Model
# -----------------------
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)


# Create database tables after models are defined
with app.app_context():
    db.create_all()


# -----------------------
# Home + Search
# -----------------------
@app.route("/")
def home():
    search_query = request.args.get("search", "").strip()

    if search_query:
        notes = (
            Note.query
            .filter(Note.content.contains(search_query))
            .order_by(Note.id.desc())
            .all()
        )
    else:
        notes = Note.query.order_by(Note.id.desc()).all()

    return render_template(
        "index.html",
        notes=notes,
        search_query=search_query,
    )


# -----------------------
# Add Note
# -----------------------
@app.route("/add", methods=["POST"])
def add_note():
    note_content = request.form.get("note", "").strip()

    if note_content:
        new_note = Note(content=note_content)
        db.session.add(new_note)
        db.session.commit()

    return redirect("/")


# -----------------------
# Edit Note
# -----------------------
@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = db.get_or_404(Note, note_id)

    if request.method == "POST":
        updated_content = request.form.get("note", "").strip()

        if updated_content:
            note.content = updated_content
            db.session.commit()

        return redirect("/")

    return render_template("edit.html", note=note)


# -----------------------
# Delete Note
# -----------------------
@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = db.get_or_404(Note, note_id)

    db.session.delete(note)
    db.session.commit()

    return redirect("/")


# -----------------------
# Health Check
# -----------------------
@app.route("/health")
def health():
    return {"status": "healthy"}, 200


# -----------------------
# Run Application
# -----------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )