from app.api.models import db


class Library(db.Model):
    __tablename__ = "library"

    #table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #relationships
    books = db.relationship(
        "LibraryBook",
        back_populates="library",
        cascade="all, delete, delete-orphan"
    )
