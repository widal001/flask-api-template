from app.models import db, Book, Library
from tests.data import BOOKS, LIBRARIES


def test_populate(client):

    # setup
    exp_book = BOOKS["world and me"]
    exp_library = LIBRARIES["central"]

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
