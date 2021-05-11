from app.models import db

UPDATE_FIELDS = ["title", "author"]


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

    # for more info on why we use setattr() read this:
    # https://medium.com/@s.azad4/modifying-python-objects-within-the-sqlalchemy-framework-7b6c8dd71ab3
    def update(self, **update_dict):
        for field, value in update_dict.items():
            if field in UPDATE_FIELDS:
                setattr(self, field, value)
