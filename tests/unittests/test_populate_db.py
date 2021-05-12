from app.models import db, Book, Library
from tests.data import BOOKS, LIBRARIES


def test_populate(client):
    """Tests the creation of a test database with the use of the client fixture

    Assertions
    ----------
    Attributes
        The records created in populate_db() exist and their attributes match
        what is specified in the data files
    """
    # setup
    exp_book = BOOKS["world and me"]
    exp_library = LIBRARIES["central"]
    print("EXPECTED")
    print(exp_book)

    # execution
    book = Book.query.get(123)
    lib = Library.query.get(123)
    lib_book = lib.books[0]

    # validation
    assert book.title == exp_book["title"]
    assert book.author == exp_book["author"]
    assert lib.name == exp_library["name"]
    assert lib_book.id == 111
    assert lib_book.book_id == book.id
