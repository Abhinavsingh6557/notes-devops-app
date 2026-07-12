import os

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

os.makedirs(app.instance_path, exist_ok=True)
database_path = os.path.join(app.instance_path, "notes.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_query = request.args.get("search", "").strip()

    if search_query:
        notes = Note.query.filter(
            Note.content.contains(search_query)
        ).order_by(Note.id.desc()).all()
    else:
        notes = Note.query.order_by(Note.id.desc()).all()

    return render_template(
        "index.html",
        notes=notes,
        search_query=search_query,
    )


@app.route("/add", methods=["POST"])
def add_note():
    note_content = request.form.get("note", "").strip()

    if note_content:
        db.session.add(Note(content=note_content))
        db.session.commit()

    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    note = db.get_or_404(Note, id)

    if request.method == "POST":
        updated_content = request.form.get("note", "").strip()

        if updated_content:
            note.content = updated_content
            db.session.commit()

        return redirect("/")

    return render_template("edit.html", note=note)


@app.route("/delete/<int:id>")
def delete_note(id):
    note = db.get_or_404(Note, id)
    db.session.delete(note)
    db.session.commit()

    return redirect("/")


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)