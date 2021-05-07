from app.models import db


class Book(db.Model):
    __tablename__ = "book"

    #table columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)

    #relationships
    libraries = db.relationship(
        "LibraryBook",
        back_populates="book",
        cascade="all, delete, delete-orphan"
    )
