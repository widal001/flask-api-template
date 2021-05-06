from app.models import db


class LibraryBook(db.Model):
    __tablename__ = "library_book"

    #table columns
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    library_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    is_available = db.Column(db.Integer)

    #relationships
    book = db.relationship("Book", back_populates="readers")
    library = db.relationship("library", back_populates="books")
