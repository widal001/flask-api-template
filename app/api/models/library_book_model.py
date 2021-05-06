from app.api.models import db


class LibraryBook(db.Model):
    __tablename__ = "library_book"

    #table columns
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey("library.id"), nullable=False)
    is_available = db.Column(db.Boolean)

    #relationships
    book = db.relationship("Book", back_populates="libraries")
    library = db.relationship("Library", back_populates="books")
