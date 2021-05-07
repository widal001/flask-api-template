from app.api.models import db, Library, Book, LibraryBook
from tests.data import BOOKS, LIBRARIES, LIBRARY_BOOKS

def populate():

    # create the library and book records
    libraries = {name: Library(**data) for name, data in LIBRARIES.items()}
    books = {name: Book(**data) for name, data in BOOKS.items()}

    for library, lib_books in LIBRARY_BOOKS.items():
        for book, data in lib_books.items():
            # create a library_book record
            lib_book = LibraryBook(**data)
            # create the relationships
            lib_book.library = libraries[library]
            lib_book.book = books[book]
            # add the record to the session
            db.session.add(lib_book)

    # commit the changes
    db.session.commit()
