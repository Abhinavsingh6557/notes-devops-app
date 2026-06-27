from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# -----------------------
# Database Model
# -----------------------
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)


# -----------------------
# Home + Search
# -----------------------
@app.route("/")
def home():

    search_query = request.args.get("search")

    if search_query:
        notes = Note.query.filter(Note.content.contains(search_query)).all()
    else:
        notes = Note.query.all()

    return render_template(
        "index.html",
        notes=notes,
        search_query=search_query
    )


# -----------------------
# Add Note
# -----------------------
@app.route("/add", methods=["POST"])
def add_note():

    note_content = request.form.get("note")

    if note_content:
        new_note = Note(content=note_content)
        db.session.add(new_note)
        db.session.commit()

    return redirect("/")


# -----------------------
# Edit Note
# -----------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_note(id):

    note = Note.query.get_or_404(id)

    if request.method == "POST":

        updated_content = request.form.get("note")

        if updated_content:
            note.content = updated_content
            db.session.commit()

        return redirect("/")

    return render_template("edit.html", note=note)


# -----------------------
# Delete Note
# -----------------------
@app.route("/delete/<int:id>")
def delete_note(id):

    note = Note.query.get_or_404(id)

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

    with app.app_context():
        db.create_all()

    app.run(debug=True)