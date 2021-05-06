from app.models import db


class Library(db.Model):
    __tablename__ = "library"

    #table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #relationships
    books = db.relationship(
        "LibraryItem",
        back_populates="libraries",
        cascade="all, delete, delete-orphan"
    )
