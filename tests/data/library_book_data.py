from tests.data import BOOKS, LIBRARIES


LIBRARY_BOOKS = {
    "central": {
        "world and me": {"id": 111, "is_available": True},
        "black butterfly": {"id": 112, "is_available": False},
        "homegoing": {"id": 113, "is_available": True},
        "beloved": {"id": 114, "is_available": True},
    },
    "waverly": {
        "world and me": {"id": 221, "is_available": True},
        "black butterfly": {"id": 222, "is_available": True},
        "homegoing": {"id": 223, "is_available": True},
    },
    "patterson": {
        "world and me": {"id": 331, "is_available": True},
        "black butterfly": {"id": 333, "is_available": True},
        "homegoing": {"id": 334, "is_available": False},
        "beloved": {"id": 335, "is_available": True},
    },
}

# creates response body for api/library/<int:lib_id>/books
LIBRARY_BOOKS_API = {}
for branch, books in LIBRARY_BOOKS.items():
    LIBRARY_BOOKS_API[branch] = {
        **LIBRARIES[branch],
        "books": [{**v, "book": BOOKS[k]} for k, v in books.items()]
    }
